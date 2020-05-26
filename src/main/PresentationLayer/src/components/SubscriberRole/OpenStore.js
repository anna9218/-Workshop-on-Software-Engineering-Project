import React, {useState} from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import {BrowserRouter as Router, Switch, Route, Link} from 'react-router-dom'
import {Container, Row, Col, Button, Dropdown, Jumbotron, Form} from 'react-bootstrap'
import * as theService from '../../services/communication';


// TODO - display a form to enter new store details. send the entered data to server.

function OpenStore(){

  const [storeNameInput, setStoreNameInput] = useState("");

  const storeNameInputHandler = (event) =>{
    setStoreNameInput(event.target.value);
};

const openStoreHandler = async () =>{
  const promise = theService.openStore(storeNameInput); // goes to register.js and sends to backend
  promise.then((data) => {
    alert(data["msg"]);
  });
  // TODO - GO BACK TO MAIN MENU -> maybe its already working
};


  return (
      <div>
        <h1>Open Store</h1>
        <Container>
        <Form className='open_store'>
          <Form.Label>Choose a name for your new store:</Form.Label>
          <Form.Control id="open-store-text" value={storeNameInput} type="text" placeholder="Store name" className="search" onChange={storeNameInputHandler}/>
        </Form>

        <Link to='/subscriber'>
          <Button variant="dark" id="open-store-button" onClick={openStoreHandler}>Open!</Button>
        </Link>
        </Container>

      </div>
  );
}

export default OpenStore;