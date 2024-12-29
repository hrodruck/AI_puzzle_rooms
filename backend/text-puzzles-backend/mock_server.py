from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import Union, Dict, Any
import asyncio
import sys
import os
import uvicorn
import json

app = FastAPI()

# Mock data for rooms
rooms_dict = {
    "room1": {"description": "Description of room1", "winning_message": "You win!", "losing_message": "You lose!"},
    "room2": {"description": "Description of room2", "winning_message": "Victory!", "losing_message": "Defeat!"}
}

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

class Command(BaseModel):
    command: str
    
class Room(BaseModel):
    room: Union[str, Dict[str, Any]] = Field(..., description="Either a pre-made room name (string) or a custom room description (dictionary)")

@app.post("/api/game")
async def game_endpoint(command: Command):
    # Mocking game response
    return {"response": f"Processed command: {command.command}"}

@app.post("/api/new-game")
async def start_game():
    # Mocking game start
    app.state.room = rooms_dict["room1"]  # Using room1 as default
    return {"status": "New game started"}

@app.post("/api/choose-room")
def choose_room(room: Room):
    if isinstance(room.room, dict):
        # Handling custom room
        app.state.room = room.room
        return {"status": f"Chose custom room"}
    else:
        # Handling pre-made room
        app.state.room = rooms_dict.get(room.room, {"description": "Unknown Room", "winning_message": "Default win", "losing_message": "Default lose"})
        return {"status": f"Room chosen: {room.room}"}


app.mount("/", StaticFiles(directory="static", html=True), name="static")

async def serve():
    port_number = int(os.getenv('GAME_SERVER_PORT_NUMBER'))
    config = uvicorn.Config(app, host="0.0.0.0", port=port_number)
    server = uvicorn.Server(config)
    await server.serve()

if __name__ == "__main__":
    asyncio.run(serve())