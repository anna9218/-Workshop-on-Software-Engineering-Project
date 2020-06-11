import React, {useState, useEffect} from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import {BrowserRouter as Router, Switch, Route, Link} from 'react-router-dom'
import {Container, Row, Col, Button, Dropdown, Jumbotron, Form} from 'react-bootstrap'
import * as theService from '../../services/communication';

import { confirmAlert } from 'react-confirm-alert'; 
import 'react-confirm-alert/src/react-confirm-alert.css'; // Import css



function EditProductsForm(props){
    const [storeName, setStoreName]= useState("");
    const [allStoreProducts, setAllStoreProducts] = useState([]);
    // const [selectedProduct, setSelectedProduct] = useState(false);

    const [productName, setProductName] = useState("");
    const [productPrice, setProductPrice] = useState(null);
    const [productCategory, setProductCategory] = useState("");
    const [productAmount, setProductAmount] = useState(null);
    const [purchaseType, setPurchaseType] = useState(null);

    const [immidiateChecked, setImmidiateChecked] = useState(false);
    const [auctionChecked, setAuctionChecked] = useState(false);
    const [lotteryChecked, setLotteryChecked] = useState(false);
  
    useEffect(() => {
        setStoreName(props.storeName);
        // const promise = theService.getProductInfo()
        const promise = theService.displayStoresProducts(props.storeName)
        promise.then((data) => {
            if(data != null){
                if (data["data"] != null){   // if there are stores to display
                    setAllStoreProducts(data["data"]);
                }
                else{
                    setAllStoreProducts(data["msg"]);      // no products to display
                }
            }
        })
    }, []);

    const setSelectedProduct = (product_name) => {
        allStoreProducts.map(product => {
            if(product["name"] === product_name){
                setProductName(product["name"]);
                setProductAmount(product["amount"]);
                setProductCategory([product["category"]]);
                setProductPrice(product["price"]);
                if(product["purchase_type"] == "DEFUALT"){
                    setImmidiateChecked(true);
                    setAuctionChecked(false);
                    setLotteryChecked(false);
                    setPurchaseType(0);
                }
                else if(product["purchase_type"] == "AUCTION"){
                    setImmidiateChecked(false);
                    setAuctionChecked(true);
                    setLotteryChecked(false);
                    setPurchaseType(1);
                }
                else{
                    setImmidiateChecked(false);
                    setAuctionChecked(false);
                    setLotteryChecked(true);
                    setPurchaseType(2);
                }
            }
        })
    }

    const editProductHandler = async () => {

    }

  return (
      <div style={{width: props["screenWidth"], height: props["screenHeight"]}}>

        <Container>
            <h1>Edit Product</h1>

            <Form.Group controlId="products_ControlSelect2" onChange={ event => {
                alert((event.target.value)[0])
                // console.log(event.target.value)
                setSelectedProduct(event.target.value)
                }}>
                <Form.Label>Please choose a product:</Form.Label>
                <Form.Control as="select">
                    <option></option>
                    {allStoreProducts.map(product => (
                        <option value={product["name"]}>{product["name"]}</option>
                    ))}
                </Form.Control>
            </Form.Group>

            {
                productName !== "" ? 
                <div>
                    <Form className='edit_product'>
                        <Form.Label>Choose the product name:</Form.Label>
                        <Form.Control id="product-name" value={productName} required type="text" placeholder={productName}
                        onChange={(event => {
                        setProductName(event.target.value)
                        })}/>

                        <Form.Label>Set the price:</Form.Label>
                        <Form.Control id="product-price" value={productPrice} required type="text" required placeholder={productPrice} 
                        onChange={(event => {
                        setProductPrice(event.target.value)
                        })}/>
                    
                        <Form.Label>Enter the category:</Form.Label>
                        <Form.Control id="product-category" value={productCategory} required type="text" placeholder={productCategory}
                        onChange={(event => {
                        setProductCategory(event.target.value)
                        })}/>
                    
                        <Form.Label>Enter the amount:</Form.Label>
                        <Form.Control id="product-amount" value={productAmount} required type="text" placeholder={productAmount}
                        onChange={(event => {
                        setProductAmount(event.target.value)
                        })}/>

                        <Form.Label>Enter the purchase type:</Form.Label>

                        <div key={`inline-checkbox`} className="mb-3" style={{border: "1px solid", borderColor: "#CCCCCC"}}>
                            <Form.Check inline label="Immidiate Purcahse" type="checkbox" id={`immidiate-purchase`} defaultChecked={immidiateChecked} onChange={(event => {setPurchaseType(0)})} />
                            <Form.Check inline label="Auction Purchase" type="checkbox" id={`auction-purchase`} defaultChecked={auctionChecked} onChange={(event => {setPurchaseType(1)})} />
                            <Form.Check inline label="Lottery Purchase" type="checkbox" id={`lottery-purchase`} defaultChecked={lotteryChecked} onChange={(event => {setPurchaseType(2)})}/>
                        </div>

                    </Form>
                    <Button variant="dark" id="edit-product-btn" onClick={editProductHandler}>Edit Product!</Button>
                </div>
                : null
            }
          
        </Container>

      </div>
  );
}

export default EditProductsForm;
// const addProductHandler = async () =>{
//     const promise = theService.addProduct(storeName, productName, productPrice, productCategory, productAmount, purchaseType); // goes to register.js and sends to backend
//     promise.then((data) => {

//         confirmAlert({
//           title: data["msg"],
//           buttons: [
//             {
//               label: 'Add another product',
//               onClick: () => { // reset the form in order to add another product
//                 setProductName("");
//                 setProductPrice("");
//                 setProductCategory("");
//                 setProductAmount("");
//                 // setDiscountType(0);
//                 setPurchaseType(0);
//                 // setDiscountPercentage(0);
//               }
//             },
//           {
//             label: 'Done',
//             onClick: () => alert('Click No')  //TODO - add an option to go back (need to disable addProductForm)
//           }
//         ]
//       });

//     });
//   };



//           