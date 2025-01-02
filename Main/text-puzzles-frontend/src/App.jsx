import React from 'react';
import { useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route, Link} from 'react-router-dom';
import GlobalStyle from './GlobalStyle';
import { Container, InnerContainer } from './GlobalStyle';
import TextAdventure from './text-adventure/components/TextAdventure';
import RoomSelection from './text-adventure/components/RoomSelection';
import { GameProvider } from './text-adventure/context/GameContext';
import { Nav, TabList, TabItem, TabLink, TabBar} from './App.styles';

function App() {
    useEffect(() => {
        document.title = `${import.meta.env.VITE_APP_TITLE}` || "Default Title";
    }, []);
    
  return (
        <Router>
        <GlobalStyle />
            <Container>
            
                <Nav>
                <TabList>
                  <TabItem>
                    <TabLink to="/" className={({ isActive }) => isActive ? "active" : ""}>Room Selection</TabLink>
                    <TabBar />
                  </TabItem>
                  <TabItem>
                    <TabLink to="/game" className={({ isActive }) => isActive ? "active" : ""}>Game</TabLink>
                    <TabBar />
                  </TabItem>
                </TabList>
                </Nav>
            
                <InnerContainer>
                    <Routes>
                      <Route path="/" element={<RoomSelection />} />
                      <Route path="/game" element={<TextAdventure />} />
                    </Routes>
                </InnerContainer>
                
            </Container>
        </Router>
  );
}

export default App;