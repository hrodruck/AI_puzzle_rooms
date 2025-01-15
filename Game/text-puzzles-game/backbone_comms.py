from copy import deepcopy
import asyncio
import os
import re
import json
from ollama import AsyncClient
from openai import AsyncOpenAI
    
class BackboneComms():    
    
    def __init__(self):
        self._comms_queue = ''
        self.progress_lock = asyncio.Lock()
        self.openai_backbone = bool(os.getenv('USE_EXTERNAL_BACKBONE'))
        self.presence_penalty = 1.0 #maybe that's specific to deepinfra?
        self.presence_penalty_json = 2.0 #maybe that's specific to deepinfra?
    
    
    async def read_comms_queue(self):
        async with self.progress_lock:
            if len(self._comms_queue)>0:
                yield self._comms_queue
                self._comms_queue = ''
        await asyncio.sleep(0.02)

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
        
        #model_str = "meta-llama/Llama-3.3-70B-Instruct-Turbo" #this one works
        model_str = "Qwen/Qwen2.5-72B-Instruct" #maybe faster for being less verbose
        
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
        return content #this can be changed if necessary to yield chunks of stream, not done currently bc API is fast enough and this change is not priority

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
        print('.')  # Add a separator after the response
        return full_response #this can be changed if necessary to yield chunks of stream, not done currently to align with openai backbone
    
    async def _chat_inner(self, history, json=False):
        if self.openai_backbone:
            response = await self.chat_openai_backbone(history, json)
        else:
            response = await self.chat_ollama_backbone(history, json)
        async with self.progress_lock:
            self._comms_queue += f"\n{response}"
        return response

    async def chat_outer(self, user_message, user_history=[], json=False, keep_history=True):
        #the first message should be the system prompt
        assert(user_history[0]['role']=='system')
        if keep_history:
                if len(user_history)>1:
                    user_history.append(user_history[0])
                user_history.append(
                    {'role': 'user', 'content':user_message}
                )
                response = await self._chat_inner(user_history, json)
                user_history.append({'role': 'assistant', 'content': response})
        else:
            '''Important! there may be some bug in this path. Setting keep_history as true everywhere for now...'''
            history_len = len(user_history)
            temp_history = deepcopy(user_history)
            #repeat system prompt if it's not the first history entry, checking if len(user_history)>1
            if len(temp_history)>1:
                temp_history.append(temp_history[0])
            temp_history.append(
                {'role': 'user', 'content':user_message}
            )
            response = await self._chat_inner(temp_history, json)
            assert(len(user_history) == history_len)
        return response