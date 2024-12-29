# Welcome

To AI puzzle rooms repo. Currently, only local running is supported. Here is an example of what you might expect once the game is loaded:

![image](example_room_2.jpg)


## Instructions to run the backend (with minimal local frontend)

Make sure you have `ollama serve`running.

Clone this repo

run these lines or similar:
```
python -m venv ai_puzzle_rooms_venv
source ai_puzzle_rooms_venv/bin/activate
cd AI_puzzle_rooms/backend/text-puzzles-backend
pip install -r requirements.txt
chmod +x ollama/start_ollama.sh
./ollama_start_ollama.sh
```

Then
```
export GAME_SERVER_PORT_NUMBER=8081
export FRONTEND_CORS_IP=*
python server.py
```

Feel free to change FRONTEND_CORS_IP for more security

To access the minimal local frontend, open your browser to http://localhost:8081

To restart a game, either restart the server or run new_game.sh

## Instructions to run the frontend

Clone this repo and

```
cd AI_puzzle_rooms/frontend/text-puzzles-frontend
export VITE_REACT_APP_BACKEND_URL=http://localhost
export VITE_REACT_APP_BACKEND_PORT=8081
npm install
npm run dev
```


# Hardware requirements

At least a 3090, not only because of the VRAM required, but also because the AI takes time to process each turn of the game.
