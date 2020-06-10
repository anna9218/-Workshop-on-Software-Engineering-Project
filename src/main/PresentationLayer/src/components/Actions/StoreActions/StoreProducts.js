import React, { useState, useEffect } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import {BrowserRouter as Router, Route, Link } from 'react-router-dom'
// import { browserHistory } from "react-router";
import {Container, Button, Table} from 'react-bootstrap'
import * as theService from '../../../services/communication';


function StoreProducts(props) {
  useEffect(() => {
    console.log(props.location.state.storeName)
    setStoreName(props.location.state.storeName)
    console.log(storeName);
    fetchStoreProducts(props.location.state.storeName);
    // setHistory(useHistory());
  }, []);

  // const [history, setHistory]= useState('');
  const [storeName, setStoreName] = useState('');
  const [storeProducts, setStoreProducts] = useState([]);
  const [productAmount, setProductAmount] = useState(0);

  const onButtonClickHandler = () => {
    alert('Product info Product info')
    //TODO, ADD OPTION TO VIEW PRICE, POLICIES
  };

  const addToCartHandler = (product_name) => {
    // need - store_name, product_name, product_amount
    const promise = theService.addToProductsCart(storeName, product_name , productAmount)
    promise.then((data => {
        if(data["msg"] != null){
          alert(data["msg"]);
        }
    }))
  }

  const fetchStoreProducts = async (storeName) => {
    const promise = theService.displayStoresProducts(storeName)
    promise.then((data) => {
      if(data != null){
        if (data["data"] != null && data["data"].length > 0){   // if there are stores to display
          setStoreProducts(data["data"]);
        }
        else{
          alert(data["msg"]);      // no products to display
        }
      }
  });
};

  return (
    <div>
      <div>
        <h1>{storeName} - Products</h1>
      </div>

      <div style={{marginTop: "3%", marginLeft: "1%", marginRight: "1%"}}>
        <Table striped bordered hover >
          <thead>
              <tr>
                  <th>Product Name</th>
                  <th>Price</th>
                  <th>Category</th>
                  <th>Amount</th>
                  <th></th>
              </tr>
          </thead>
          <tbody>
              {
                  storeProducts.map(storeProduct => {
                      return(
                          <tr>
                              <td>{storeProduct["name"]}</td>
                              <td>{storeProduct["price"]}</td>
                              <td>{storeProduct["category"]}</td>
                              <td>{storeProduct["amount"]}</td>
                              <td>
                                
                                <Button variant="dark" id="addToCartBtn" onClick={(event => productAmount > 0 ? addToCartHandler(storeProduct["name"]) : null)}>
                                    Add To Cart
                                </Button>
                              </td>
                          </tr>
                      );
                  })
              }
          </tbody>
        </Table>
      </div>
    </div>
  );
}

// TODO - add back button


export default StoreProducts;