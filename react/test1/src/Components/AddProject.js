import React, { Component } from 'react';
import axios from 'axios'

class AddProject extends Component {
  constructor(){
    super();
    this.state = {
      newStudent: {}
    }
  }

  handleSubmit(e){
    if(this.refs.idd.value === ''){
      alert('ID is required');
    }
    else
    {
      this.setState({newStudent:{
        ID: this.refs.idd.value,
        Name: this.refs.name.value
      }}, function()
      {
        console.log(this.state);
      });
    }
    console.log(this.refs.name.value);
    console.log(this.refs.idd.value);
    e.preventDefault();
  }

  render() {
     return (
      <div>
        <h3> Add Project </h3>
        <form onSubmit={this.handleSubmit.bind(this)}>
        <label>
          Name:
        <input type="text" ref="name" />
        </label> <br/>
        <label>
          ID: 
        <input type="number" ref="idd" />
        </label>
        <br/>
        <input type="submit" value="Submit" />
        </form>
      </div>
    );
  }
}

export default AddProject;
