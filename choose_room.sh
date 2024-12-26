curl -X POST \
  'http://localhost:8081/api/choose-room' \
  -H 'Content-Type: application/json' \
  -d '{"room": "room_2"}'
  
curl -X POST \
  'http://localhost:8081/api/new-game' 