import React, {useState} from 'react';
import {Container, Row, Col, Button, Dropdown, Jumbotron, Form} from 'react-bootstrap'
import {Link} from 'react-router-dom'
import * as theService from '../../services/communication';
import SubscriberAPI from '../SubscriberRole/SubscriberAPI';



//---------- WHAT AN OWNER CAN DO? ----------//
// Guest actions 
// Subscriber actions - Logout, Open store, View personal purchase history
// Manage stock (4.1) 
// (4.2)
// Appoint additional owner (4.3)
// Appoint additional manager (4.5)
// Edit manager’s permissions (4.6)
// Remove a store manager (4.7)
// View store’s purchase history (4.10)

// Manage store (5.1) (MANAGER)


class OwnerAPI extends React.Component {
    constructor(props) {
        super(props);
  
      this.logoutHandler = this.logoutHandler.bind(this);
    }

    logoutHandler = async () =>{
        const promise = theService.logout(); // goes to register.js and sends to backend
        promise.then((data) => {
          alert(data["msg"]);
            this.props.history.push("/");
        });
    };

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

                    <Button variant="secondary" size="lg" block as={Link} to="/manageinventory">
                        Manage Stock
                    </Button>

                    <Button variant="secondary" size="lg" block as={Link} to="/appointowner">
                        Appoint Additional Owner
                    </Button>

                    <Button variant="secondary" size="lg" block as={Link} to="/appointmanager">
                        Appoint Additional Manager
                    </Button>

                    <Button variant="secondary" size="lg" block as={Link} to="/editpermissions">
                        Edit Manager’s Permissions
                    </Button>

                    <Button variant="secondary" size="lg" block as={Link} to="/removemanager">
                        Remove A Store Manager
                    </Button>

                    <Button variant="secondary" size="lg" block as={Link} to="/storehistory">
                        View Store’s Purchase History
                    </Button>

                    <Button variant="secondary" size="lg" block as={Link} to="/managestore">
                        Manage Store
                    </Button>
                </Row>
            </Container>
            
        );
    }
    

}

export default OwnerAPI;