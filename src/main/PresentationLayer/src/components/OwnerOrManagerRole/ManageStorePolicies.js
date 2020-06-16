import React, { useState, useEffect } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import {BrowserRouter as Router,  Route, Link } from 'react-router-dom'
// import { browserHistory } from "react-router";
import {Container, Button, Accordion, Card, Form, Row} from 'react-bootstrap'
import * as theService from '../../services/communication';
import * as BackOption from '../Actions/GeneralActions/Back';
import AddPurchaseForm from './AddPurchaseForm';
import EditPurchaseForm from './EditPurchaseForm';


// import Icon from 'react-native-vector-icons/FontAwesome';

function ManageStorePolicies(props) {
  useEffect(() => {
    // console.log(props.location.state.storeName)
    setStoreName(props.location.store)
    // console.log(storeName);
    fetchPurchasePolicies("purchase", props.location.store);
    fetchDiscountPolicies("discount", props.location.store);
    // setHistory(useHistory());
  }, []);

  // const [history, setHistory]= useState('');
  const [storeName, setStoreName] = useState('');
  const [purchasePolicies, setPurchasePolicies] = useState(["There are no purchase policies."]);
  const [purchaseAction, setPurchaseAction] = useState("");
  const [policyName, setPolicyName] = useState("");
  const [filterCategory, setFilterCategory] = useState("");
  const [filterMinPrice, setFilterMinPrice] = useState(-1);
  const [filterMaxPrice, setFilterMaxPrice] = useState(-1);


  
  const addPurchaseHandler = (event) =>{
    setPurchaseAction("addPurchasePolicy")
  };

  const editPurchaseHandler = (event) =>{
    setPurchaseAction("editPurchasePolicy")
  };

  const PurchasesCombinationHandler = (event) =>{
    setPurchaseAction("purchasesCombination")
  };

  const fetchPurchasePolicies = (policy_name, store_name) => {
    const promise = theService.getPolicies(policy_name, store_name);
    promise.then((data) => {

      if(data != null){
        if (data["data"] != null && data["data"].length > 0){   // if there are stores to display
          setPurchasePolicies(data["data"]);
          // setPolicyName(0);
        //   alert(data["msg"]);      // no products to display

        }
        else{
          setPurchasePolicies(["There are no purchase policies."]);
        }
      }
  });
};

const fetchDiscountPolicies = () => {}


  return (
    <div style={{width: props["screenWidth"], height: props["screenHeight"]}}>
      <div style={{marginTop:"1%"}}>
        <h2> {storeName} - Manage Store Policies </h2>
      </div>

     <Accordion>
        <Card>
            {/******** Purchase Card *********/}
            <Card.Header>
            <Accordion.Toggle as={Button} type="radio" variant="link" eventKey="0">
                Purchase Policy
            </Accordion.Toggle>
            </Card.Header>
            <Accordion.Collapse eventKey="0">
            <Card.Body>

            <Container> 
            <div style={{marginTop:"2%" , marginLeft: "25%", marginRight: "25%", border: "1px solid", borderColor: "#CCCCCC"}}>
                <h3 style={{marginTop:"2%"}}>Select action</h3>
                <Form style={{marginRight:"5%" , marginLeft: "5%", marginBottom:"2%"}}>
                    <Row><Form.Check onClick={addPurchaseHandler} type="radio" label="Add Purchase Policy" name="formHorizontalRadios" id="Radios1"/>
                    </Row>
                    <Row><Form.Check inline onClick={editPurchaseHandler} type="radio" label="Edit Purchase Policy" name="formHorizontalRadios"id="Radios2"/>
                    </Row>
                    <Row><Form.Check inline onClick={PurchasesCombinationHandler} type="radio" label="Edit Policies Combinations" name="formHorizontalRadios"id="Radios3"/>
                    </Row>
                </Form>
            </div>
            <div style={{marginTop: "5%"}}>
                { purchaseAction === "addPurchasePolicy" ? <AddPurchaseForm storeName={storeName} history={props.location.props} /> : null }
            </div>
            <div style={{marginTop: "5%"}}>
                { purchaseAction === "editPurchasePolicy" ? <EditPurchaseForm storeName={storeName} history={props.location.props} /> : null }
            </div>
            <div style={{marginTop: "5%"}}>
                { purchaseAction === "purchasesCombination" ? <PurchaseCombinationsForm storeName={storeName} history={props.location.props} /> : null }
            </div>

            <Button style={{marginTop: "1%"}}  variant="dark" id="add_product-button" onClick={event => BackOption.BackToHome(props.location.props)}>Back</Button>
          
            </Container>
{/*                 
                <div style={{marginTop:"0.5%" , marginLeft: "10%", marginRight: "10%", border: "1px solid", borderColor: "#CCCCCC"}}>
                    
                    <Form>
                        <fieldset>
                            <Form.Group as={Row}  style={{ marginTop:"2%", marginRight:"1%" , marginLeft: "1%"}}>
                            <Form.Label as="legend">
                                    Select action:
                                </Form.Label>
                              <Form.Control as="select">
                                  {purchasePolicies.map(store => (
                                      <option value={store}>{store}</option>
                                  ))}
                              </Form.Control>
                                <Form.Label as="legend" style={{ marginTop:"2%", marginRight:"5%" , marginLeft: "5%"}} column sm={2}>
                                    Policies Combinations:
                                </Form.Label>
                                <Form.Check inline onClick={(event => {setPolicyCombinationType("xor")})} type="radio" label="Activate One Policy" name="formHorizontalRadios"id="Radios1"/>
                                <Form.Check inline onClick={(event => {setPolicyCombinationType("or")})} type="radio" label="Activate At Least One Policy" name="formHorizontalRadios"id="Radios2"/>
                                <Form.Check inline onClick={(event => {setPolicyCombinationType("and")})} type="radio" label="Activate All policies" name="formHorizontalRadios"id="Radios3"/>
                                
                            </Form.Group>
                        </fieldset>
                        <Form.Group as={Row} style={{marginRight:"1%" , marginLeft: "1%"}}>
                            <Row><Button style={{marginLeft:"10%"}}  type="reset" variant="dark">Add</Button></Row>
                            <Row><Button  type="reset" variant="dark">Edit</Button></Row>
                        </Form.Group>
                    </Form>
                </div> */}

            </Card.Body>
            </Accordion.Collapse>
        </Card>
        <Card>
              {/***************** Discount card *******************/}

            <Card.Header>
            <Accordion.Toggle as={Button} variant="link" eventKey="1">
                Discount Policy
            </Accordion.Toggle>
            </Card.Header>
            <Accordion.Collapse eventKey="1">
            <Card.Body>
                <div style={{marginTop:"0.5%" , marginLeft: "10%", marginRight: "10%", border: "1px solid", borderColor: "#CCCCCC"}}>
                    {/* <Form>
                        <fieldset>
                        <Form.Group as={Row} style={{marginTop: "1%", marginRight:"4%" , marginLeft: "0%"}} >
                            <Form.Label column sm="2">
                                <Form.Check inline onClick={(event => {setFilterType(1)})} type="radio" label="By price range" name="formHorizontalRadios"id="Radios1"/>                                
                            </Form.Label>
                            <Col sm="10">
                                <Form.Control disabled={(filterType !== 1)} placeholder="Enter min price" onChange={(event =>{
                                        try{ 
                                            let value = parseInt(event.target.value);
                                            if(value < 0)
                                                alert("Error - Price has to be bigger than 0.");
                                            else
                                                setFilterMinPrice(value);
                                        }
                                        catch(e){
                                            alert("Error - Price has to be a number.");
                                        }
                                    })}/>
                                <Form.Control disabled={(filterType !== 1)} style={{marginTop: "1%"}} placeholder="Enter max price"  onChange={(event =>{
                                        try{ 
                                            let value = parseInt(event.target.value);
                                            if(value < 0)
                                                alert("Error - Price has to be bigger than 0.");
                                            else
                                                setFilterMaxPrice(value);
                                        }
                                        catch(e){
                                            alert("Error - Price has to be a number.");
                                        }
                                    })}/>
                            </Col>
                            <Form.Label column sm="2" >
                                <Form.Check inline onClick={(event => {setFilterType(2)})} type="radio" label="By category" name="formHorizontalRadios"id="Radios1"/>                                
                            </Form.Label>
                            <Col sm="10">
                                <Form.Control disabled={(filterType !== 2)} style={{marginTop: "1%"}} placeholder="Enter category" onChange={(event => {setFilterCategory(event.target.value)})}/>
                            </Col>
                                
                        </Form.Group>
                        </fieldset>
                        

                        <Form.Group as={Row} style={{marginRight:"3%" , marginLeft: "3%"}}>
                            <Button type="reset" disabled={(
                                                            !(filterType === 1 && (filterMaxPrice !== -1 && filterMinPrice !== -1)) &&
                                                            !(filterType === 2 && filterCategory !== ""))}onClick= {(event => {FilterProductsHandler()})} >Filter</Button>
                        </Form.Group>
                    </Form> */}
                </div>
            </Card.Body>
            </Accordion.Collapse>

      </Card>
      </Accordion>
    </div>
  );
}

