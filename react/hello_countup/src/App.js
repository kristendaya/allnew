import React, { Component } from 'react';
 
 class App extends Component {
   state = {
    hello: 'Hello App.js~!! by Kristen daya Lee'
   }
   
   countup = () => {
    this.setState({
      count : this.state.count + 1
     })
   }
   
   render() {
     return (
      <div className="App">
       <div>{this.state.count}</div>
       <button onClick={this.countup}>prove how much u love me! </button>
      </div>
      )
    }
}
   
export default App;
 
 
