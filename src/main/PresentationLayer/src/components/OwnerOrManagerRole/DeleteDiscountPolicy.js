import React, { useState, useEffect } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import {BrowserRouter as Link } from 'react-router-dom'
import {Container, Button, Form} from 'react-bootstrap'
import * as theService from '../../services/communication';
import { confirmAlert } from 'react-confirm-alert'; 

function DeleteDiscountPolicy(props){
    useEffect(() => {
        setStoreName(props.storeName)
        fetchDiscountPolicies(props.storeName)
      }, []);


    const [storeName, setStoreName] = useState("");
    const [policyName, setPolicyName] = useState('Select policy');
    const [policies, setPolicies] = useState([]);


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


    const deletePolicyHandler = async () =>{
      
        const promise = theService.deletePolicy('discount', storeName, policyName)
        promise.then((data) => {
                if(data !== undefined){
                    confirmAlert({
                        title: data["msg"],
                        buttons: [
                            {   label: 'Ok',
                                onClick: () => { // reset the form in order to add another product
                                    fetchDiscountPolicies(storeName)
                                    setPolicyName('Select policy')
                            }},
                        ]
                    });
                }

        });
      }
    
    return (
        <div style={{marginTop:"2%" , marginLeft: "20%", marginRight: "20%", border: "1px solid", borderColor: "#CCCCCC"}}>
  
          <Container>
            <h4 style={{marginTop:"2%"}}>Delete Discount Policy</h4>
            <Form className='add_policy'>
                <Form.Group controlId="products_ControlSelect2" value={policyName} onChange={event => {setPolicyName(event.target.value)}}>
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

                <Button style={{marginBottom:"2%"}} variant="dark" id="open-store-button" type='reset' disabled={policyName === 'Select policy'} onClick={deletePolicyHandler}>Delete Policy!</Button>
   
            </Form>
          </Container>
  
        </div>
    );
 }
  

export default DeleteDiscountPolicy;
