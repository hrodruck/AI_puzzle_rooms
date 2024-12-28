import React, { useState } from 'react';
import useGame from './hooks/useGame';
import CommandInput from './components/CommandInput';
import GameOutput from './components/GameOutput';
import RoomSelection from './components/RoomSelection'; // New component for room selection

const TextAdventure = () => {
  const { output, error, sendCommand, startGame, chooseRoom } = useGame();
  const [command, setCommand] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    sendCommand(command);
    setCommand('');
  };

  const handleStartGame = () => {
    startGame();
  };

  const handleChooseRoom = (room) => {
    chooseRoom(room);
  };

  return (
    <div>
      <button onClick={handleStartGame}>Start New Game</button>
      <RoomSelection onChooseRoom={handleChooseRoom} />
      <CommandInput command={command} setCommand={setCommand} handleSubmit={handleSubmit} />
      <GameOutput output={output} error={error} />
    </div>
  );
};

export default TextAdventure;