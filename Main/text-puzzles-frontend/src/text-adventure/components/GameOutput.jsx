import React from 'react';
import scrollOnUpdate from '../hooks/UINiceties';
import { OutputDiv } from './GameOutput.Styles';

const GameOutput = ({ output }) => {
  const outputRef = scrollOnUpdate(output)
  
  return <OutputDiv ref={outputRef} id="output" aria-live="polite" style={{ whiteSpace: 'pre-wrap' }}>{output}</OutputDiv>;
};

export default GameOutput;