from engine import Game
from room_2 import description, winning_message, losing_message
from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import asyncio

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
    return {"response": response}
    
    
@app.post("/api/newgame")
async def game_endpoint(command: Command):
    if command=='slack':
        restart_game()
        return {"response": 'Game has restarted.'}
    else:
        return {"response": 'You have no permission!'}

def restart_game():
    app.state.game = Game()
    game = app.state.game
    game.set_scene(description, winning_message, losing_message)
    game.start_game()

def serve():
    restart_game()
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=41801)

if __name__ == "__main__":
    serve()

