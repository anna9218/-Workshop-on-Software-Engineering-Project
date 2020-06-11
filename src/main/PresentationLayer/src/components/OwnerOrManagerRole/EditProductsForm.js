import React, {useState, useEffect} from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import {Container, Button, Form} from 'react-bootstrap'
import * as theService from '../../services/communication';
import * as BackOption from '../Actions/GeneralActions/Back'
import { confirmAlert } from 'react-confirm-alert'; 
import 'react-confirm-alert/src/react-confirm-alert.css'; // Import css



function EditProductsForm(props){
    const [allStoreProducts, setAllStoreProducts] = useState([]);
    // const [selectedProduct, setSelectedProduct] = useState(false);

    const [productName, setProductName] = useState(null);
    const [newProductName, setNewProductName] = useState(null);
    const [productPrice, setProductPrice] = useState(null);
    const [newProductPrice, setNewProductPrice] = useState(null);
    const [newProductCategory, setNewProductCategory] = useState(null);
    const [productCategory, setProductCategory] = useState(null);
    const [productAmount, setProductAmount] = useState(null);
    const [newProductAmount, setNewProductAmount] = useState(null);
    const [purchaseType, setPurchaseType] = useState(null);
    const [newPurchaseType, setNewPurchaseType] = useState(null);

    const [immidiateChecked, setImmidiateChecked] = useState(false);
    const [auctionChecked, setAuctionChecked] = useState(false);
    const [lotteryChecked, setLotteryChecked] = useState(false);
  
    useEffect(() => {
        // alert(props.history)
        const promise = theService.displayStoresProducts(props.storeName)
        promise.then((data) => {
            if(data !== undefined){
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
                setProductCategory(product["category"]);
                setProductPrice(product["price"]);
                if(product["purchase_type"] === "DEFUALT"){
                    setImmidiateChecked(true);
                    setAuctionChecked(false);
                    setLotteryChecked(false);
                    setPurchaseType(0);
                }
                else if(product["purchase_type"] === "AUCTION"){
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
        const promise = theService.editProduct(props.storeName, productName, newProductName, newProductAmount, newProductPrice, newProductCategory, newPurchaseType)
        promise.then((data) => {
            if(data !== undefined){
                confirmAlert({
                    title: data["msg"],
                    buttons: [
                      {
                        label: 'Add another product',
                        onClick: () => { // reset the form in order to add another product
                            // reset form
                            setProductName(null);
                            setProductAmount(null);
                            setProductCategory(null);
                            setProductPrice(null);
                            setImmidiateChecked(false);
                            setAuctionChecked(false);
                            setLotteryChecked(false);
                            setNewProductAmount(null);
                            setNewProductCategory(null);
                            setNewProductName(null);
                            setNewProductPrice(null);
                            setNewPurchaseType(null);
                        }
                      },
                      {
                        label: 'Done',
                        onClick: () => {BackOption.BackToHome(props.history)}  
                      }
                    ]
                });
            }
        });
    }

  return (
      <div style={{width: props["screenWidth"], height: props["screenHeight"]}}>

        <Container>
            <h1>Edit Product</h1>

            <Form.Group controlId="products_ControlSelect2" onChange={ event => {
                setSelectedProduct(event.target.value)
                }}>
                <Form.Label>Please choose a product:</Form.Label>
                <Form.Control as="select">
                    <option>Select Product</option>
                    {allStoreProducts !== null ?
                        allStoreProducts.map(product => (
                        <option value={product["name"]}>{product["name"]}</option>
                        ))
                        : null
                    }
                </Form.Control>
            </Form.Group>

            {
                productName !== null ? 
                <div>
                    <Form className='edit_product'>
                        <Form.Label>Choose the product name:</Form.Label>
                        <Form.Control id="product-name" value={newProductName} required type="text" placeholder={productName}
                        onChange={(event => {
                        setNewProductName(event.target.value)
                        })}/>

                        <Form.Label>Set the price:</Form.Label>
                        <Form.Control id="product-price" value={newProductPrice} required type="text" required placeholder={productPrice} 
                        onChange={(event => {
                        setNewProductPrice(event.target.value)
                        })}/>
                    
                        <Form.Label>Enter the category:</Form.Label>
                        <Form.Control id="product-category" value={newProductCategory} required type="text" placeholder={productCategory}
                        onChange={(event => {
                        setNewProductCategory(event.target.value)
                        })}/>
                    
                        <Form.Label>Enter the amount:</Form.Label>
                        <Form.Control id="product-amount" value={newProductAmount} required type="text" placeholder={productAmount}
                        onChange={(event => {
                        setNewProductAmount(event.target.value)
                        })}/>

                        <Form.Label>Enter the purchase type:</Form.Label>

                        <div key={`inline-checkbox`} className="mb-3" style={{border: "1px solid", borderColor: "#CCCCCC"}}>
                            <Form.Check inline label="Immidiate Purcahse" type="checkbox" id={`immidiate-purchase`} defaultChecked={immidiateChecked} onChange={(event => {setNewPurchaseType(0)})} />
                            <Form.Check inline label="Auction Purchase" type="checkbox" id={`auction-purchase`} defaultChecked={auctionChecked} onChange={(event => {setNewPurchaseType(1)})} />
                            <Form.Check inline label="Lottery Purchase" type="checkbox" id={`lottery-purchase`} defaultChecked={lotteryChecked} onChange={(event => {setNewPurchaseType(2)})}/>
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