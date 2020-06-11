import React, {useState, useEffect} from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import {Container, Button, Form} from 'react-bootstrap'
import * as theService from '../../services/communication';

function RemoveManager(props){
    useEffect(() => {
        setSelectedStore(props.location.store);
        fetchManagersAppointees();
    }, []);

    const [selectedStore, setSelectedStore] = useState("");
    const [subscriberNickname, setSubscriberNickname] = useState("");
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

    const removeManagerHandler = async () =>{
        if(managers[0] === "No managers were appointed by you..."){
            alert("No managers were appointed by you...");
        }
        else{
            const promise = theService.removeManager(selectedStore, subscriberNickname);
            promise.then((data) => {
                alert(data["msg"]);

                // reset feilds
                setSelectedStore(selectedStore);
                setSubscriberNickname("");
                fetchManagersAppointees();
            });
        }
        
      };

    return (
        <div style={{width: props["screenWidth"], height: props["screenHeight"]}}>
          <h2>{selectedStore} - Remove Store Manager</h2>
          <div style={{marginLeft: "30%", marginRight: "30%" , marginTop: "2%"}}>
            <Form.Group controlId="managers_appointees" onChange={ event => {setSubscriberNickname(event.target.value)}}>
            <Form.Label>Please choose a manager to remove:</Form.Label>
            <Form.Control as="select">
                {managers.map(nickname => (
                    <option value={nickname}>{nickname}</option>
                ))}
            </Form.Control>
            </Form.Group>


            <Container> 
                <Button variant="dark" id="appoint-manager-button" onClick={removeManagerHandler}>Commit</Button>
            </Container>
            </div>
        </div>
    );
}

export default RemoveManager;