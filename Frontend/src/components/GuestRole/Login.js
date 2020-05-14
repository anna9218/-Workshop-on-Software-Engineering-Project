import React from 'react';
import {Container, Button, Jumbotron, Form} from 'react-bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css';
import {BrowserRouter as Router, Switch, Route, Link} from 'react-router-dom'
import * as registerService from '../../services/register';


class Login extends React.Component{
  constructor(props) {
    super(props);
    this.state = {
        nickname: '',
        password: '',
    };
    this.handleLogin = this.handleLogin.bind(this);
    this.handleEmailChange = this.handleEmailChange.bind(this);
    this.handlePasswordChange = this.handlePasswordChange.bind(this);
  }

  handleLogin = event =>{
    event.preventDefault();
        const promise = registerService.login(this.state.nickname, this.state.password) // goes to register.js and sends to backend
        promise.then((data) => {
          alert(data["msg"]);
          if(data["data"]){ // if logged in
              return;
              //TODO - redirect to other page
            }
            else{
              return;
              //TODO - redirect to other page
            }
        });
  }

  handleEmailChange(event){
    this.setState({nickname: event.target.value});
  }

  handlePasswordChange(event){
    this.setState({password: event.target.value});
  }

  render(){
    return (
      <div>
        <h1>Login</h1>
        <form>
         <input type="text" name="email" placeholder="Email" value={this.state.email} onChange={this.handleEmailChange} />
             <input type="password" name="password" placeholder="Password" value={this.state.password} onChange={this.handlePasswordChange}/>
             {/* <Link to='/'> */}
                 {/* <Button variant="dark" id="regbtn">Register</Button> */}
             <button type="button" onClick={this.handleLogin}>Login</button>
             {/* </Link> */}
         </form>
         </div>);
  }
}



        {/* <Container>
            <Form onSubmit={this.handleLogin}>
            <Form.Group controlId="formBasicEmail">
                <Form.Label>Email address</Form.Label>
                <Form.Control inputRef={nickname => this.state.nickname = nickname} type="email" placeholder="Enter email" />
            </Form.Group>

            <Form.Group controlId="formBasicPassword">
                <Form.Label>Password</Form.Label>
                <Form.Control inputRef={password => this.state.password = password} type="password" placeholder="Password" />
            </Form.Group>
            <Button variant="primary" type="submit">
                Login
            </Button>
            </Form>
          </Container> */}


export default Login;
