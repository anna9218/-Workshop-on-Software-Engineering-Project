import React, {useState, useEffect} from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import {Container, Row, Col, Button, Dropdown, Jumbotron, Form} from 'react-bootstrap'
import * as theService from '../../services/communication';
import * as BackOption from '../Actions/GeneralActions/Back'


function AppointStoreManager(props){
    useEffect(() => {
        setSelectedStore(props.location.store)

    }, []);

    const [selectedStore, setSelectedStore] = useState("");
    const [subscriberNickname, setSubscriberNickname] = useState("");
    const [permissions, setPermissions] = useState([10]);


    const addPermissions = async (permission) => {
        setPermissions(permissions.concat(permission));
    };

    const appointManagerHandler = async () =>{
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

          <div style={{marginLeft: "30%", marginRight: "30%", marginTop: "2%"}}>
        
            <Form.Label>Enter subscriber's nickname to appoint as manager:</Form.Label>
            <Form.Control id="subscriber-nickname" value={subscriberNickname} required type="text" placeholder="Subscriber's nickname" 
                onChange={(event => {setSubscriberNickname(event.target.value)})}/>

            <Form.Label>Select permissions:</Form.Label>
            
            <div>
            <div key={`inline-checkbox`} className="mb-3" style={{ border: "1px solid", borderColor: "#CCCCCC"}}>
                <div style={{ marginLeft:"4%"}}>
                <Row><Form.Check style = {{position: "sticky"}} label="Manage Stock" type="checkbox" id={`auction-purchase`} onChange={(event => {addPermissions(1)})} />
                </Row><Row><Form.Check style = {{position: "sticky"}}  label="Manage Store policies" type="checkbox" id={`auction-purchase`} onChange={(event => {addPermissions(2)})} />
                </Row><Row><Form.Check style = {{position: "sticky"}}  label="Appoint Additional Owner" type="checkbox" id={`lottery-purchase`} onChange={(event => {addPermissions(3)})}/>
                </Row><Row><Form.Check style = {{position: "sticky"}}  label="Appoint Additional Manager" type="checkbox" id={`lottery-purchase`} onChange={(event => {addPermissions(5)})}/>
                </Row><Row><Form.Check style = {{position: "sticky"}}  label="Edit Manager's Permissions" type="checkbox" id={`lottery-purchase`} onChange={(event => {addPermissions(6)})}/>
                </Row><Row><Form.Check style = {{position: "sticky"}}  label="Remove Store Manager" type="checkbox" id={`lottery-purchase`} onChange={(event => {addPermissions(7)})}/>
                </Row>
                </div>
            </div>
             </div>

             <Form >
                 <Form.Group as={Row} style={{marginRight:"0%" , marginLeft: "0%"}}>
                 <div><Button type='reset' variant="dark" id="appoint-manager-button" disabled={subscriberNickname === ""} onClick={appointManagerHandler}>Commit</Button></div>
                 <div style={{marginLeft:"1%"}}> <Button  variant="dark" id="back-btn" onClick={event => BackOption.BackToHome(props)}>Back</Button></div>
                 </Form.Group>
             </Form>
            </div>
        </div>
    );
}


export default AppointStoreManager;