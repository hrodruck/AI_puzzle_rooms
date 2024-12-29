// src/App/GlobalStyle.js
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
  
  #root { // Assuming your root div ID is 'root', adjust if different
    flex: 1;
    display: flex;
    flex-direction: column;
  }
  
  body {
    font-family: Arial, sans-serif; // Example global font setting
    background-color: #f9f9f9; // Example background color
  }
`;

export const Container = styled.div`
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  width: 100vw;
  flex-direction: column; // To stack nav and content vertically
  background-color: #f9f9f9; // Example background color
  padding: 20px;
  font-family: 'Arial, sans-serif';
`;

export const InnerContainer = styled.div`
  max-width: 800px;
  width: 100%;
  padding: 20px;
  background: white;
  border-radius: 8px;
  box-shadow: 0 0 10px rgba(0,0,0,0.1);
  display: flex;
  flex-direction: column;
  align-items: center;
`;


export default GlobalStyle;