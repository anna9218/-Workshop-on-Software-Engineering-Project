import React, { useState, useEffect } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import {BrowserRouter as Router, Switch, Route, Link} from 'react-router-dom'
import {Container, Button} from 'react-bootstrap'
import * as registerService from '../services/register';


function StoreDetail(props) {
  useEffect(() => {
    console.log(props)
    setStoreName(props.location.state.storeName)
  }, []);
  //TODO - need to send a REQUEST to display store's products

  const [storeName, setStoreName]= useState('');

  const onStoreInfoClickHandler = () => {
    alert('Store info bla bla')
  };

  return (
      <div>
        <h1>{storeName}</h1>
        <Container>
                <Button variant="dark" id="storeinfobtn" block onClick={onStoreInfoClickHandler}>Store Info</Button>
            <Link to={{
                  pathname:'/stores/'+storeName+'/products', 
                  state: {
                      storeName: storeName               
                    }}}>
                <Button variant="dark" id="productsbtn" block>Products</Button>
            </Link>
            <Link to={{
                  pathname:'/stores'
                  }}>
                <Button variant="dark" id="backbtn" block>Back</Button>
            </Link>
        </Container>
      </div>
  );
}


export default StoreDetail;