// TODO - add back button


export default ManageStorePolicies;

function PurchaseCombinationsForm(props) {
    useEffect(() => {
      // console.log(props.location.state.storeName)
      setStoreName(props.storeName)
      fetchPurchaseCombination(props.storeName)
    }, []);
  
    // const [history, setHistory]= useState('');
    const [storeName, setStoreName] = useState('');
    const [operator, setOperator] = useState('');
  


    const fetchPurchaseCombination = (store_name) => {
        const promise = theService.getPurchasePoliciesOperator(store_name);
        promise.then((data) => {
            setOperator(data["data"])
      });
    };

    const setOperatorHandler = () => {
        const promise = theService.setPurchasePoliciesOperator(storeName, operator);
        promise.then((data) => {
            alert("Purchase Policies combination updated successfully!")
            fetchPurchaseCombination(storeName)
      });
    };
    
    return (
        <div style={{marginTop:"2%" , marginLeft: "25%", marginRight: "25%", border: "1px solid", borderColor: "#CCCCCC"}}>
                <h4 style={{marginTop:"2%"}}>Update policies combinations:</h4>
                <Form style={{marginRight:"5%" , marginLeft: "5%", marginBottom:"2%"}}>
                   
                    <label >Select the wanted combination between the policies</label>
                    <Row><Form.Check inline checked={operator === 'xor'} onChange={(event => {setOperator('xor')})} type="radio" label="Activate only one policy" name="formHorizontalRadios" id="xor_operator"/>
                    </Row>
                    <Row><Form.Check inline checked={operator === 'or'} onChange={(event => {setOperator('or')})} type="radio" label="Activate at least one policy" name="formHorizontalRadios"id="or_operator"/>
                    </Row>
                    <Row><Form.Check inline checked={operator === 'and'} onChange={(event => {setOperator('and')})} type="radio" label="Activate all policies" name="formHorizontalRadios"id="and_operator"/>
                    </Row>
                    <Button variant='dark' onClick={setOperatorHandler}>Commit Change</Button>
                </Form>
            </div>
    );
}

