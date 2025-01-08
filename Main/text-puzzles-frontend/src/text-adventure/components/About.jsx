import React from 'react';
import { TextBox } from './About.Styles';
import { useGameContext } from '../context/GameContext';

const About = () => {
  const text = `Hello! I'm Rodrigo, an AI researcher and engineer. 
This project's code can be found at [GitHub](https://github.com/hrodruck/AI_puzzle_rooms)

The idea of the game is that one may choose a room and try to escape from it using free-form, creative text inputs. You can attempt a backflip, summoning a dragon, or even tricking the AI engine under the hood, though success is not guaranteed!
You can even interact with the puzzles in a clever way, you may find alternate solutions if you're creative enough.

The system takes long processing inputs; if you want to see what's under the hood, consider taking a peak at the [GameMaster mode](/gamemaster)
My contacts: [LinkedIn](https://www.linkedin.com/in/rodrigo-mello-32571a291/) and [X](https://x.com/Professor_Ho_Oh)

Thanks! See ya!`;

  // Function to convert markdown-like links to JSX
  const createLinks = (str) => {
    const linkRegex = /\[(.*?)\]\((.*?)\)/g;
    return str.split('\n').map((line, index) => {
      const withLinks = line.replace(linkRegex, (_, text, href) => 
        `<a href="${href}" target="_blank" rel="noopener noreferrer">${text}</a>`
      );
      return <React.Fragment key={index}>
          <span dangerouslySetInnerHTML={{ __html: withLinks }} />
          <br />
        </React.Fragment>;
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