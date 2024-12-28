import React, { createContext, useContext, useState } from 'react';
import useGame from '../hooks/useGame';

const GameContext = createContext();

export const GameProvider = ({ children }) => {
  const { output, error, setOutput, sendCommand, startGame, chooseRoom } = useGame();
  
  return (
    <GameContext.Provider value={{ 
      output, 
      error, 
      sendCommand, 
      startGame, 
      chooseRoom 
    }}>
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