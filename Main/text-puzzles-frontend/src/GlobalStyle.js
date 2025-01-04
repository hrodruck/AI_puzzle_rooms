import { createGlobalStyle } from 'styled-components';
import styled from 'styled-components';

const GlobalStyle = createGlobalStyle`
  body, html {
    margin: 0;
    padding: 0;
    height: 100%;
    width: 100%;
    display: flex;
    flex-direction: column;
  }
  
  #root {
    flex: 1;
    display: flex;
    flex-direction: column;
  }
  
  body {
    font-family: Arial, sans-serif;
    background-color: #f9f9f9;
    color: #333333;
  }
  
  input {
    background-color: #ffffff;
    color: #333333;
  }
  
  textarea {
    background-color: #ffffff;
    color: #333333;
  }
  
`;

export const Container = styled.div`
  display: flex;
  justify-content: center; // This ensures horizontal centering
  align-items: center; // Center vertically, but this might need adjustment if InnerContainer should stretch full height
  height: 100vh;
  width: 100vw;
  flex-direction: column;
  background-color: #f9f9f9;
  padding: 20px;
  font-family: 'Arial, sans-serif';
`;

export const InnerContainer = styled.div`
  max-width: 800px;
  width: 100%;
  height: 100%; // Ensure it takes up full height
  padding: 20px;
  background: white;
  border-radius: 8px;
  box-shadow: 0 0 10px rgba(0,0,0,0.1);
  display: flex;
  flex-direction: column;
  align-items: center; // Center content horizontally within this container
  overflow-y: auto; // Enable vertical scrolling if content exceeds the container's height
  justify-content: flex-start; // Align items at the top of the container
  min-height: 0; // This ensures the flex container doesn't grow beyond its parent
`;


export default GlobalStyle;