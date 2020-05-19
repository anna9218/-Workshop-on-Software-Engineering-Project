import React, {useState, useEffect} from 'react';
import {Container, Row, Col, Button, Dropdown, Jumbotron, Form} from 'react-bootstrap'
import {Link} from 'react-router-dom'
import * as registerService from '../../services/register';



//---------- WHAT A MANAGER CAN DO? ----------//
// Manage store (5.1) - according to the given permissions

//---------- EXISTING PERMISSIONS: -----------//
// EDIT_INV = 1
// EDIT_POLICIES = 2
// APPOINT_OWNER = 3
// DEL_OWNER = 4  # you can delete only the one's you appoint
// APPOINT_MANAGER = 5
// EDIT_MANAGER_PER = 6
// DEL_MANAGER = 7
// CLOSE_STORE = 8
// USERS_QUESTIONS = 9
// WATCH_PURCHASE_HISTORY = 10


// TODO - need to check permission and display matching buttons (??)

function ManagerAPI(){
    useEffect(() => {
    // fetchPermissions();
  }, []);

  const [permissions, setPermissions] = useState([]); // to hold the fetched permissions


  // get the manager's permissions
  const fetchPermissions = async () => {
    const promise = registerService.getManagerPermissions(); // goes to register.js and sends to backend
    promise.then((data) => {
        setPermissions(data["data"])
      // TODO - how do we get the permissions? need to think here
    });
  };



    return(

        // TODO - THINK HOW TO DISPLAY BUTTONS ACCORDING TO THE PERMISSIONS
        <Container>
            <div>
                <h1>Welcome Dear Manager!</h1>
            </div>


            {/* <Link to='/managestore'>
                <Button variant="dark" id="manage_store">Manage store</Button>
            </Link> */}

        </Container>
    );

}

export default ManagerAPI;