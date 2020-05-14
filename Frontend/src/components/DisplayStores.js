import React, { useState, useEffect } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import {BrowserRouter as Router, Switch, Route, Link} from 'react-router-dom'
import {Button, Jumbotron} from 'react-bootstrap'
import * as registerService from '../services/register';


function DisplayStores(){
  useEffect(() => {
    setCount(count + 1);
    fetchStores();
  }, []);

  const [count, setCount] = useState(1);
  const [stores, setStores] = useState([]); // Declare a new state variable, which we'll call "stores"

  const fetchStores = async () => {
    const promise = registerService.displayStores(); // goes to register.js and sends to backend
    promise.then((data) => {
      setStores(data["data"])
    });
  };

  return (
    //SET SOME KIND OF COUNTER ID FOR LINK - SOLVED IT WITH STORE NAME
      <div>
        <h1>Display Stores</h1>
        {stores.map(store => (
          <h1>
          <Link to={{
            pathname:'/stores/'+store, 
            state:{
              storeName: store}
            }}>
            <Button variant="dark">{store}</Button>
          </Link>
          </h1>
        ))}
        <Link to={{
            pathname:'/'
            }}>
            <Button variant="dark" id="backbtn">Back</Button>
          </Link>
      </div>
  );
}

export default DisplayStores;




          // <h1 key={store.id}>
          //   <Link to={'/stores/${store.id}'}>
          //     <Button variant="dark">{store.name}</Button>
          //   {/* <button type="button" onClick={this.handleRegister}></button> */}
          //   </Link>
          // </h1>