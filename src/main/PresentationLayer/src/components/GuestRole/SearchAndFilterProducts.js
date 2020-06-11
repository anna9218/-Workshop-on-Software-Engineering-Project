import React, { useState, useEffect } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import {BrowserRouter as Router,  Route, Link } from 'react-router-dom'
// import { browserHistory } from "react-router";
import {Container, Button, Accordion, Card, Table, Form, Col, Row, InputGroup, FormControl, FormCheck} from 'react-bootstrap'
import * as theService from '../../services/communication';


function SearchAndFilterProducts(props) {
  useEffect(() => {
    // console.log(props.location.state.storeName)
    // setStoreName(props.location.state.storeName)
    // console.log(storeName);
    // fetchStoreProducts(props.location.state.storeName);
    // setHistory(useHistory());
  }, []);

  // const [history, setHistory]= useState('');
  const [storeName, setStoreName] = useState('');
  const [storeProducts, setStoreProducts] = useState([]);
  const [productAmount, setProductAmount] = useState(0);
  const [showAddToCart, setShowAddToCart] = useState(false);
  const [amountValidated, setAmountValidated] = useState(true);
  const [input, setInput] = useState("");
  const [searchType, setSearchType] = useState(0);
  const [filterType, setFilterType] = useState(0);
  const [filterCategory, setFilterCategory] = useState("");
  const [filterMinPrice, setFilterMinPrice] = useState(0);
  const [filterMaxPrice, setFilterMaxPrice] = useState(0);

  const onButtonClickHandler = () => {
    alert('Product info Product info')
    //TODO, ADD OPTION TO VIEW PRICE, POLICIES
  };

  const addToCartHandler = async (store_name, product_name) => {
    // need - store_name, product_name, product_amount
    const promise = theService.addToProductsCart(store_name, product_name , productAmount)
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

  const SearchProductsHandler = () => {
    const promise = theService.searchProductsBy(searchType, input);
    promise.then((data) => {

      if(data != null){
        if (data["data"] != null && data["data"].length > 0){   // if there are stores to display
          setStoreProducts(data["data"]);
          alert(data["msg"]);      // no products to display

        }
        else{
          alert("There are no results.");      // no products to display
        }
      }
  });
};

const FilterProductsHandler = () => {
    // const promise;
    if(filterType === 1){
        const promise = theService.filterProductsByRange(storeProducts, filterType, filterMinPrice, filterMaxPrice);
        promise.then((data) => {

            if(data != null){
              if (data["data"] != null && data["data"].length > 0){   // if there are stores to display
                setStoreProducts(data["data"]);
                // alert(data["msg"]);      // no products to display
      
              }
              else{
                alert("There are no results.");      // no products to display
              }
            }
        });
    }
    else if(filterType === 2){
        const promise = theService.filterProductsByCategory(storeProducts, filterType, filterCategory);
        promise.then((data) => {

            if(data != null){
              if (data["data"] != null && data["data"].length > 0){   // if there are stores to display
                setStoreProducts(data["data"]);
                // alert(data["msg"]);      // no products to display
      
              }
              else{
                alert("There are no results.");      // no products to display
              }
            }
        });

    }
    
};

  return (
    <div style={{width: props["screenWidth"], height: props["screenHeight"]}}>
      <div style={{marginTop:"1%"}}>
        <h2>Search and filter Products </h2>
      </div>

     <Accordion>
        <Card>
            <Card.Header>
            <Accordion.Toggle as={Button} type="radio" variant="link" eventKey="0">
                Search products
            </Accordion.Toggle>
            </Card.Header>
            <Accordion.Collapse eventKey="0">
            <Card.Body>
                
                {/******** search component *********/}
                <div style={{marginTop:"0.5%" , marginLeft: "10%", marginRight: "10%", border: "1px solid", borderColor: "#CCCCCC"}}>
                    <Form>
                        <fieldset>
                            <Form.Group as={Row} >
                                <Form.Label as="legend" column sm={2}>
                                    Search products by:
                                </Form.Label>
                                <Form.Check inline onClick={(event => {setSearchType(1)})} type="radio" label="By name" name="formHorizontalRadios"id="Radios1"/>
                                <Form.Check inline onClick={(event => {setSearchType(2)})} type="radio" label="By keyword" name="formHorizontalRadios"id="Radios2"/>
                                <Form.Check inline onClick={(event => {setSearchType(3)})} type="radio" label="By category" name="formHorizontalRadios"id="Radios3"/>
                                <Form.Control style={{marginRight:"2%" , marginLeft: "2%"}} onChange={(event => {setInput(event.target.value)})} placeholder="Enter relevant text..." />
                            </Form.Group>
                        </fieldset>
                        <Form.Group as={Row} style={{marginRight:"1%" , marginLeft: "1%"}}>
                            <Button  onClick= {(event => {SearchProductsHandler()})} >Search</Button>
                        </Form.Group>
                    </Form>
                </div>

            </Card.Body>
            </Accordion.Collapse>
        </Card>
        <Card>
            <Card.Header>
            <Accordion.Toggle as={Button} variant="link" eventKey="1">
                Filter products
            </Accordion.Toggle>
            </Card.Header>
            <Accordion.Collapse eventKey="1">
            <Card.Body>
                {/******** filter component *********/}
                <div style={{marginTop:"0.5%" , marginLeft: "10%", marginRight: "10%", border: "1px solid", borderColor: "#CCCCCC"}}>
                    <Form>
                        <fieldset>
                            {/* <Form.Group as={Row} >
                                <Form.Label as="legend" column sm={2}>
                                    Filter products by:
                                </Form.Label>
                                <Form.Check inline onClick={(event => {setSearchType(1)})} type="radio" label="By price range" name="formHorizontalRadios"id="Radios1"/>
                                <Form.Check inline onClick={(event => {setSearchType(2)})} type="radio" label="By category" name="formHorizontalRadios"id="Radios2"/>
                                
                                <Form.Control style={{marginRight:"2%" , marginLeft: "2%"}} onChange={(event => {setInput(event.target.value)})} placeholder="Enter relevant text..." />
                            </Form.Group> */}

                        <Form.Group as={Row} style={{marginTop: "1%", marginRight:"4%" , marginLeft: "0%"}} >
                            <Form.Label column sm="2">
                                <Form.Check inline onClick={(event => {setFilterType(1)})} type="radio" label="By price range" name="formHorizontalRadios"id="Radios1"/>                                
                            </Form.Label>
                            <Col sm="10">
                                <Form.Control placeholder="Enter min price" onChange={(event => {setFilterMinPrice(event.target.value)})} />
                                <Form.Control style={{marginTop: "1%"}} placeholder="Enter max price" onChange={(event => {setFilterMaxPrice(event.target.value)})}/>
                            </Col>
                            <Form.Label column sm="2" >
                                <Form.Check inline onClick={(event => {setFilterType(2)})} type="radio" label="By category" name="formHorizontalRadios"id="Radios1"/>                                
                            </Form.Label>
                            <Col sm="10">
                                <Form.Control style={{marginTop: "1%"}} placeholder="Enter category" onChange={(event => {setFilterCategory(event.target.value)})}/>
                            </Col>
                                
                        </Form.Group>
                        </fieldset>
                        

                        <Form.Group as={Row} style={{marginRight:"3%" , marginLeft: "3%"}}>
                            <Button  onClick= {(event => {FilterProductsHandler()})} >Filter</Button>
                        </Form.Group>
                    </Form>
                </div>
            </Card.Body>
            </Accordion.Collapse>

      </Card>
      </Accordion>
        {/******** diplay products *********/}
      <div style={{marginTop: "3%", marginLeft: "1%", marginRight: "1%"}}>
        <Table striped bordered hover >
          <thead>
              <tr>
                  <th>Store Name</th>
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
                      <td>{storeProduct["store_name"]}</td>
                      <td>{storeProduct["product_name"]}</td>
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
                                    amountValidated ? addToCartHandler(storeProduct["store_name"], storeProduct["product_name"]) : alert("Please enter number greater than 0 and smaller than " + storeProduct["amount"]);
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