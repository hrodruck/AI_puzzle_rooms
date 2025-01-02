import React, { useState } from 'react';
import GameOutput from './GameOutput';
import { Button, CustomInput, OutputBox } from './TextAdventure.Styles';
import { useGameContext } from '../context/GameContext';

const TextAdventure = () => {
  const { output, error, sendCommand, startGame, isGameStarted } = useGameContext();
  const [command, setCommand] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    sendCommand(command);
    setCommand('');
  };

  return (
    <div>
        <OutputBox>
        <GameOutput output={output} error={error} />
        </OutputBox>
        
        <Button onClick={startGame}>Start or Restart Game</Button>
        <CustomInput 
        value={command} 
        onChange={(e) => setCommand(e.target.value)} 
        placeholder="Enter your command here... (example: look around)"
        />
        <Button onClick={handleSubmit} disabled={!isGameStarted} >Submit Command</Button>
        
    </div>
  );
};

export default TextAdventure;