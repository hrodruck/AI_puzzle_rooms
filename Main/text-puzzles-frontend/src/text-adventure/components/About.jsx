import React from 'react';
import { Link } from 'react-router-dom';
import Parser from 'html-react-parser';
import { TextBox } from './About.Styles';
import { useGameContext } from '../context/GameContext';

const About = () => {
  const text = `Hello! I'm Rodrigo, an AI researcher and engineer. 
This project's code can be found at [GitHub](https://github.com/hrodruck/AI_puzzle_rooms)

The idea of the game is that one may choose a room and try to escape from it using free-form, creative text inputs. You can attempt a backflip, summoning a dragon, or even tricking the AI engine under the hood, though success is not guaranteed!
You can even interact with the puzzles in a clever way, you may find alternate solutions if you're creative enough.

The system takes long processing inputs; if you want to see what's under the hood, consider taking a peak at the [GameMaster mode](/gamemaster) (it will show the inner logic after you start a game).
My contacts: [LinkedIn](https://www.linkedin.com/in/rodrigo-mello-32571a291/) and [X](https://x.com/Professor_Ho_Oh)

Thanks! See ya!`;

  // Function to convert markdown-like links to HTML first, then to JSX
  const createLinks = (str) => {
    const linkRegex = /\[(.*?)\]\((.*?)\)/g;
    const htmlText = str.split('\n').map(line => {
      return line.replace(linkRegex, (_, text, href) => {
        if (href[0] !== '/') {
          return `<a href="${href}" target="_blank" rel="noopener noreferrer">${text}</a>`;
        } else {
          return `<span data-link="${href}">${text}</span>`;
        }
      });
    }).join('<br />');
    
    // Transform function for parser
    const transform = (node, index) => {
      if (node.type === 'tag' && node.name === 'span' && node.attribs['data-link']) {
        return <Link to={node.attribs['data-link']} key={index}>{node.children[0].data}</Link>;
      }
      return node;
    };

    return Parser(htmlText, {
      replace: transform
    });
  };

  return (
    <div>
      <TextBox>
        <p>{createLinks(text)}</p>
      </TextBox>
    </div>
  );
};

export default About;