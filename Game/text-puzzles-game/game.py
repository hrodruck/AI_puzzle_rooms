import asyncio
import json
import copy
import os
import re
from engine_game_object import EngineGameObject
from game_object import GameObject

class Game():

    def __init__(self):
        self.game_ended = False
        self.game_progress_queue = ''
        self.progress_lock = asyncio.Lock()
        self.game_objects = {}
        self.engine_game_object = None
        print ("Engine is running. Use set_scene and start_game!")

    async def get_progress_queue(self):
        if not self.game_ended:
            async with self.progress_lock:
                if self.engine_game_object is not None:
                    async for item in self.engine_game_object.get_progress_queue():
                        self.game_progress_queue += item #do not directly yield the item because there may be more data from add_to_progress_queue
                        yield self.game_progress_queue
                        self.game_progress_queue = ''
                        await asyncio.sleep(0.02)
                for k, v in self.game_objects.items():
                    async for item in self.game_objects[k].get_progress_queue():
                        self.game_progress_queue += item
                        yield self.game_progress_queue
                        self.game_progress_queue = ''
                        await asyncio.sleep(0.02)
        else:
            raise StopAsyncIteration
        
    async def add_to_progress_queue(self, message):
        async with self.progress_lock:
            self.game_progress_queue += message

    def set_scene(self, scene_description, winning_message= None, losing_message=None):
        if 'prompts' in scene_description.keys(): #else, it's the legacy rooms that only contain prompts directly
            self.scene_objects_prompts = scene_description['prompts']
            self.scene_objects_resposibilities = scene_description['responsibilities']
        else:
            self.scene_objects_prompts = scene_description
            self.scene_objects_resposibilities = None
        assert (self.scene_objects_resposibilities == None or self.scene_objects_resposibilities.keys() ==  self.scene_objects_prompts.keys())
        self.winning_message = winning_message
        self.losing_message = losing_message

    async def initialize_game_objects(self):    
        await self.add_to_progress_queue('<display_to_player> Filling room with objects...\n</display_to_player>')        
        designer_assistant_prompt = 'You are an assistant game designer. Please keep your answers brief whenever possible.'
        designer_user_prompt = "I am designing a text adventure in which the goal is to escape a room. I will provide brief descriptions of each object in the room and your task is to fill those descriptions such that they are usable in game format. When prompted, answer only the latest description"
        designer_assistant = GameObject()
        designer_assistant.set_system_message(designer_assistant_prompt)
        await designer_assistant.process_game_input(designer_user_prompt)
        
        game_object_template = 'You simulate an object within a scene for a videogame. Keep track of your own description, using common sense to answer questions about the object or change it. Do not spontaneously add characteristics to the simulated object without being provoked to do so. Do not disappear after being used. The object you simulate is a <object_name>. Your initial description is \"<my_description>\". That initial description might have changed. Important! Minimize changes when updating your state when possible'
        game_object_template += '\nBe extremely brief'
        #initialize all gameobjects first so the dictionary size doesn't change during polling game progress
        for k, v in self.scene_objects_prompts.items():
            self.game_objects[k] = GameObject()
            self.game_objects[k].object_name = k
        
        tasks = []
        for k, v in self.scene_objects_prompts.items():            
            applied_game_object_template = game_object_template
            applied_game_object_template = applied_game_object_template.replace('<object_name>', k)
            applied_game_object_template = applied_game_object_template.replace('<my_description>', v)
            self.game_objects[k].set_system_message(applied_game_object_template)
            tasks.append(designer_assistant.process_game_input(f'This is the general instruction for the current game object:\n\n {applied_game_object_template}\n\n. As an assistant game designer, determine the initial description for that game object. ', keep_history=False))
        designer_descriptions = await asyncio.gather(*tasks)
        
        tasks = []
        for key, description in zip (self.game_objects.keys(), designer_descriptions):
            tasks.append(self.game_objects[key].process_game_input(f'this is your current state:"{description}"'))
        await asyncio.gather(*tasks)
        
        
    async def get_game_state(self):
        await self.add_to_progress_queue('<display_to_player>Computing game state...\n</display_to_player>')
        tasks = []
        summarization_prompt = 'What is your current state? Answer in first person: I...'
        
        for k, v in self.game_objects.items():
            tasks.append(v.process_game_input(summarization_prompt, keep_history=True))
        results = await asyncio.gather(*tasks)

        game_state = {k: result for k, result, v in zip(self.game_objects.keys(), results, self.game_objects.values())}

        return game_state
            
    async def initialize_engine_simulator(self):
        await self.add_to_progress_queue('<display_to_player>Initializing game engine...\n</display_to_player>')
        game_engine_sys_prompt = 'You are a text game engine simulator. Your task is to reply using common sense to the questions about the player\'s text input to the game. I am the game designer. DO NOT add details or descriptions to any aspect of the game. Creating extra details is extraneous and detracts from the game experience. Be brief and concise in all your statements. You are called "game engine".'
        game_string = str(await self.get_game_state())
        for key in self.game_objects.keys():
            asyncio.create_task(self.game_objects[key].process_game_input(f'this the state of all objects:"{game_string}"'))
        
        engine_initialization_prompt= ''
        if self.scene_objects_resposibilities != None:
            engine_initialization_prompt += f'This is every object in the room and their roles within the game: {str(self.scene_objects_resposibilities)}\n'
        engine_initialization_prompt += f'This is the current game state: {game_string}'
        self.engine_game_object = EngineGameObject()
        self.engine_game_object.set_system_message(game_engine_sys_prompt)
        self.engine_game_object.winning_message = self.winning_message
        self.engine_game_object.losing_message = self.losing_message
        await self.engine_game_object.process_game_input(engine_initialization_prompt)
        for k, v in self.game_objects.items():
            self.engine_game_object.add_active_game_object(k, v)
        self.engine_game_object.game_string = game_string
        self.engine_game_object.object_name = 'game_engine'
        if self.scene_objects_resposibilities != None:
            self.engine_game_object.roles_string = str(self.scene_objects_resposibilities)
        else:
            self.engine_game_object.roles_string = ''
            
    async def process_input(self, p_in):
        player_response, has_ended = await self.engine_game_object.process_player_input(p_in)
        self.game_ended = has_ended
        return player_response
    
        
    async def start_game(self):
        await self.initialize_game_objects()
        await self.initialize_engine_simulator()