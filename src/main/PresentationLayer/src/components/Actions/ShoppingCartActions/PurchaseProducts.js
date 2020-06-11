import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import * as theService from '../../../services/communication';
import {Container, Table, Form, Button} from 'react-bootstrap'


class PurchaseProducts extends React.Component{
  constructor(props){
    super(props);

    this.state={
      purchase_ls: {},
      total_price: 0,
      purchases: [], // purchases = [{store_name, basket_price, products=[{product_name, product_price, amount}]}]
      details_filled: false,
      address: ""
    }

    this.handleConfirm = this.handleConfirm.bind(this);
  }

  handleConfirm = () => {
    const promise = theService.confirmPurchase(this.state.address, this.state.purchase_ls)
    promise.then((data) => {
      if(data != null){
        alert(data["msg"]);
        if(data["data"]){
          // return to home screen
        }
      }
    })
  }

  componentWillMount = () =>{
    const promise = theService.purchaseCart();
    promise.then((data) => {
      if(data != null){
        this.setState({total_price: data["data"]["total_price"], purchases: data["data"]["purchases"], purchase_ls: data["data"]})
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
          // purchase = {store_name, basket_price, products=[{product_name, product_price, amount}]}
          this.state.purchases.map(purchase => (
            <div style={{border: "1px solid", borderColor: "#CCCCCC"}}>
              <h2 style={{position: "relative", right: "40%"}}>Store: {purchase["store_name"]}</h2>
              {
                // purchaseProduct = [{product_name, product_price, amount}]
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
              <p style={{position: "relative", right: "-43%"}} >Basket Price: {purchase["basket_price"]}</p>
              </div>
          ))
        }
        <p>Total Price: {this.state.total_price}</p>

        {/* here we ask the user for all details needed for payment confirmation (for now address only) */}

        <Form.Control id="address" value={this.state.address} required type="text" placeholder="Delivery Address" 
            onChange={(event => {
              let value = event.target.value
              if(value != ""){
                this.setState({address: value})
                this.setState({details_filled: true}) // this is set once all details are filled only
              }
              else{
                this.setState({address: ""})
                this.setState({details_filled: false}) // this is set if SOME detail is invalid
              }
            })}
        />

        <Button variant="secondary" style={{marginTop: "1%"}} onClick={this.handleConfirm} disabled={!this.state.details_filled}>
          Confirm Purchase
        </Button>
        
      </Container>  
    );
  };
}

export default PurchaseProducts;