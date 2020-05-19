import React, {useState} from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import {BrowserRouter as Router, Switch, Route, Link} from 'react-router-dom'
import {Container, Row, Col, Button, Dropdown, Jumbotron, Form} from 'react-bootstrap'
import * as registerService from '../../services/register';


// TODO - display a form to enter new store details. send the entered data to server.

function OpenStore(){

  const [storeNameInput, setStoreNameInput] = useState('');

  const storeNameInputHandler = (event) =>{
    setStoreNameInput(event.target.value);
};

const openStoreHandler = async () =>{
  const promise = registerService.openStore(storeNameInput); // goes to register.js and sends to backend
  promise.then((data) => {
    alert(data["msg"]);
  });
  // TODO - GO BACK TO MAIN MENU -> maybe its already working
};


  return (
      <div>
        <h1>Open Store</h1>
        <Container>
        <Form>
          <Form.Label>Choose a name for your new store:</Form.Label>
          <Form.Control type="text" placeholder="Store name" className="search" onChange={storeNameInputHandler}/>
        </Form>

        <Link to='/subscriber'>
                <Button variant="dark" id="view_personal_history" onClick={openStoreHandler}>Open!</Button>
        </Link>
        </Container>

      </div>
  );
}

export default OpenStore;