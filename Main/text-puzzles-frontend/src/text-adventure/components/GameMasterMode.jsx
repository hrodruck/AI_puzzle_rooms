import React from 'react';
import { TextBox } from './GameMasterMode.Styles';
import { useGameContext } from '../context/GameContext';

const GameMasterMode = () => {
  const welcomeText = `Welcome to game master mode! Beware spoilers!`;
  const { gameProgress } = useGameContext();
  return (
    <div>
      <TextBox>
        <p id="welcome-gm-text">{welcomeText}</p>
        <br />
        <br />
        <p>{gameProgress}</p>
      </TextBox>
    </div>
  );
};

export default GameMasterMode;