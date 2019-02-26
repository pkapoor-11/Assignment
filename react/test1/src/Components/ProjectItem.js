import React, { Component } from 'react';

class ProjectItem extends Component {
  render() {
    console.log(this.props);
    return (
      <li className="Projects">
      	<strong> {this.props.project.Name} </strong> = {this.props.project.ID}
      </li>
    );
  }
}

export default ProjectItem;
