import React, {useState, useEffect} from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import {Row, Button, Form} from 'react-bootstrap'
import * as theService from '../../services/communication';
import { confirmAlert } from 'react-confirm-alert'; 


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
                if(data["data"] ){
                    confirmAlert({
                        title: data["msg"],
                        buttons: [
                            {   label: 'Appoint another manager',
                                onClick: () => { // reset the form in order to add another product
                                    setPermissions([10])
                                    setSubscriberNickname("")
                            }},
                            {
                                label: 'Back',
                                onClick: () => {
                                    props.history.push("./owner")
                            }}
                        ]
                    });
                }
                else 
                    alert(data["msg"]);
            });
        }
      };

    return (
        <div style={{width: props["screenWidth"], height: props["screenHeight"]}}>
            <h1 style={{marginTop: "2%"}}>{selectedStore} - Appoint Store Manager</h1>

            <div style={{marginLeft: "30%", marginRight: "30%", marginTop: "2%", border: "1px solid", borderColor: "#CCCCCC"}}>
                <div style={{marginLeft: "3%", marginRight: "3%"}} >
                    <Form.Label style={{ marginTop:"3%"}}>Enter subscriber's nickname to appoint as manager:</Form.Label>
                    <Form.Control id="subscriber-nickname" value={subscriberNickname} required type="text" placeholder="Subscriber's nickname" 
                        onChange={(event => {setSubscriberNickname(event.target.value)})}/>

                    <Form.Label style={{ marginTop:"3%"}}>Select permissions:</Form.Label>
                    
                    <div key={`inline-checkbox`} className="mb-3" style={{ border: "1px solid", borderColor: "#CCCCCC"}}>
                        <div style={{ marginLeft:"4%"}}>
                                  <Row><Form.Check style = {{position: "sticky"}} checked={permissions.includes(1)} label="Manage Stock" type="checkbox" id={`auction-purchase`} onChange={(event => {addPermissions(1)})} />
                            </Row><Row><Form.Check style = {{position: "sticky"}} checked={permissions.includes(2)} label="Manage Store policies" type="checkbox" id={`auction-purchase`} onChange={(event => {addPermissions(2)})} />
                            </Row><Row><Form.Check style = {{position: "sticky"}} checked={permissions.includes(3)} label="Appoint Additional Owner" type="checkbox" id={`lottery-purchase`} onChange={(event => {addPermissions(3)})}/>
                            </Row><Row><Form.Check style = {{position: "sticky"}} checked={permissions.includes(5)} label="Appoint Additional Manager" type="checkbox" id={`lottery-purchase`} onChange={(event => {addPermissions(5)})}/>
                            </Row><Row><Form.Check style = {{position: "sticky"}} checked={permissions.includes(6)} label="Edit Manager's Permissions" type="checkbox" id={`lottery-purchase`} onChange={(event => {addPermissions(6)})}/>
                            </Row><Row><Form.Check style = {{position: "sticky"}} checked={permissions.includes(7)} label="Remove Store Manager" type="checkbox" id={`lottery-purchase`} onChange={(event => {addPermissions(7)})}/>
                            </Row>
                        </div>
                    </div>
                </div>
            </div>
            <div style={{ marginTop:"3%"}}><Button type='reset' variant="dark" id="appoint-manager-button" disabled={subscriberNickname === ""} onClick={appointManagerHandler}>Commit</Button></div>
        </div>
    );
}


export default AppointStoreManager;