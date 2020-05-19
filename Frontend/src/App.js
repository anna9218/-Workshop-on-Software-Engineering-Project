import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import {Navbar, Nav,Form, FormControl,Button,  NavDropdown} from 'react-bootstrap';
import {BrowserRouter as Router, Switch, Route, Link} from 'react-router-dom'
import './App.css';

// import Nav from './components/Nav'
import GuestRoleAPI from './components/GuestRole/GuestRoleAPI'
import RegisterForm from './components/GuestRole/RegisterForm'
import Login from './components/GuestRole/Login'

import DisplayStores from './components/Actions/DisplayStores'
import DisplayProducts from './components/DisplayProducts'
import Search from './components/Search'
import ShoppingCart from './components/ShoppingCart'
import PurchaseProducts from './components/PurchaseProducts'
import StoreDetail from './components/StoreDetail'
import StoreProducts from './components/StoreProducts'
import SearchResults from './components/SearchResults'

import SubscriberAPI from './components/SubscriberRole/SubscriberAPI'
import OpenStore from './components/SubscriberRole/OpenStore'
import PersonalPurchaseHistory from './components/SubscriberRole/PersonalPurchaseHistory'

import OwnerAPI from './components/OwnerOrManagerRole/OwnerAPI'

import ManagerAPI from './components/OwnerOrManagerRole/ManagerAPI'


function App(){
  return (
    <Router>
      <div className="App">
        {/* Navigation Bar */}
        <Navbar bg="dark" variant="dark">
          <Navbar.Brand as={Link} to="/">Trade Control</Navbar.Brand>
          <Nav className="mr-auto">
            {/* <Nav.Link href="#home">Home</Nav.Link>
            <Nav.Link href="#features">Features</Nav.Link>
            <Nav.Link href="#pricing">Pricing</Nav.Link> */}
             <NavGuestDropDown/>
             <NavSubscriberDropDown/>
             <NavStoreOwnerDropDown/>
             <NavSystemManagerDropDown/>
             {/* <Nav.Link as={Link} to="/stores" >Stores</Nav.Link>
             <Nav.Link as={Link} to="/displayproducts" >Products</Nav.Link>
             <Nav.Link as={Link} to="/viewcart" >Shoping Cart</Nav.Link> */}

          </Nav>
          <Form inline>
            <FormControl type="text" placeholder="Search" className="mr-sm-2" />
            <Button variant="outline-info">Search</Button>
          </Form>
        </Navbar>
      <Switch>
        <Route path="/" exact component={GuestRoleAPI} />
        <Route path="/register" exact component={RegisterForm} />
        <Route path="/login" exact component={Login} />
        <Route path="/displayproducts" exact component={DisplayProducts} />
        <Route path="/stores" exact component={DisplayStores} />
        {/* <Route path="/search" exact component={Search} /> */}
        <Route path="/purchase" exact component={PurchaseProducts} />
        <Route path="/viewcart" exact component={ShoppingCart} />
        <Route path="/stores/:store" exact component={StoreDetail} />
        <Route path="/stores/:store/products" exact component={StoreProducts} />
        <Route path="/searchresults" exact component={SearchResults} />

        <Route path="/subscriber" exact component={SubscriberAPI} />
        <Route path="/openstore" exact component={OpenStore} />
        <Route path="/history" exact component={PersonalPurchaseHistory} />

        <Route path="/owner" exact component={OwnerAPI} />

        <Route path="/manager" exact component={ManagerAPI} />
        {/* <Route path="/history" exact component={PersonalPurchaseHistory} />
        <Route path="/history" exact component={PersonalPurchaseHistory} />
        <Route path="/history" exact component={PersonalPurchaseHistory} />
        <Route path="/history" exact component={PersonalPurchaseHistory} /> */}



      </Switch>
      </div>
    </Router>
  );
}

  const Home = () => (
    <div>
      <h1>Home Page</h1>
    </div>
  );

export default App;



function NavGuestDropDown(props){
  // return <NavDropdown style={{position: "absolute"}} id="basic-nav-dropdown" title={}
  //         <div>
  //            <NavDropdown.Item as={Link} to="/stores" >Stores</NavDropdown.Item>
  //            <NavDropdown.Item as={Link} to="/displayproducts" >Products</NavDropdown.Item>
  //            <NavDropdown.Item as={Link} to="/viewcart" >Shoping Cart</NavDropdown.Item>
  //         </div>
  //       </NavDropdown>
  return <NavDropdown id="basic-nav-dropdown" title="Guest">
          <div>
            <NavDropdown.Item as={Link} to="/stores" >Search Stores</NavDropdown.Item>
            <NavDropdown.Item as={Link} to="/displayproducts">Search Products</NavDropdown.Item>
            <NavDropdown.Item as={Link} to="/viewcart" >Shoping Cart</NavDropdown.Item>
            {/* <NavDropdown.Item as={Link} to="/PurchaseProducts" >Purchase Products</NavDropdown.Item> */}
          </div>
         </NavDropdown>
}

function NavSubscriberDropDown(props){
  return <NavDropdown id="basic-nav-dropdown" title="Subscriber">
          <div>
            <NavDropdown.Item as={Link} to="/openstore">Open Store</NavDropdown.Item>
            <NavDropdown.Item as={Link} to="/history" >Personal Purchase History</NavDropdown.Item>
          </div>
         </NavDropdown>
}

function NavStoreOwnerDropDown(props){
  return <NavDropdown id="basic-nav-dropdown" title="Store Owner">
          <div>
            <NavDropdown.Item as={Link} to="/stores" >Manage Inventory</NavDropdown.Item>
            <NavDropdown.Item as={Link} to="/displayproducts" >Manage Policies</NavDropdown.Item>
            <NavDropdown.Item as={Link} to="/displayproducts" >Appoint Store Manager</NavDropdown.Item>
          </div>
         </NavDropdown>
}

function NavSystemManagerDropDown(props){
  return <NavDropdown id="basic-nav-dropdown" title="System Manager">
          <div>
            <NavDropdown.Item as={Link} to="/stores" >View Purchases History</NavDropdown.Item>
          </div>
         </NavDropdown>
}


  // // calls the fetch function
  // componentDidMount() {
  //   this.callBackendAPI().then(res => this.setState({ data: res.express })).catch(err => console.log(err));
  // }

  // callBackendAPI = async () => {
  //   const response = await fetch("/express_backend");
  //   const body = await response.json();

  //   if(response.status !== 200){
  //     throw Error(body.message);
  //   }
  //   return body;
  // }


