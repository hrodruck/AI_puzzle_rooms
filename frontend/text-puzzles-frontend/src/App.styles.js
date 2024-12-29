// src/App/App.styles.js
import { NavLink } from 'react-router-dom';
import styled from 'styled-components';

export const Nav = styled.nav`
  background-color: #f1f1f1;
  padding: 10px 0;
  border-bottom: 1px solid #ccc;
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

  &:hover {
    background-color: #ddd;
  }
`;

export const TabLink = styled(NavLink)`
  text-decoration: none;
  color: #333;
  padding: 10px 20px;

  &:hover {
    background-color: #ddd;
    text-decoration: none;
  }

  &.active {
    color: #007bff;
    font-weight: bold;
  }
`;
export const TabBar = styled.span`
  display: block;
  height: 2px;
  background-color: #007bff;
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