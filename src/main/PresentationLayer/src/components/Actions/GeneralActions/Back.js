import React, {useState, useEffect} from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import { BrowserRouter} from 'react-router-dom'
import {Container, Button, Form} from 'react-bootstrap'
import * as theService from '../../../services/communication';
import 'react-confirm-alert/src/react-confirm-alert.css'; // Import css



export function BackToHome(props){
    // const history = BrowserRouter.browserHistory
    alert(props)
    const promise = theService.getUserType().then((data) => {
      alert(props)

        if(data !== undefined){
            if(data["data"] === "OWNER"){
                // return to subscriber home page
                props.history.push({pathname: '/owner', props: props});
              }
              else if(data["data"] === "MANAGER"){
                // return to subscriber home page
                    props.history.push({pathname: '/manager', props: props});
              }
              else if(data["data"] === "SUBSCRIBER"){
                // return to subscriber home page
                props.history.push({pathname: '/subscriber', props: props});
              }
              else if(data["data"] === "SYS-MANAGER"){
                props.history.push({pathname: '/systemmanager', props: props});
              }
              else{
                  // return to guest home screen
                  props.history.push({pathname: '/', props: props});
              }
        }
    })
}

export default BackToHome;