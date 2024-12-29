// src/App.styles.js
import { NavLink } from 'react-router-dom';
import styled from 'styled-components';

export const Nav = styled.nav`
  background-color: #f8f9fa; // Slightly lighter header
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05); // Very subtle shadow under header
  padding: 10px 0; // Increased padding for larger navbar
  border-bottom: 1px solid #e0e0e0;
`;

export const TabList = styled.ul`
  display: flex;
  justify-content: space-around;
  list-style: none;
  padding: 0;
  margin: 0;
`;

export const TabItem = styled.li`
  position: relative;
  padding: 10px 20px;
  cursor: pointer;
  transition: background-color 0.3s;
  font-size: 16px; // Larger font for better visibility
  color: #333; // Dark gray text for contrast

  &:hover {
    background-color: #e0e0e0; // Hover effect for better interaction
  }

  &.active {
    background-color: #e0e0e0; // Highlight active tab
    font-weight: bold;
    color: #1a73e8; // Accent color when active
  }
`;

export const TabLink = styled(NavLink)`
  text-decoration: none;
  color: #333; // Match with TabItem color
  padding: 10px 20px;

  &:hover {
    text-decoration: none;
  }

  &.active {
    color: #1a73e8; // Accent color when active
    font-weight: bold; // Bold for emphasis on active tab
  }
`;

export const TabBar = styled.span`
  display: block;
  height: 2px;
  background-color: #1a73e8; // Accent color for the tab bar
  position: absolute;
  bottom: -2px;
  left: 0;
  right: 0;
  opacity: 0;
  transition: opacity 0.3s;

  ${TabItem}.active & {
    opacity: 1;
  }
`;