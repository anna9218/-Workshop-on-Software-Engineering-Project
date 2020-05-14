import React, { useState, useEffect } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import {BrowserRouter as Router, Route, Link } from 'react-router-dom'
// import { browserHistory } from "react-router";
import {Container, Button} from 'react-bootstrap'
import * as registerService from '../services/register';


function StoreProducts(props) {
  useEffect(() => {
    console.log(props)
    setStoreName(props.location.state.storeName)
    fetchStoreProducts();
    // setHistory(useHistory());
  }, []);

  // const [history, setHistory]= useState('');
  const [storeName, setStoreName]= useState('');
  const [storeProducts, setStoreProducts]= useState([]);

  const onButtonClickHandler = () => {
    alert('Product info Product info')
    //TODO, ADD OPTION TO VIEW PRICE, POLICIES
  };

  const fetchStoreProducts = async () => {
    const promise = registerService.displayShoppingCart()
    promise.then((data) => {
      data["data"].map(storeName =>
      setStoreProducts(data["data"]))
    });
  };

  

  return (
      <div>
        <h1>{storeName} - Products</h1>
        {storeProducts.map(storeProduct => (
          <h1>
            <Button variant="dark" onClick={onButtonClickHandler}>{storeProduct}</Button>
          </h1>
        ))}
        {/* <Link to={{
                  pathname:'/stores/'+storeName
                  }}> */}
                {/* <Button variant="dark" id="backbtn" onClick={history.goBack}>Back</Button> */}
            {/* </Link> */}
      </div>
  );
}

// TODO - add back button


export default StoreProducts;