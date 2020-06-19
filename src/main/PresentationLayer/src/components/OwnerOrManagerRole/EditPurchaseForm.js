import React, { useState, useEffect } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import {BrowserRouter as Router,  Route, Link } from 'react-router-dom'
import {Container, Button,Form, Col, Row, } from 'react-bootstrap'
import * as theService from '../../services/communication';
import * as BackOption from '../Actions/GeneralActions/Back';
import {IoMdCloseCircle} from 'react-icons/io' 
import { confirmAlert } from 'react-confirm-alert'; 

function EditPurchaseForm(props){
    useEffect(() => {
        // console.log(props.location.state.storeName)
        setStoreName(props.storeName)
        fetchStoreProducts(props.storeName)
      }, []);


    const [storeName, setStoreName] = useState("");
    const [policyName, setPolicyName] = useState("");
    const [storeProducts, setStoreProducts] = useState(["There are no products in the store inventory..."]);
    const [policyProducts, setPolicyProducts] = useState([]);
    const [policyTypes, setPolicyTypes] = useState([]);
    const [minAmount, setMinAmount] = useState(null);
    const [maxAmount, setMaxAmount] = useState(null);
    const [dates, setDates] = useState(null);
    const [showMinAmount, setShowMinAmount] = useState(false);
    const [showMaxAmount, setShowMaxAmount] = useState(false);
    const [showDates, setShowDates] = useState(false);
  
    const fetchStoreProducts = (store_name) =>{
        const promise = theService.displayStoresProducts(store_name); // goes to register.js and sends to backend
        promise.then((data) => {
            if(data !== undefined){
                if (data["data"] != null){   // if there are stores to display
                    setStoreProducts(data["data"]);
                }
                else{
                    alert(data["msg"])
                    setStoreProducts(["There are no products in the store inventory..."]);      // no products to display
                }
            }

        });
    };

    const addPolicyHandler = async () =>{

      if(policyTypes.includes('min_amount') && (minAmount === null || minAmount < 0))
        alert("Minimum amount need to be set and must be bigger than 0.")
      else if(policyTypes.includes('max_amount') && (maxAmount === null || maxAmount < 0))
        alert("Maximum amount need to be set and must be bigger than 0.")
      else if(policyTypes.includes('forbidden_dates') && (dates === null || dates.length === 0))
        alert("For forbidden dates, you must select at least one date.")
      else{
        const promise = theService.addPurchasePolicy(props.storeName, policyName, policyProducts, 
            minAmount, maxAmount, dates, policyTypes.includes('bundle') ? true : null); // goes to register.js and sends to backend
        promise.then((data) => {
            if(data !== undefined){
                confirmAlert({
                    title: data["msg"],
                    buttons: [
                        {   label: 'Add another product',
                            onClick: () => { // reset the form in order to add another product
                            //   setPolicyName("");
                            //   setProductPrice("");
                            //   setProductCategory("");
                            //   setProductAmount("");
                            //   setPurchaseType(null);
                        }},
                        {   label: 'Done',
                            onClick: () => {BackOption.BackToHome(props.history)}
                        }]
                });
            }

        });
      }
      
    };
  
    const addPolicyType = async (policy_type) =>{
        if(policyTypes.includes(policy_type)){
            policyTypes.pop(policy_type)
            if(policy_type === 'min_amount')
                setMinAmount(null);
            else if(policy_type === 'max_amount')
                setMaxAmount(null); 
            else if(policy_type === 'forbidden_dates')
                setDates(null);
        }
        else {
            policyTypes.push(policy_type)
        }
    };

    const detailsFilled = () => {
      if(policyName !== "" && policyProducts.length > 0 ){
            return true;
      }
      return false;
    }
    
    const addPolicyProducts = (product_name) =>{
        if(policyProducts.includes(product_name))
            alert("Product was already selected.")
        else if(product_name !== "Select Product")
            setPolicyProducts(policyProducts.concat([product_name]))
    }

    const removeProductPolicy = async (product_name) =>{
        if(policyProducts.includes(product_name))
            policyProducts.pop(product_name)
    }

    const removeDates = async (date) =>{
        if(dates.includes(date)){
            dates.pop(date)
            if(dates.length === 0)
                setDates(null)
        }
    }
    
    return (
        // <div style={{width: props["screenWidth"], height: props["screenHeight"]}}>
        <div style={{marginTop:"2%" , marginLeft: "20%", marginRight: "20%", border: "1px solid", borderColor: "#CCCCCC"}}>
  
          <Container>
            <h4 style={{marginTop:"2%"}}>Edit Purchase Policy</h4>
            <Form className='add_policy'>
              <Form.Label>Choose the policy name:</Form.Label>
              <Form.Control id="policy-name" required type="text" placeholder="Policy name"
              onChange={(event => {
                setPolicyName(event.target.value)
              })}/>
  
              <Form.Label style={{marginTop:"2%"}}>Enter the purchase type (at least one):</Form.Label>
                <div key={`inline-checkbox`} className="mb-3" style={{ border: "1px solid", borderColor: "#CCCCCC"}}>
                    <div style={{marginLeft:"4%"}}>
                    <Row style={{marginTop: "1.5%"}}>
                        <Form.Label column  sm="6" style={{left: "-8%"}}>
                            <Form.Check inline label="Minimum product amount" type="checkbox" id={`minimun-amount`}  onChange={(event => {
                                                                                                                        addPolicyType('min_amount')
                                                                                                                        showMinAmount ? setShowMinAmount(false) : setShowMinAmount(true)
                                                                                                                        })} />
                        </Form.Label>
                        <Col sm="6" style={{left: "-8%"}}>
                            <Form.Control type="number" min="0"  disabled={!showMinAmount} required placeholder="Enter minimum amount" onChange={(event => {setMinAmount(event.target.valueAsNumber)})}/>
                        </Col>
                    </Row>
                    <Row style={{marginTop: "1.5%"}}>
                        <Form.Label column  sm="6" style={{left: "-8%"}}>
                            <Form.Check inline label="Maximum product amount" value={minAmount} type="checkbox" id={`maximum-amount`} name="formHorizontalRadios" onChange={(event => {
                                                                                                                        addPolicyType('max_amount')
                                                                                                                        showMaxAmount ? setShowMaxAmount(false) : setShowMaxAmount(true);
                                                                                                                        })} />
                        </Form.Label>
                        <Col sm="6" style={{left: "-8%"}}>
                            <Form.Control type="number" min="0" data-bind="value:replyNumber" disabled={!showMaxAmount} required placeholder="Enter maximum amount" onChange={(event => {setMaxAmount(event.target.valueAsNumber)})}/>
                        </Col>
                    </Row>
                    <Row style={{marginTop: "1.5%"}}>
                        <Form.Label column  sm="6" style={{left: "-19%"}}>
                            <Form.Check inline label="Bundle" type="checkbox" id={`bundel`} name="formHorizontalRadios" onChange={(event => {addPolicyType('bundle')})}/>
                        </Form.Label>
                    </Row>
                    <Row style={{marginTop: "1.5%", marginBottom: "1%"}}>
                        <Form.Label column  sm="6" style={{left: "-14%"}}>
                            <Form.Check inline label="Forbidden dates" type="checkbox" id={`Forbidden-dates`} name="formHorizontalRadios" onChange={(event => {
                                                                                                                        addPolicyType('forbidden_dates')
                                                                                                                        showDates ? setShowDates(false) : setShowDates(true)
                                                                                                                        })}/>
                        </Form.Label>
                        <Col sm="6" style={{left: "-8%"}}>
                            <Form.Control id="product-name" disabled={!showDates} required type="date" min={(new Date()).toUTCString()} onChange={(event => dates === null? setDates([(event.target.valueAsDate)]) :
                                                                                                                                           ! dates.map(date => date.toLocaleDateString()).includes((event.target.valueAsDate).toLocaleDateString()) ? 
                                                                                                                                                setDates(dates.concat([(event.target.valueAsDate)])) : alert("This date has been selected already."))}/>
                        </Col>

                        {dates !== null && dates.length > 0 && showDates?
                            <div style={{marginTop:"2%", marginLeft:"45%"}}>
                            <Form.Label>Your selected dates are:</Form.Label>
                            <div key={`inline-checkbox`} className="mb-3" style={{ border: "1px solid", borderColor: "#CCCCCC"}}>
                                <div style={{marginLeft:"12%"}}>
                                    {/* <option>No products were</option> */}
                                    {dates !== null ?
                                        dates.map(date => (
                                        <Row><Link class="text-decoration-none" onClick={event => removeDates(date)}> <IoMdCloseCircle /> {date.toLocaleDateString()}</Link></Row>
                                        ))
                                        : null
                                    }
                                </div>
                            </div></div> : null}
                    </Row>
                    </div>
                </div>


                <Form.Group controlId="products_ControlSelect2" onChange={event => addPolicyProducts(event.target.value)}>
                    <Form.Label>Select products to apply the policy on:</Form.Label>
                    <Form.Control as="select">
                            <option>Select Product</option>
                            {storeProducts !== null ?
                                storeProducts.map(product => (
                                <option value={product["name"]}>{product["name"]}</option>
                                ))
                                : null
                            }
                </Form.Control>
                </Form.Group>

                {policyProducts.length > 0 ?
                    <div>
                    <Form.Label>Your selected products are:</Form.Label>
                    <div key={`inline-checkbox`} className="mb-3" style={{ border: "1px solid", borderColor: "#CCCCCC"}}>
                        <div style={{marginLeft:"4%"}}>
                            {/* <option>No products were</option> */}
                            {policyProducts !== null ?
                                policyProducts.map(product => (
                                <Row><Link class="text-decoration-none" onClick={event => removeProductPolicy(product)}> <IoMdCloseCircle /> {product}</Link></Row>
                                ))
                                : null
                            }
                        </div>
                    </div></div> : null}
    
              
              {/* <Form.Check type="checkbox" label="Add Discount Type" onChange={handleShowDiscount} style={{position: "relative", right: "43%"}}/> */}
  
              {/* <ShowDiscount showDiscount={showDiscount} setDiscountType={setDiscountType} discountType={discountType} setDiscountPercentage={setDiscountPercentage} /> */}
              
            </Form>
            <Button style={{marginBottom:"2%"}} variant="dark" id="open-store-button" disabled={!detailsFilled()} onClick={addPolicyHandler}>Update Policy!</Button>
          </Container>
  
        </div>
    );
  }

export default EditPurchaseForm;
