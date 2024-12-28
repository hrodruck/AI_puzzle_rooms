from engine import Game
from rooms import *
from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Union
import asyncio
import sys
import os
import uvicorn

app = FastAPI()

origins = [
    os.getenv('FRONTEND_CORS_IP'),
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def read_root():
    return FileResponse("static/index.html")

class Command(BaseModel):
    command: str
    
class Room(BaseModel):
    room: Union[dict[str, str], str]

@app.post("/api/game")
async def game_endpoint(command: Command):
    game = app.state.game
    response = await game.process_input(command.command)
    #response = await game.brazilian_portuguese_output(command.command)
    return {"response": response}

@app.post("/api/new-game")
async def start_game():
    app.state.game = Game()
    game = app.state.game
    room = app.state.room
    game.set_scene(room['description'], room['winning_message'], room['losing_message'])
    await game.start_game()

@app.post("/api/choose-room")
def choose_room(room: Room):
    if isinstance(room, Room):
        room = room.room
    if isinstance(room, str):
        app.state.room = rooms_dict[room]
    else: #room should be a dictionary
        app.state.room = room
    
    

async def serve():
    port_number = os.getenv('GAME_SERVER_PORT_NUMBER')
    await start_game()
    config = uvicorn.Config(app, host="0.0.0.0", port=port_number)
    server = uvicorn.Server(config)
    await server.serve()

if __name__ == "__main__":
    choose_room(rooms_dict['room_1'])
    asyncio.run(serve())
    