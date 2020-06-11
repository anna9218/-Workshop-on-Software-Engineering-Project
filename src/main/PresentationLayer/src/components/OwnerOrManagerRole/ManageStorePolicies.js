import React, { useState, useEffect } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import {BrowserRouter as Router,  Route, Link } from 'react-router-dom'
// import { browserHistory } from "react-router";
import {Container, Button, Accordion, Card, Table, Form, Col, Row, InputGroup, FormControl, FormCheck} from 'react-bootstrap'
import * as theService from '../../services/communication';


function ManageStorePolicies(props) {
  useEffect(() => {
    // console.log(props.location.state.storeName)
    setStoreName(props.location.store)
    // console.log(storeName);
    fetchPurchasePolicies("purchase", props.location.store);
    fetchDiscountPolicies("discount", props.location.store);
    // setHistory(useHistory());
  }, []);

  // const [history, setHistory]= useState('');
  const [storeName, setStoreName] = useState('');
  const [purchasePolicies, setPurchasePolicies] = useState(["There are no purchase policies."]);
  const [input, setInput] = useState("");
  const [policyName, setPolicyName] = useState("");
  const [filterCategory, setFilterCategory] = useState("");
  const [filterMinPrice, setFilterMinPrice] = useState(-1);
  const [filterMaxPrice, setFilterMaxPrice] = useState(-1);


  


  // const addToCartHandler = async (store_name, product_name) => {
  //   // need - store_name, product_name, product_amount
  //   const promise = theService.addToProductsCart(store_name, product_name , productAmount)
  //   promise.then((data => {
  //     if(data != null){
  //       if(data["msg"] != null){
  //         alert(data["msg"]);
  //       }
  //     }
  //   }))
  // }

  const fetchPurchasePolicies = (policy_name, store_name) => {
    const promise = theService.getPolicies(policy_name, store_name);
    promise.then((data) => {

      if(data != null){
        if (data["data"] != null && data["data"].length > 0){   // if there are stores to display
          setPurchasePolicies(data["data"]);
          // setPolicyName(0);
        //   alert(data["msg"]);      // no products to display

        }
        else{
          setPurchasePolicies(["There are no purchase policies."]);
        }
      }
  });
};

const fetchDiscountPolicies = () => {}
// const FilterProductsHandler = () => {
//     // const promise;
//     if(filterType === 1){
//         if(filterMinPrice > filterMaxPrice)
//             alert("Error, minimum price can't be bigger than maximum");
//         else{
//             const promise = theService.filterProductsByRange(storeProducts, filterType, filterMinPrice, filterMaxPrice);
//             promise.then((data) => {

//                 if(data != null){
//                 if (data["data"] != null && data["data"].length > 0){   // if there are stores to display
//                     setStoreProducts(data["data"]);
//                     setFilterType(0);
//                     setFilterCategory("");
//                     setFilterMaxPrice(-1);
//                     setFilterMinPrice(-1);
//                     // alert(data["msg"]);      // no products to display
        
//                 }
//                 else{
//                     setStoreProducts([]);
//                     // alert(data["msg"]);
//                     alert("There are no results.");      // no products to display
//                     setFilterType(0);
//                     setFilterCategory("");
//                     setFilterMaxPrice(-1);
//                     setFilterMinPrice(-1);
                    
//                 }
//                 }
//             });
//         }
//     }
//     else if(filterType === 2){
//         const promise = theService.filterProductsByCategory(storeProducts, filterType, filterCategory);
//         promise.then((data) => {

//             if(data != null){
//               if (data["data"] != null && data["data"].length > 0){   // if there are stores to display
//                 setStoreProducts(data["data"]);
//                 // alert(data["msg"]);      // no products to display
      
//               }
//               else{
//                 setStoreProducts([]);
//                 alert("There are no results.");      // no products to display
//               }
//             }
//         });

//     }
    
// };

  return (
    <div style={{width: props["screenWidth"], height: props["screenHeight"]}}>
      <div style={{marginTop:"1%"}}>
        <h2> {storeName} - Manage Store Policies </h2>
      </div>

     <Accordion>
        <Card>
            {/******** Purchase Card *********/}
            <Card.Header>
            <Accordion.Toggle as={Button} type="radio" variant="link" eventKey="0">
                Purchase Policy
            </Accordion.Toggle>
            </Card.Header>
            <Accordion.Collapse eventKey="0">
            <Card.Body>
                
                <div style={{marginTop:"0.5%" , marginLeft: "10%", marginRight: "10%", border: "1px solid", borderColor: "#CCCCCC"}}>
                    
                  
                    <Form>
                        <fieldset>
                            <Form.Group as={Row}  style={{ marginTop:"2%", marginRight:"1%" , marginLeft: "1%"}}>
                              <Form.Control as="select">
                                  {purchasePolicies.map(store => (
                                      <option value={store}>{store}</option>
                                  ))}
                              </Form.Control>
                                {/* <Form.Label as="legend" column sm={2}>
                                    Search products by:
                                </Form.Label> */}
                                {/* <Form.Check inline onClick={(event => {setSearchType(1)})} type="radio" label="By name" name="formHorizontalRadios"id="Radios1"/>
                                <Form.Check inline onClick={(event => {setSearchType(2)})} type="radio" label="By keyword" name="formHorizontalRadios"id="Radios2"/>
                                <Form.Check inline onClick={(event => {setSearchType(3)})} type="radio" label="By category" name="formHorizontalRadios"id="Radios3"/>
                                <Form.Control disabled={!searchType}  style={{marginRight:"2%" , marginLeft: "2%"}} onChange={(event => {setInput(event.target.value)})} placeholder="Enter relevant text..." /> */}
                            </Form.Group>
                        </fieldset>
                        <Form.Group as={Row} style={{marginRight:"1%" , marginLeft: "1%"}}>
                            <Button inline type="reset" variant="dark">Add</Button>
                            <Button inline type="reset" variant="dark">Edit</Button>
                        </Form.Group>
                    </Form>
                </div>

            </Card.Body>
            </Accordion.Collapse>
        </Card>
        <Card>
              {/***************** Discount card *******************/}

            <Card.Header>
            <Accordion.Toggle as={Button} variant="link" eventKey="1">
                Discount Policy
            </Accordion.Toggle>
            </Card.Header>
            <Accordion.Collapse eventKey="1">
            <Card.Body>
                <div style={{marginTop:"0.5%" , marginLeft: "10%", marginRight: "10%", border: "1px solid", borderColor: "#CCCCCC"}}>
                    {/* <Form>
                        <fieldset>
                        <Form.Group as={Row} style={{marginTop: "1%", marginRight:"4%" , marginLeft: "0%"}} >
                            <Form.Label column sm="2">
                                <Form.Check inline onClick={(event => {setFilterType(1)})} type="radio" label="By price range" name="formHorizontalRadios"id="Radios1"/>                                
                            </Form.Label>
                            <Col sm="10">
                                <Form.Control disabled={(filterType !== 1)} placeholder="Enter min price" onChange={(event =>{
                                        try{ 
                                            let value = parseInt(event.target.value);
                                            if(value < 0)
                                                alert("Error - Price has to be bigger than 0.");
                                            else
                                                setFilterMinPrice(value);
                                        }
                                        catch(e){
                                            alert("Error - Price has to be a number.");
                                        }
                                    })}/>
                                <Form.Control disabled={(filterType !== 1)} style={{marginTop: "1%"}} placeholder="Enter max price"  onChange={(event =>{
                                        try{ 
                                            let value = parseInt(event.target.value);
                                            if(value < 0)
                                                alert("Error - Price has to be bigger than 0.");
                                            else
                                                setFilterMaxPrice(value);
                                        }
                                        catch(e){
                                            alert("Error - Price has to be a number.");
                                        }
                                    })}/>
                            </Col>
                            <Form.Label column sm="2" >
                                <Form.Check inline onClick={(event => {setFilterType(2)})} type="radio" label="By category" name="formHorizontalRadios"id="Radios1"/>                                
                            </Form.Label>
                            <Col sm="10">
                                <Form.Control disabled={(filterType !== 2)} style={{marginTop: "1%"}} placeholder="Enter category" onChange={(event => {setFilterCategory(event.target.value)})}/>
                            </Col>
                                
                        </Form.Group>
                        </fieldset>
                        

                        <Form.Group as={Row} style={{marginRight:"3%" , marginLeft: "3%"}}>
                            <Button type="reset" disabled={(
                                                            !(filterType === 1 && (filterMaxPrice !== -1 && filterMinPrice !== -1)) &&
                                                            !(filterType === 2 && filterCategory !== ""))}onClick= {(event => {FilterProductsHandler()})} >Filter</Button>
                        </Form.Group>
                    </Form> */}
                </div>
            </Card.Body>
            </Accordion.Collapse>

      </Card>
      </Accordion>
    </div>
  );
}

// TODO - add back button


export default ManageStorePolicies;