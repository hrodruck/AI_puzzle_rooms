import React, { useState } from 'react';
import useGame from '../hooks/useGame';
import GameOutput from './GameOutput';
import { Button, CustomInput, OutputBox } from './TextAdventure.styles';

const TextAdventure = () => {
  const { output, error, sendCommand, startGame } = useGame();
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
        placeholder="Enter your command here..."
        />
        <Button onClick={handleSubmit}>Submit Command</Button>
        
    </div>
  );
};

export default TextAdventure;