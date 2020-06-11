import React, { useState, useEffect } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import {Table, Button} from 'react-bootstrap'
import * as theService from '../../services/communication';
import * as BackOption from '../Actions/GeneralActions/Back'


function PersonalPurchaseHistory(props){
  useEffect(() => {
    fetchPersonalPurchaseHistory();
  }, []);


  const [purchaseHistory, setPurchaseHistory] = useState([]); 

  const fetchPersonalPurchaseHistory = async () => {
    const promise = theService.fetchPersonalPurchaseHistory(); // goes to register.js and sends to backend
    promise.then((data) => {
      setPurchaseHistory(data["data"])
    });
  };

  return (
    <div style={{width: props["screenWidth"], height: props["screenHeight"]}}>
      <h1>Personal Purchase History</h1>

      {/* purchaseHistory = [{store_name, nickname, date, total_price, products=[{amount, product_name, products_price}]}] */}
      {/* purchase =  {store_name, nickname, date, total_price, products=[{amount, product_name, products_price}]}*/}
      {
        purchaseHistory.map(purchase => (
          <div style={{marginRight: "5%", marginLeft: "5%", border: "1px solid", borderColor: "#CCCCCC"}}>
            <h2>Store: {purchase["store_name"]}</h2>

            {
              // purchaseProduct = [{amount, product_name, products_price}]
              purchase["products"].map(purchaseProduct => (
                <Table striped bordered hover >
                  <thead>
                      <tr>
                          <th>Product Name</th>
                          <th>Price</th>
                          <th>Amount</th>
                      </tr>
                  </thead>
                  <tbody>
                    {
                      // product = {product_name, product_price, amount}
                      purchase["products"].map(product => (
                        <tr>
                            <td>{product["product_name"]}</td>
                            <td>{product["product_price"]}</td>
                            <td>{product["amount"]}</td>
                        </tr>
                      ))
                    }
                  </tbody>
                </Table>
              ))
            }
            <p>Date: {purchase["date"]}</p>
            <p>Total Price: {purchase["total_price"]}</p>
          </div>
        ))
      }
      <Button style={{marginTop: "1%"}} variant="dark" id="back-btn" onClick={event => BackOption.BackToHome(props)}>Back</Button>
      
  </div>
  );
}

export default PersonalPurchaseHistory;