import asyncio
from game_object import GameObject

class EngineGameObject(GameObject):

    def __init__(self):
        super().__init__()
        self.game_ended = False
        self.active_game_objects = {}
        self.aux_bluff_history = [{'role':'system', 'content':''}]
        self.aux_success_history = [{'role':'system', 'content':''}]
        self.winning_message = '' #set externally
        self.losing_message = '' #set externally
        self.game_string = '' #set internally later
    
    async def get_binary_answer(self, prompt, history, key):
        # Get a binary (True/False) answer from backbone
        response = await self._chat_with_backbone(prompt, history, json=True)
        dict_answer = self.comms_backbone.load_json_from_llm(response)
        return dict_answer[key]
    
    def add_active_game_object(self, key, new_game_object):
        self.active_game_objects[key] = new_game_object #TODO throw error if game object already exists
    
    def deactivate_game_object(self, key):
        self.active_game_objects[key].is_active=False
        del self.active_game_objects[key]
        
    async def update_current_game_state(self):
        game_state_broadcast_prompt = 'What is your current description? Answer in first person: I...'
        self.game_string = str(await self.send_same_broadcast(game_state_broadcast_prompt, keep_history=True))
    
    async def process_player_input(self, player_input):
        await self.add_to_progress_queue("\n\n<display_to_player>Received player input!\n</display_to_player>")
        
        if self.game_ended:
            await self.add_to_progress_queue("The game has ended!")
            return "The game has ended!", True
        
        game_object_names = list(self.active_game_objects.keys())
        if self.game_string == '': #not initialized
            await self.update_current_game_state()
            #otherwise, the game state from last iteration will suffice
        
        bluff, success = await asyncio.gather(self.sanity_bluff_check(player_input, game_object_names, self.game_string), self.ingame_success_check(player_input, game_object_names, self.game_string))
        #bluff = await self.sanity_bluff_check(player_input, game_object_names, self.game_string)
        #success = await self.ingame_success_check(player_input, game_object_names, self.game_string)
        
        if not bluff and success:
            json_example ='{'
            for s in game_object_names:
                json_example += f'"{s}": Move aside.'
            json_example += '}'
            
            order_prompt = f"It seems the player succeeded in their action. The action I'm talking about is {player_input}. What orders should be given to each game object?\
                Remember to include all game objects in your json response. These are the game objects:{str(game_object_names)}\
                In your json, Use only one string per game object. Do not nest properties. Include all game objects, except win and lose conditions.\
                Example of json format: {json_example}"
            await self.add_to_progress_queue("<display_to_player>##Giving orders to game objects after player success...##\n</display_to_player>")
            json_orders = await self._chat_with_backbone(order_prompt, self._my_history, json=True)
            dict_orders = self.comms_backbone.load_json_from_llm(json_orders)
            await self.send_broadcast(dict_orders)
        else:
            failure_prompt = f"It seems the player has failed in their action. The action I'm talking about is {player_input}. Please reflect on why they failed. There may be multiple causes. Pay special attention to mentions to objects that don't exist."
            await self.add_to_progress_queue("<display_to_player>##Reflecting on player failure...##\n</display_to_player>")
            await self._chat_with_backbone(failure_prompt, self._my_history)
            
        await self.add_to_progress_queue("<display_to_player>##Summarizing player action to all game objects...##\n</display_to_player>")
        broadcast_prompt = f"Relay the state of affairs as a result of the player's actions as a single message to all game objects. Make sure to include whether they were bluffing. Return a single text message summarizing what happened, not json."
        broadcast_message = await self._chat_with_backbone(broadcast_prompt, self._my_history)
        broadcast_message += '\n "Do not reply to this message. Merely use it for future responses"'
        await self.send_same_broadcast(broadcast_message)
        
        await self.update_current_game_state()
        
        response_prompt = f"This is the new state of every object in the game:{self.game_string}\
            This is the message that was sent to all game objects to tell them of the player's actions: {broadcast_message}\
            Relay the state of affairs as a result of the player's actions to the player. Include interesting details about the game state, but do not reveal information on the win and/or lose conditions of the game. If the player failed, explain why.\
            Do not reveal secret or confidential game information, such as a hidden object."
        await self.add_to_progress_queue("<display_to_player>##Generating response to the player...##\n</display_to_player>")
        response_to_player = await self._chat_with_backbone(response_prompt, self._my_history, keep_history=True)
        response_to_player = '\n\n' + response_to_player
        
        await self.add_to_progress_queue("<display_to_player>##Checking if the game has ended...##\n\n</display_to_player>")
        ending_message, has_ended = await self.check_ending()
        if has_ended:
            response_to_player += ending_message
        return response_to_player, has_ended

    async def sanity_bluff_check(self, player_input, game_object_names, game_state):
        await self.add_to_progress_queue("<display_to_player>##Checking for bluffs...##\n</display_to_player>")
        
        bluff_prompt = f"This is the input from the player: {player_input}\
            Please briefly answer each of the following questions:\
            Can the player reasonably perform the action they want?\
            Also consider this: Why would the action be impossible? This player is prone to bluffing, are they doing that now?\
            What questions need to be transmitted to each objects in the game, if any, in order to determine if the player is not making something up? These are the game objects:{str(game_object_names)}.\
            These are the game states for each object: {game_state}\
            Be specially watchful of the player inventing objects or features that do not exist and block that from happening.\
            Do not let the player ask for advice about win conditions, such as 'How do I win?' Or similar. Those are considered bluffs from the player.\
            However, don't forbid interactions for the sake of just intended player experience alone. If it's a possible and plausible action, allow it.\
            Do not block the player action because of danger. This is a game and the player should be able to put themselves in danger if they so choose."
        
        await self._chat_with_backbone(bluff_prompt, self.aux_bluff_history)
        bluff_answers = await self.ask_away(game_object_names, self.aux_bluff_history)
        
        bluff_eval_prompt = f"Here are the answers of each game object: {bluff_answers}.\n Is the player desired action ({player_input}) reasonable after all?"
        await self._chat_with_backbone (bluff_eval_prompt, self.aux_bluff_history)
        
        binary_bluff_prompt="Return wether the player had sucess in their action or not. Be strict. Return a json like {bluff:True} or {bluff:False}. Do not mention previous questions or answers, only a json with the \"bluff\" key and either the value True or the value False. The json should not start with curly braces." 
        return await self.get_binary_answer(binary_bluff_prompt, self.aux_bluff_history, 'bluff')
        
    async def ingame_success_check(self, player_input, game_object_names, game_state):
        await self.add_to_progress_queue("<display_to_player>##Checking for player success...##\n</display_to_player>")
        success_questions_prompt = f"What objects, if any, would be affected by the player's actions?\
            What questions, if any, would need to be asked of those game objects to determine if the player is able to perform their command?\
            The aim is to determine whether the player can do what he wants to do.\
            This is the list of game objects: {game_object_names}\
            This is the game state for each object: {game_state}\
            This is what the player said:{player_input}\
            Be brief. Avoid asking unnecessary questions."
        
        await self._chat_with_backbone(success_questions_prompt, self.aux_success_history)
        success_answers = await self.ask_away(game_object_names, self.aux_success_history)
        
        success_eval_prompt = f"These are the answers returned by each relevant game object {success_answers}. Reason about them a bit. Does the player manage to do what they want to (remember, that is \"{player_input}\")? Do they have the means?\
            If the answer is ambiguous, attribute success to the player. Lean towards player success. Player injury is not a reason for disallowing success."
        await self._chat_with_backbone(success_eval_prompt, self.aux_success_history)
        
        binary_success_prompt="Return wether the player had sucess in their action or not. Return a json like {success:True} or {success:False}. Do not mention anything else, only a json with the \"success\" key and either the value True or the value False. The value of the json should be true if the action is feasible to the player" 
        return await self.get_binary_answer(binary_success_prompt, self.aux_success_history, 'success')

    async def ask_away(self, game_object_names, history):        
        json_example ='{'
        for s in game_object_names:
            json_example += f'"{s}":What is your state? Is it possible to turn you into a frog?'
        json_example += '}'
        
        questions_prompt = f"Please transmit those same questions to each game object in json format.\
            Answer in json format for each object in the game. Say N/A if the question is not particularly relevant for the given object.\
            Prefer to say N/A\
            Remember to include all game objects in your json response. These are the game objects:{str(game_object_names)}\
            In your json, Use only one string per game object. Do not nest properties. Include all game objects.\
            Example of json format: {str(json_example)}. Only answer this json. Multiple json in the same response is a wrong answer!!\
            You can make more than one question per object. Make sure to include all the questions you thought of. Ask away!\
            \nMake sure you only ask questions, not statements."
            
        json_questions = await self._chat_with_backbone(questions_prompt, history, json=True)
        dict_questions = self.comms_backbone.load_json_from_llm(json_questions)
        dict_answers = await self.send_broadcast(dict_questions, keep_history=False)
        return str(dict_answers)

    async def check_ending(self):
        ending_prompt = "Now let's take a step back and evaluate if the player has achieved their final goal. Please don't respond, more details will be given in the next message"
        await self._chat_with_backbone (ending_prompt, self._my_history)
        
        ending_state_question = "What is your state?"
        #TODO somewhere before this assert that we do have a win condition
        win_condition_state = await self.active_game_objects['win_condition'].process_game_input(input_contents=ending_state_question, json=False, keep_history=True)
        
        win_prompt = f"This is the state of the condition: {win_condition_state}" + "If the state of 'win condition' says the player wins, say so.\
            Return a json like {won:True} or {won:False}. Do not mention anything else, only a json with the \"won\" key and either the value True or the value False."
        won = await self.get_binary_answer(win_prompt, self._my_history, 'won')
        if won:
            print (self.winning_message)
            await self.add_to_progress_queue(self.winning_message)
            self.game_ended=True
            return '\n' + self.winning_message, True
        elif 'loss_condition' in self.active_game_objects:
            loss_condition_state = await self.active_game_objects['loss_condition'].process_game_input(input_contents=ending_state_question, json=False, keep_history=True)
            loss_prompt = f"This is the state of the condition: {loss_condition_state}" + "If the state of 'lose condition' says the player loses, say so.\
            Return a json like {lost:True} or {lost:False}. Do not mention anything else, only a json with the \"lost\" key and either the value True or the value False."
            lost = await self.get_binary_answer(loss_prompt, self._my_history, 'lost')
            if lost:
                print(self.losing_message)
                await self.add_to_progress_queue(self.losing_message)
                self.game_ended = True
                return '\n' + self.losing_message, True
        return '', False
        
    async def send_same_broadcast(self, broadcast_message, keep_history=True):
        broadcast_dict = {}
        for k in self.active_game_objects.keys():
            broadcast_dict[k] = broadcast_message
        return await self.send_broadcast(broadcast_dict, keep_history)
        
    async def send_broadcast(self, dict_messages, keep_history=True):
        #keys of dict_messages should be the same as keys in self.active_game_objects
        await self.add_to_progress_queue("<display_to_player>##Querying gameobjects...##\n</display_to_player>")
        tasks = []
        for k, v in dict_messages.items():
            if "N/A" in v:
                continue
            tasks.append(self.active_game_objects[k].process_game_input(v, keep_history=keep_history, json=False))
        
        results = await asyncio.gather(*tasks)
        
        game_object_answers={}
        counter = 0
        for k, v in dict_messages.items():
            if "N/A" in v:
                continue
            game_object_answers[k] = results[counter]
            counter += 1
        
        return game_object_answers