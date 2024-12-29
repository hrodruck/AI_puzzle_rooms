import styled from 'styled-components';


export const Button = styled.button`
  background-color: #4CAF50; /* Green */
  border: none;
  color: white;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  cursor: pointer;
  border-radius: 8px;
  transition: background-color 0.3s;

  &:hover {
    background-color: #45a049;
  }
`;

export const CustomInput = styled.textarea`
  width: 100%;
  height: 100px;
  margin: 10px 0;
  padding: 10px;
  border: 2px solid #ddd;
  border-radius: 4px;
  &::placeholder {
    color: #606060; // Darker placeholder color
  }
  &:focus {
    outline: none;
    border-color: #4CAF50; // Highlight on focus
  }
`;

export const OutputBox = styled.div`
  border: 1px solid #ddd;
  border-radius: 4px;
  padding: 10px;
  margin-top: 20px;
  max-height: 300px;
  overflow-y: auto;
  &::-webkit-scrollbar {
    width: 10px;
  }
  &::-webkit-scrollbar-track {
    background: #f1f1f1;
  }
  &::-webkit-scrollbar-thumb {
    background: #888;
  }
  &::-webkit-scrollbar-thumb:hover {
    background: #555;
  }
`;