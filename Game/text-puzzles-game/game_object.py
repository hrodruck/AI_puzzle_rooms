from copy import deepcopy
import asyncio
from backbone_comms import BackboneComms

class GameObject():
    
    def __init__(self):
        self.comms_backbone = BackboneComms()
        self.progress_queue = ''
        self._my_history=[]
        self.progress_lock = asyncio.Lock()
        self.processing_lock = asyncio.Lock()
        self.comms_backbone.model_string = "meta-llama/Llama-3.3-70B-Instruct-Turbo"
        #self.comms_backbone.model_string = "meta-llama/Meta-Llama-3.1-405B-Instruct"

        self.object_name = ''

    async def get_progress_queue(self):        
        async with self.progress_lock:
            async for item in self.comms_backbone.read_comms_queue():
                self.progress_queue += f'{self.object_name}: {item}\n.\n' #do not directly yield the item because there may be more data from add_to_progress_queue
                yield self.progress_queue
                self.progress_queue = ''
        await asyncio.sleep(0.02)
        
        
    async def _chat_with_backbone(self, user_message, user_history=[], json=False, keep_history=True):
        return await self.comms_backbone.chat_outer(user_message, user_history, json, keep_history)
        
    async def add_to_progress_queue(self, message):
        async with self.progress_lock:
            self.progress_queue += message

    async def process_game_input(self, input_contents, json=False, keep_history=True):
        if keep_history:
            async with self.processing_lock:
                reply = await self._chat_with_backbone(input_contents, self._my_history, json, keep_history)
        else: #no need for lock
            reply = await self._chat_with_backbone(input_contents, self._my_history, json, keep_history)
        return reply
        
    def set_system_message(self, message_contents):
        assert (len(self._my_history)==0)
        self._my_history.append({'role':'system', 'content':message_contents})
        
    
    def history_checkpoint(self):
        assert (len(self._my_history) % 3 ==0) #system, user, assistant
        self._checkpoint_len = len(self._my_history)
            
    def forget_old_history(self):
        assert (len(self._my_history) % 3 ==0) #system, user, assistant
        forgetting_len = self._checkpoint_len
        forgetting_len = min(forgetting_len, len(self._my_history)-3) #leave at least one (system, user, assitant) exchange. It will be the most recent one
        self._my_history = deepcopy(self._my_history[forgetting_len:])
        assert (len(self._my_history) % 3 ==0)
        print (len(self._my_history))