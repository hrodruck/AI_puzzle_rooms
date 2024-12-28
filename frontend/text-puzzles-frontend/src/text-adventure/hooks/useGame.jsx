import { useState } from 'react';
import notificationSound from '../sounds/ping.wav';

export default function useGame() {
  const [output, setOutput] = useState('Welcome! Processing the room... You\'ll be able to issue commands once the room is loaded. \n \n');
  
  const notifyReply = () => {
    const audio = new Audio(notificationSound);
    audio.play().catch(error => {
      console.error('Failed to play sound:', error);
    });
  };
  
  const sendCommand = async (command) => {
    setOutput(prevOutput => prevOutput + "\n\n Command sent! Command was \n" + command + "\nIt takes a while for the AI to respond, a sound will ring when it's done. \n \n ");
    try {
      const response = await fetch(`${import.meta.env.VITE_REACT_APP_BACKEND_URL}:${import.meta.env.VITE_REACT_APP_BACKEND_PORT}/api/game`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({command: command})
      });
      
      if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
      const data = await response.json();
      setOutput(prevOutput => prevOutput + data.response);
      notifyReply();
    } catch (error) {
      setOutput(prevOutput => prevOutput + "\nAn error occurred: ");
      console.log(error);
    }
  };

  return { output, setOutput, sendCommand };
}