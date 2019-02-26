import React, { Component } from 'react';

class Display extends Component {
  render() 
    return (
      <div className="Display">
       <table border="1" cellpadding="5" cellspacing="5">
        {% for row in rv %}
        <tr>
        {% for d in row %}
            <td>{{ d }}</td>
        {% endfor %}
        </tr>
        {% endfor %}
        </table>
      </div>
    );
  }
}

export default Display;
