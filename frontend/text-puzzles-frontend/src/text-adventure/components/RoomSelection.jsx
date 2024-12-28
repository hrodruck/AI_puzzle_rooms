import React, { useState } from 'react';

const RoomSelection = ({ onChooseRoom }) => {
  const [selectedRoom, setSelectedRoom] = useState('');
  const [customRoom, setCustomRoom] = useState('');

  const handleRoomSelect = (room) => {
    setSelectedRoom(room);
    setCustomRoom('');
    onChooseRoom(room);
  };

  const handleCustomRoomSubmit = (e) => {
    e.preventDefault();
    if (customRoom) {
      try {
        const roomObject = JSON.parse(customRoom);
        onChooseRoom(roomObject);
      } catch (error) {
        alert('Invalid JSON for custom room description. Please check your input.');
      }
    }
  };

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
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