import asyncio
import json
import copy
import os
import re
import copy
from sys import exit
from ollama import AsyncClient
from openai import AsyncOpenAI

class Game():

    def __init__(self):
        self.openai_backbone = True
        self.general_forgetting_threshold = 25000 #in characters
        self.presence_penalty = 1.0 #maybe that's specific to deepinfra?
        self.presence_penalty_json = 2.0 #maybe that's specific to deepinfra?
        print ("Engine is running. Use set_scene and start_game!")

    def extract_json_between_markers(self, text):
        match = None
        pattern = r'```json\s*(.*?)\s*```'
        matches = re.findall(pattern, text, re.DOTALL)
        if matches:
            match = matches[-1]
        else:
            pattern = r'\{.*?\}'
            matches = re.findall(pattern, text, re.DOTALL)
            if matches:
                match = matches[-1]
        return match
            
    def load_json_from_llm(self, text):
        if self.openai_backbone:
            json_text = self.extract_json_between_markers(text)
        else:
            json_text = text
        return json.loads(json_text)

    async def chat_openai_backbone(self, history, json=False):
        openai = AsyncOpenAI(
            api_key=os.getenv('OPEN_API_KEY'),
            base_url=os.getenv('OPEN_API_URL'),
        )
        
        model_str = "meta-llama/Llama-3.3-70B-Instruct-Turbo"
        
        if json:
            chat_completion = await openai.chat.completions.create(
                model=model_str,
                max_tokens=16834,
                messages=history,
                response_format={"type": "json"},
                presence_penalty=self.presence_penalty_json
            )
        else:
            chat_completion = await openai.chat.completions.create(
                model=model_str,
                max_tokens=16834,
                messages=history,
                presence_penalty=self.presence_penalty
            )
        
        content = chat_completion.choices[0].message.content
        print(content)
        print('.')
        return content

    async def chat_ollama_backbone(self, history, json=False):
        client = AsyncClient()
        full_response = ""
        if not json:
            async for part in await client.chat(model='gemma2:27b', messages=history, stream=True):
                content = part['message']['content']
                print(content, end='', flush=True)
                full_response += content
        else:
            async for part in await client.chat(model='gemma2:27b', messages=history, format='json', stream=True):
                content = part['message']['content']
                print(content, end='', flush=True)
                full_response += content
        print('.')  # Add a newline after the response
        return full_response
    
    async def chat_inner(self, history, json=False):
        if self.openai_backbone:
            return await self.chat_openai_backbone(history, json)
        else:
            return await self.chat_ollama_backbone(history, json)

    async def chat_outer(self, user_message, user_history=[], json=False, keep_history=True):
        #repeat system prompt
        if len(user_history)>0 and user_history[0]['role']=='system':
            user_history.append(user_history[0])
        user_history.append(
            {'role': 'user', 'content':user_message}
        )
        response = await self.chat_inner(user_history, json)
        user_history.append({'role': 'assistant', 'content': response})
        if not keep_history:
            user_history = user_history[:-3]
        elif len(str(user_history))>self.general_forgetting_threshold:
            user_history = user_history[:2] + user_history[2+6:] # remember the very (system and user messages: 2 messages) and forget some messages in the middle (system, user, assistant: a multiple of three)
        return response

    def set_scene(self, scene_description, winning_message= None, losing_message=None):
        self.scene_objects_prompts = scene_description
        self.winning_message = winning_message
        self.losing_message = losing_message

    async def initialize_game_objects(self):
        designer_assistant_prompt = 'You are an assistant game designer. Please keep your answers brief whenever possible.'
        self.designer_assistant_history=[
            {'role': 'system', 'content': designer_assistant_prompt},
            {'role': 'user', 'content': 'I am designing a text adventure in which the goal is to escape a room. I will provide brief descriptions of each object in the room and your task is to fill those descriptions such that they are usable in game format.'},
        ]
        await self.chat_inner(self.designer_assistant_history)
        
        game_object_template = {
            'role': 'system',
            'content': 'You simulate an object within a room for a videogame. Keep track of your own description, using common sense to answer questions about the object or change it. Do not spontaneously add characteristics to the simulated object without being provoked to do so. Do not disappear after being used. The object you simulate is a <object_name>. Your initial description is \"<my_description>\". That initial description might have changed. Be brief.',
        }
        self.game_object_histories = {}
            
        for item in self.scene_objects_prompts.items():
            k, v = item
            applied_game_object_template = copy.deepcopy(game_object_template)
            applied_game_object_template['content'] = applied_game_object_template['content'].replace('<object_name>', k)
            applied_game_object_template['content'] = applied_game_object_template['content'].replace('<my_description>', v)
            self.game_object_histories[k] = [applied_game_object_template]
            result = await self.chat_outer(v, self.designer_assistant_history)
            self.game_object_histories[k].append({'role':'user', 'content':f'this is your initial state: {result}'})
        
        return self.designer_assistant_history, self.game_object_histories
        
    async def get_game_state(self):
        game_state={}
        summarization_prompt = 'What is your current description? Answer in first person: I...'
        for k, v in self.game_object_histories.items(): #first all items, then a list of all mesages for each one. And each message is a dict of role and content.
            game_state[k] = await self.chat_outer (summarization_prompt, v)
        return game_state
            
    async def initialize_engine_simulator(self):
        game_engine_sys_prompt = 'You are a text game engine simulator. Your task is to reply using common sense to the questions about the player\'s text input to the game. Be brief unless talking directly to the player. I am the game designer.'
        game_state = await self.get_game_state()
        game_string = str(game_state)
        self.game_engine_history = [
            {'role':'system', 'content':game_engine_sys_prompt},
            {'role':'user', 'content': f'This is the current game state: {game_string}'},
        ]
        return self.game_engine_history
            
    async def process_input(self, p_in):
        
        if self.game_ended:
            return "The game has ended!"
        
        frozen_game_engine_history = copy.deepcopy(self.game_engine_history)
        print ([x['role'] for x in frozen_game_engine_history])
        
        game_object_names = list(self.game_object_histories.keys())
        
        bluff = await self.sanity_bluff_check(p_in, game_object_names)
        if not bluff:
            success = await self.ingame_success_check(p_in, game_object_names)
            if success:
                json_example ='{'
                for s in game_object_names:
                    json_example += f'"{s}": Move aside.'
                json_example += '}'
                
                order_prompt = f"It seems the player succeeded in their action. The action I'm talking about is {p_in}. What orders should be given to each game object?\
                    Remember to include all game objects in your json response. These are the game objects:{str(game_object_names)}\
                    In your json, Use only one string per game object. Do not nest properties. Include all game objects, except win and lose conditions.\
                    Example of json format: {json_example}"
                json_orders = await self.chat_outer(order_prompt, self.game_engine_history, json=True)
                dict_orders = self.load_json_from_llm(json_orders)
                await self.send_broadcast(dict_orders)
            else:
                failure_prompt = f"It seems the player has failed in their action. The action I'm talking about is {p_in}. Please reflect on why they failed. There may be multiple causes. Pay special attention to mentions to objects that don't exist."
                await self.chat_outer(failure_prompt, self.game_engine_history)
        else:
            failure_prompt = f"It seems the player has failed in their action. The action I'm talking about is {p_in}. The game has determined that the player was somehow bluffing or attempting an impossible feat. Pay special attention to mentions to objects that don't exist."
            await self.chat_outer(failure_prompt, self.game_engine_history)
        broadcast_prompt = f"Relay the state of affairs as a result of the player's actions as a single message to all game objects. Make sure to include whether they were bluffing."
        broadcast_message = await self.chat_outer(broadcast_prompt, self.game_engine_history, keep_history=False)
        broadcast_message += "\n Do not reply to this message. Merely use it for future responses"
        broadcast_dict = {}
        for k in self.game_object_histories.keys():
            broadcast_dict[k] = broadcast_message
        await self.send_broadcast(broadcast_dict)
        
        game_string = str (await self.get_game_state())
        
        
        self.game_engine_history = copy.deepcopy(frozen_game_engine_history)
        
        response_prompt = f"This is the new state of every object in the game:{game_string}\
            This is the message that was sent to all game objects to tell them of the player's actions: {broadcast_message}\
            Relay the state of affairs as a result of the player's actions to the player. Include interesting details about the game state, but do not reveal information on the win and/or lose conditions of the game. If the player failed, explain why.\
            Do not reveal secret or confidential game information, such as a hidden object."
        response_to_player = await self.chat_outer(response_prompt, self.game_engine_history, keep_history=False)
        
        ending_message = await self.check_ending()
        response_to_player += ending_message
        
        self.game_engine_history = copy.deepcopy(frozen_game_engine_history) #reset again
        
        update_game_history_prompt = f"This is what the player saw since last turn and the last state of each object. Update the game history accordingly:\n\
            This is ground truth data about the game.\
            What the player saw:\n{response_to_player}\n\
            Game object states:{game_string}\n\n"
        
        
        
        await self.chat_outer(update_game_history_prompt, self.game_engine_history)
        
        return response_to_player

    async def sanity_bluff_check(self, p_in, game_object_names):
        bluff_prompt = f"This is the input from the player: {p_in}\
            Please briefly answer each of the following questions:\
            Can the player reasonably perform the action they want?\
            Is the action's success or completition assured, within common sense?\
            Also consider this: Why would the action be impossible? This player is prone to bluffing, are they doing that now? You can ask multiple questions to game objects to verify consistency.\
            What questions need to be transmitted to each objects in the game, if any, in order to determine if the player is not making something up? These are the game objects:{str(game_object_names)}.\
            Be specially watchful of the player inventing objects or features that do not exist and block that from happening.\
            Do not let the player ask for advice about win conditions, such as 'How do I win?' Or similar. Those are considered bluffs from the player.\
            However, don't forbid interactions for the sake of just intended player experience alone. If it's a possible and plausible action, allow it.\
            Do not block the player action because of danger. This is a game and the player should be able to put themselves in danger if they so choose."
        frozen_game_engine_history = copy.deepcopy(self.game_engine_history)
        
        await self.chat_outer(bluff_prompt, self.game_engine_history)
        
        bluff_answers = await self.ask_away(game_object_names)
        
        gradient_bluff_prompt = f"Here are the answers of each game object: {bluff_answers}.\n Is the player desired action ({p_in}) reasonable after all?"
        await self.chat_outer (gradient_bluff_prompt, self.game_engine_history)
        
        binary_bluff_prompt="Return wether the player had sucess in their action or not. Be strict. Return a json like {bluff:True} or {bluff:False}. Do not mention previous questions or answers, only a json with the \"bluff\" key and either the value True or the value False." 
        binary_bluff_answer = await self.chat_outer(binary_bluff_prompt, self.game_engine_history, json=True)
        dict_binary_bluff = self.load_json_from_llm(binary_bluff_answer)
        binary_bluff = dict_binary_bluff['bluff']
        
        self.game_engine_history = copy.deepcopy(frozen_game_engine_history)
        return binary_bluff
    
    async def ingame_success_check(self, p_in, game_object_names):
        success_questions_prompt = f"What objects, if any, would be affected by the player's actions?\
            What questions would need to be asked of those game objects to determine if the player succeeds?\
            This is the list of game objects: {game_object_names}\
            This is what the player said:{p_in}"
        #frozen_game_engine_history = copy.deepcopy(self.game_engine_history)
        
        await self.chat_outer(success_questions_prompt, self.game_engine_history)
        success_answers = await self.ask_away(game_object_names)
        
        gradient_success_prompt = f"These are the answers returned by each relevant game object {success_answers}. Reason about them a bit. Does the player manage to do what they want to (remember, that is \"{p_in}\")? Do they have the means?\
            If the answer is ambiguous, attribute success to the player. Lean towards player success. Player injury is not a reason for disallowing success."
        await self.chat_outer(gradient_success_prompt, self.game_engine_history)
        binary_success_prompt="Return wether the player had sucess in their action or not. Be strict. Return a json like {success:True} or {success:False}. Do not mention anything else, only a json with the \"success\" key and either the value True or the value False." 
        binary_success_answer = await self.chat_outer(binary_success_prompt, self.game_engine_history, json=True)
        dict_binary_sucess = self.load_json_from_llm(binary_success_answer)
        binary_success = dict_binary_sucess['success']
        
        #self.game_engine_history = copy.deepcopy(frozen_game_engine_history)
        return binary_success

    async def ask_away(self, game_object_names):
        questions_train_prompt = f"Summarize the questions that need to be transmitted to each objects in the game\
            Be consistent. You can ask more than one question per game object. Make sure to include all the questions you thought of."
        await self.chat_outer(questions_train_prompt, self.game_engine_history)
        
        json_example ='{'
        for s in game_object_names:
            json_example += f'"{s}":What is your state? Is it possible to turn you into a frog?'
        json_example += '}'
        
        questions_prompt = f"Please transmit those same questions to each game object in json format.\
            Answer in json format for each object in the game. Say N/A if the question is not particularly relevant for the given object.\
            Prefer to say N/A\
            Remember to include all game objects in your json response. These are the game objects:{str(game_object_names)}\
            In your json, Use only one string per game object. Do not nest properties. Includde all game objects.\
            Example of json format: {str(json_example)}. Only answer this json. Multiple json in the same response is a wrong answer!!\
            You can make more than one question per object. Make sure to include all the questions you thought of. Ask away!\
            \nMake sure you only ask questions, not statements."
            
        json_questions = await self.chat_outer(questions_prompt, self.game_engine_history, json=True)
        dict_questions = self.load_json_from_llm(json_questions)
        frozen_game_object_histories = self.game_object_histories
        dict_answers = await self.send_broadcast(dict_questions)
        self.game_object_histories = frozen_game_object_histories
        return str(dict_answers)

    async def check_ending(self):
        frozen_game_engine_history = copy.deepcopy(self.game_engine_history)
        
        ending_train_prompt = "Now let's take a step back and evaluate if the player has achieved their final goal. Please don't respond, more details will be given in the next message"
        await self.chat_outer (ending_train_prompt, self.game_engine_history)
        
        ending_prompt = f"This is the state of the condition: {self.game_object_histories['win_condition']}" + "If the state of 'win condition' says the player wins, say so.\
            Return a json like {won:True} or {won:False}. Do not mention anything else, only a json with the \"won\" key and either the value True or the value False."
        ending_response = await self.chat_outer(ending_prompt, self.game_engine_history, json=True)
        ending_dict = self.load_json_from_llm(ending_response)
        if ending_dict['won']:
            print (self.winning_message)
            self.game_ended=True
            self.game_engine_history = copy.deepcopy(frozen_game_engine_history)
            return '\n' + self.winning_message
        elif 'loss_condition' in self.game_object_histories.keys():
            ending_prompt = f"This is the state of the condition: {self.game_object_histories['loss_condition']}" + "If the state of 'lose condition' says the player loses, say so.\
            Return a json like {lost:True} or {lost:False}. Do not mention anything else, only a json with the \"lost\" key and either the value True or the value False."
            ending_response = await self.chat_outer(ending_prompt, self.game_engine_history, json=True)
            ending_dict = self.load_json_from_llm(ending_response)
            if ending_dict['lost']:
                print(self.losing_message)
                self.game_ended = True
                self.game_engine_history = copy.deepcopy(frozen_game_engine_history)
                return '\n' + self.losing_message
        self.game_engine_history = copy.deepcopy(frozen_game_engine_history)
        return ''
        
    async def send_broadcast(self, dict_messages):
            
        game_object_answers={}
        for k, v in dict_messages.items():
            if "N/A" in v:
                continue
            game_object_answers[k] = await self.chat_outer(v,self.game_object_histories[k])
        
        return game_object_answers
        
        
    async def start_game(self):
        self.designer_assistant_history, self.game_object_histories = await self.initialize_game_objects()
        self.game_engine_history = await self.initialize_engine_simulator()
        self.game_ended = False

    async def brazilian_portuguese_output(self, pt_br_input):
        eng_input = await self.chat_outer(f'Translate this to English: {pt_br_input}')
        response = await self.process_input(eng_input)
        pt_br_response = await(self.chat_outer(f'Translate this to Brazilian Portuguese: {response}'))
        return pt_br_response