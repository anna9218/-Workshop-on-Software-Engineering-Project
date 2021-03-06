import React, {useState, useEffect} from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import {Container, Button, Form, Row} from 'react-bootstrap'
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
        getProductList();
    }, []);

    const getProductList = () => {
        const promise = theService.displayStoresProducts(props.storeName)
        promise.then((data) => {
            if(data !== undefined){
                if (data["data"] != null){   // if there are stores to display
                    setAllStoreProducts(data["data"]);
                }
                else{
                    alert(data["msg"])
                    setAllStoreProducts([]);      // no products to display
                }
            }
        })
    }

    const setSelectedProduct = (product_name) => {
        allStoreProducts.map(product => {
            if(product["name"] === product_name){
                setProductName(product["name"]);
                setProductAmount(product["amount"]);
                setProductCategory(product["category"]);
                setProductPrice(product["price"]);
                if(product["purchase_type"] === "DEFAULT"){ 
                    setImmidiateChecked(true);
                    setAuctionChecked(false);
                    setLotteryChecked(false);
                    setPurchaseType(0);
                    setNewPurchaseType(0);
                }
                else if(product["purchase_type"] === "AUCTION"){
                    setImmidiateChecked(false);
                    setAuctionChecked(true);
                    setLotteryChecked(false);
                    setPurchaseType(1);
                    setNewPurchaseType(1);

                }
                else{
                    setImmidiateChecked(false);
                    setAuctionChecked(false);
                    setLotteryChecked(true);
                    setPurchaseType(2);
                    setNewPurchaseType(2);
                }
            }
        })
    }

    const editProductHandler = async () => {
        // alert(parseInt(newProductAmount))
        if(newProductName !== null && newProductName === "")
            alert("Oops, Product's name can't be an empty string.");
        else if(newProductAmount !== null && parseInt(newProductAmount) < 0)
            alert("Oops, Product's amount can't be less than 0.");
        else if(newProductPrice !== null && parseFloat(newProductPrice) < 0)
            alert("Oops, Product's price can't be less than 0.");
        else {
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
                                getProductList();
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
                        <Form.Control id="product-name" value={newProductName} as="input" required type="text" placeholder={productName}
                        onChange={(event => {
                        setNewProductName(event.target.value)
                        })}/>

                        <Form.Label>Set the price:</Form.Label>
                        <Form.Control id="product-price" value={newProductPrice} as="input" required type="number" min={0} required placeholder={productPrice} 
                        onChange={(event => {
                        setNewProductPrice(event.target.valueAsNumber)
                        })}/>
                    
                        <Form.Label>Enter the category:</Form.Label>
                        <Form.Control id="product-category" value={newProductCategory} as="input" required type="text" placeholder={productCategory}
                        onChange={(event => {
                        setNewProductCategory(event.target.value)
                        })}/>
                    
                        <Form.Label>Enter the amount:</Form.Label>
                        <Form.Control id="product-amount" value={newProductAmount} as="input" required type="number" min={0} placeholder={productAmount}
                        onChange={(event => {
                        setNewProductAmount(event.target.valueAsNumber)
                        })}/>

                        <Form.Label>Enter the purchase type:</Form.Label>

                        {/* <div style={{marginTop:"3%" , marginLeft: "25%", marginRight: "25%", border: "1px solid", borderColor: "#CCCCCC"}}>

                            <Form style={{marginRight:"5%" , marginLeft: "5%", marginBottom:"2%"}}>
                                <Row><Form.Check inline type="radio" label="Add Products" name="formHorizontalRadios"id="Radios1"/>
                                </Row>
                                <Row><Form.Check inline type="radio" label="Remove Products" name="formHorizontalRadios"id="Radios2"/>
                                </Row>
                                <Row><Form.Check inline type="radio" label="Edit Products Details" name="formHorizontalRadios"id="Radios3"/>
                                </Row>
                            </Form>
                        </div> */}

                        <div key={`inline-checkbox`} className="mb-3" style={{border: "1px solid", borderColor: "#CCCCCC"}}>
                            <div style={{marginLeft:"2%"}}>
                                <Row><Form.Check inline label="Immidiate Purcahse" type="radio" id={`immidiate-purchase2`} name="formHorizontalRadios" checked={immidiateChecked} onChange={(event => {setNewPurchaseType(0); setImmidiateChecked(true); setAuctionChecked(false); setLotteryChecked(false)})} /></Row>
                                <Row><Form.Check inline label="Auction Purchase" type="radio" id={`auction-purchase2`} name="formHorizontalRadios" checked={auctionChecked} onChange={(event => {setNewPurchaseType(1); setImmidiateChecked(false); setAuctionChecked(true); setLotteryChecked(false)})} /></Row>
                                <Row><Form.Check inline label="Lottery Purchase" type="radio" id={`lottery-purchase2`} name="formHorizontalRadios" checked={lotteryChecked} onChange={(event => {setNewPurchaseType(2); setAuctionChecked(false); setAuctionChecked(false); setLotteryChecked(true)})}/></Row>
                            </div>
                            {/* <Form.Check inline label="Immidiate Purcahse" type="checkbox" id={`immidiate-purchase`} defaultChecked={immidiateChecked} onChange={(event => {setNewPurchaseType(0)})} />
                            <Form.Check inline label="Auction Purchase" type="checkbox" id={`auction-purchase`} defaultChecked={auctionChecked} onChange={(event => {setNewPurchaseType(1)})} />
                            <Form.Check inline label="Lottery Purchase" type="checkbox" id={`lottery-purchase`} defaultChecked={lotteryChecked} onChange={(event => {setNewPurchaseType(2)})}/> */}
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