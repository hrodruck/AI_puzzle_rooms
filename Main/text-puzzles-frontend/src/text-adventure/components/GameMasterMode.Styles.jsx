import styled from 'styled-components';

const TextBox = styled.div`
  /* Base styles for terminal-like interface */
  background-color: #000000; /* Black background */
  color: #00FF00; /* Bright green text */
  font-family: 'Courier New', Courier, monospace; /* Monospace font for terminal feel */
  padding: 20px;
  border-radius: 0; /* No border radius to simulate terminal window */
  box-shadow: none; /* No shadow for a true terminal look */
  max-width: 800px;
  margin: 0 auto;
  line-height: 1.6;
  white-space: pre-line;

  /* Terminal cursor simulation */
  p {
    margin-bottom: 1em;
    &::after {
      content: '|';
      animation: blink 1s infinite;
      color: #00FF00;
    }
  }


  /* Responsive adjustments */
  @media (max-width: 768px) {
    padding: 15px;
    font-size: 14px;
  }

  @media (max-width: 480px) {
    padding: 10px;
    font-size: 12px;
  }

  /* Keyframe for blinking cursor */
  @keyframes blink {
    0%, 100% {
      opacity: 1;
    }
    50% {
      opacity: 0;
    }
  }
`;

export { TextBox };