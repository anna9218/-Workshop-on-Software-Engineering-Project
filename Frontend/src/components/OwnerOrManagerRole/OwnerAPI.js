import React, {useState} from 'react';
import {Container, Row, Col, Button, Dropdown, Jumbotron, Form} from 'react-bootstrap'
import {Link} from 'react-router-dom'
import * as registerService from '../../services/register';
import SubscriberAPI from '../SubscriberRole/SubscriberAPI';



//---------- WHAT AN OWNER CAN DO? ----------//
// Guest actions 
// Subscriber actions - Logout, Open store, View personal purchase history
// Manage stock (4.1) 
// (4.2)
// Appoint additional owner (4.3)
// Appoint additional manager (4.5)
// Edit manager’s permissions (4.6)
// Remove a store manager (4.7)
// View store’s purchase history (4.10)

// Manage store (5.1) (MANAGER)


function OwnerAPI(){


    return(
        <Container>
            <div>
                <h1>Welcome Dear Owner!</h1>
            </div>


            <Link to='/openstore'>
                <Button variant="dark" id="open_store">Open Store</Button>
            </Link>

            <Link to='/history'>
                <Button variant="dark" id="view_personal_history">View personal purchase history</Button>
            </Link>

            <Link to='/'>
                <Button variant="dark" id="logout">Logout</Button>
            </Link>




            <Link to='/managestock'>
                <Button variant="dark" id="manage_stock">Manage Stock</Button>
            </Link>

            <Link to='/appointowner'>
                <Button variant="dark" id="appoint_owner">Appoint additional owner</Button>
            </Link>

            <Link to='/appointmanager'>
                <Button variant="dark" id="appoint_manager">Appoint additional manager</Button>
            </Link>

            <Link to='/editpermissions'>
                <Button variant="dark" id="edit_perm">Edit manager’s permissions</Button>
            </Link>

            <Link to='/removemanager'>
                <Button variant="dark" id="remove_manager">Remove a store manager</Button>
            </Link>

            <Link to='/storehistory'>
                <Button variant="dark" id="store_history">View store’s purchase history</Button>
            </Link>

            <Link to='/managestore'>
                <Button variant="dark" id="manage_store">Manage store</Button>
            </Link>

        </Container>
    );

}

export default OwnerAPI;