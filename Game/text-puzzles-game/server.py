from engine import Game
from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict, Any
import os
import asyncio
import uvicorn

app = FastAPI()

origins = [
    os.getenv('MAIN_SERVER_IP'),
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

class RoomData(BaseModel):
    room: Dict[str, Any]
    session_id: str

class CommandData(BaseModel):
    command: str
    session_id: str
    
class SessionData(BaseModel):
    session_id:str

# This session management is simplified since it's only for Game processing
sessions = {}
game_progress = {}

async def get_game_from_session(session_id: str):
    return sessions[session_id]
    
async def new_session(session_id: str, game: Any):
    sessions[session_id] = game #this is stored indefinetely in memory for now
    game_progress[session_id]=''
    async for progress in game.get_progress_queue(): #the game instance clears the queue on its own
        if len(progress)>0:
            game_progress[session_id] += progress
        await asyncio.sleep(0.1)

async def get_game_progress(session_id:str):
    if session_id in sessions.keys():
        progress = game_progress[session_id]
        game_progress[session_id]='' #TODO there might be race conditions with setting game progress elsewhere
        return progress
    else:
        return ''
    
#endpoints
@app.post("/api/game-progress")
async def game_progress_endpoint(data: SessionData):
    session_id = data.session_id
    progress = await get_game_progress(session_id)
    return JSONResponse(content={"status": "success", "response": progress})
    

@app.post("/api/process-input")
async def process_input(data: CommandData):
    game = await get_game_from_session(data.session_id)
    print(data.session_id)
    response = await game.process_input(data.command)
    return JSONResponse(content={"status": "success", "response": response})

@app.post("/api/start-game")
async def start_game(data: RoomData):
    try:
        session_id = data.session_id
        game = Game() #start a new instance anyways, since the player could be restarting their game
        asyncio.create_task(new_session(session_id, game))
        room = data.room
        room_description = room['description']
        room_description.pop('customObjects', None) #weirdness from the frontend regarding custom rooms
        room_description.pop('winning_message', None)
        room_description.pop('losing_message', None)
        game.set_scene(room_description, room['winning_message'], room['losing_message'])
        print(f"{session_id=}")
        await game.start_game()
        return JSONResponse(content={"status": "success", "message": "New game started!"})
    except Exception as e:
        print(e)
        return JSONResponse(content={"status": "error", "message": "Could not start new game, please try again."})

async def serve():
    port_number = int(os.getenv('GAME_SERVER_PORT_NUMBER'))
    config = uvicorn.Config(app, host="0.0.0.0", port=port_number)
    server = uvicorn.Server(config)
    await server.serve()

if __name__ == "__main__":
    asyncio.run(serve())
    
# Note: This server only needs to manage game state, not room selection or session creation