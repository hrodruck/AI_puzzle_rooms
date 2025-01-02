import React from 'react';

const CommandInput = ({ command, setCommand, handleSubmit }) => {
  return (
    <form onSubmit={handleSubmit}>
      <textarea 
        id="input" 
        value={command} 
        onChange={(e) => setCommand(e.target.value)} 
        placeholder="You command (example: Look around)" 
        aria-label="Enter game command"
      />
      <button 
        id="submitButton" 
        type="submit" 
        disabled={!command}
        aria-label="Submit command"
      >
        Submit
      </button>
    </form>
  );
};

export default CommandInput;