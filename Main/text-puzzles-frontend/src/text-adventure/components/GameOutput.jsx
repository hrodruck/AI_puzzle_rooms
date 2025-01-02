import React from 'react';

const GameOutput = ({ output }) => {
  return <div id="output" aria-live="polite" style={{ whiteSpace: 'pre-wrap' }}>{output}</div>;
};

export default GameOutput;