import React, {useState, useEffect} from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import {BrowserRouter as Router, Switch, Route, Link} from 'react-router-dom'
import {Container, Row, Col, Button, Dropdown, Jumbotron, Form} from 'react-bootstrap'
import * as theService from '../../services/communication';
import AddProductsForm from './AddProductsForm'


function ManageInventory(props){
    useEffect(() => {
        fetchOwnedStores();
    }, []);

    const [stores, setStores] = useState(["No owned stores"]);
    const [selectedStore, setSelectedStore] = useState("");
    const [showAddForm, setShowAddForm] = useState(false);
    const [showOptionsForm, setShowOptionsForm] = useState(false);


    const fetchOwnedStores = async () => {
        const promise = theService.fetchOwnedStores();  // goes to communication.js and sends to server
        promise.then((data) => {
            if (data["data"]["response"].length > 0){   // if there are owned stores
                setStores(data["data"]["response"]);
            }
            else{
                setStores([data["data"]["msg"]]);       // no owned stores, array if empty
            }
        });
    };

    const addProductsHandler = (event) =>{
        if(selectedStore == ""){
            setSelectedStore(stores[0]);
        }

        setShowAddForm(true);
    };

    const removeProductsHandler = (event) =>{
        if(selectedStore == ""){
            setSelectedStore(stores[0]);
        }

        setShowAddForm(false)
        //TODO
    };

    const editProductsHandler = (event) =>{
        if(selectedStore == ""){
            setSelectedStore(stores[0]);
        }

        setShowAddForm(false)
        //TODO
    };



    return (
        <div style={{width: props["screenWidth"], height: props["screenHeight"]}}>
          <h1>Manage Inventory</h1>

            <Form.Group controlId="stores_ControlSelect1" onChange={ event => {setSelectedStore(event.target.value);}}>
            <Form.Label>Please choose a store:</Form.Label>
            <Form.Control as="select">
                {stores.map(store => (
                    <option value={store}>{store}</option>
                ))}
            </Form.Control>
            </Form.Group>


            <Container> 
                <Button variant="dark" id="open-store-button" onClick={addProductsHandler}>Add Products</Button>
                <Button variant="dark" id="open-store-button" onClick={removeProductsHandler}>Remove Products</Button>
                <Button variant="dark" id="open-store-button" onClick={editProductsHandler}>Edit Products Details</Button>

            <div style={{marginTop: "5%"}}>
                { showAddForm ? <AddProductsForm storeName={selectedStore} /> : null }
            </div>
            {/* { showAddForm ? <AddProductsForm storeName={selectedStore} showForm={() => setShowAddForm(false)}/> : null } */}
          
          
            </Container>
  
        </div>
    );

}



export default ManageInventory;