import React, { useState, useEffect } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import {BrowserRouter as Router, Switch, Route, Link} from 'react-router-dom'
import {Container, Button} from 'react-bootstrap'
import * as theService from '../../../services/communication';
import {Accordion, Card, Table} from 'react-bootstrap'



function StoreDetail(props) {
  useEffect(() => {
    console.log(props)
    setStoreName(props.location.state.storeName)
  }, []);
  //TODO - need to send a REQUEST to display store's info

  const [storeName, setStoreName]= useState('');
  const [owners, setOwners]= useState(null);
  const [managers, setManagers]= useState(null);
  const [viewStore, setViewStore]= useState(false);
  

  const onStoreInfoClickHandler = () => {
    const promise = theService.displayStoresStores(storeName)
    promise.then((data) => {
      if(data){
        if(data["data"]["name"] !== storeName){
          alert("different name recieved");
          setStoreName(data["data"]["name"]);
        }
        setManagers(data["data"]["managers"]);
        setOwners(data["data"]["owners"]);
        setViewStore(true);
      }
    });
  };

  return (
    <div>
      {viewStore && <ShowStoreInfo storeName={storeName} managers={managers} owners={owners} />}
      {!viewStore && <ShowStore viewStore={viewStore} storeName={storeName} onStoreInfoClickHandler={onStoreInfoClickHandler} />}
    </div>
  );
}

function ShowStoreInfo(props){
  return(
    <div>
      <h1>{props.storeName}</h1>
      <div style={{marginTop: "3%", marginLeft: "1%", marginRight: "1%"}}>
        <Accordion>
          <Card>
            <Card.Header>
              <Accordion.Toggle as={Button} variant="link" eventKey="0">
                Store Owners
              </Accordion.Toggle>
            </Card.Header>
            <Accordion.Collapse eventKey="0">
              <Card.Body>
                <Table striped bordered hover >
                  <tbody>
                      {
                          props.owners.map(owner => {
                              return(
                                  <tr>
                                      <td>{owner}</td>
                                  </tr>
                              );
                          })
                      }
                  </tbody>
                </Table>
              </Card.Body>
            </Accordion.Collapse>
          </Card>
          <Card>
            <Card.Header>
              <Accordion.Toggle as={Button} variant="link" eventKey="1">
                Store Managers
              </Accordion.Toggle>
            </Card.Header>
            <Accordion.Collapse eventKey="1">
              <Card.Body>
              <Table striped bordered hover color="black">
                  <tbody>
                      {
                        props.managers == [] || props.managers == null ? <p>No Managers Exsist For The Store Yet!</p> :
                          props.managers.map(manager => {
                              return(
                                  <tr>
                                      <td>{manager}</td>
                                  </tr>
                              );
                          })
                      }
                  </tbody>
                </Table>
              </Card.Body>
            </Accordion.Collapse>
          </Card>
        </Accordion>
      </div>
      <Button style={{marginTop: "1%"}} variant="dark" id="back-btn" as={Link} to="/stores" >Back</Button>

    </div>
  )
}

function ShowStore(props){
  return(
    <div>
      <h1>{props.storeName}</h1>
      <Container>
              <Button variant="dark" id="storeinfobtn" block onClick={props.onStoreInfoClickHandler}>Store Info</Button>
          <Link to={{
                pathname:'/stores/'+props.storeName+'/products', 
                state: {
                    storeName: props.storeName               
                  }}}>
              <Button variant="dark" id="productsbtn" block>Products Info</Button>
          </Link>
          <Link to={{
                pathname:'/stores'
                }}>
              <Button variant="dark" id="backbtn" block>Back</Button>
          </Link>
      </Container>
    </div>
  )
}

export default StoreDetail;