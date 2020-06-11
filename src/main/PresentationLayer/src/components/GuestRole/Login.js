import React from 'react';
import {Container, Button, Jumbotron, Form} from 'react-bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css';
import {BrowserRouter as Router, Switch, Route, Link} from 'react-router-dom'
import * as theService from '../../services/communication';


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

  // componentWillUnmount = () =>{

  // }

  handleLogin = event =>{
    event.preventDefault();
        const promise = theService.login(this.state.nickname, this.state.password) // goes to register.js and sends to backend
        promise.then((data) => {
          let is_manager = data["msg"] === "SYS_MANAGER";
          if(!is_manager){
            alert(data["msg"]);
          }
          if(data["data"]){ // if logged in
              if(is_manager){
                // if system manager - redirect to system manager home page
                this.props.history.push({pathname: '/systemmanager', props: this.props});
              }
              else{
                const userType = theService.getUserType();
                userType.then((data) => {
                  if(data["data"] === "OWNER"){
                    // if store owner - redirect to subscriber home page
                    this.props.history.push({pathname: '/owner', props: this.props});
                  }
                  else if(data["data"] === "MANAGER"){
                    // if store manager - redirect to subscriber home page
                    this.props.history.push({pathname: '/manager', props: this.props});
                  }
                  else{
                    // if subscriber - redirect to subscriber home page
                    this.props.history.push({pathname: '/subscriber', props: this.props});
                  }
                })
              }
            }
            else{
              // user didn't succeed to log in
              this.state.nickname = ''
              this.state.password = ''
              return;
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
      <div style={{width: this.props["screenWidth"], height: this.props["screenHeight"]}}>
        <h1>Login</h1>
        <form className='login'>
         <input id="email" type="text" name="email" placeholder="Email" value={this.state.email} onChange={this.handleEmailChange} />
             <input id="password" type="password" name="password" placeholder="Password" value={this.state.password} onChange={this.handlePasswordChange}/>
             <Link to='/'>
                 {/* <Button variant="dark" id="regbtn" onClick={this.handleLogin}>Login</Button> */}
             <button type="button" onClick={this.handleLogin}>
               Login
               </button>
             </Link>
         </form>
         <Button variant="secondary" style={{marginTop: "1%"}} as={Link} to="./register">
                Register
          </Button>
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
