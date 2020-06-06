import React, {useState, useEffect} from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import {BrowserRouter as Router, Switch, Route, Link} from 'react-router-dom'
import {Container, Row, Col, Button, Dropdown, Jumbotron, Form} from 'react-bootstrap'
import * as theService from '../../services/communication';

import { confirmAlert } from 'react-confirm-alert'; 
import 'react-confirm-alert/src/react-confirm-alert.css'; // Import css



function AddProductsForm(props){
  useEffect(() => {
    console.log(props);
    setStoreName(props.storeName);
    // setShowAddFormFunction(props.showForm);
  }, []);

  const [storeName, setStoreName]= useState("");
  // const [showAddFormFunction, setShowAddFormFunction]= useState();

  const [productName, setProductName] = useState("");
  const [productPrice, setProductPrice] = useState();
  const [productCategory, setProductCategory] = useState("");
  const [productAmount, setProductAmount] = useState();

  const addProductHandler = async () =>{
    const promise = theService.addProduct(storeName, productName, productPrice, productCategory, productAmount); // goes to register.js and sends to backend
    promise.then((data) => {

        confirmAlert({
        title: data["msg"],
        buttons: [
          {
            label: 'Add another product',
            onClick: () => { // reset the form in order to add another product
              setProductName("");
              setProductPrice("");
              setProductCategory("");
              setProductAmount("");
            }
          },
          {
            label: 'Done',
            onClick: () => alert('Click No')  //TODO - add an option to go back (need to disable addProductForm)
          }
        ]
      });

    });
  };


  return (
      <div style={{width: props["screenWidth"], height: props["screenHeight"]}}>

        <Container>
        <h1>Add a New Product</h1>
        <Form className='add_product'>
          <Form.Label>Choose the product name:</Form.Label>
          <Form.Control id="product-name" value={productName} required type="text" placeholder="Product name"
          onChange={(event => {
            setProductName(event.target.value)
          })}/>

          <Form.Label>Set the price:</Form.Label>
          <Form.Control id="product-price" value={productPrice} required type="text" required placeholder="Product price" 
          onChange={(event => {
            setProductPrice(event.target.value)
          })}/>
          
          <Form.Label>Enter the category:</Form.Label>
          <Form.Control id="product-category" value={productCategory} required type="text" placeholder="Category" 
          onChange={(event => {
            setProductCategory(event.target.value)
          })}/>
          
          <Form.Label>Enter the amount:</Form.Label>
          <Form.Control id="product-amount" value={productAmount} required type="text" placeholder="Product amount" 
          onChange={(event => {
            setProductAmount(event.target.value)
          })}/>
        </Form>

        <Button variant="dark" id="open-store-button" onClick={addProductHandler}>Add Product!</Button>
        </Container>

      </div>
  );
}

export default AddProductsForm;