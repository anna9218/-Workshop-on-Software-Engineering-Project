import React, {useState} from 'react';
import {browserHistory} from 'react-router';
import {Container, Button, Form, Row, Col} from 'react-bootstrap'
import * as theService from '../../services/communication';
import {Link, useHistory, Redirect} from 'react-router-dom';
import * as BackOption from '../Actions/GeneralActions/Back';
import { confirmAlert } from 'react-confirm-alert'; 


class RegisterForm extends React.Component{
    constructor(props) {
        super(props);
        this.state = {
            nickname: '',
            password: '',
        };

        this.handleRegister = this.handleRegister.bind(this);
        this.handleEmailChange = this.handleEmailChange.bind(this);
        this.handlePasswordChange = this.handlePasswordChange.bind(this);
      }

    handleRegister = event =>{
        event.preventDefault();
        const promise = theService.register(this.state.nickname, this.state.password) // goes to register.js and sends to backend
        promise.then((data) => {
            if(data['data']){
                confirmAlert({
                    title: data["msg"],
                    buttons: [
                        {   label: 'Register',
                            onClick: () => { // reset the form in order to add another product
                                this.setState({nickname: ''});
                                this.setState({password: ''});
                        }},
                        {
                            label: 'Login',
                            onClick: () => {
                                this.props.history.push("./login")}
                        }
                    ]
                });
            }
            else alert(data["msg"])
        })
    }

    handleEmailChange(event){
        this.setState({nickname: event.target.value});
    }

    handlePasswordChange(event){
        this.setState({password: event.target.value});
    }
        
    render(){
        return (
            <div style={{width: this.props["screenWidth"], height: this.props["screenHeight"]}}>
            <div style={{marginTop:"1%"}}>
                <h2>Registration </h2>
            </div>
            <div style={{marginTop:"0.5%" , marginLeft: "25%", marginRight: "25%", border: "1px solid", borderColor: "#CCCCCC"}}>
                <Form >
                    <fieldset>
                        <Form.Group as={Row} >
                            <Form.Label as="legend" column sm={6}>
                                Please enter a unique nickname and password:
                            </Form.Label>
                           <Form.Control style={{marginRight:"3%" , marginLeft: "3%"}} type="text" id="email" name="email" placeholder="Nickname" value={this.state.nickname} onChange={this.handleEmailChange} />
                            <Form.Control style={{marginTop:"1%", marginRight:"3%" , marginLeft: "3%"}} type="password" id="password" name="password" placeholder="Password" value={this.state.password} onChange={this.handlePasswordChange}/>
                        </Form.Group>
                    </fieldset>
                    <Form.Group as={Row} style={{marginRight:"1%" , marginLeft: "1%"}}>
                        <Button type="reset" variant="dark" disabled={this.state.email === "" | this.state.password === ""} onClick={this.handleRegister} to='/'>Register</Button>

                    </Form.Group>
                </Form>
            </div>
            <div style={{marginTop:"1%" , marginLeft: "25%", marginRight: "25%"}}>
                <Form >
                    <Form.Group as={Row} style={{marginRight:"1%" , marginLeft: "1%"}}>
                    <div><Button variant="dark" as={Link} to="./login">Login</Button></div>
                    {/* <div style={{marginLeft:"1%"}}> <Button variant="dark" id="back-btn" onClick={event => BackOption.BackToHome(this.props)}>Back</Button></div> */}
                    </Form.Group>
                </Form>
            </div>

        </div>

            
        );
    }
}

export default RegisterForm;



