import React, {useState} from 'react';
import {Container, Row, Col, Button, Dropdown, Jumbotron, Form} from 'react-bootstrap'
import {Link} from 'react-router-dom'
import * as theService from '../../services/communication';
import SubscriberAPI from '../SubscriberRole/SubscriberAPI';


class OwnerAPI extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            ownedStores: [],
            selectedStore: ""
        }
        
      this.logoutHandler = this.logoutHandler.bind(this);
    }

    logoutHandler = async () =>{
        const promise = theService.logout(); // goes to register.js and sends to backend
        promise.then((data) => {
          alert(data["msg"]);
          // TODO: yarin  
            this.props.history.push("/");
        });
    };

    componentDidMount = () => {
        const promise = theService.fetchOwnedStores();  // goes to communication.js and sends to server
        promise.then((data) => {
            if(data != null){
                if (data["data"].length > 0){   // if there are owned stores
                    this.setState({ownedStores: data["data"], selectedStore: data["data"][0]})
                }
                else{
                    alert([data["msg"]]);       // no owned stores, array is empty
                }
            }
        });
    }

    render(){
        return(
            <Container style={{width: this.props["screenWidth"], height: this.props["screenHeight"]}}>
                <Jumbotron fluid>
                    <Row>
                        <Col />
                        <Col xs={7}>
                            <h1 style={{textAlign: "center"}}>Welcome Dear Owner!</h1>
                        </Col>
                        <Col>
                        <Link to='/logout'>
                            <Button variant="dark" id="logout" onClick={this.logoutHandler}>Logout</Button>
                        </Link>
                        </Col>
                    </Row>
                </Jumbotron>
                
                <Form.Group controlId="stores_ControlSelect2" onChange={ event => {this.setState({selectedStore: event.target.value})}}>
                <Form.Label>Please choose a store:</Form.Label>
                <Form.Control as="select">
                    {/* <option value={""} >Select Store</option> */}
                    {this.state.ownedStores.map(store => (
                        <option value={store}>{store}</option>
                    ))}
                </Form.Control>
                </Form.Group>
    
                {/*
                    need options for:
                    // for guest only
                    1. register - > now button -> redirect to ./register -> ok
                    2. login - > now button -> redirect to ./login -> ok 

                    // guest and up
                    3. display stores and products info, display stores ->  redirect to ./stores
                    4. search products by + filter products by -> in navbar
                    5. save products to basket -> in shopping cart
                    6. view and update shopping cart -> in shopping cart

                    // subscriber and up
                    7. purchase shopping cart -> in shopping cart
                    8. open store
                    9. view personal purchase history
                    10. logout - > now button -> redirect to ./login -> ok

                    // shop owner and up
                    11. manage stock
                    12. appoint owner
                    13. appoint manager
                    14. edit permissions
                    15. remove manager
                    16. view store history
                    17. manage store
                */}

                <Row>
                    <Button variant="secondary" size="lg" block as={Link} to="/stores">
                        Display Stores And Products Information
                    </Button>
    
                    <Button variant="secondary" size="lg" block as={Link} to="/openstore">
                        Open Store
                    </Button>
    
                    <Button variant="secondary" size="lg" block as={Link} to="/history">
                        View Personal Purchase History
                    </Button>

                    <Button variant="secondary" size="lg" block as={Link} to={{pathname: "/manageinventory/" + this.state.selectedStore, 
                                                                               store: this.state.selectedStore, props: this.props}} >
                        Manage Inventory
                    </Button>

                    <Button variant="secondary" size="lg" block as={Link} to={{pathname: "/appointowner", 
                                                                               store: this.state.selectedStore, props: this.props}}>
                        Appoint Additional Owner
                    </Button>
                    <Button variant="secondary" size="lg" block as={Link} to={{pathname: "/removeowner", 
                                                                               store: this.state.selectedStore, props: this.props}}>
                        Remove Owner
                    </Button>

                    <Button variant="secondary" size="lg" block as={Link} to={{pathname: "/appointmanager", 
                                                                               store: this.state.selectedStore, props: this.props}}>
                        Appoint Additional Manager
                    </Button>

                    <Button variant="secondary" size="lg" block as={Link} to={{pathname: "/editpermissions", 
                                                                               store: this.state.selectedStore, props: this.props}}>
                        Edit Manager’s Permissions
                    </Button>

                    <Button variant="secondary" size="lg" block as={Link} to={{pathname: "/removemanager", 
                                                                               store: this.state.selectedStore, props: this.props}}>
                        Remove A Store Manager
                    </Button>

                    <Button variant="secondary" size="lg" block as={Link} to={{pathname: "/storehistory", 
                                                                             store: this.state.selectedStore, props: this.props}}>
                        View Store’s Purchase History
                    </Button>

                    <Button variant="secondary" size="lg" block as={Link} to={{pathname: "/managestorepolicies", 
                                                                               store: this.state.selectedStore, props: this.props}}>
                        Manage Store Policies
                    </Button>

                    <Button variant="secondary" size="lg" block as={Link} to="/notifications">
                        Notifications
                    </Button>

                </Row>
            </Container>
            
        );
    }
    

}

export default OwnerAPI;