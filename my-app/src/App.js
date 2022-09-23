import logo from './logo.svg';
import './App.css';
import React, { useEffect } from 'react';

function App() {
  useEffect(() => {
    document.title = 'Giri';
  });
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
    </header>
    </div >
  );
}

export default App;
