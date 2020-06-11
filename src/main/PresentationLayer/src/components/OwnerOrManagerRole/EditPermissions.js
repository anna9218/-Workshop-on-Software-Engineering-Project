import React, {useState, useEffect} from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import {Container, Button, Form} from 'react-bootstrap'
import * as theService from '../../services/communication';
import * as BackOption from '../Actions/GeneralActions/Back'


function EditPermissions(props){
    useEffect(() => {
        setSelectedStore(props.location.store)
        fetchManagersAppointees();
    }, []);

    const [selectedStore, setSelectedStore] = useState("");
    const [subscriberNickname, setSubscriberNickname] = useState("");
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
        setPermissions(permissions.concat(permission));
    };

    const appointManagerHandler = async () =>{
        if(subscriberNickname === ""){
            alert("Please enter subscriber's nickname to appoint");
        }
        else{
            const promise = theService.editManagerPermissions(selectedStore, subscriberNickname, permissions);
            promise.then((data) => {
                alert(data["msg"]);
            });
        }
      };

    return (
        <div style={{width: props["screenWidth"], height: props["screenHeight"]}}>
          <h2>{selectedStore} - Update Manager's Permissions</h2>

          <div style={{marginLeft: "30%", marginRight: "30%", marginTop: "2%"}}>
            <Form.Group controlId="managers_appointees" onChange={ event => {setSubscriberNickname(event.target.value)}}>
            <Form.Label>Please choose a manager:</Form.Label>
            <Form.Control as="select">
                {managers.map(nickname => (
                    <option value={nickname}>{nickname}</option>
                ))}
            </Form.Control>
            </Form.Group>

            {/* <Form.Control id="subscriber-nickname" value={subscriberNickname} required type="text" placeholder="Subscriber's nickname" 
                onChange={(event => {setSubscriberNickname(event.target.value)})}/> */}

            <Form.Label>Select permissions:</Form.Label>
            
            <div>
            <div key={`inline-checkbox`} className="mb-3" style={{border: "1px solid", borderColor: "#CCCCCC"}}>
              <Form.Check style = {{position: "sticky"}} label="Manage Stock" type="checkbox" id={`auction-purchase`} onChange={(event => {addPermissions(1)})} />
              <Form.Check style = {{position: "sticky"}}  label="Manage Store policies" type="checkbox" id={`auction-purchase`} onChange={(event => {addPermissions(2)})} />
              <Form.Check style = {{position: "sticky"}}  label="Appoint Additional Owner" type="checkbox" id={`lottery-purchase`} onChange={(event => {addPermissions(3)})}/>
              <Form.Check style = {{position: "sticky"}}  label="Appoint Additional Manager" type="checkbox" id={`lottery-purchase`} onChange={(event => {addPermissions(5)})}/>
              <Form.Check style = {{position: "sticky"}}  label="Edit Manager's Permissions" type="checkbox" id={`lottery-purchase`} onChange={(event => {addPermissions(6)})}/>
              <Form.Check style = {{position: "sticky"}}  label="Remove Store Manager" type="checkbox" id={`lottery-purchase`} onChange={(event => {addPermissions(7)})}/>
             </div>
             </div>
             <Container> 
                <Button variant="dark" id="appoint-manager-button" onClick={appointManagerHandler}>Commit</Button>
             </Container>

            </div>
  
            <Button style={{marginTop: "1%"}} variant="dark" id="back-btn" onClick={event => BackOption.BackToHome(props)}>Back</Button>
        </div>
    );
}


export default EditPermissions;