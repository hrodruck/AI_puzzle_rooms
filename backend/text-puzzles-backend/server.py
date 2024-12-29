from engine import Game
from rooms import rooms_dict
from fastapi import FastAPI, Request, Depends
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import Union, Dict, Any
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

class Command(BaseModel):
    command: str
    
class Room(BaseModel):
    room: Union[str, Dict[str, Any]] = Field(..., description="Either a pre-made room name (string) or a custom room description (dictionary)")

sessions = {}

async def get_session(request: Request):
    session_id = request.cookies.get("session_id")
    if not session_id:
        session_id = os.urandom(24).hex()  # Generate a new session ID if none exists
        # Instead of returning JSONResponse, we'll set the cookie in the route handler
        sessions[session_id] = {"game": Game(), "room": None}
        return {"new_session": True, "session_id": session_id}
    if session_id not in sessions:
        sessions[session_id] = {"game": Game(), "room": None}
    return sessions[session_id]

@app.post("/api/game")
async def game_endpoint(command: Command, session: dict = Depends(get_session)):
    game = session['game']
    room = session['room']
    if room is None:
        return JSONResponse(content={"status": "error", "message": "No room selected"})
    game.set_scene(room['description'], room['winning_message'], room['losing_message'])
    response = await game.process_input(command.command)
    return JSONResponse(content={"status": "success", "response": response})

@app.post("/api/new-game")
async def start_game(request: Request, session: dict = Depends(get_session)):
    session['game'] = Game()  # Reset the game for this session
    room = session['room']
    if room is None:
        return JSONResponse(content={"status": "error", "message": "No room selected"})
    
    game = session['game']
    game.set_scene(room['description'], room['winning_message'], room['losing_message'])
    await game.start_game()
    
    response = JSONResponse(content={"status": "success", "message": "New game started"})
    
    # Set cookie for new sessions
    if 'new_session' in session:
        response.set_cookie(key="session_id", value=session['session_id'], samesite="None", secure=True)
    
    return response

@app.post("/api/choose-room")
async def choose_room(room: Room, session: dict = Depends(get_session)):
    try:
        if isinstance(room.room, dict):
            session['room'] = room.room
            return JSONResponse(content={"status": "success", "message": "Chose custom room"})
        else:
            session['room'] = rooms_dict[room.room]
            return JSONResponse(content={"status": "success", "message": f"Room chosen: {room.room}"})
    except KeyError:
        return JSONResponse(content={"status": "error", "message": "Room not found"}, status_code=404)

app.mount("/", StaticFiles(directory="static", html=True), name="static")

async def serve():
    port_number = int(os.getenv('GAME_SERVER_PORT_NUMBER'))
    config = uvicorn.Config(app, host="0.0.0.0", port=port_number)
    server = uvicorn.Server(config)
    await server.serve()

if __name__ == "__main__":
    asyncio.run(serve())