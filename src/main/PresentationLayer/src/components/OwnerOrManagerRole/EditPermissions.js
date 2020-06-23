import React, {useState, useEffect} from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import {Container, Button, Form, Row} from 'react-bootstrap'
import * as theService from '../../services/communication';
import { confirmAlert } from 'react-confirm-alert'; 


function EditPermissions(props){
    useEffect(() => {
        setSelectedStore(props.location.store)
        fetchManagersAppointees();
    }, []);

    const [selectedStore, setSelectedStore] = useState("");
    const [subscriberNickname, setSubscriberNickname] = useState("Select manager");
    const [permissions, setPermissions] = useState([10]);
    const [managers, setManagers] = useState(["No managers were appointed by you..."]);

    const fetchManagersAppointees = async () => {
        const promise = theService.fetchManagersAppointees(props.location.store);  // goes to communication.js and sends to server
        promise.then((data) => {
            if (data["data"].length > 0){   // if there are owned stores
                setManagers(data["data"]);
                setSubscriberNickname(data["data"][0]);
            }
        });
    };

    const addPermissions = async (permission) => {
        if(permissions.includes(permission))
            permissions.splice(permissions.indexOf(permission), 1)
        else setPermissions(permissions.concat([permission]));
    };

    const appointManagerHandler = async () =>{
        if(managers[0] === "No managers were appointed by you..."){
            alert("No managers were appointed by you...");
        }
        else if(subscriberNickname === "" || subscriberNickname === "Select manager"){
            alert("Please enter subscriber's nickname to appoint");
        }
        else{
            const promise = theService.editManagerPermissions(selectedStore, subscriberNickname, permissions);
            promise.then((data) => {
                if(data["data"]){
                    confirmAlert({
                        title: data["msg"],
                        buttons: [
                            {   label: 'Edit permissions',
                                onClick: () => { // reset the form in order to add another product
                                    setPermissions([10])
                                    fetchManagersAppointees();
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
          <h2 style={{marginTop:"2%"}}>{selectedStore} - Update Manager's Permissions</h2>

          <div style={{marginLeft: "30%", marginRight: "30%", marginTop: "2%" ,border: "1px solid", borderColor: "#CCCCCC"}}>
            <div style={{marginLeft: "3%", marginRight: "3%"}}>
                <Form.Group controlId="managers_appointees" onChange={ event => {setSubscriberNickname(event.target.value)}}>
                <Form.Label style={{marginTop:"2%"}}>Please choose a manager:</Form.Label>
                <Form.Control as="select">
                    <option>Select manager</option>
                    {managers.map(nickname => (
                        <option value={nickname}>{nickname}</option>
                    ))}
                </Form.Control>
                </Form.Group>

                <Form.Label>Select permissions:</Form.Label>
                
                <div>
                <div key={`inline-checkbox`} className="mb-3" style={{border: "1px solid", borderColor: "#CCCCCC"}}>
                <div style={{ marginLeft:"4%"}}>
                    <Row><Form.Check style = {{position: "sticky"}}       checked={permissions.includes(1)}  label="Manage Stock" type="checkbox" id={`auction-purchase`} onChange={(event => {addPermissions(1)})} />
                    </Row><Row><Form.Check style = {{position: "sticky"}} checked={permissions.includes(2)} label="Manage Store policies" type="checkbox" id={`auction-purchase`} onChange={(event => {addPermissions(2)})} />
                    {/* </Row><Row><Form.Check style = {{position: "sticky"}} checked={permissions.includes(3)} label="Appoint Additional Owner" type="checkbox" id={`lottery-purchase`} onChange={(event => {addPermissions(3)})}/> */}
                    </Row><Row><Form.Check style = {{position: "sticky"}} checked={permissions.includes(5)} label="Appoint Additional Manager" type="checkbox" id={`lottery-purchase`} onChange={(event => {addPermissions(5)})}/>
                    </Row><Row><Form.Check style = {{position: "sticky"}} checked={permissions.includes(6)} label="Edit Manager's Permissions" type="checkbox" id={`lottery-purchase`} onChange={(event => {addPermissions(6)})}/>
                    </Row><Row><Form.Check style = {{position: "sticky"}} checked={permissions.includes(7)} label="Remove Store Manager" type="checkbox" id={`lottery-purchase`} onChange={(event => {addPermissions(7)})}/>
                    </Row>
                    </div>
                </div>
                </div>

                
                <Container> 
                </Container>

                </div>
            </div>
    
            <Form style={{marginTop:"3%"}} >
                <div><Button variant="dark" id="appoint-manager-button" onClick={appointManagerHandler}>Commit</Button></div>
            </Form>
        </div>
    );
}


export default EditPermissions;