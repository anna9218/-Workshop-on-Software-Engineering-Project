import React, { useState, useEffect } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import {BrowserRouter as Router, Route, Link } from 'react-router-dom'
// import { browserHistory } from "react-router";
import {Container, Button} from 'react-bootstrap'
import * as theService from '../services/communication';


function StoreProducts(props) {
  useEffect(() => {
    console.log(props.location.state.storeName)
    setStoreName(props.location.state.storeName)
    console.log(storeName);
    fetchStoreProducts(props.location.state.storeName);
    // setHistory(useHistory());
  }, []);

  // const [history, setHistory]= useState('');
  const [storeName, setStoreName]= useState('');
  const [storeProducts, setStoreProducts]= useState([]);

  const onButtonClickHandler = () => {
    alert('Product info Product info')
    //TODO, ADD OPTION TO VIEW PRICE, POLICIES
  };

  const fetchStoreProducts = async (storeName) => {
    const promise = theService.displayStoresProducts(storeName)
    promise.then((data) => {
      //TODO make sure this works, maybe bug with response - products are returned as Product objects from the server
      console.log(data["data"]["response"]);
      if (data["data"]["response"].length > 0){   // if there are stores to display
          setStoreProducts(data["data"]["response"]);
      }
      else{
        alert(data["data"]["msg"]);      // no products to display
      }
  });
};

  

  return (
      <div>
        <h1>{storeName} - Products</h1>
        {/* {storeProducts.map(storeProduct => (
          <h1>
            <Button variant="dark" onClick={onButtonClickHandler}>{storeProduct}</Button>
          </h1>
        ))} */}
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