import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useGameContext } from '../context/GameContext';

const RoomSelection = () => {
  const [selectedRoom, setSelectedRoom] = useState('');
  const [customRoom, setCustomRoom] = useState('');
  const { chooseRoom, isRoomChosen } = useGameContext();
  const navigate = useNavigate();

  const handleRoomSelect = (room) => {
    chooseRoom(room);
    setSelectedRoom(room);
    setCustomRoom('');
    navigate('/game'); // Navigate to the game page after selecting a room
  };

  const handleCustomRoomSubmit = (e) => {
    e.preventDefault();
    if (customRoom) {
      try {
        const roomObject = JSON.parse(customRoom);
        chooseRoom(roomObject)
        navigate('/game'); // Navigate to the game page after submitting a custom room
      } catch (error) {
        alert('Invalid JSON for custom room description. Please check your input.');
      }
    }
  };

  return (
    <div>
      <select value={selectedRoom} onChange={(e) => handleRoomSelect(e.target.value)}>
        <option value="">Choose a room</option>
        <option value="room_1">Room One</option>
        <option value="room_2">Room Two</option>
      </select>
      <form onSubmit={handleCustomRoomSubmit}>
        <textarea 
          value={customRoom} 
          onChange={(e) => setCustomRoom(e.target.value)} 
          rows="10" 
          cols="50"
          placeholder='Custom room goes here...'
        />
        <button type="submit">Submit Custom Room</button>
      </form>
    </div>
  );
};

export default RoomSelection;