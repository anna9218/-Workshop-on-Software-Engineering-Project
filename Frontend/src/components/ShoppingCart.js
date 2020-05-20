import React, { useState, useEffect } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import {BrowserRouter as Router, Switch, Route, Link} from 'react-router-dom'
import * as registerService from '../services/register';
import {Button, Jumbotron, Form, Row, Col, Container} from 'react-bootstrap'


function ShoppingCart(){
  useEffect(() => {
    fetchShoppingCart();
  }, []);

  const [shoppingCart, setShoppingCart] = useState([]);

  const [selectedProducts, setSelectedProducts] = useState([]);

  const fetchShoppingCart = async () => {
    const promise = registerService.displayShoppingCart()
    // const stores = await promise.json();
    promise.then((data) => {
      setShoppingCart(data["data"])
    });
  };

  const onButtonClickHandler = () => {
    alert('Product info Product info')
    //TODO, ADD OPTION TO VIEW PRICE, POLICIES
  };

  const removeProductHandler = (event) => {
    const promise = registerService.updateShoppingCart("remove", event.target.value); // goes to register.js and sends to backend
    promise.then((data) => {
      alert(data["msg"])
    });
    //TODO - pass product
  }

  const updateProductAmountHandler = (event) => {
    const promise = registerService.updateShoppingCart("update", event.target.value); // goes to register.js and sends to backend
    promise.then((data) => {
      alert(data["msg"])
    });
    //TODO
  }

  const purchaseProductsHandler = (event) => {
    //TODO
  }

  const selectedProductsHandler = (event) => {
        if(selectedProducts.includes(event.target.value)){
            var index = selectedProducts.indexOf(event.target.value);
            console.log(selectedProducts);
            setSelectedProducts(selectedProducts.splice(index, index+1));
            console.log(selectedProducts);
        }
        else{
            console.log(selectedProducts);
            setSelectedProducts(selectedProducts.concat(event.target.value));
            console.log(selectedProducts);
        }
        console.log(selectedProducts);
    }

  return (
      <div>
        <h1>Shopping Cart</h1>
        <Container>
        {shoppingCart.map(product => (
          <h1>
            
            <Row>
                    <Col />
                    <Col xs={14}>
                        <Row>
            <Button variant="dark" onClick={onButtonClickHandler}>{product}</Button>
            <Form.Check label="select" value={product} 
                            onChange={selectedProductsHandler} type='checkbox' id={`inline-radio-1`} />
            <Button variant="dark" onClick={removeProductHandler}>Remove</Button>
            <Button variant="dark" onClick={updateProductAmountHandler}>Update Amount</Button>
            </Row>
                    </Col>
                    <Col />
                </Row>
                
           
          </h1>
        ))}
        <Button variant="dark" block onClick={purchaseProductsHandler}>Purchase Products</Button>

      </Container>
      </div>
      
  );
}

export default ShoppingCart;