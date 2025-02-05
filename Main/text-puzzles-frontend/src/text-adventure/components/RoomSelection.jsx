import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useGameContext } from '../context/GameContext';
import { 
  RoomSelectionContainer, 
  RoomSelect, 
  FormGroup, 
  Label, 
  CustomTextArea, 
  CustomInput, 
  CustomButton, 
  CustomObjectContainer,
  JSONTextArea,
  ExportButton,
  ImportButton,
  SubmitButton,
  ButtonContainer,
} from './RoomSelection.Styles'; // Adjust the path as per your project structure

const RoomSelection = () => {
  const [formData, setFormData] = useState({
    room_itself: '',
    win_condition: '',
    loss_condition: '',
    winning_message: '',
    losing_message: '',
    room_description: '',
    customObjects: []
  });
  const [selectedRoom, setSelectedRoom] = useState('');
  const [customRoomJson, setCustomRoomJson] = useState('');
  const navigate = useNavigate();
  const { chooseRoom } = useGameContext();

  const handleRoomSelect = (room) => {
    chooseRoom(room);
    setSelectedRoom(room);
    setFormData({
      room_itself: '',
      win_condition: '',
      loss_condition: '',
      winning_message: '',
      losing_message: '',
      room_description: '',
      customObjects: []
    });
    setCustomRoomJson('');
    navigate('/game'); 
  };

  const handleCustomRoomSubmit = (e) => {
    e.preventDefault();
    const roomObject = {
      room: {
        description: {
          ...formData,
          ...Object.fromEntries(formData.customObjects.map(obj => [obj.key, obj.value]))
        },
        winning_message: formData.winning_message,
        losing_message: formData.losing_message,
        room_description: formData.room_description
      }
    };

    chooseRoom(roomObject);
    navigate('/game'); 
  };

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prevState => ({
      ...prevState,
      [name]: value
    }));
  };

  const addCustomObject = () => {
    setFormData(prevState => ({
      ...prevState,
      customObjects: [...prevState.customObjects, { key: '', value: '' }]
    }));
  };

  const removeCustomObject = (index) => {
    setFormData(prevState => ({
      ...prevState,
      customObjects: prevState.customObjects.filter((_, i) => i !== index)
    }));
  };

  const handleCustomObjectChange = (index, field, value) => {
    setFormData(prevState => {
      const newCustomObjects = [...prevState.customObjects];
      newCustomObjects[index][field] = value;
      return {
        ...prevState,
        customObjects: newCustomObjects
      };
    });
  };

  const exportCustomRoom = () => {
    const jsonString = JSON.stringify({
      room: {
        description: {
          ...formData,
          ...Object.fromEntries(formData.customObjects.map(obj => [obj.key, obj.value]))
        },
        winning_message: formData.winning_message,
        losing_message: formData.losing_message,
        room_description: formData.room_description
      }
    }, null, 2);
    const blob = new Blob([jsonString], { type: "application/json" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'custom_room.json';
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
  };

  const setFormFromJSON = (customRoomJson) => { 
      try {
        const roomObject = JSON.parse(customRoomJson);
        setFormData({
          room_itself: roomObject.room.description.room_itself || '',
          win_condition: roomObject.room.description.win_condition || '',
          loss_condition: roomObject.room.description.loss_condition || '',
          winning_message: roomObject.room.winning_message || '',
          losing_message: roomObject.room.losing_message || '',
          room_description: roomObject.room.room_description || '',
          customObjects: Object.entries(roomObject.room.description)
            .filter(([key]) => !['room_itself', 'win_condition', 'loss_condition'].includes(key))
            .map(([key, value]) => ({ key, value }))
        });
      } catch (error) {
        alert('Invalid JSON format. Please check your input.');
      }
  }

  const importCustomRoom = (e) => {
    e.preventDefault();
    if (customRoomJson) {
      setFormFromJSON(customRoomJson);
    }
  };

  const loadExampleRoom = async () => {
      const response = await fetch('example_room.json');
      const roomData = await response.json();
      setFormFromJSON(JSON.stringify(roomData));     
  }

  return (
    <RoomSelectionContainer>
      <h2>Select a Room</h2>
      <RoomSelect value={selectedRoom} onChange={(e) => handleRoomSelect(e.target.value)}>
        <option value="">Choose a room</option>
        <option value="room_1">Doormat Tutorial</option>
        <option value="room_2">Two Doors Tutorial</option>
        <option value="room_3">Kitchen</option>
        <option value="room_4">Doormat Challenge</option>
        <option value="room_6">Submarine</option>
        <option value="mage_tower_room_entrance_lvl_1">Mage Tower Entrance Lvl 1</option>
        <option value="mage_tower_room_entrance_lvl_2">Mage Tower Entrance Lvl 2</option>
      </RoomSelect>
      <details>
        <summary><h3>Or Create Your Custom Room:</h3></summary>
        
        <ImportButton 
        type="button" 
        onClick={loadExampleRoom}
        >
        Load Example Custom Room
        </ImportButton>
        <form onSubmit={handleCustomRoomSubmit}>
        <FormGroup>
          <Label htmlFor="room_itself">Room Itself (from the game's perspective):</Label>
          <CustomTextArea id="room_itself" name="room_itself" value={formData.room_itself} onChange={handleChange} />
        </FormGroup>
        <FormGroup>
          <Label htmlFor="win_condition">Win Condition:</Label>
          <CustomTextArea id="win_condition" name="win_condition" value={formData.win_condition} onChange={handleChange} />
        </FormGroup>
        <FormGroup>
          <Label htmlFor="loss_condition">Loss Condition:</Label>
          <CustomTextArea id="loss_condition" name="loss_condition" value={formData.loss_condition} onChange={handleChange} />
        </FormGroup>
        <FormGroup>
          <Label htmlFor="winning_message">Winning Message:</Label>
          <CustomInput type="text" id="winning_message" name="winning_message" value={formData.winning_message} onChange={handleChange} />
        </FormGroup>
        <FormGroup>
          <Label htmlFor="losing_message">Losing Message:</Label>
          <CustomInput type="text" id="losing_message" name="losing_message" value={formData.losing_message} onChange={handleChange} />
        </FormGroup>
        <FormGroup>
          <Label htmlFor="room_description">Room Description (to be displayed to the player):</Label>
          <CustomInput type="text" id="room_description" name="room_description" value={formData.room_description} onChange={handleChange} />
        </FormGroup>

        <h4>Custom Objects</h4>
        <CustomButton type="button" onClick={addCustomObject}>Add Custom Object</CustomButton>
        {formData.customObjects.map((obj, index) => (
          <CustomObjectContainer key={index}>
            <CustomInput 
              type="text" 
              placeholder="Key" 
              value={obj.key} 
              onChange={(e) => handleCustomObjectChange(index, 'key', e.target.value)}
            />
            <CustomTextArea 
              placeholder="Value" 
              value={obj.value} 
              onChange={(e) => handleCustomObjectChange(index, 'value', e.target.value)}
            />
            <CustomButton type="button" onClick={() => removeCustomObject(index)}>Remove</CustomButton>
          </CustomObjectContainer>
        ))}

        <h3>Export/Import JSON</h3>
        <ExportButton 
          type="button" 
          onClick={exportCustomRoom}
        >
          Export Custom Room as JSON
        </ExportButton>
        <JSONTextArea 
          value={customRoomJson} 
          onChange={(e) => setCustomRoomJson(e.target.value)} 
          placeholder='Paste JSON here to import...'
        />
        <ImportButton 
          type="button" 
          onClick={importCustomRoom}
        >
          Import Custom Room from JSON
        </ImportButton>

        <div style={{ marginTop: '20px' }}>
        <ButtonContainer>
          <SubmitButton 
            type="submit"
          >
            Submit Custom Room
          </SubmitButton>
        </ButtonContainer>
        </div>

        </form>
      </details>
    </RoomSelectionContainer>
  );
};

export default RoomSelection;