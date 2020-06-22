import React, { useState, useEffect } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import {BrowserRouter as Link } from 'react-router-dom'
import {Container, Button, Form, Row} from 'react-bootstrap'
import * as theService from '../../services/communication';
import { confirmAlert } from 'react-confirm-alert'; 

function AddCompositeDiscountPolicyForm(props){
    useEffect(() => {
        setStoreName(props.storeName)
        fetchDiscountPolicies(props.storeName)
      }, []);


    const [storeName, setStoreName] = useState("");
    const [policies, setPolicies] = useState([]);
    const [policy1, setPolicy1] = useState(null);
    const [policy2, setPolicy2] = useState(null);
    const [operator, setOperator] = useState('');
    const [policyName, setPolicyName] = useState("");
    const [percentage, setPercentage] = useState(0);
    const [date, setDate] = useState("");

  
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

    const addPolicyHandler = async () =>{
        if( policy1 === policy2)
            alert("Second policy can't be equal to the first policy.")
        else{
            const promise = theService.addCompositeDiscountPolicy(storeName, policy1, policy2, operator,percentage, policyName ,date)
            promise.then((data) => {
                if(data !== undefined){
                    confirmAlert({
                        title: data["msg"],
                        buttons: [
                            {   label: 'Ok',
                                onClick: () => { // reset the form in order to add another product
                                    setDate(null);
                                    setPercentage(0);
                                    setPolicyName("")
                                    setOperator("")
                            }},
                        ]
                    });
                }
    
            });
        }
        
    }
      

    const detailsFilled = () => {
      if(policyName !== '' && date !== null && percentage !== 0 && operator !== '' &&
         policy1 !== null && policy2 != null && policy1 !== 'Select Policy' && policy2 !== 'Select Policy'){
            return true;
      }
      return false;
    }

    
    return (
        <div style={{width: props["screenWidth"], height: props["screenHeight"]}}>
        <div style={{marginTop:"2%" , marginLeft: "20%", marginRight: "20%", border: "1px solid", borderColor: "#CCCCCC"}}>
  
          <Container>
            <h4 style={{marginTop:"2%"}}>Add Composite Discount Policy</h4>
            <Form>
                <Form.Label>Enter policy name:</Form.Label>
                <Form.Control id="policy-name" value={policyName} required type="text" placeholder="Policy name"
                    onChange={(event => {setPolicyName(event.target.value)})}/>
    
                    
                <Form.Group  style={{marginTop:"2%"}} controlId="ControlSelect2" onChange={event => setPolicy1(event.target.value)}>
                    <Form.Label>Select first policy:</Form.Label>
                    <Form.Control as="select">
                            <option>Select Policy</option>
                            {policies !== null ?
                                policies.map(policy => (
                                <option value={policy["name"]}>{policy["name"]}</option>
                                ))
                                : null
                            }
                    </Form.Control>
                </Form.Group>

                <Form.Group  style={{marginTop:"2%"}} controlId="ControlSelect2" onChange={event => setPolicy2(event.target.value)}>
                    <Form.Label>Select second policy:</Form.Label>
                    <Form.Control as="select">
                            <option>Select Policy</option>
                            {policies !== null ?
                                policies.map(policy => (
                                <option value={policy["name"]}>{policy["name"]}</option>
                                ))
                                : null
                            }
                    </Form.Control>
                </Form.Group>

                <Form.Label >Enter percentage:</Form.Label>
                <Form.Control id="Discount percentage" required type="number" min={0} max={100} title="percentage has to be between 0 to 100." placeholder="Discount percentage" value={percentage}
                        onChange={(event => {setPercentage(event.target.valueAsNumber)})}/>
                
                <Form.Label  style={{marginTop:"2%"}}>Enter expiration date:</Form.Label>
                <Form.Control id="policy-name" required type="date" placeholder="Discount expiration date"  min={(new Date()).toJSON().split('T')[0]}
                        onChange={(event => {setDate(event.target.valueAsDate)})}/>
            
                
                <Form.Label style={{marginTop:"2%"}}>Select the wanted combination between the policies</Form.Label>
                <div style={{ position:"inherit", border: "1px solid", borderColor: "#CCCCCC"}}>
                    <Form style={{marginRight:"5%" , marginLeft: "5%", marginBottom:"2%",  marginTop:"2%"}}>
                        <Row><Form.Check inline checked={operator==='xor'} onChange={(event => {setOperator('xor')})} type="radio" label="Activate only one policy" name="formHorizontalRadios" id="xor_operator"/>
                        </Row>
                        <Row><Form.Check inline checked={operator==='or'} onChange={(event => {setOperator('or')})} type="radio" label="Activate at least one policy" name="formHorizontalRadios"id="or_operator"/>
                        </Row>
                        <Row><Form.Check inline checked={operator==='and'} onChange={(event => {setOperator('and')})} type="radio" label="Activate all policies" name="formHorizontalRadios"id="and_operator"/>
                        </Row>
                    </Form>
                </div>
                
                <Button style={{marginBottom:"2%", marginTop:"2%"}} type='reset' variant="dark" id="open-store-button" disabled={!detailsFilled()} onClick={addPolicyHandler}>Add Policy!</Button>
                
            </Form>
          </Container>
  
        </div>
        </div>
    );
  }

export default AddCompositeDiscountPolicyForm;
