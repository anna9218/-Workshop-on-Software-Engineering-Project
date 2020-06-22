import React, {useState, useEffect} from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import {Button, Form, Row} from 'react-bootstrap'
import * as theService from '../../services/communication';
import { confirmAlert } from 'react-confirm-alert'; 

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
                if(data["data"] ){
                    confirmAlert({
                        title: data["msg"],
                        buttons: [
                            {   label: 'Appoint another owner',
                                onClick: () => { // reset the form in order to add another product
                                setSubscriberNickname("");

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
            <h2 style={{marginTop: "2%"}}>{selectedStore} - Appoint Store Owner</h2>
            <Form>
                <div style={{marginLeft: "30%", marginRight: "30%", marginTop: "2%" , border: "1px solid", borderColor: "#CCCCCC"}}>
                    <Form.Label style={{marginTop: "2%"}}>Enter subscriber's nickname to appoint as owner:</Form.Label>
                    <div style={{marginTop: "2%", marginLeft: "3%", marginRight: "3%", marginBottom:"3%"}}>
                        <Form.Control id="subscriber-nickname" value={subscriberNickname} required type="text"  placeholder="Subscriber's nickname" 
                                                                    onChange={(event => {setSubscriberNickname(event.target.value)})}/>
                    </div>
                    
                </div>
                <div style={{marginTop:"2%"}}>
                    <Button type='reset' variant="dark" disabled={subscriberNickname === ""} id="appoint-manager-button" onClick={appointOwnerHandler}>Commit</Button>
                </div>
            </Form>
        </div>
    );
}

export default AppointOwner;