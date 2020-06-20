import React, {useState, useEffect} from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import {Button, Form, Row} from 'react-bootstrap'
import * as theService from '../../services/communication';
import * as BackOption from '../Actions/GeneralActions/Back'

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
          <Form>
          <fieldset>

            <div style={{marginLeft: "30%", marginRight: "30%", marginTop: "2%"}}>
                <Form.Label>Enter subscriber's nickname to appoint as owner:</Form.Label>
                <Form.Control id="subscriber-nickname" value={subscriberNickname} required type="text"  placeholder="Subscriber's nickname" 
                onChange={(event => {setSubscriberNickname(event.target.value)})}/>
                
            </div>
            </fieldset>

            <div style={{marginTop:"1%" , marginLeft: "25%", marginRight: "25%"}}>
                 <Form.Group as={Row} style={{marginRight:"10%" , marginLeft: "10%"}}>
                 <div><Button  type='reset' variant="dark" disabled={subscriberNickname === ""} id="appoint-manager-button" onClick={appointOwnerHandler}>Commit</Button></div>
                 <div style={{marginLeft:"1%"}}> <Button  variant="dark" id="back-btn" onClick={event => BackOption.BackToHome(props)}>Back</Button></div>
                 </Form.Group>
            
            </div>
            </Form>
        </div>
    );
}

export default AppointOwner;