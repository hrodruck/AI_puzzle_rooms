import React, { useState } from 'react';
import useGame from './hooks/useGame';
import CommandInput from './components/CommandInput';
import GameOutput from './components/GameOutput';

const TextAdventure = () => {
  const { output, sendCommand } = useGame();
  const [command, setCommand] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    sendCommand(command);
    setCommand('');
  };

  return (
    <div>
      <CommandInput command={command} setCommand={setCommand} handleSubmit={handleSubmit} />
      <GameOutput output={output} />
    </div>
  );
};

export default TextAdventure;