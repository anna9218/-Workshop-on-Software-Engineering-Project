import React, {useState} from 'react';
import {browserHistory} from 'react-router';
import {Container, Button, Form} from 'react-bootstrap'
import * as registerService from '../../services/register';
import {Link, useHistory, Redirect} from 'react-router-dom'

// function RegisterForm(){
//     useEffect(() => {
//         setCount(count + 1);
//         fetchStores();
//       }, []);

    
//     const [count, setCount] = useState(1);
// }


class RegisterForm extends React.Component{
    constructor(props) {
        super(props);
        // this.emailEl = React.createRef();
        // this.passwordEl = React.createRef();
        this.state = {
            nickname: '',
            password: '',
            // history: useHistory(),
        };
        // this.nickname='';
        // this.password='';
        this.handleRegister = this.handleRegister.bind(this);
        this.handleEmailChange = this.handleEmailChange.bind(this);
        this.handlePasswordChange = this.handlePasswordChange.bind(this);
      }

    handleRegister = event =>{
        event.preventDefault();
        const promise = registerService.register(this.state.nickname, this.state.password) // goes to register.js and sends to backend
        promise.then((data) => {alert(data["msg"])})
        // alert("msg")
        // this.state.history.push("/");
        // browserHistory.push('/');


        //   <Route>
        //       <Redirect to={{
        //     pathname: '/login',
        //     search: '?utm=your+face',
        //     state: { referrer: currentLocation }
        //   }}/>

        // <Redirect to="/"/>
        // TODO - redirect to other page

        // if (result.status == 200){
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
            <h1>Registration</h1>
            <form className='register'>
              <input type="text" id="email" name="email" placeholder="Email" value={this.state.email} onChange={this.handleEmailChange} />
              <input type="password" id="password" name="password" placeholder="Password" value={this.state.password} onChange={this.handlePasswordChange}/>
              <Link to='/'>
                 {/* <Button variant="dark" id="regbtn">Register</Button> */}
              <button type="button" onClick={this.handleRegister}>Register</button>
              </Link>
            </form>




            {/* <Container>
            <Form onSubmit={this.handleRegister}>
            <Form.Group controlId="formBasicEmail">
                <Form.Label>Email address</Form.Label>
                <Form.Control inputRef={nickname => this.state.nickname = nickname} type="email" placeholder="Enter email" />
                <Form.Text className="text-muted">
                We'll never share your email with anyone else.
                </Form.Text>
            </Form.Group>

            <Form.Group controlId="formBasicPassword">
                <Form.Label>Password</Form.Label>
                <Form.Control inputRef={password => this.state.password = password} type="password" placeholder="Password" />
                <Form.Text className="text-muted">
                Password must contain at least 6 characters.
                </Form.Text>
            </Form.Group>
            <Form.Group controlId="formBasicCheckbox">
                <Form.Check type="checkbox" label="I accept the terms and conditions" />
            </Form.Group>
            <Button variant="primary" type="submit">
                Register
            </Button>
            </Form>
            </Container> */}
            </div>
        );
    }
}

export default RegisterForm;



