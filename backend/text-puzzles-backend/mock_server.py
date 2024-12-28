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
    '*',
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

# Mock game response
async def mock_game_response(command):
    return f"Processed command: {command}"

@app.post("/api/game")
async def game_endpoint(command: Command):
    # Mock the game response without actually calling game methods
    response = await mock_game_response(command.command)
    return {"response": response}

@app.post("/api/new-game")
async def start_game():
    # Mock starting a new game
    return {"status": "New game started"}

@app.post("/api/choose-room")
def choose_room(room: Room):
    # Mock choosing a room
    if isinstance(room.room, str):
        return {"status": f"Room chosen: {room.room}"}
    return {"status": "Room chosen"}

async def serve():
    port_number = int(os.getenv('GAME_SERVER_PORT_NUMBER'))
    await start_game()
    config = uvicorn.Config(app, host="0.0.0.0", port=port_number)
    server = uvicorn.Server(config)
    await server.serve()

if __name__ == "__main__":
    # Mock room selection
    app.state.room = {"description": "A dark room", "winning_message": "You win!", "losing_message": "Game over!"}
    asyncio.run(serve())