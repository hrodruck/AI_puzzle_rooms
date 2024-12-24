from engine import Game
from room_1 import description, winning_message, losing_message
from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import asyncio
import sys

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def read_root():
    return FileResponse("static/index.html")

class Command(BaseModel):
    command: str

@app.post("/api/game")
async def game_endpoint(command: Command):
    game = app.state.game
    response = await game.process_input(command.command)
    #response = await game.brazilian_portuguese_output(command.command)
    return {"response": response}
    
    
@app.post("/api/newgame")
async def game_endpoint(command: Command):
    if command.command=='slack':
        restart_game()
        return {"response": 'Game has restarted.'}
    else:
        return {"response": 'You have no permission!'}

def restart_game():
    # this currently doesn't work. Restart manually.
    app.state.game = Game()
    game = app.state.game
    game.set_scene(description, winning_message, losing_message)
    game.start_game()

def serve():
    restart_game()
    import uvicorn
    if len(sys.argv)<2:
        print('please specify port number as an argument to the server script')
    else:
        port_number = int(sys.argv[1])
        uvicorn.run(app, host="0.0.0.0", port=port_number)

if __name__ == "__main__":
    serve()
    