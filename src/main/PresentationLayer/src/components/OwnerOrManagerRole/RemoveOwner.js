import React, {useState, useEffect} from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import {Button, Form, Row} from 'react-bootstrap'
import * as theService from '../../services/communication';
import * as BackOption from '../Actions/GeneralActions/Back'

function RemoveOwner(props){
    useEffect(() => {
        setSelectedStore(props.location.store);
        fetchOwnersAppointees();
    }, []);

    const [selectedStore, setSelectedStore] = useState("");
    const [subscriberNickname, setSubscriberNickname] = useState("");
    const [owners, setOwners] = useState(["No owners were appointed by you..."]);


    const fetchOwnersAppointees = async () => {
        const promise = theService.fetchOwnersAppointees(props.location.store);  // goes to communication.js and sends to server
        promise.then((data) => {
            if (data["data"].length > 0){   // if there are owned stores
                setOwners(data["data"]);
                setSubscriberNickname(data["data"][0]);
            }
            else {
                setOwners(["No owners were appointed by you..."])
            }
        });
    };

    const removeOwnerHandler = () =>{
        if(owners[0] === "No owners were appointed by you..."){
            alert("No owners were appointed by you...");

        }
        else{
            const promise = theService.removeOwner(selectedStore, subscriberNickname);
            promise.then((data) => {
                alert(data["msg"]);
                alert(data["data"]);
    
                // reset feilds
                setSelectedStore(selectedStore);
                setSubscriberNickname("");
                fetchOwnersAppointees();
            });
        }
        
      };

    return (
        <div style={{width: props["screenWidth"], height: props["screenHeight"]}}>
          <h2>{selectedStore} - Remove Store Owner</h2>
          <div style={{marginLeft: "30%", marginRight: "30%" , marginTop: "2%"}}>
            <Form.Group controlId="owners_appointees" onChange={ event => {setSubscriberNickname(event.target.value)}}>
            <Form.Label>Please choose a owner to remove:</Form.Label>
            <Form.Control as="select">
                {owners.map(nickname => (
                    <option value={nickname}>{nickname}</option>
                ))}
            </Form.Control>
            </Form.Group>

            <Form >
                 <Form.Group as={Row} style={{marginRight:"0%" , marginLeft: "0%"}}>
                 <div><Button variant="dark"  onClick={removeOwnerHandler}>Commit</Button></div>
                 {/* <div style={{marginLeft:"1%"}}> <Button style={{marginTop: "1%"}} variant="dark" id="back-btn" onClick={event => BackOption.BackToHome(props)}>Back</Button></div> */}
                 </Form.Group>
             </Form>
            </div>
           
        </div>
    );
}

export default RemoveOwner;