import styled from 'styled-components';

export const Button = styled.button`
  background-color: #4CAF50; // Green accent
  color: white;
  border: none;
  border-radius: 5px;
  padding: 10px 20px;
  cursor: pointer;
  transition: background-color 0.3s;

  &:hover {
    background-color: #45a049; // Darker green on hover
  }

  &:disabled {
    background-color: #cccccc; // Light grey for disabled state
    color: #666666; // Darker grey text for contrast
    cursor: not-allowed; // Change cursor to indicate it's not clickable
  }
`;

export const CustomInput = styled.textarea`
  width: 100%;
  height: 100px;
  margin: 10px 0;
  padding: 10px;
  border: 1px solid #ccc; // Lighter border for a softer look
  border-radius: 5px;
  font-family: 'Arial', sans-serif; // Match with global font

  &::placeholder {
    color: #aaa; // Placeholder text color
  }

  &:focus {
    outline: none;
    border-color: #4CAF50; // Green border color when focused
    box-shadow: 0 0 5px rgba(76, 175, 80, 0.5); // Green shadow when focused
  }
`;

export const OutputBox = styled.div`
  border: 1px solid #ddd;
  border-radius: 5px; // Rounded corners for a modern look
  padding: 10px;
  margin-top: 20px;
  max-height: 300px;
  overflow-y: auto;
  background-color: #fff; // White background for contrast with text

  &::-webkit-scrollbar {
    width: 10px; // Width of the scrollbar
  }

  &::-webkit-scrollbar-track {
    background: #f1f1f1; // Lighter track background
  }

  &::-webkit-scrollbar-thumb {
    background: #888; // Darker thumb for visibility
  }

  &::-webkit-scrollbar-thumb:hover {
    background: #555; // Even darker on hover for interaction
  }

  p {
    margin: 5px 0; // Less margin for more compact text display
  }
`;