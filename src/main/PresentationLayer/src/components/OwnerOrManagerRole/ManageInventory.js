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
          <h2>Manage Inventory</h2>

            <Container> 
            <div style={{marginTop:"3%" , marginLeft: "25%", marginRight: "25%", border: "1px solid", borderColor: "#CCCCCC"}}>

                <h3 style={{marginTop:"2%"}}>Store: {selectedStore}</h3>
                <Form style={{marginRight:"5%" , marginLeft: "5%", marginBottom:"2%"}}>
                    <Row><Form.Check onClick={addProductsHandler} type="radio" label="Add Products" name="formHorizontalRadios" id="Radios1"/>
                    </Row>
                    <Row><Form.Check inline onClick={removeProductsHandler} type="radio" label="Remove Products" name="formHorizontalRadios"id="Radios2"/>
                    </Row>
                    <Row><Form.Check inline onClick={editProductsHandler} type="radio" label="Edit Products Details" name="formHorizontalRadios"id="Radios3"/>
                    </Row>
                </Form>
            </div>
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