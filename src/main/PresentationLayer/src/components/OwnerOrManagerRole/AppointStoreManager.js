import React, {useState, useEffect} from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import {BrowserRouter as Router, Switch, Route, Link} from 'react-router-dom'
import {Container, Row, Col, Button, Dropdown, Jumbotron, Form} from 'react-bootstrap'
import * as theService from '../../services/communication';


function AppointStoreManager(props){
    useEffect(() => {
        // fetchOwnedStores();
        setSelectedStore(props.location.store)

    }, []);

    // const [stores, setStores] = useState(["No owned stores"]);
    const [selectedStore, setSelectedStore] = useState("");
    const [subscriberNickname, setSubscriberNickname] = useState("");
    const [permissions, setPermissions] = useState([10]);


    // const fetchOwnedStores = async () => {
    //     const promise = theService.fetchOwnedStores();  // goes to communication.js and sends to server
    //     promise.then((data) => {
    //         if (data["data"]["response"].length > 0){   // if there are owned stores
    //             setStores(data["data"]["response"]);
    //         }
    //         else{
    //             setStores([data["data"]["msg"]]);       // no owned stores, array if empty
    //         }
    //     });
    // };

    const addPermissions = async (permission) => {
        setPermissions(permissions.concat(permission));
    };

    const appointManagerHandler = async () =>{
        // if(selectedStore === ""){
        //     setSelectedStore(stores[0]);
        // }
        if(subscriberNickname === ""){
            alert("Please enter subscriber's nickname to appoint");
        }
        else{
            
            const promise = theService.appointStoreManager(subscriberNickname, selectedStore, permissions);
            promise.then((data) => {
                alert(data["msg"]);
            });
        }
      };


    return (
        <div style={{width: props["screenWidth"], height: props["screenHeight"]}}>
          <h1>{selectedStore} - Appoint Store Manager</h1>

           
{/* 
            <Form.Group controlId="stores_ControlSelect1" value={selectedStore} onChange={ event => {setSelectedStore(event.target.value);}}>
            <Form.Label>Please choose a store:</Form.Label>
            <Form.Control as="select">
                {stores.map(store => (
                    <option value={store}>{store}</option>
                ))}
            </Form.Control>
            </Form.Group> */}
        
            <Form.Label>Enter subscriber's nickname to appoint as manager:</Form.Label>
            <Form.Control id="subscriber-nickname" value={subscriberNickname} required type="text" placeholder="Subscriber's nickname" 
            onChange={(event => {setSubscriberNickname(event.target.value)})}/>

            <Form.Label>Select permissions:</Form.Label>
            
            <div>
            <div key={`inline-checkbox`} className="mb-3" style={{border: "1px solid", borderColor: "#CCCCCC"}}>
              <Form.Check inline style = {{position: "relative"}} label="Manage Stock" type="checkbox" id={`auction-purchase`} onChange={(event => {addPermissions(1)})} />
              <Form.Check inline style = {{position: "relative"}}  label="Manage Store policies" type="checkbox" id={`auction-purchase`} onChange={(event => {addPermissions(2)})} />
              <Form.Check inline style = {{position: "relative"}}  label="Appoint Additional Owner" type="checkbox" id={`lottery-purchase`} onChange={(event => {addPermissions(3)})}/>
              <Form.Check inline style = {{position: "relative"}}  label="Appoint Additional Manager" type="checkbox" id={`lottery-purchase`} onChange={(event => {addPermissions(5)})}/>
              <Form.Check inline style = {{position: "relative"}}  label="Edit Manager's Permissions" type="checkbox" id={`lottery-purchase`} onChange={(event => {addPermissions(6)})}/>
              <Form.Check inline style = {{position: "relative"}}  label="Remove Store Manager" type="checkbox" id={`lottery-purchase`} onChange={(event => {addPermissions(7)})}/>
             </div>
             </div>
            <Container> 
                <Button variant="dark" id="appoint-manager-button" onClick={appointManagerHandler}>Commit</Button>

            {/* <div style={{marginTop: "5%"}}>
                { showAddForm ? <AddProductsForm storeName={selectedStore} /> : null }
            </div>
           */}
            </Container>
  
        </div>
    );

}



export default AppointStoreManager;