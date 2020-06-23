import React, {useState, useEffect} from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import {Button, Form, Row} from 'react-bootstrap'
import * as theService from '../../services/communication';
import { confirmAlert } from 'react-confirm-alert'; 
 
import store from './OwnerAPI';


class AppointOwner extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            selectedStore: props.location.store,
            subscriberNickname: ""
        }
        
        // this.setPermissions = this.setPermissions.bind(this);
        this.appointOwnerHandler = this.appointOwnerHandler.bind(this);
    }

    // this function automatically occures once the window opens
    // componentDidMount = () => {
    //     const promise = theService.fetchManagedStores();  // goes to communication.js and sends to server
    //     promise.then((data) => {
    //         if(data != null){
    //             if (data["data"].length > 0){   // if there are owned stores
    //                 this.setState({managedStores: data["data"], store: data["data"][0]})
    //                 const promise2 = theService.fetchManagerPermissions(this.state.store);  // goes to communication.js and sends to server
    //                 promise2.then((data) => {
    //                     this.setState({permissions: data["data"]});
    //                 });
    //             }
    //             else{
    //                 alert([data["msg"]]);       // no owned stores, array is empty
    //             }
    //         }
    //     });

    // }
    setSubscriberNickname = (nickname) =>{
        this.setState({subscriberNickname: nickname})
    }
    
    appointOwnerHandler = async () =>{
        if(this.state.subscriberNickname === ""){
            alert("Please enter subscriber's nickname to appoint");
        }
        else{
            const promise = theService.appointStoreOwner(this.state.subscriberNickname, this.state.selectedStore);
            promise.then((data) => {
                if(data["data"] ){
                    confirmAlert({
                        title: data["msg"],
                        buttons: [
                            {   label: 'Appoint another owner',
                                onClick: () => { // reset the form in order to add another product
                                this.setSubscriberNickname("");

                            }},
                            {
                                label: 'Back',
                                onClick: () => {
                                    this.props.history.push("./owner")
                            }}
                        ]
                    });
                }
                else 
                    alert(data["msg"]);
            });
        }
      };

    render(){
        return(
            <div style={{width: this.props["screenWidth"], height: this.props["screenHeight"]}}>
                <h2 style={{marginTop: "2%"}}>{this.state.selectedStore} - Appoint Store Owner</h2>
                <Form>
                    <div style={{marginLeft: "30%", marginRight: "30%", marginTop: "2%" , border: "1px solid", borderColor: "#CCCCCC"}}>
                        <Form.Label style={{marginTop: "2%"}}>Enter subscriber's nickname to appoint as owner:</Form.Label>
                        <div style={{marginTop: "2%", marginLeft: "3%", marginRight: "3%", marginBottom:"3%"}}>
                            <Form.Control id="subscriber-nickname" value={this.state.subscriberNickname} required type="text"  placeholder="Subscriber's nickname" 
                                                                        onChange={(event => {this.setSubscriberNickname(event.target.value)})}/>
                        </div>
                        
                    </div>
                    <div style={{marginTop:"2%"}}>
                        <Button type='reset' variant="dark" disabled={this.state.subscriberNickname === ""} id="appoint-manager-button" onClick={this.appointOwnerHandler}>Commit</Button>
                    </div>
                </Form>
            </div>
        );
    }
    

}

export default AppointOwner;


