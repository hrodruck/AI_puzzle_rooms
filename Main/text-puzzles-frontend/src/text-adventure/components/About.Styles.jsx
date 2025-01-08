import styled from 'styled-components';

const TextBox = styled.div`
  /* Base styles */
  background-color: #f0f0f0;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  max-width: 800px;
  margin: 0 auto;
  font-family: 'Arial', sans-serif;
  line-height: 1.6;
  color: #333;
  
  white-space: pre-line;


  /* Responsive adjustments */
  @media (max-width: 768px) {
    padding: 15px;
    font-size: 14px;
  }

  @media (max-width: 480px) {
    padding: 10px;
    font-size: 12px;
  }

  p {
    margin-bottom: 1em;
  }

  a {
    color: #0077cc;
    text-decoration: none;
    transition: color 0.3s ease;

    &:hover {
      color: #0055aa;
      text-decoration: underline;
    }
  }
`;

export { TextBox };