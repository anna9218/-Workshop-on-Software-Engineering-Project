import React, {useState} from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import {BrowserRouter as Router, Switch, Route, Link} from 'react-router-dom'
import {Container, Row, Col, Button, Dropdown, Jumbotron, Form} from 'react-bootstrap'
import * as theService from '../../services/communication';
import AddProductsForm from './AddProductsForm'


function ManageInventory(){

    const [showAddForm, setShowAddForm] = useState(false);


    const addProductsHandler = (event) =>{
        setShowAddForm(true);
    };
    const removeProductsHandler = (event) =>{
        setShowAddForm(true)
        //TODO
    };
    const editProductsHandler = (event) =>{
        setShowAddForm(true)
        //TODO
    };



    return (
        <div>
          <h1>Manage Inventory</h1>
          <Container> 
            <Button variant="dark" id="open-store-button" onClick={addProductsHandler}>Add Products</Button>
            <Button variant="dark" id="open-store-button" onClick={removeProductsHandler}>Remove Products</Button>
            <Button variant="dark" id="open-store-button" onClick={editProductsHandler}>Edit Products Details</Button>

            { showAddForm ? <AddProductsForm /> : null }
          
          
          
          
          </Container>
  
        </div>
    );

}



export default ManageInventory;