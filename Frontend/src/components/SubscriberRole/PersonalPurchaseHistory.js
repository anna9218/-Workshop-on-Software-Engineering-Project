import React, { useState, useEffect } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import {BrowserRouter as Router, Switch, Route, Link} from 'react-router-dom'
import {Container, Row, Col, Button, Dropdown, Jumbotron, Form} from 'react-bootstrap'
import * as registerService from '../../services/register';


// TODO - call the server, get the purchases, display

function PersonalPurchaseHistory(){
  useEffect(() => {
    fetchPersonalPurchaseHistory();
  }, []);


  const [purchaseHistory, setPurchaseHistory] = useState([]); 

  const fetchPersonalPurchaseHistory = async () => {
    const promise = registerService.fetchPersonalPurchaseHistory(); // goes to register.js and sends to backend
    promise.then((data) => {
      setPurchaseHistory(data["data"])
    });
  };

  const recordOnClickHandler = () => {
    alert('purchase info purchase info')
  };



  return (
      <div>
        <h1>Personal Purchase History</h1>


        {purchaseHistory.map(record => (
          <h1>
            <Button variant="dark" onClick={recordOnClickHandler}>{record}</Button>
          </h1>
        ))}

        <Link to={{
            pathname:'/subscriber'
            }}>
            <Button variant="dark" id="backbtn">Back</Button>
          </Link>


      </div>
  );
}

export default PersonalPurchaseHistory;