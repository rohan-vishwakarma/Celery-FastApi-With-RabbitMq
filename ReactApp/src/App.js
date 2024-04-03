import './App.css';
import React, { Component } from 'react';  
import PrimarySearchAppBar from './Components/Navbar';


class App extends Component{

  render(){

    return(
      <div>  
            <h1>JavaTpoint</h1>  
          <h2>Training Institutes</h2>  
            <p>This website contains the best CS tutorials.</p>  
            <PrimarySearchAppBar />
      </div>  
    );

  }

}



export default App;
