import React, {useState, useEffect} from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import {Container, Button, Form} from 'react-bootstrap'
import * as theService from '../../services/communication';

function AppointOwner(props){
    useEffect(() => {
        setSelectedStore(props.location.store)

    }, []);

    const [selectedStore, setSelectedStore] = useState("");
    const [subscriberNickname, setSubscriberNickname] = useState("");

    const appointOwnerHandler = async () =>{
        if(subscriberNickname === ""){
            alert("Please enter subscriber's nickname to appoint");
            
        }
        else{
            const promise = theService.appointStoreOwner(subscriberNickname, selectedStore);
            promise.then((data) => {
                alert(data["msg"]);
                if(data["response"])
                setSubscriberNickname("");
            });
        }
      };

    return (
        <div style={{width: props["screenWidth"], height: props["screenHeight"]}}>
          <h2>{selectedStore} - Appoint Store Owner</h2>
            <div style={{marginLeft: "30%", marginRight: "30%", marginTop: "2%"}}>
                <Form.Label>Enter subscriber's nickname to appoint as owner:</Form.Label>
                <Form.Control id="subscriber-nickname" value={subscriberNickname} required type="text"  placeholder="Subscriber's nickname" 
                onChange={(event => {setSubscriberNickname(event.target.value)})}/>
                <div style={{margintop: "5%"}}>
                <Button  variant="dark" id="appoint-manager-button" onClick={appointOwnerHandler}>Commit</Button>
                </div>
            </div>
        </div>
    );
}

export default AppointOwner;