import React, { Component } from 'react';
import './App.css';
//import Projects from './Components/Projects';
//import AddProject from './Components/AddProject';
import NewStudent from './Components/NewStudent';
//import {BrowserRouter as Router, Route} from 'react-router-dom'

class App extends Component {

  constructor(){
    super()
    this.state = {
      projects :
      [
      {
        ID: '1234',
        Name: 'John'
      },
      {
        ID: '5678',
        Name: 'Doe'
      }
      ]
    }
  }
  render() {
    return (
      <div className="App">
        <NewStudent />
        
         </div>
    );
  }
}

export default App;
