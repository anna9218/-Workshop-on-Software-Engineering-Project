import React, { useState, useEffect } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import {BrowserRouter as Router, Switch, Route, Link} from 'react-router-dom'
import {Container, Row, Col, Button, Dropdown, Jumbotron, Form} from 'react-bootstrap'
import * as theService from '../../services/communication';


function PurchaseHistoryUsersStores(){

//   const [userPurchaseHistory, setUserPurchaseHistory] = useState([]);
//   const [storePurchaseHistory, setStorerPurchaseHistory] = useState([]); 
  const [purchaseHistory, setPurchaseHistory] = useState([]); 
  const [userInput, setUserNameInput] = useState('');
  const [storeNameInput, setStoreNameInput] = useState('');
  const [choice, setChoice] = useState(0);

  const userInputHandler = (event) =>{
    setUserNameInput(event.target.value);
    setChoice(1);
  };

  const storeNameInputHandler = (event) =>{
    setStoreNameInput(event.target.value);
    setChoice(2);
  };

  const fetchUserPurchaseHistory = async () => {
    const promise = theService.fetchUserPurchaseHistory(userInput); // goes to register.js and sends to backend
    promise.then((data) => {
        setPurchaseHistory(data["data"]);
    })
  };

  const fetchStorePurchaseHistory = async () => {
    const promise = theService.fetchStorePurchaseHistory(storeNameInput); // goes to register.js and sends to backend
    promise.then((data) => {
        setPurchaseHistory(data["data"]);
    })
  };

  const onViewHandler = () =>{
      if(choice == 1){ // user
        fetchUserPurchaseHistory();
      }
      else{ // store
        fetchStorePurchaseHistory();
      }
  };






  return (
      <div>
        <h1>Purchase History</h1>

        {purchaseHistory.map(record => (
            <h1>
                <Row>
                    <Col />
                    <Col>
                        <Row>
                            <Button variant="dark">{record}</Button>
                        </Row>
                    </Col>
                    <Col />
                </Row>
            </h1>
          ))}

        <Container>
        <Form className='purchase_history'>
        <fieldset>
            <Form.Group as={Row}>
            <Form.Label id="purchase-1" as="legend" column sm={2}>
                Please select:
            </Form.Label>
            <Col>
            <Row>
                <Form.Check
                type="radio"
                label="View users’ purchase history"
                name="purchase-radio"
                id="purchase-radio-1"
                onChange={() => {setChoice(1);}}
                checked={choice==1}
                />
                 <Form.Control type="text" id="purchase-username" value={userInput} placeholder="User name" disabled={choice!=1} onChange={userInputHandler} className="user_name"/>
                </Row>
                <Row>
                <Form.Check
                type="radio"
                label="View stores’ purchase history"
                name="purchase-radio"
                id="purchase-radio-2"
                onChange={() => {setChoice(2);}}
                checked={choice==2}
                />
                <Form.Control type="text" id="purchase-storename" value={storeNameInput} placeholder="Store name" disabled={choice!=2} onChange={storeNameInputHandler} className="store_name"/>
                </Row>
                </Col>
            </Form.Group>
        </fieldset>
        </Form>


        <Button variant="dark" id="purchase-view" onClick={onViewHandler}>View</Button>
        <Link to='/'>
            <Button variant="dark" id="purchase-back">Back</Button>
        </Link>

        </Container>
      </div>
  );
}

export default PurchaseHistoryUsersStores;