import asyncio
from copy import deepcopy
from game_object import GameObject

class EngineGameObject(GameObject):

    def __init__(self):
        super().__init__()
        self.game_ended = False
        self.active_game_objects = {}
        self.aux_bluff_history = []
        self.aux_success_history = []
        self.winning_message = '' #set externally
        self.losing_message = '' #set externally
        self.game_string = '' #set internally later
        self.comms_backbone.model_string = "meta-llama/Llama-3.3-70B-Instruct-Turbo"
        #self.comms_backbone.model_string = "meta-llama/Meta-Llama-3.1-405B-Instruct"
        self.round_counter = 0
        self.update_game_state_task = None
        self.roles_string = ''
    
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
        game_state_broadcast_prompt = f'This is the new state of the room: {self.game_string}. Update yourself accordingly. As an answer, reply your new description.'
        self.game_string = str (await self.send_same_broadcast(game_state_broadcast_prompt, keep_history=True))
        
    
    async def process_player_input(self, player_input):
        await self.add_to_progress_queue("\n\n<display_to_player>Received player input!\n</display_to_player>")
        
        if self.game_ended:
            await self.add_to_progress_queue("The game has ended!")
            return "The game has ended!\n\n", True
        
        #if self.round_counter % 2 == 0:
        self.history_checkpoint()
        for k, v in self.active_game_objects.items():
            v.history_checkpoint() 
        
        self.aux_bluff_history = deepcopy(self._my_history)
        self.aux_success_history = deepcopy(self._my_history)
        my_history_initial_len = len(self._my_history)
        
        multiple_actions_prompt = f'Is the player trying to perform multiple actions with a single input? Their input was {player_input}. Lean towards saying the player performed one action. That is, if you\'re not sure, consider it to be one action.' +  'Return a json like {multiple:True} or {multiple:False} to indicate whether the player has performed multiple actions.'
        multiple_actions = await self.get_binary_answer(multiple_actions_prompt, self._my_history, 'multiple')
        if multiple_actions:
            return 'Please perform one action per turn\n', False
        
        
        #related to the speed optimization
        if self.round_counter > 0:
            self.game_string = await self.update_game_state_task
        
        self.aux_bluff_history = deepcopy(self._my_history)
        self.aux_success_history = deepcopy(self._my_history)
        my_history_initial_len = len(self._my_history)
        
        multiple_actions_prompt = f'Is the player trying to perform multiple actions with a single input? Their input was {player_input}. Lean towards saying the player performed one action. That is, if you\'re not sure, consider it to be one action.' +  'Return a json like {multiple:True} or {multiple:False} to indicate whether the player has performed multiple actions.'
        multiple_actions = await self.get_binary_answer(multiple_actions_prompt, self._my_history, 'multiple')
        if multiple_actions:
            return 'Please perform one action per turn\n', False
        
        '''
        #related to the speed optimization
        if self.round_counter > 0:
            self.game_string = await self.update_game_state_task
        '''
        game_object_names = list(self.active_game_objects.keys())
        
        tasks = [self.sanity_bluff_check(player_input, game_object_names, self.game_string), self.sanity_bluff_check(player_input, game_object_names, self.game_string), self.ingame_success_check(player_input, game_object_names, self.game_string)]
        bluff_1, bluff_2, success = await asyncio.gather(*tasks)
        bluff = bluff_1 or bluff_2 #this is to mitigate cases where the engine might detect a false negative bluff.
        
        response_prompt = ''
        
        response_prompt = ''
        
        if not bluff and success:
            await self.add_to_progress_queue("<display_to_player>You succeeded in your action! Pondering consequences...\n</display_to_player>")
            
            await self.add_to_progress_queue("<display_to_player>##Updating game state...##\n</display_to_player>")
            self.game_string = str(await self.send_same_broadcast(f"It seems the player did an action. The action I'm talking about is {player_input}. Reply to this message with your new state."))
            await self.update_current_game_state()
            response_prompt += f"This is the state of every object in the game at the end of the round:{self.game_string}\n."
        else:
            await self.add_to_progress_queue("<display_to_player>You failed in your action! Reflecting on causes...\n</display_to_player>")
            if bluff:
                self.aux_failure_history = self.aux_bluff_history[my_history_initial_len:]
            else: #that is, "if not sucess"
                self.aux_failure_history = self.aux_success_history[my_history_initial_len:]
            failure_prompt = f"It seems the player has failed in attempting an action. The action I'm talking about is {player_input}. Reflect on the reasons for this failure."
            failure_reasoning = await self._chat_with_backbone(failure_prompt, self.aux_failure_history, keep_history=False)
            response_prompt += f'These seem to have been the reasons for player failure: {failure_reasoning}\n'
        
        response_prompt += "Relay the state of affairs as a result of the player's actions to the player. Include interesting details about the game state, but do not reveal information on the win and/or lose conditions of the game. If the player failed, explain why that failure happened or why it was considered a bluff.\
            Do not reveal secret or confidential game information, such as a hidden object.\
            If any gameobject has spoken to the player, relay the game object's message verbatim, word-by-word, as part of your response.\
            Do not talk to the player as if you're in a game. Maintain the illusion of fantasy!\
            Remember the player's initial command: {player_input}."
        
        response_to_player = await self._chat_with_backbone(response_prompt, self._my_history, keep_history=True)
        response_to_player = '\n\n' + response_to_player
        
        ending_message, has_ended = await self.check_ending()
        if has_ended:
            response_to_player += ending_message
        
        #if self.round_counter % 2 == 1:
        self.forget_old_history()
        for k, v in self.active_game_objects.items():
            v.forget_old_history()
        
        #Speed optimization: the game objects update asynchronously while the player reads the message from the game and decides what to do
        self.update_game_state_task = asyncio.create_task(self.send_same_broadcast(f'This is what the game engine said to the player this round: {response_to_player}\n. Consider those events.'))
        
        
        self.round_counter += 1
        
        return response_to_player, has_ended

    async def sanity_bluff_check(self, player_input, game_object_names, game_state):
        await self.add_to_progress_queue("<display_to_player>##Checking for bluffs...##\n</display_to_player>")
        
        bluff_prompt = f"This is the input from the player: {player_input}.\
            Please briefly answer each of the following questions:\
            Can the player reasonably perform the action they want? Why would the action be impossible? This player is prone to bluffing, are they doing that now?\
            What questions need to be transmitted to each objects in the game, if any, in order to determine if the player is not making something up? These are the game states for each object: {game_state}\ These are the game objects:{str(game_object_names)}.\n Consider the role of each object in the game. {self.roles_string}\n \
            Remember, only ask questions needed to determine if the player is bluffing. Other questions are not necessary.\
            Do not ask if the player did their action. Only attempt to determine if the player is able to to their action. Only the potential capacity for the action should be investigated. Avoid questions such as 'is the player...?'. If necessary, ask 'can the player...?'\
            Be specially watchful of the player inventing objects or features that do not exist and block that from happening.\
            Do not let the player ask for advice about win conditions, such as 'How do I win?' Or similar. Those are considered bluffs from the player.\
            However, don't forbid interactions for the sake of just intended player experience alone. If it's a possible and plausible action, allow it.\
            Do not block the player action because of danger. This is a game and the player should be able to put themselves in danger if they so choose.\
            Be brief and concise in all your statements."

        bluff_examples_prompt = "Commands that would make the player bypass challenges such as:\
                                'I win'\
                                'I solve the riddle'\
                                'I defeat the enemy'\
                                "

        
        await self._chat_with_backbone(bluff_prompt, self.aux_bluff_history)
        bluff_answers = await self.ask_away(game_object_names, self.aux_bluff_history, player_input)
        
        bluff_eval_prompt = f"Here are the answers of each game object: {bluff_answers}.\n Is the player desired action ({player_input}) reasonable after all?\
            However, if the player is relying on knowledge they don't possess, that is a bluff.\
            Do not let the player perform actions such as the following, they are bluffs:{bluff_examples_prompt}."
            
        
        await self._chat_with_backbone (bluff_eval_prompt, self.aux_bluff_history)
        
        binary_bluff_prompt="Return wether the player was bluffing or not. Return a json like {bluff:True} or {bluff:False}. Do not mention previous questions or answers, only a json with the \"bluff\" key and either the value True or the value False. Your response should be based on your previous reasoning." 
        return await self.get_binary_answer(binary_bluff_prompt, self.aux_bluff_history, 'bluff')
        
    async def ingame_success_check(self, player_input, game_object_names, game_state):
        await self.add_to_progress_queue("<display_to_player>##Checking for player success...##\n</display_to_player>")
        success_questions_prompt = f"What objects, if any, would be affected by the player's actions?\
            What questions, if any, would need to be asked of those game objects to determine if the player is able to perform their command?\
            The aim is to determine whether the player can do what he wants to do.\
            This is the list of game objects: {game_object_names}\
            This is the game state for each object: {game_state} \n Consider the role of each object in the game. {self.roles_string}\n\
            Remember, only ask questions needed to determine if the player can do what they want within game rules. Other questions are not necessary.\
            Do not ask if the player did their action. Only attempt to determine if the player is able to to their action. Only the potential capacity for the action should be investigated.  Avoid questions such as 'is the player...?'. If necessary, ask 'can the player...?'\
            This is what the player said:{player_input}.\
            Be brief and concise in all your statements."
        
        await self._chat_with_backbone(success_questions_prompt, self.aux_success_history)
        success_answers = await self.ask_away(game_object_names, self.aux_success_history, player_input)
        
        success_eval_prompt = f"These are the answers returned by each relevant game object {success_answers}. Reason about them a bit. Does the player manage to do what they want to (remember, that is \"{player_input}\")? Do they have the means?\
            If the answer is ambiguous, attribute success to the player. Lean towards player success. Player injury is not a reason for disallowing success."
        await self._chat_with_backbone(success_eval_prompt, self.aux_success_history)
        
        binary_success_prompt="Return wether the player had sucess in their action or not. Return a json like {success:True} or {success:False}. Do not mention anything else, only a json with the \"success\" key and either the value True or the value False. Your response should be based on your previous reasoning." 
        return await self.get_binary_answer(binary_success_prompt, self.aux_success_history, 'success')

    async def ask_away(self, game_object_names, history, player_input):        
        json_example ='{'
        for s in game_object_names:
            json_example += f'"{s}":What is your state? Is it possible to turn you into a frog?'
        json_example += '}'
        
        questions_prompt = f"Please transmit those same questions to each game object in json format.\
            Answer in json format for each object in the game. Say N/A if the question is not particularly relevant for the given object. Heavily prefer saying N/A. Be very brief.\
            Remember to include all game objects in your json response. These are the game objects:{str(game_object_names)}\
            Consider the role each game object playes in the game. {self.roles_string}\
            In your json, Use only one string per game object. Do not nest properties. Include all game objects.\
            Example of json format: {str(json_example)}. Only answer this json. Multiple json in the same response is a wrong answer!!\
            You can make more than one question per object. Make sure to include all the questions you thought of. Ask away!\
            \nMake sure you only ask questions, not statements."
            
        json_questions = await self._chat_with_backbone(questions_prompt, history, json=True)
        dict_questions = self.comms_backbone.load_json_from_llm(json_questions)
        for k, v in dict_questions.items():
            v += f'\nThis was the player input: {player_input}\n'
        dict_answers = await self.send_broadcast(dict_questions, keep_history=False)
        return str(dict_answers)

    async def check_ending(self):
        ending_prompt = "Now let's take a step back and evaluate if the player has achieved their final goal in the game as a whole.\n"
        
        win_prompt = ending_prompt + f"Looking at the state of all game objects,\n {self.game_string}, consider the state of the win_condition" + "If the state of win_condition indicates the player wins, say so.\
            Return a json like {won:True} or {won:False}. Do not mention anything else, only a json with the \"won\" key and either the value True or the value False."
        won = await self.get_binary_answer(win_prompt, self._my_history, 'won')
        if won:
            print (self.winning_message)
            await self.add_to_progress_queue(self.winning_message)
            self.game_ended=True
            return '\n' + self.winning_message, True
        elif 'loss_condition' in self.active_game_objects.keys():
            loss_prompt = ending_prompt + f"Looking at the state of all game objects,\n {self.game_string}, consider the state of the loss_condition." + "If the state of 'loss condition' indicates the player loses, say so.\
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