# Welcome!

This repository is about an "escape the room" text adventure game. It allows for freeform text input "do a backflip"; "summon a dragon", though not all actions are permitted by the game (you might get injured by the backflip and the summoning attempt may fail if you can't use magic)

The idea is to interact with the contents of the room in creative ways in order to fulfill the escape conditions!
The game runs at https://rodmel.me if you want to try it out.

## Game screenshot
![alt text](game_screenshot.png)

## Running with Docker

By default, the game runs through https. Please put your privkey.pem (your key file) and fullchain.pem (your fullchain file) in a directory `ssl` in the project root.

Create .env file with OPEN_API_KEY, OPEN_API_URL and SERVER_IP, also in the project root.

then `docker-compose up`

Attention! Due to vite's environment variable behavior, it may be necessary to manually compile the frontend in order to expose the right ports if you change the default ones.