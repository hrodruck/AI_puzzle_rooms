from fastapi import FastAPI, Request, Depends
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import Union, Dict, Any
import asyncio
import os
import uvicorn
import httpx


TENSORDOCK_API_KEY = os.getenv('TENSORDOCK_API_KEY')
TENSORDOCK_API_URL = "https://console.tensordock.com/api/v1"

class TensorDockInstance:
    def __init__(self, id: str, ip: str, gpu_type: str):
        self.id = id
        self.ip = ip
        self.gpu_type = gpu_type

async def find_and_start_instance(gpu_type: str) -> TensorDockInstance:
    async with httpx.AsyncClient() as client:
        # Authentication header
        headers = {
            "Authorization": f"Bearer {TENSORDOCK_API_KEY}"
        }
        
        # Query for available GPUs. This is a mock endpoint; adjust according to actual API documentation.
        response = await client.get(f"{TENSORDOCK_API_URL}/gpu/availability", headers=headers)
        response.raise_for_status()  # Check for errors
        available_gpus = response.json()['available_gpus']  # Assuming response format
        
        # Find available GPU of the specified type
        matching_gpus = [gpu for gpu in available_gpus if gpu['type'] == gpu_type]
        if not matching_gpus:
            raise ValueError(f"No available {gpu_type} GPUs")

        # Deploy a server with the matching GPU
        deploy_payload = {
            "gpu_type": gpu_type,
            "os": "Ubuntu 20.04",  # Example OS
            "vcpu": 4,
            "ram": 8  # Example config
        }
        
        deploy_response = await client.post(f"{TENSORDOCK_API_URL}/servers", headers=headers, json=deploy_payload)
        deploy_response.raise_for_status()
        
        deployed_server = deploy_response.json()
        
        return TensorDockInstance(
            id=deployed_server['id'],
            ip=deployed_server['ip'],
            gpu_type=gpu_type
        )

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
        sessions[session_id] = {"room": None}
        return {"new_session": True, "session_id": session_id}
    if session_id not in sessions:
        sessions[session_id] = {"room": None}
    return sessions[session_id]

@app.post("/api/game")
async def game_endpoint(command: Command, session: dict = Depends(get_session)):
    if session['room'] is None:
        return JSONResponse(content={"status": "error", "message": "No room selected"})
    
    async with httpx.AsyncClient() as client:
        response = await client.post(f"http://{TENSORDOCK_GPU_SERVER_IP}/api/process-input", 
                                     json={"command": command.command, "session_id": session_id})
        return JSONResponse(content=response.json())

@app.post("/api/new-game")
async def start_game(request: Request, session: dict = Depends(get_session)):
    if session['room'] is None:
        return JSONResponse(content={"status": "error", "message": "No room selected"})
    
    try:
        # Start a new GPU server instance
        instance = await find_and_start_instance("RTX 3090")  # Example GPU type
        print(f"Started new instance at {instance.ip}")
        
        # Here, you would typically save instance details to session or database for later use
        session['gpu_instance'] = instance.__dict__
        
        # Now, communicate with this instance for game logic
        async with httpx.AsyncClient() as client:
            response = await client.post(f"http://{instance.ip}/api/start-game", 
                                         json={"room": session['room'], "session_id": request.cookies.get("session_id")})
            resp = JSONResponse(content=response.json())
            
            if 'new_session' in session:
                resp.set_cookie(key="session_id", value=request.cookies.get("session_id"), samesite="None", secure=True)
            
            return resp
    except Exception as e:
        print(f"Failed to start game with error: {e}")
        return JSONResponse(content={"status": "error", "message": "Failed to start game"}, status_code=500)

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