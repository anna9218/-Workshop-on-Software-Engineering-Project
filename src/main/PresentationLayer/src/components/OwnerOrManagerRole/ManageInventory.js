import React, {useState, useEffect} from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import {BrowserRouter as Router, Switch, Route, Link} from 'react-router-dom'
import {Container, Row, Col, Button, Dropdown, Jumbotron, Form} from 'react-bootstrap'
import * as theService from '../../services/communication';
import AddProductsForm from './AddProductsForm'
import EditProductsForm from './EditProductsForm';
import * as BackOption from '../Actions/GeneralActions/Back'
import DeleteProductsForm from './DeleteProductForm';


function ManageInventory(props){
    useEffect(() => {
        // alert(props.location.props)
        setSelectedStore(props.location.store)
    }, []);

    const [selectedStore, setSelectedStore] = useState("");
    const [showAddForm, setShowAddForm] = useState(false);
    const [showEditForm, setShowEditForm] = useState(false);
    const [showDeleteForm, setShowDeleteForm] = useState(false);

    const addProductsHandler = (event) =>{
        setShowAddForm(true);
        setShowDeleteForm(false);
        setShowEditForm(false);
    };

    const removeProductsHandler = (event) =>{
        setShowAddForm(false)
        setShowDeleteForm(true);
        setShowEditForm(false);
    };

    const editProductsHandler = (event) =>{
        setShowAddForm(false)
        setShowDeleteForm(false);
        setShowEditForm(true);
    };

    return (
        <div style={{width: props["screenWidth"], height: props["screenHeight"]}}>
          <h1>Manage Inventory</h1>

            <Container> 
                <h1>Store: {selectedStore}</h1>
                <Button variant="dark" id="add_product-button" onClick={addProductsHandler}>Add Products</Button>
                <Button variant="dark" id="delete-product-button" onClick={removeProductsHandler}>Remove Products</Button>
                <Button variant="dark" id="edit-product-button" onClick={editProductsHandler}>Edit Products Details</Button>

            <div style={{marginTop: "5%"}}>
                { showAddForm ? <AddProductsForm storeName={selectedStore} history={props.location.props} /> : null }
            </div>
            <div style={{marginTop: "5%"}}>
                { showEditForm ? <EditProductsForm storeName={selectedStore} history={props.location.props} /> : null }
            </div>
            <div style={{marginTop: "5%"}}>
                { showDeleteForm ? <DeleteProductsForm storeName={selectedStore} history={props.location.props} /> : null }
            </div>

            <Button style={{marginTop: "1%"}}  variant="dark" id="add_product-button" onClick={event => BackOption.BackToHome(props.location.props)}>Back</Button>
          
            </Container>
  
        </div>
    );

}

export default ManageInventory;