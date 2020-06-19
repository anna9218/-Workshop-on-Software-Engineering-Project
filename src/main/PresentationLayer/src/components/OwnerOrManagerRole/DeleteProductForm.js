import React, {useState, useEffect} from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import {Container, Button, Form} from 'react-bootstrap'
import * as theService from '../../services/communication';
import * as BackOption from '../Actions/GeneralActions/Back'
import { confirmAlert } from 'react-confirm-alert'; 
import 'react-confirm-alert/src/react-confirm-alert.css'; // Import css



function DeleteProductsForm(props){
    const [allStoreProducts, setAllStoreProducts] = useState([]);
    // const [selectedProduct, setSelectedProduct] = useState(false);

    const [productName, setProductName] = useState(null);
  
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
                    alert(data["msg"] );
                    setAllStoreProducts([]);      // no products to display
                }
            }
        })
    }

    const removeProductHandler = async () => {
        const promise = theService.deleteProduct(props.storeName, productName)
        promise.then((data) => {
            if(data !== undefined){
                confirmAlert({
                    title: data["msg"],
                    buttons: [
                      {
                        label: 'Remove another product',
                        onClick: () => { // reset the form in order to add another product
                            // reset form
                            setProductName(null);
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

  return (
      <div style={{width: props["screenWidth"], height: props["screenHeight"]}}>

        <Container>
            <h1>Remove Product</h1>

            <Form.Group controlId="products_ControlSelect2" onChange={ event => {
                setProductName(event.target.value)
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

            <Button variant="dark" id="edit-product-btn" onClick={removeProductHandler}>Remove Product!</Button>
          
        </Container>

      </div>
  );
}

export default DeleteProductsForm;
    