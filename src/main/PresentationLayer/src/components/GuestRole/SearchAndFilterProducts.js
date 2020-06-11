import React, { useState, useEffect } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import {BrowserRouter as Router,  Route, Link } from 'react-router-dom'
// import { browserHistory } from "react-router";
import {Container, Button, Table, Form, Col, Row, InputGroup, FormControl} from 'react-bootstrap'
import * as theService from '../../services/communication';


function SearchAndFilterProducts(props) {
  useEffect(() => {
    console.log(props.location.state.storeName)
    setStoreName(props.location.state.storeName)
    console.log(storeName);
    fetchStoreProducts(props.location.state.storeName);
    // setHistory(useHistory());
  }, []);

  // const [history, setHistory]= useState('');
  const [storeName, setStoreName] = useState('');
  const [storeProducts, setStoreProducts] = useState([]);
  const [productAmount, setProductAmount] = useState(0);
  const [showAddToCart, setShowAddToCart] = useState(false);
  const [amountValidated, setAmountValidated] = useState(true);

  const onButtonClickHandler = () => {
    alert('Product info Product info')
    //TODO, ADD OPTION TO VIEW PRICE, POLICIES
  };

  const addToCartHandler = async (product_name) => {
    // need - store_name, product_name, product_amount
    const promise = theService.addToProductsCart(storeName, product_name , productAmount)
    promise.then((data => {
      if(data != null){
        if(data["msg"] != null){
          alert(data["msg"]);
        }
      }
    }))
  }

  const showAddToCartHandler = async () => {
    if(showAddToCart){
      setShowAddToCart(false);
    }
    else{
      setShowAddToCart(true);
    }
  }

  const fetchStoreProducts = async (storeName) => {
    const promise = theService.displayStoresProducts(storeName)
    promise.then((data) => {
      if(data != null){
        if (data["data"] != null && data["data"].length > 0){   // if there are stores to display
          setStoreProducts(data["data"]);
        }
        else{
          alert(data["msg"]);      // no products to display
        }
      }
  });
};

  return (
    <div style={{width: props["screenWidth"], height: props["screenHeight"]}}>
      <div style={{marginTop:"1%"}}>
        <h2>Search and filter Products </h2>
      </div>

      <div style={{marginTop:"3%" , marginRight: "89%"}}> Search products by: </div>
      <div style={{marginTop:"0.5%" , marginLeft: "1%", marginRight: "1%", border: "1px solid", borderColor: "#CCCCCC"}}>
      <Form>
        <Form.Group as={Row} controlId="formHorizontalPassword">
            <Form.Label column sm={2}>
            Password
            </Form.Label>
            <Col sm={10}>
            <Form.Control type="password" placeholder="Enter relevant text..." />
            </Col>
        </Form.Group>
        <fieldset>
            <Form.Group as={Col}>
            <Row sm={10}>

            <Form.Label as="legend" column sm={2}>
                Search products by:
            </Form.Label>
                <Form.Check type="radio" label="By name" name="formHorizontalRadios"id="Radios1"/>
                <Form.Check type="radio" label="By keyword" name="formHorizontalRadios"id="Radios2"/>
                <Form.Check type="radio" label="By category" name="formHorizontalRadios"id="Radios3"/>
               
            </Row>
            </Form.Group>
        </fieldset>

        <Form.Group as={Row}>
            <Col sm={{ span: 10, offset: 2 }}>
            <Button type="submit">Sign in</Button>
            </Col>
        </Form.Group>
        </Form>
      </div>

      <div style={{marginTop: "3%", marginLeft: "1%", marginRight: "1%"}}>
        <Table striped bordered hover >
          <thead>
              <tr>
                  <th>Product Name</th>
                  <th>Price</th>
                  <th>Category</th>
                  <th>Amount</th>
                  <th>
                    <Form.Check id="add-to-cart-checkbox" type="checkbox" label="Add To Cart" onChange={showAddToCartHandler} />
                  </th>
              </tr>
          </thead>
          <tbody>
              {
                storeProducts.map(storeProduct => (
                  <tr>
                      <td>{storeProduct["name"]}</td>
                      <td>{storeProduct["price"]}</td>
                      <td>{storeProduct["category"]}</td>
                      <td>{storeProduct["amount"]}</td>
                      <td>
                        {
                          showAddToCart ? 
                          <div>
                              <InputGroup className="mb-3">
                                <Form.Control id="product-amount" required type="text" placeholder="Product amount" style={{width:"1px"}}
                                  onChange={(event => {
                                    try{
                                      let value = parseInt(event.target.value);
                                      if(value > 0 && value <= storeProduct["amount"]){
                                        setProductAmount(value);
                                        setAmountValidated(true);
                                      }
                                      else{
                                        setAmountValidated(false);                             
                                      }
                                    }
                                    catch(e){
                                      setAmountValidated(false);
                                    }
                                    
                                  })}/>
                                  
                                <InputGroup.Prepend>
                                  <Button variant="dark" id="addToCartBtn" onClick={(event => {
                                    amountValidated ? addToCartHandler(storeProduct["name"]) : alert("Please enter number greater than 0 and smaller than " + storeProduct["amount"]);
                                    })}>
                                      Add To Cart
                                  </Button>
                                </InputGroup.Prepend>
                              </InputGroup>
                          </div>
                          : null
                        }
                      </td>
                  </tr>
                ))
              }
          </tbody>
        </Table>
      </div>
    </div>
  );
}

// TODO - add back button


export default SearchAndFilterProducts;