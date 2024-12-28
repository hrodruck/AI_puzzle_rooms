import React, { createContext, useContext, useState } from 'react';
import useGame from '../hooks/useGame';

const GameContext = createContext();

export const GameProvider = ({ children }) => {
  const { output, setOutput, sendCommand } = useGame();
  
  return (
    <GameContext.Provider value={{ output, setOutput, sendCommand }}>
      {children}
    </GameContext.Provider>
  );
};

export const useGameContext = () => {
  const context = useContext(GameContext);
  if (context === undefined) {
    throw new Error('useGameContext must be used within a GameProvider');
  }
  return context;
};