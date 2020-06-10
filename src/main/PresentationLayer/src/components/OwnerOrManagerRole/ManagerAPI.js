// import React, {useState} from 'react';
// import {Container, Row, Col, Button, Dropdown, Jumbotron, Form} from 'react-bootstrap'
// import {Link} from 'react-router-dom'
// import * as theService from '../../services/communication';
// import SubscriberAPI from '../SubscriberRole/SubscriberAPI';



// //---------- WHAT AN OWNER CAN DO? ----------//
// // Guest actions 
// // Subscriber actions - Logout, Open store, View personal purchase history
// // Manage stock (4.1) 
// // (4.2)
// // Appoint additional owner (4.3)
// // Appoint additional manager (4.5)
// // Edit manager’s permissions (4.6)
// // Remove a store manager (4.7)
// // View store’s purchase history (4.10)

// // Manage store (5.1) (MANAGER)


// class ManagerAPI extends React.Component {
//     constructor(props) {
//         super(props);
  
//       this.state = {
//         stores: []
//         permissions: []
//       }
//       this.setStores = this.setStores.bind(this);
//       this.setPermissions = this.setPermissions.bind(this);
//       this.logoutHandler = this.logoutHandler.bind(this);
//     }

//     setStores = async (stores) =>{
//       this.state.stores = stores; 
//     }

//     setPermissions = async (permissions) =>{
//       this.state.setPermissions = permissions; 
//     }

//     logoutHandler = async () =>{
//         const promise = theService.logout(); // goes to register.js and sends to backend
//         promise.then((data) => {
//           alert(data["msg"]);
//             this.props.history.push("/");
//         });
//     };

    
//     // this function automatically occures once the window opens
//     componentWillMount = async () =>{
//       const promise = theService.fetchManagedStores();  // goes to communication.js and sends to server
//       promise.then((data) => {
//           this.setStores(data["data"]);
//       });

//       const promise = theService.fetchManagedStores();  // goes to communication.js and sends to server
//       promise.then((data) => {
//           this.setStores(data["data"]);
//       });
//     }

//     render(){
//         return(
//             <Container style={{width: this.props["screenWidth"], height: this.props["screenHeight"]}}>
//                 <Jumbotron fluid>
//                     <Row>
//                         <Col />
//                         <Col xs={7}>
//                             <h1 style={{textAlign: "center"}}>Welcome Dear Store Manager!</h1>
//                         </Col>
//                         <Col>
//                         <Link to='/logout'>
//                             <Button variant="dark" id="logout" onClick={this.logoutHandler}>Logout</Button>
//                         </Link>
//                         </Col>
//                     </Row>
//                 </Jumbotron>
    
//                 {/*
//                     need options for:
//                     // for guest only
//                     1. register - > now button -> redirect to ./register -> ok
//                     2. login - > now button -> redirect to ./login -> ok 

//                     // guest and up
//                     3. display stores and products info, display stores ->  redirect to ./stores
//                     4. search products by + filter products by -> in navbar
//                     5. save products to basket -> in shopping cart
//                     6. view and update shopping cart -> in shopping cart

//                     // subscriber and up
//                     7. purchase shopping cart -> in shopping cart
//                     8. open store
//                     9. view personal purchase history
//                     10. logout - > now button -> redirect to ./login -> ok

//                     // shop owner and up
//                     11. manage stock
//                     12. appoint owner
//                     13. appoint manager
//                     14. edit permissions
//                     15. remove manager
//                     16. view store history
//                     17. manage store ploicies
//                 */}

//                 <Row>
//                     <div>
//                       {
//                         this.state.stores.map(store => (
//                         <option value={store}>{store}</option>
//                         ))}
//                     </div>
//                     <Button variant="secondary" size="lg" block as={Link} to="/stores">
//                         Display Stores And Products Information
//                     </Button>
    
//                     <Button variant="secondary" size="lg" block as={Link} to="/openstore">
//                         Open Store
//                     </Button>
    
//                     <Button variant="secondary" size="lg" block as={Link} to="/history">
//                         View Personal Purchase History
//                     </Button>

//                     {/* opptional actions for manager - according to his permissions */}
                          
//                     <Button variant="secondary" size="lg" block as={Link} to="/manageinventory">
//                         Manage Stock
//                     </Button>

//                     <Button variant="secondary" size="lg" block as={Link} to="/appointowner">
//                         Appoint Additional Owner
//                     </Button>

//                     <Button variant="secondary" size="lg" block as={Link} to="/appointmanager">
//                         Appoint Additional Manager
//                     </Button>

//                     <Button variant="secondary" size="lg" block as={Link} to="/editpermissions">
//                         Edit Manager’s Permissions
//                     </Button>

//                     <Button variant="secondary" size="lg" block as={Link} to="/removemanager">
//                         Remove A Store Manager
//                     </Button>

//                     <Button variant="secondary" size="lg" block as={Link} to="/storehistory">
//                         View Store’s Purchase History
//                     </Button>

//                     <Button variant="secondary" size="lg" block as={Link} to="/managestore">
//                         Manage Store
//                     </Button>
//                 </Row>
//             </Container>
//         );
//     }
    

// }

// export default ManagerAPI;

import React, {useState, useEffect} from 'react';
import {Container, Row, Col, Button, Dropdown, Jumbotron, Form} from 'react-bootstrap'
import {Link} from 'react-router-dom'
import * as theService from '../../services/communication';



//---------- WHAT A MANAGER CAN DO? ----------//
// Manage store (5.1) - according to the given permissions

//---------- EXISTING PERMISSIONS: -----------//
// EDIT_INV = 1
// EDIT_POLICIES = 2
// APPOINT_OWNER = 3
// DEL_OWNER = 4  # you can delete only the one's you appoint
// APPOINT_MANAGER = 5
// EDIT_MANAGER_PER = 6
// DEL_MANAGER = 7
// CLOSE_STORE = 8
// USERS_QUESTIONS = 9
// WATCH_PURCHASE_HISTORY = 10


// TODO - need to check permission and display matching buttons (??)

function ManagerAPI(props){
    useEffect(() => {
    // fetchPermissions();
  }, []);

  const [permissions, setPermissions] = useState([]); // to hold the fetched permissions


  // get the manager's permissions
  const fetchPermissions = async () => {
    const promise = theService.getManagerPermissions(); // goes to register.js and sends to backend
    promise.then((data) => {
        setPermissions(data["data"])
      // TODO - how do we get the permissions? need to think here
    });
  };



    return(

        // TODO - THINK HOW TO DISPLAY BUTTONS ACCORDING TO THE PERMISSIONS
        <Container style={{width: props["screenWidth"], height: props["screenHeight"]}}>
            <div>
                <h1>Welcome Dear Manager!</h1>
            </div>


            {/* <Link to='/managestore'>
                <Button variant="dark" id="manage_store">Manage store</Button>
            </Link> */}

        </Container>
    );

}

export default ManagerAPI;