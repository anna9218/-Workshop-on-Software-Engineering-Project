import React, { useState, useEffect } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import {Link} from 'react-router-dom'
import * as theService from '../../../services/communication';
import {Button, Jumbotron, Form, Row, Table, Container} from 'react-bootstrap'
import * as BackOption from '../GeneralActions/Back'


function ShoppingCart(props){
  useEffect(() => {
    // alert(props.history)
    fetchShoppingCart();
  }, []);

  const [shoppingCart, setShoppingCart] = useState([]);

  const [selectedProducts, setSelectedProducts] = useState([]);

  const fetchShoppingCart = async () => {
    const promise = theService.displayShoppingCart()
    // const stores = await promise.json();
    promise.then((data) => {
      if(data != null){
        if(data["data"].length > 0)
          setShoppingCart(data["data"])
        else
          alert(data["msg"]);
      }
    });
  };

  const onButtonClickHandler = () => {
    alert('Product info Product info')
    //TODO, ADD OPTION TO VIEW PRICE, POLICIES
  };

  const removeProductHandler = (event) => {
    const promise = theService.updateShoppingCart("remove", event.target.value); // goes to register.js and sends to backend
    promise.then((data) => {
      alert(data["msg"])
    });
    //TODO - pass product
  }

  const updateProductAmountHandler = (event) => {
    const promise = theService.updateShoppingCart("update", event.target.value); // goes to register.js and sends to backend
    promise.then((data) => {
      alert(data["msg"])
    });
    //TODO
  }

  // const purchaseProductsHandler = (event) => {
  //   const promise = theService.purchaseCart();
  //   promise.then((data) => {
  //     if(data != null){
  //       alert(data["msg"])
  //       // data["data"] ={ total_price, purchases=[{store_name, basket_price, products=[{product_name, product_price, amount}]}] }
        
  //     }
  //   })
  // }

  const selectedProductsHandler = (event) => {
        if(selectedProducts.includes(event.target.value)){
            var index = selectedProducts.indexOf(event.target.value);
            console.log(selectedProducts);
            setSelectedProducts(selectedProducts.splice(index, index+1));
            console.log(selectedProducts);
        }
        else{
            console.log(selectedProducts);
            setSelectedProducts(selectedProducts.concat(event.target.value));
            console.log(selectedProducts);
        }
        console.log(selectedProducts);
    }

  return (
      <div style={{width: props["screenWidth"], height: props["screenHeight"]}}>
        <h1 style={{marginTop:"2%"}}>Shopping Cart</h1>
        <Container>
        {
          // shopping cart = [{store_name, basket = [{product_name, amount}]}]
          shoppingCart.map(basket => (
            <div>
              <h2>Store: {basket["store_name"]}</h2>
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
                  basket["basket"].map(storeProduct => (
                    <tr>
                        <td>{storeProduct["product_name"]}</td>
                        <td>{storeProduct["price"]}</td>
                        <td>{storeProduct["amount"]}</td>
                    </tr>
                  ))
              }
          </tbody>
        </Table>
            </div>
          ))
        }

        {
          shoppingCart.length > 0 ? 
            <Row style={{marginLeft:"0%"}}><Button variant="dark" id="purchaseBtn" as={Link} to="/confirm_purchase" >
              Purchase Shopping Cart
            </Button></Row>
            : null
        }

        <div style={{marginTop:"-3.45%", marginRight:"58%"}}><Button variant="dark" id="add_product-button" onClick={event => BackOption.BackToHome(props)}>Back</Button>
        </div>
      </Container>
    </div>
         
      
  );
}

export default ShoppingCart;