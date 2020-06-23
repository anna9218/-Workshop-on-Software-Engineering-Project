import React, { useState, useEffect } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import {BrowserRouter as Router,  Route, Link } from 'react-router-dom'
import {Container, Button,Form, Col, Row, } from 'react-bootstrap'
import * as theService from '../../services/communication';
import {IoMdCloseCircle} from 'react-icons/io' 
import { confirmAlert } from 'react-confirm-alert'; 

function EditPurchasePolicyForm(props){
    useEffect(() => {
        setStoreName(props.storeName)
        fetchPurchasePolicies(props.storeName)
        fetchStoreProducts(props.storeName)
      }, []);


    const [storeName, setStoreName] = useState("");
    const [policyName, setPolicyName] = useState('Select policy');
    const [policies, setPolicies] = useState([]);
    const [storeProducts, setStoreProducts] = useState(["There are no products in the store inventory..."]);
    const [policyProducts, setPolicyProducts] = useState([]);
    const [policyTypes, setPolicyTypes] = useState([]);
    const [minAmount, setMinAmount] = useState(null);
    const [maxAmount, setMaxAmount] = useState(null);
    const [dates, setDates] = useState(null);
    const [showMinAmount, setShowMinAmount] = useState(false);
    const [showMaxAmount, setShowMaxAmount] = useState(false);
    const [showDates, setShowDates] = useState(false);
    const [checkBundle, setCheckBundle] = useState(false);
    
    const setSelectedPolicy = async (policy_name) => {
        setPolicyProducts([]);
        setPolicyTypes([]);
        setMinAmount(null);
        setMaxAmount(null);
        setDates(null);
        setShowMinAmount(false)
        setShowMaxAmount(false)
        setShowDates(false)
        setCheckBundle(false)
        policies.map(policy => {
            if(policy["name"] === policy_name){
                setPolicyName(policy_name);
                setPolicyProducts(policy["products"]);
                setDates(null);
                
                if(policy['min_amount'] !== undefined){
                    policyTypes.push('min_amount')
                    setMinAmount(policy["min_amount"]);
                    setShowMinAmount(true)
                }
                if(policy['max_amount'] !== undefined){
                    policyTypes.push('max_amount')
                    setMaxAmount(policy["max_amount"]);
                    setShowMaxAmount(true)
                }
                if(policy['dates'] !== undefined){
                    var stringDates = policy["dates"].map(date => (new Date(date)).toLocaleDateString())
                    setDates(stringDates);
                    policyTypes.push('dates')
                    setShowDates(true)
                }
                if(policy['bundle'] !== undefined){
                    updatePolicyType('bundle')
                    setCheckBundle(true)
                }
                
            }
        })
    }

    const fetchPurchasePolicies = async (store_name) =>{
        const promise = theService.getPolicies('purchase', store_name); // goes to register.js and sends to backend
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

    const fetchStoreProducts = async (store_name) =>{
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

    const editPolicyHandler = async () =>{

      if(showMinAmount && (minAmount === null || minAmount < 0))
        alert("Minimum amount need to be set and must be bigger than 0.")
      else if(showMaxAmount && (maxAmount === null || maxAmount < 0))
        alert("Maximum amount need to be set and must be bigger than 0.")
      else if(showDates && (dates === null || dates.length === 0))
        alert("For forbidden dates, you must select at least one date.")
      else{
        const promise = theService.addAndUpdatePurchasePolicy('update', props.storeName, policyName, policyProducts, 
            minAmount, maxAmount, dates, checkBundle ? true : null); // goes to register.js and sends to backend
        promise.then((data) => {
            if(data !== undefined){
                confirmAlert({
                    title: data["msg"],
                    buttons: [
                        {   label: 'Ok',
                            onClick: () => { // reset the form in order to add another product
                                fetchPurchasePolicies(storeName)
                                setPolicyName('Select policy')
                        }}]
                });
            }

        });
      }
      
    };
  
    const updatePolicyType =  (policy_type) =>{
        if(policy_type === 'min_amount')
            setMinAmount(null);
        else if(policy_type === 'max_amount')
            setMaxAmount(null); 
        else if(policy_type === 'forbidden_dates')
            setDates(null);
        
        if(policyTypes.includes(policy_type)){
            policyTypes.pop(policy_type)
            
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
            policyProducts.splice(policyProducts.indexOf(product_name), 1)
    }

    const removeDates = async (date) =>{
        if(dates.includes(date)){
            dates.splice(dates.indexOf(date), 1)
            if(dates.length === 0)
                setDates(null)
        }
    }
    
    return (
        <div style={{width: props["screenWidth"], height: props["screenHeight"]}}>
        <div style={{marginTop:"2%" , marginLeft: "20%", marginRight: "20%", border: "1px solid", borderColor: "#CCCCCC"}}>
  
          <Container>
            <h4 style={{marginTop:"2%"}}>Edit Purchase Policy</h4>
            <Form className='add_policy'>
                <Form.Group controlId="products_ControlSelect2" value={policyName}  onChange={ event => {
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
              <Form.Label>Policy name:</Form.Label>
              <Form.Control id="policy-name" required type="text" placeholder={policyName} disabled={true}/>
  
              <Form.Label style={{marginTop:"2%"}}>Enter the purchase type (at least one):</Form.Label>
                <div key={`inline-checkbox`} className="mb-3" style={{ border: "1px solid", borderColor: "#CCCCCC"}}>
                    <div style={{marginLeft:"4%"}}>
                    <Row style={{marginTop: "1.5%"}}>
                        <Form.Label column  sm="6" style={{left: "-8%"}}>
                            <Form.Check inline label="Minimum product amount" checked={showMinAmount} type="checkbox" id={`minimun-amount`}  onChange={(event => {
                                                                                                                        updatePolicyType('min_amount')
                                                                                                                        setShowMinAmount(!showMinAmount)
                                                                                                                        })} />
                        </Form.Label>
                        <Col sm="6" style={{left: "-8%"}}>
                            {showMinAmount ? <Form.Control type="number" min={0} title="Has to be bigger than 0." required placeholder={minAmount} onChange={(event => {setMinAmount(event.target.valueAsNumber)})}/>
                            : null}
                        </Col>
                    </Row>
                    <Row style={{marginTop: "1.5%"}}>
                        <Form.Label column  sm="6" style={{left: "-8%"}}>
                            <Form.Check inline label="Maximum product amount" checked={showMaxAmount} type="checkbox" id={`maximum-amount`} name="formHorizontalRadios" onChange={(event => {
                                                                                                                        updatePolicyType('max_amount')
                                                                                                                         setShowMaxAmount(!showMaxAmount)
                                                                                                                        })} />
                        </Form.Label>
                        <Col sm="6" style={{left: "-8%"}}>
                            {showMaxAmount ? <Form.Control type="number" min={0} title="Has to be bigger than 0." data-bind="value:replyNumber" required placeholder={maxAmount} onChange={(event => {setMaxAmount(event.target.valueAsNumber)})}/>
                            : null}
                        </Col>
                    </Row>
                    <Row style={{marginTop: "1.5%"}}>
                        <Form.Label column  sm="6" style={{left: "-19%"}}>
                            <Form.Check inline label="Bundle" type="checkbox" id={`bundle`} checked={checkBundle} name="formHorizontalRadios" onChange={(event => { 
                                                                                                                        updatePolicyType('bundle')
                                                                                                                         setCheckBundle(!checkBundle)})}/>
                        </Form.Label>
                    </Row>
                    <Row style={{marginTop: "1.5%", marginBottom: "1%"}}>
                        <Form.Label column  sm="6" style={{left: "-14%"}}>
                            <Form.Check inline label="Forbidden dates" type="checkbox" checked={showDates} id={`Forbidden-dates`} name="formHorizontalRadios" onChange={(event => {
                                                                                                                        updatePolicyType('forbidden_dates')
                                                                                                                        setShowDates(!showDates)
                                                                                                                        })}/>
                        </Form.Label>
                        <Col sm="6" style={{left: "-8%"}}>
                            {showDates ? <Form.Control id="product-name"  required type="date" min={(new Date()).toJSON().split('T')[0]} onChange={(event => dates === null? setDates([(event.target.valueAsDate).toLocaleDateString()]) :
                                                                                                                                           ! dates.includes((event.target.valueAsDate).toLocaleDateString()) ? 
                                                                                                                                                setDates(dates.concat([(event.target.valueAsDate).toLocaleDateString()])) : alert("This date has been selected already."))}/>
                            : null}
                        </Col>

                        {dates !== null && dates.length > 0 && showDates?
                            <div style={{marginTop:"2%", marginLeft:"45%"}}>
                            <Form.Label>Your selected dates are:</Form.Label>
                            <div key={`inline-checkbox`} className="mb-3" style={{ border: "1px solid", borderColor: "#CCCCCC"}}>
                                <div style={{marginLeft:"12%"}}>
                                    {/* <option>No products were</option> */}
                                    {dates !== null ?
                                        dates.map(date => (
                                        <Row><Link class="text-decoration-none" onClick={event => removeDates(date)}> <IoMdCloseCircle /> {date}</Link></Row>
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
    
            
            <Button style={{marginBottom:"2%"}} variant="dark" id="open-store-button" type='reset' disabled={!detailsFilled()} onClick={editPolicyHandler}>Update Policy!</Button>
          
            </div> : null}
            </Form>
          </Container>
  
        </div>
        </div>
    );
  }

export default EditPurchasePolicyForm;
