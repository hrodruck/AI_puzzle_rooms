    import { useState, useRef, useEffect } from 'react';
    import notificationSound from '../sounds/ping.wav';

    export default function useGame() {
      const [output, setOutput] = useState('Welcome!  \n \n');
      const [error, setError] = useState(null);
      const [isRoomChosen, setIsRoomChosen] = useState(false);
      const [isGameStarted, setIsGameStarted] = useState(false);
      const [isProcessing, setIsProcessing] = useState(false);
      const [gameProgress, setGameProgress] = useState('');
      const intervalRef = useRef(null);

      const notifyReply = () => {
        const audio = new Audio(notificationSound);
        audio.play().catch(error => {
          console.error('Failed to play sound:', error);
        });
      };

      useEffect(() => {
        const pollGameProgress = async () => {
            try{
                const response = await fetch(`${import.meta.env.VITE_REACT_APP_BACKEND_URL}:${import.meta.env.VITE_REACT_APP_BACKEND_PORT}/api/game-progress`, {
                    method: 'GET',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    credentials: 'include',
                });
                const data = await response.json();
                const newGameProgress = data.response;
                setGameProgress(prevGameProgress  => prevGameProgress + newGameProgress);
                let displayToPlayerBegin = newGameProgress.indexOf('<display_to_player>');
                if (displayToPlayerBegin != -1){
                    let displayToPlayerEnd = newGameProgress.indexOf('</display_to_player>');
                    displayToPlayerBegin += '<display_to_player>'.length;
                    const displayToPlayerString = newGameProgress.slice(displayToPlayerBegin,displayToPlayerEnd);
                    console.log(displayToPlayerString)
                    setOutput(prevOutput => prevOutput + displayToPlayerString)
                }
            }
            catch(error){
                console.error('Error getting game progress', error);
            }
            if (isProcessing) {
            intervalRef.current = setTimeout(pollGameProgress, 1000);
        }
        };
        if (isProcessing){
            pollGameProgress();
        }
        return () => {
            if (intervalRef.current) {
              clearInterval(intervalRef.current);
              intervalRef.current = null;
            }
        };
      }, [isProcessing]);

      const sendCommand = async (command) => {
        if (!isGameStarted){
            setOutput(prevOutput => prevOutput + "\n... Please wait, game is still starting.\n");
            return;
        }
         
         if (isProcessing) {
            // If already processing, do not start another command
            setOutput(prevOutput => prevOutput + "\n... Please wait, the AI is thinking, and it can be slow!\n");
            return;
        }
        
        setIsProcessing(true);
        
        setOutput(prevOutput => prevOutput + "\n\n Command sent! Command was \n" + command + "\nIt takes a while for the game to respond, a sound will ring when it's done. \n \n ");
        try {
          const response = await fetch(`${import.meta.env.VITE_REACT_APP_BACKEND_URL}:${import.meta.env.VITE_REACT_APP_BACKEND_PORT}/api/game`, {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
            },
            credentials: 'include',
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
        } finally {
          setIsProcessing(false); // Reset processing state after command is handled
        }
      };

    const startGame = async () => {
      if (!isRoomChosen) {
          setOutput(prevOutput => prevOutput + "\nPlease choose a room before starting the game.");
        return;
      }
      
      if (isProcessing && !isGameStarted){
            setOutput(prevOutput => prevOutput + "\n...Please wait, game is still starting (it takes long).\n");
            return;
        }
      
      if (isProcessing) {
            // If already processing, do not start another game
            setOutput(prevOutput => prevOutput + "\n...Please wait, the AI is thinking, and it can be slow!\n");
            return;
        }
        
      setIsProcessing(true);
      setIsGameStarted(false);
      
      setOutput(prevOutput => prevOutput + "\nStarting the game! \nIt can take a long time for the game to finish processing, a sound will ring when it's done. \n");
      
      try {
        const response = await fetch(`${import.meta.env.VITE_REACT_APP_BACKEND_URL}:${import.meta.env.VITE_REACT_APP_BACKEND_PORT}/api/new-game`, {
          method: 'POST',
          credentials: 'include' // Include cookies in the request
        });
        
        if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
        const data = await response.json();
        
        setOutput(prevOutput => prevOutput + "\n" + data.message);
        notifyReply();
        setIsProcessing(false);
        if (data.status == 'success'){
            setOutput(data.message); // Clear the output as a new game starts
            setOutput(prevOutput => prevOutput + '(a sound will always ring when a command is completed)\n'); 
            setIsGameStarted(true);
        }
      } catch (error) {
        setOutput(prevOutput => prevOutput + "\nFailed to start new game: " + error.message);
        setError(error.message);
        console.error(error);
      }
      finally {
        setIsProcessing(false);
      }
    };

      useEffect(() => {
        if (isGameStarted){
            
            sendCommand('Describe the room');
        }
          
      }, [isGameStarted]);

    const chooseRoom = async (room) => {
      try {
        const roomData = typeof room === 'string' ? { room } : room; // If it's a string, wrap it in an object, otherwise use the object directly
        const response = await fetch(`${import.meta.env.VITE_REACT_APP_BACKEND_URL}:${import.meta.env.VITE_REACT_APP_BACKEND_PORT}/api/choose-room`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          credentials: 'include', // Include cookies in the request
          body: JSON.stringify(roomData)
        });
        
        if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
        const data = await response.json();
        setOutput(prevOutput => prevOutput + "\n" + data.message);
        setIsRoomChosen(true);
      } catch (error) {
        setOutput(prevOutput => prevOutput + "\nFailed to choose room: " + error.message);
        setError(error.message);
        console.error(error);
      }
    };

      return { 
        output, 
        error, 
        setOutput, 
        sendCommand, 
        startGame, 
        chooseRoom,
        isGameStarted, 
        isRoomChosen,
        isProcessing,
        gameProgress
      };
    }