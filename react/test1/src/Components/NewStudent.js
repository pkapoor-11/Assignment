import React, {Component} from 'react';
import ReactDOM from 'react-dom';
import axios from 'axios'

class NewStudent extends Component{
    render(){
        return (
            <div className="form">
                 <h1> Student Assignment </h1> <br/>
                <form method="POST" action="http://localhost:5000/users/ins">
                   <h4> 1. Create </h4> <br/>
                    ID: <input type="text" name="ID"/> <br/> <br/>
                    Name: <input type="text" name="Name"/> <br/> <br/>
                     <input type="submit" value="Submit"/> 
                </form>

                <form method="GET" action="http://localhost:5000/users/view">
                <br/> <h4> 2. Delete </h4> <br/>
                <input type="submit" name="view" value="View Students" />
                </form>

                <form method="POST" action="http://localhost:5000/users/upd">
                <br/> <h4> 3. Update </h4>
                <br/> ID to be updated: <input type="text" name="up_ID"/> <br/>
                 <br/> New Name: <input type="text" name="new_Name"/> 
                <br/><br/> <input type="submit" name="upd" value="Update Student" />
                </form>

            </div>
        );
    }
}
ReactDOM.render(
    <NewStudent/>,
    document.getElementById('root')
);

export default NewStudent;