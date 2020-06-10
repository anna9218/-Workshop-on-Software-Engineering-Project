import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import {BrowserRouter as Router, Switch, Route, Link} from 'react-router-dom'
import * as theService from '../../../services/communication';
import {Container, Table} from 'react-bootstrap'


class PurchaseProducts extends React.Component{
  constructor(props){
    super(props);

    this.state={
      total_price: 0,
      purchases: []
    }
  }

  componentWillMount = () =>{
    const promise = theService.purchaseCart();
    promise.then((data) => {
      if(data != null){
        // data["data"] ={ total_price, purchases=[{store_name, basket_price, products=[{product_name, product_price, amount}]}] }
        this.state.total_price = data["data"]["total_price"];
        this.state.purchases = data["data"]["purchases"];
      }
    })
  }

  render(){
    return (
      <Container style={{width: this.props["screenWidth"], height: this.props["screenHeight"]}}>
        <div>
          <h1>Purchase Products</h1>
        </div>

        {
          // purchases = [{store_name, basket_price, products=[{product_name, product_price, amount}]}]
          this.state.purchases.map(purchase => (
            <div>
              <h2>Store: {purchase["store_name"]}</h2>
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
                        purchase["products"].map(purchaseProduct => (
                          <tr>
                              <td>{purchaseProduct["product_name"]}</td>
                              <td>{purchaseProduct["price"]}</td>
                              <td>{purchaseProduct["amount"]}</td>
                          </tr>
                        ))
                    }
                </tbody>
              </Table>
            <p>Basket Price: {purchase["basket_price"]}</p>
            </div>
          ))
        }
        <p>Total Price: {this.state.total_price}</p>
      </Container>  
    );
  };
}

export default PurchaseProducts;