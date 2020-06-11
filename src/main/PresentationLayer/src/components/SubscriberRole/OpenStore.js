import React, {useState} from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import {BrowserRouter as Router, Switch, Route, Link, Redirect} from 'react-router-dom'
import {Container, Row, Col, Button, Dropdown, Jumbotron, Form} from 'react-bootstrap'
import * as theService from '../../services/communication';
import * as BackOption from '../Actions/GeneralActions/Back'
// TODO - display a form to enter new store details. send the entered data to server.

class OpenStore extends React.Component {
    constructor(props){
      super(props);
      this.state = {
        storeNameInput: "",
      }

      // bind handlers
      this.storeNameInputHandler = this.storeNameInputHandler.bind(this);
      this.openStoreHandler = this.openStoreHandler.bind(this);
    }

  storeNameInputHandler = (event) =>{
    this.setState({storeNameInput: event.target.value});
  };

  openStoreHandler = async () =>{
    const promise = theService.openStore(this.state.storeNameInput); // goes to register.js and sends to backend
    promise.then((data) => {
      alert(data["msg"]);
      if(data["data"]){ // store created
          // redirect to store owner home page
          this.props.history.push("./owner")
      }
      else{
        return;
      }
    });
  };

  render(){
    return (
      <div style={{width: this.props["screenWidth"], height: this.props["screenHeight"]}}>
        <h1>Open Store</h1>
        <Container>
        <Form className='open_store'>
          <Form.Label>Choose a name for your new store:</Form.Label>
          <Form.Control id="open-store-text" value={this.state.storeNameInput} type="text" placeholder="Store name" className="search" onChange={this.storeNameInputHandler}/>
        </Form>

        <Button variant="dark" id="add_product-button" onClick={event => BackOption.BackToHome(this.props)} style={{marginTop: "1%"}}>Back</Button>
        <Button variant="dark" id="open-store-button" onClick={this.openStoreHandler} style={{marginTop: "1%", marginLeft: "1%"}}>Open!</Button>

        </Container>
        
      </div>
    );
  }
  
}

export default OpenStore;