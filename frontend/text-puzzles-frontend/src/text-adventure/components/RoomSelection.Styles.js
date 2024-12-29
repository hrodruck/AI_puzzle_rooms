import styled from 'styled-components';

export const RoomSelectionContainer = styled.div`
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  background-color: #f9f9f9; // Light grey background for contrast
  border-radius: 10px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
`;

export const RoomSelect = styled.select`
  width: 100%;
  padding: 10px;
  margin-bottom: 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
  font-family: 'Arial', sans-serif;
  appearance: none; // Remove default browser styling

  &:focus {
    outline: none;
    border-color: #4CAF50; // Green border color when focused
    box-shadow: 0 0 5px rgba(76, 175, 80, 0.5); // Green shadow when focused
  }
`;

export const FormGroup = styled.div`
  margin-bottom: 15px;
`;

export const Label = styled.label`
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
`;

export const CustomTextArea = styled.textarea`
  width: 100%;
  height: 100px;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  font-family: 'Arial', sans-serif;

  &::placeholder {
    color: #aaa; // Placeholder text color
  }

  &:focus {
    outline: none;
    border-color: #4CAF50; // Green border color when focused
    box-shadow: 0 0 5px rgba(76, 175, 80, 0.5); // Green shadow when focused
  }
`;

export const CustomInput = styled.input`
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  font-family: 'Arial', sans-serif;

  &::placeholder {
    color: #aaa; // Placeholder text color
  }

  &:focus {
    outline: none;
    border-color: #4CAF50; // Green border color when focused
    box-shadow: 0 0 5px rgba(76, 175, 80, 0.5); // Green shadow when focused
  }
`;

export const CustomButton = styled.button`
  background-color: #4CAF50; // Green accent
  color: white;
  border: none;
  border-radius: 5px;
  padding: 10px 20px;
  cursor: pointer;
  transition: background-color 0.3s;
  margin: 10px 0;

  &:hover {
    background-color: #45a049; // Darker green on hover
  }

  &:disabled {
    background-color: #cccccc; // Light grey for disabled state
    color: #666666; // Darker grey text for contrast
    cursor: not-allowed; // Change cursor to indicate it's not clickable
  }
`;

export const CustomObjectContainer = styled.div`
  display: flex;
  flex-direction: column;
  margin-bottom: 10px;

  & > input, & > textarea {
    margin-bottom: 5px;
  }
`;

// Add these to your existing styled-components import or file

export const ExportButton = styled(CustomButton)`
  background-color: #2196F3; // Blue for export/import
  border-color: #2196F3;
`;

export const ImportButton = styled(CustomButton)`
  background-color: #2196F3; // Blue for export/import
  border-color: #FF9800;
`;

export const SubmitButton = styled(CustomButton)`
  background-color: #9C27B0; // Purple for submit
  border-color: #9C27B0;
`;

export const ButtonContainer = styled.div`
  margin-top: 20px;
`;

export const JSONTextArea = styled.textarea`
  width: 100%;
  height: 200px;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  font-family: 'Arial', sans-serif;

  &::placeholder {
    color: #aaa; // Placeholder text color
  }

  &:focus {
    outline: none;
    border-color: #4CAF50; // Green border color when focused
    box-shadow: 0 0 5px rgba(76, 175, 80, 0.5); // Green shadow when focused
  }
`;