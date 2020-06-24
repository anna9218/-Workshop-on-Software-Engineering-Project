import React, { useState, useEffect } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import {BrowserRouter as Link } from 'react-router-dom'
// import { browserHistory } from "react-router";
import {Container, Button, Form, Col, Row} from 'react-bootstrap'
import * as theService from '../../services/communication';
import { confirmAlert } from 'react-confirm-alert'; 

function EditDiscountPolicyForm(props){
    useEffect(() => {
        setStoreName(props.storeName)
        fetchDiscountPolicies(props.storeName)
        fetchStoreProducts(props.storeName)
      }, []);


    const [storeName, setStoreName] = useState("");

    const [policyName, setPolicyName] = useState('Select policy');
    const [newPolicyName, setNewPolicyName] = useState(null);
    const [storeProducts, setStoreProducts] = useState(["There are no products in the store inventory..."]);
    const [policies, setPolicies] = useState([]);
    const [selectedProduct, setSelectedProduct] = useState("Select Product");
    const [percentage, setPercentage] = useState(0);
    const [date, setDate] = useState("");

    const [productPreCondition, setProductPreCondition] = useState("Any product");
    const [minPurchasePrice, setMinPurchasePrice] = useState(null);
    const [minProductAmount, setMinProductAmount] = useState(null);

    const [showProductPreCondition, setShowProductPreCondition] = useState(false);
    const [showMinPurchasePreCondition, setShowMinPurchasePreCondition] = useState(false);
    const [showMinProductPreCondition, setShowMinProductPreCondition] = useState(false);

    
    const [preConditions, setPreConditions] = useState([]);

    const fetchDiscountPolicies = async (store_name) =>{
        const promise = theService.getPolicies('discount', store_name); // goes to register.js and sends to backend
        promise.then((data) => {
            if(data !== undefined){
                if (data["data"] != null){   // if there are stores to display
                    setPolicies(data["data"]);
                }
                else{
                    alert(data["msg"])
                    setPolicies(["There are no purchase policies..."]);      // no products to display
                }
            }

        });
    };

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

    const setSelectedPolicy =  (policy_name) => {
        setDate(null);
        setPercentage(0);
        setSelectedProduct("Select Product")
        setPolicyName("")
        
        setPreConditions([]);

        setMinProductAmount(null);
        setMinPurchasePrice(null);
        setProductPreCondition("Any product");
        
        setShowMinProductPreCondition(false)
        setShowMinPurchasePreCondition(false)
        setShowProductPreCondition(false)

        policies.map(policy => {
            if(policy["name"] === policy_name){
                setPolicyName(policy_name);
                setNewPolicyName(policy_name);
                setPercentage(policy['percentage']);
                setSelectedProduct(policy["product"]);
                setDate(policy["valid_until"]);
                
                if(policy['precondition'] !== undefined && policy['precondition'] !== null){
                    setShowProductPreCondition(true)
                    setProductPreCondition(policy['precondition']['product'])
                    preConditions.push('product')

                    if(policy['precondition']['min_amount'] !== 0 && policy['precondition']['min_amount'] !== null){
                        setShowMinProductPreCondition(true)
                        setMinProductAmount(policy['precondition']['min_amount'])
                        preConditions.push('min_product_amount')

                    }

                    if(policy['precondition']['min_basket_price'] !== 0 && policy['precondition']['min_basket_price'] !== null){
                        setShowMinPurchasePreCondition(true)
                        setMinPurchasePrice(policy['precondition']['min_basket_price'])
                        preConditions.push('min_purchase_price')

                    }
                }
            }
        })
    }

    const addPolicyHandler = async () =>{
    //   if(preConditions.length > 0 && !preConditions.includes('product')){
      if((showMinProductPreCondition || showMinPurchasePreCondition) && !showProductPreCondition){
        alert('To set any additional pre-conditions, you must select the \'Buy with\' option')
      }
      else if(showMinProductPreCondition && (minProductAmount === null || minProductAmount < 0))
        alert("Minimum product amount has to be set and must be bigger than 0.")
      else if(showMinPurchasePreCondition && (minPurchasePrice === null || minPurchasePrice < 0)
              && !(showProductPreCondition && productPreCondition === 'Any product'))
        alert("Minimum purchase price has to be set and must be bigger than 0.")
      else if(date === "")
        alert("You must set expiration date.")
      else{
        //   alert(productPreCondition)
        var product_amount_precondition = minProductAmount
        var new_policy_name = newPolicyName
        if(showMinProductPreCondition && showProductPreCondition && productPreCondition === 'Any product'){
            // setMinProductAmount(null)
            product_amount_precondition = null
        }
        if(policyName === newPolicyName)
            new_policy_name = null
        alert([storeName, policyName, selectedProduct, date, percentage, new_policy_name, !showProductPreCondition ? null : (productPreCondition === "Any product" ? "all" : productPreCondition), product_amount_precondition, minPurchasePrice])
        const promise = theService.addAndUpdateDiscountPolicy('update', storeName, policyName, selectedProduct, date, percentage, new_policy_name, !showProductPreCondition ? null : (productPreCondition === "Any product" ? "all" : productPreCondition), product_amount_precondition, minPurchasePrice)
        promise.then((data) => {
            if(data !== undefined){
                confirmAlert({
                    title: data["msg"],
                    buttons: [
                        {   label: 'Ok',
                            onClick: () => { // reset the form in order to add another product
                                if(data['data']){
                                    fetchDiscountPolicies(storeName)
                                    setPolicyName('Select policy')
                                    alert(policyName)

                                }
                                // setDate(null);
                                // setPercentage(0);
                                // setSelectedProduct("Select Product")
                                // setPolicyName("")
                                // setNewPolicyName(null)
                                
                                // setPreConditions([]);

                                // setMinProductAmount(null);
                                // setMinPurchasePrice(null);
                                // setProductPreCondition(null);
                                
                                // setShowMinProductPreCondition(false)
                                // setShowMinPurchasePreCondition(false)
                                // setShowProductPreCondition(false)
                        }},
                        // {   label: 'Done',
                        //     onClick: () => {BackOption.BackToHome(props.history)}
                        // }
                    ]
                });
            }

        });
      }
      
    };
  
    const addPreCondition = (pre_condition) =>{
        // if(preConditions.includes(pre_condition)){
        //     preConditions.pop(pre_condition)
        //     if(pre_condition === 'product')
        //         setProductPreCondition("Any product");
        //     else if(pre_condition === 'min_purchase_price')
        //         setMinPurchasePrice(null); 
        //     else if(pre_condition === 'min_product_amount')
        //         setMinProductAmount(null);
        // }
        // else {
        //     preConditions.push(pre_condition)
        // }
        if(pre_condition === 'product'){
            alert(productPreCondition)
            if(showProductPreCondition)
                setProductPreCondition("Any product");
            setShowProductPreCondition(!showProductPreCondition)
            alert(productPreCondition)

        }
        else if(pre_condition === 'min_purchase_price'){
            if(showMinPurchasePreCondition){}
                setMinPurchasePrice(null); 
            setShowMinPurchasePreCondition(!showMinPurchasePreCondition)

        }
        else if(pre_condition === 'min_product_amount'){
            if(showMinProductPreCondition)
                setMinProductAmount(null);
            setShowMinProductPreCondition(!showMinProductPreCondition)
        }
    };

    const detailsFilled = () => {
      if(policyName !== "" && date !== null && percentage !== 0 && selectedProduct !== "Select Product"){
            return true;
      }
      return false;
    }

    
    return (
        // <div style={{width: props["screenWidth"], height: props["screenHeight"]}}>
        <div style={{marginTop:"2%" , marginLeft: "20%", marginRight: "20%", border: "1px solid", borderColor: "#CCCCCC"}}>
  
          <Container>
            <h4 style={{marginTop:"2%"}}>Update a New Discount Policy</h4>
            <Form className='add_policy'>
                <Form.Group controlId="products_ControlSelect2" value={policyName} type='reset' onChange={ event => {
                        event.target.value === 'Select policy' ? setPolicyName('Select policy') : setSelectedPolicy(event.target.value)
                        }}>
                        <Form.Label>Please choose a policy:</Form.Label>
                        <Form.Control as="select">
                            <option>Select policy</option>
                            {policies !== null ?
                                policies.map(policy => (
                                <option value={policy["name"]}>{policy["name"]}</option>
                                ))
                                : null
                            }
                        </Form.Control>
                    </Form.Group>

                { policyName !== "Select policy" ? <div>

                <Form.Label>Enter policy name:</Form.Label>
                <Form.Control id="policy-name" value={newPolicyName} required type="text" placeholder="Policy name"
                        onChange={(event => {setNewPolicyName(event.target.value)})}/>
  
                <Form.Group  style={{marginTop:"2%"}} controlId="products_ControlSelect2" onChange={event => setSelectedProduct(event.target.value)}>
                    <Form.Label>Select products to apply the policy on:</Form.Label>
                    <Form.Control as="select" value={selectedProduct}>
                            <option>Select Product</option>
                            {storeProducts !== null ?
                                storeProducts.map(product => (
                                <option value={product["name"]}>{product["name"]}</option>
                                ))
                                : null
                            }
                    </Form.Control>
                </Form.Group>

                <Form.Label >Enter percentage:</Form.Label>
                <Form.Control id="Discount percentage" required type="number" min={0} max={100} title="percentage has to be between 0 to 100." placeholder="Discount percentage" value={percentage}
                        onChange={(event => {setPercentage(event.target.valueAsNumber)})}/>
                
                <Form.Label  style={{marginTop:"2%"}}>Enter expiration date:</Form.Label>
                <Form.Control id="policy-name" required type="date" placeholder="Discount expiration date" min={(new Date()).toJSON().split('T')[0]} value={(new Date(date)).toJSON().split('T')[0]}
                        onChange={(event => {setDate(event.target.valueAsDate)})}/>

              <Form.Label style={{marginTop:"2%"}}>Select additional dicount pre-conditions:</Form.Label>
                <div key={`inline-checkbox`} className="mb-3" style={{ border: "1px solid", borderColor: "#CCCCCC"}}>
                    <div style={{marginLeft:"4%"}}>
                    <Row style={{marginTop: "1.5%"}}>
                        <Form.Label column  sm="6" style={{left: "-17%"}}>
                            <Form.Check inline label="Buy with:" type="checkbox" checked={showProductPreCondition} id={`minimun-amount`} value={showProductPreCondition} onChange={(event => {
                                                                                                                        addPreCondition('product')
                                                                                                                        showProductPreCondition ? setShowProductPreCondition(false) : setShowProductPreCondition(true)
                                                                                                                        })} />
                        </Form.Label>
                        <Col sm="6" style={{left: "-8%"}}>
                            <Form.Control as="select" disabled={!showProductPreCondition} value={productPreCondition} onChange={(event => {setProductPreCondition(event.target.value)})}>
                                <option>Any product</option>
                                {storeProducts !== null ?
                                    storeProducts.map(product => (
                                    <option value={product["name"]}>{product["name"]}</option>
                                    ))
                                    : null
                                }
                            </Form.Control>
                        </Col>
                    </Row>
                    <Row style={{marginTop: "1.5%"}}>
                        <Form.Label column  sm="6" style={{left: "-8.1%"}}>
                            <Form.Check inline label="Minimum purchase price" checked={showMinPurchasePreCondition} value={showMinPurchasePreCondition} type="checkbox" id={`minimum-price`} name="formHorizontalRadios" onChange={(event => {
                                                                                                                        addPreCondition('min_purchase_price')
                                                                                                                        showMinPurchasePreCondition ? setShowMinPurchasePreCondition(false) : setShowMinPurchasePreCondition(true);
                                                                                                                        })} />
                        </Form.Label>
                        <Col sm="6" style={{left: "-8%"}}>
                            <Form.Control type="number" min={0} data-bind="value:replyNumber" value={minPurchasePrice} disabled={!showMinPurchasePreCondition} required placeholder="Enter minimum price" onChange={(event => {setMinPurchasePrice(event.target.valueAsNumber)})}/>
                        </Col>
                    </Row>
                    <Row style={{marginTop: "1.5%", marginBottom: "1.5%"}}>
                        <Form.Label column  sm="6" style={{left: "-7.2%"}}>
                            <Form.Check inline label="Minimum product amount" checked={showMinProductPreCondition} disabled={showProductPreCondition && "Any product" === productPreCondition} value={showMinProductPreCondition} type="checkbox" id={`minimum-price`} name="formHorizontalRadios" onChange={(event => {
                                                                                                                        addPreCondition('min_product_amount')
                                                                                                                        showMinProductPreCondition ? setShowMinProductPreCondition(false) : setShowMinProductPreCondition(true);
                                                                                                                        })} />
                        </Form.Label>
                        <Col sm="6" style={{left: "-8%"}}>
                            <Form.Control type="number" min={0} data-bind="value:replyNumber" disabled={!showMinProductPreCondition} value={minProductAmount} required placeholder="Enter minimum amount" onChange={(event => {setMinProductAmount(event.target.valueAsNumber)})}/>
                        </Col>
                    </Row>
                    </div>
                </div>
                <Button style={{marginBottom:"2%"}} variant="dark" id="open-store-button" disabled={!detailsFilled()} onClick={addPolicyHandler}>Update Policy!</Button>

             </div> : null }   
                
            </Form>
          </Container>
  
        </div>
    );
  }

export default EditDiscountPolicyForm;
