from engine import Game
from rooms import *
from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import Union
import asyncio
import sys
import uvicorn

app = FastAPI()

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
    await start_game()
    if len(sys.argv)<2:
        print('please specify port number as an argument to the server script')
    else:
        port_number = int(sys.argv[1])
        config = uvicorn.Config(app, host="0.0.0.0", port=port_number)
        server = uvicorn.Server(config)
        await server.serve()

if __name__ == "__main__":
    choose_room(rooms_dict['room_1'])
    asyncio.run(serve())
    