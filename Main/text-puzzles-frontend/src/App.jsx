import React from 'react';
import { useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route, Link} from 'react-router-dom';
import GlobalStyle from './GlobalStyle';
import { Container, InnerContainer } from './GlobalStyle';
import TextAdventure from './text-adventure/components/TextAdventure';
import RoomSelection from './text-adventure/components/RoomSelection';
import About from './text-adventure/components/About';
import GameMasterMode from './text-adventure/components/GameMasterMode';
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
                    <TabLink to="/" className={({ isActive }) => isActive ? "active" : ""}>About</TabLink>
                    <TabBar />
                  </TabItem>
                  <TabItem>
                    <TabLink to="/room-selection" className={({ isActive }) => isActive ? "active" : ""}>Room Selection</TabLink>
                    <TabBar />
                  </TabItem>
                  <TabItem>
                    <TabLink to="/game" className={({ isActive }) => isActive ? "active" : ""}>Game</TabLink>
                    <TabBar />
                  </TabItem>
                  <TabItem>
                    <TabLink to="/gamemaster" className={({ isActive }) => isActive ? "active" : ""}>GameMaster Mode</TabLink>
                    <TabBar />
                  </TabItem>
                </TabList>
                </Nav>
            
                <InnerContainer>
                    <Routes>
                      <Route path="/" element={<About />} />
                      <Route path="/room-selection" element={<RoomSelection />} />
                      <Route path="/game" element={<TextAdventure />} />
                      <Route path="/gamemaster" element={<GameMasterMode />} />
                    </Routes>
                </InnerContainer>
                
            </Container>
        </Router>
  );
}

export default App;