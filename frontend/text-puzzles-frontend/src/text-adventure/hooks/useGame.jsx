import { useState } from 'react';
import notificationSound from '../sounds/ping.wav';

export default function useGame() {
  const [output, setOutput] = useState('Welcome! Processing the room... A sound will ring when room is loaded. \n \n');
  const [error, setError] = useState(null);

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
        body: JSON.stringify({command})
      });
      
      if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
      const data = await response.json();
      setOutput(prevOutput => prevOutput + data.response);
      notifyReply();
    } catch (error) {
      setOutput(prevOutput => prevOutput + "\nAn error occurred: " + error.message);
      setError(error.message);
      console.error(error);
    }
  };

  const startGame = async () => {
    try {
      const response = await fetch(`${import.meta.env.VITE_REACT_APP_BACKEND_URL}:${import.meta.env.VITE_REACT_APP_BACKEND_PORT}/api/new-game`, {
        method: 'POST',
      });
      
      if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
      const data = await response.json();
      
      // Clear the output before adding the new game message
      setOutput('New game started. Welcome back!\n');
      setOutput(prevOutput => prevOutput + "\n" + data.status);
      notifyReply();
    } catch (error) {
      setOutput(prevOutput => prevOutput + "\nFailed to start new game: " + error.message);
      setError(error.message);
      console.error(error);
    }
  };

  const chooseRoom = async (room) => {
      try {
        const roomData = typeof room === 'string' ? { room } : room; // If it's a string, wrap it in an object, otherwise use the object directly
        const response = await fetch(`${import.meta.env.VITE_REACT_APP_BACKEND_URL}:${import.meta.env.VITE_REACT_APP_BACKEND_PORT}/api/choose-room`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(roomData)
        });
        
        if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
        const data = await response.json();
        setOutput(prevOutput => prevOutput + "\n" + data.status);
        notifyReply();
      } catch (error) {
        setOutput(prevOutput => prevOutput + "\nFailed to choose room: " + error.message);
        setError(error.message);
        console.error(error);
      }
    };

  return { output, error, setOutput, sendCommand, startGame, chooseRoom };
}