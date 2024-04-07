import React from 'react';
import './App.css';
import Navbar from "./components/Navbar";
import * as logo from './images/plane_icon512.png';

function App() { 
  return (
    <div>
      <img src={logo} alt="logo" />
      <Navbar/>
    </div>
  );
}

export default App;
