import asyncio
from backbone_comms import BackboneComms

class GameObject():
    
    def __init__(self):
        self.comms_backbone = BackboneComms()
        self.progress_queue = ''
        self._my_history=[]
        self.progress_lock = asyncio.Lock()

    async def get_progress_queue(self):        
        async with self.progress_lock:
            async for item in self.comms_backbone.read_comms_queue():
                self.progress_queue += item #do not directly yield the item because there may be more data from add_to_progress_queue
                yield self.progress_queue
                self.progress_queue = ''
        await asyncio.sleep(0.1)
        
        
    async def _chat_with_backbone(self, user_message, user_history=[], json=False, keep_history=True):
        return await self.comms_backbone.chat_outer(user_message, user_history, json, keep_history)
        
    async def add_to_progress_queue(self, message):
        async with self.progress_lock:
            self.progress_queue += message

    async def process_game_input(self, input_contents, json=False, keep_history=True):
        return await self._chat_with_backbone(input_contents, self._my_history, json, keep_history)
        
    def set_system_message(self, message_contents):
        if len(self._my_history)==0:
            self._my_history.append({'role':'system', 'content':message_contents})
        else:
            self._my_history[0] = {'role':'system', 'content':message_contents}