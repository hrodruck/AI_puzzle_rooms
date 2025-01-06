from fastapi import FastAPI, Request, Depends
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from starlette.exceptions import HTTPException
from starlette.responses import FileResponse
from pydantic import BaseModel, Field
from typing import Union, Dict, Any
from pathlib import Path
from rooms import rooms_dict
import asyncio
import os
import uvicorn
import httpx

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

async def get_session(request: Request) -> Dict:
    session_id = request.cookies.get("session_id")
    if not session_id:
        session_id = os.urandom(24).hex()
        sessions[session_id] = {"room": None, "session_id": session_id}
    if session_id not in sessions:
        sessions[session_id] = {"room": None, "session_id": session_id}
    print (f'Main server: {session_id=}')
    return sessions[session_id]

@app.post("/api/game")
async def game_endpoint(command: Command, session: Dict = Depends(get_session)):
    if session['room'] is None:
        return JSONResponse(content={"status": "error", "message": "No room detected. Please try selecting again"})
    
    async with httpx.AsyncClient(timeout=None) as client:
        response = await client.post(f"http://{os.getenv('GAME_SERVER_IP')}:{os.getenv('GAME_SERVER_PORT_NUMBER')}/api/process-input", 
                                     json={"command": command.command, "session_id": session.get('session_id')})
        return JSONResponse(content=response.json())

@app.post("/api/new-game")
async def start_game(request: Request, session: Dict = Depends(get_session)):    
    if session['room'] is None:
        return JSONResponse(content={"status": "error", "message": "No room detected. Please try selecting again"})
    print (f"starting game from session {session.get('session_id')}")
    async with httpx.AsyncClient(timeout=None) as client:
        response = await client.post(f"http://{os.getenv('GAME_SERVER_IP')}:{os.getenv('GAME_SERVER_PORT_NUMBER')}/api/start-game", 
                                     json={'room': session['room'], "session_id": session.get('session_id')})
        resp = JSONResponse(content=response.json())
        return resp
        

@app.post("/api/choose-room")
async def choose_room(room: Room, session: Dict = Depends(get_session)):
    try:
        if isinstance(room.room, dict):
            session['room'] = room.room
            resp = JSONResponse(content={"status": "success", "message": "Chose custom room"})
        else:
            session['room'] = rooms_dict[room.room]['room']
            resp = JSONResponse(content={"status": "success", "message": f"Room chosen: {room.room}"})
        resp.set_cookie(key="session_id", value=session.get('session_id'), samesite="lax", secure=True)
        return resp
    except KeyError:
        return JSONResponse(content={"status": "error", "message": "Room not found"}, status_code=404)

@app.exception_handler(HTTPException)
async def custom_http_exception_handler(request: Request, exc: HTTPException):
    if exc.status_code == 404:
        return FileResponse("static/index.html")
    return JSONResponse(content={"status": "error", "message": "An error occurred"}, status_code=exc.status_code)

app.mount("/", StaticFiles(directory="static", html=True), name="static")


async def serve():
    port_number = int(os.getenv('MAIN_SERVER_PORT_NUMBER'))
    config = uvicorn.Config(app, host="0.0.0.0", port=port_number, ssl_keyfile=os.getenv('SSL_KEYFILE_PATH'), ssl_certfile=os.getenv('SSL_CERTFILE_PATH'))
    server = uvicorn.Server(config)
    await server.serve()

if __name__ == "__main__":
    asyncio.run(serve())
    