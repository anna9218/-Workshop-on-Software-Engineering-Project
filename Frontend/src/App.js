import React, {useState} from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import {Navbar, Nav,Form, FormControl, Button,  NavDropdown, Dropdown} from 'react-bootstrap';
import {BrowserRouter as Router, Switch, Route, Link} from 'react-router-dom'
import './App.css';
import * as theService from './services/communication';


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

import PurchaseHistoryUsersStores from './components/SystemManagerRole/PurchaseHistoryUsersStores'


function App(){

  const [searchOption, setSearchOption] = useState(0);
  const [searchInput, setSearchInput] = useState('');
  const [categories, setCategories] = useState([]);

  const byNameHandler = () =>{
      setSearchOption(1);
  };
  const byKeywordHandler = () =>{
      setSearchOption(2);
  };
  const byCategoryHandler = (input) =>{
      setSearchOption(3);
      setSearchInput(input);
  };
  const searchInputHandler = (event) =>{
      setSearchInput(event.target.value);
  };

  // for the search functionality
  const fetchCategories = async () =>{
      const promise = theService.getCategories(); // goes to register.js and sends to backend
  promise.then((data) => {setCategories(data["data"])});
  };








  return (
    <Router>
      <div className="App">
        {/* Navigation Bar */}
        <Navbar id="navbar" bg="dark" variant="dark">
          <Navbar.Brand as={Link} id="navbar-logo" to="/">Trade Control</Navbar.Brand>
          <Nav id="navbar-nav" className="mr-auto">
            {/* <Nav.Link href="#home">Home</Nav.Link>
            <Nav.Link href="#features">Features</Nav.Link>
            <Nav.Link href="#pricing">Pricing</Nav.Link> */}
             <NavGuestDropDown/>
             <NavSubscriberDropDown/>
             <NavStoreOwnerDropDown/>
             <NavSystemManagerDropDown/>
                          
             <Link to='/viewcart'>
              <Button variant="outline-info" id="navbar-shopping-cart">Shopping Cart</Button>
             </Link>
             {/* <Nav.Link as={Link} to="/stores" >Stores</Nav.Link>
             <Nav.Link as={Link} to="/displayproducts" >Products</Nav.Link>
             <Nav.Link as={Link} to="/viewcart" >Shoping Cart</Nav.Link> */}

          </Nav>
          {/* <Form inline>
            <FormControl type="text" placeholder="Search" className="mr-sm-2" />

            <Button variant="outline-info">Search</Button>
          </Form> */}

                
                <Form inline id="form">
                <Form.Control id="form-search-text" type="text" placeholder="Search" className="search" value={searchInput} onChange={searchInputHandler}/>
                <Dropdown>
                <Dropdown.Toggle variant="outline-info" id="dropdown-searchby">
                    By
                </Dropdown.Toggle>
                <Dropdown.Menu variant="outline-info" id="form-dropdown-menu">
                    {/* <Link to='/search'> */}
                    <Dropdown.Item id="form-dropdown-item1" href="#/action-1" onClick={byNameHandler} variant="dark">By Name</Dropdown.Item>
                    <Dropdown.Item id="form-dropdown-item2" href="#/action-2" onClick={byKeywordHandler} variant="dark">By Keyword</Dropdown.Item>
                            

                    <Dropdown drop='left' onClick={fetchCategories}>
                    <Dropdown.Toggle variant="outline-info" id="form-dropdown-item3">
                        By Category
                    </Dropdown.Toggle>

                    <Dropdown.Menu id="form-category-dropdown" variant="dark">
                        {categories.map(category => (
                            <Dropdown.Item variant="dark" onClick={e => byCategoryHandler(category)}>{category}</Dropdown.Item>
                        ))}
                    </Dropdown.Menu>

                    </Dropdown>
                </Dropdown.Menu>
                </Dropdown>

                    <Link to={{
                        pathname:'/searchresults', 
                        state: {
                            searchOption: searchOption,
                            input: searchInput,
                            categories: categories
                        }
                        }}>
                        <Button id="form-search-button" variant="outline-info">Search</Button>
                        </Link>

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

        <Route path="/allhistory" exact component={PurchaseHistoryUsersStores} />

        {/* <Route path="/history" exact component={PersonalPurchaseHistory} />
        <Route path="/history" exact component={PersonalPurchaseHistory} />
        <Route path="/history" exact component={PersonalPurchaseHistory} />
        <Route path="/history" exact component={PersonalPurchaseHistory} /> */}
      </Switch>
      </div>
    </Router>
  );
}




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
            <NavDropdown.Item as={Link} to="/stores" >Display Stores</NavDropdown.Item>
            {/* <NavDropdown.Item as={Link} to="/displayproducts">Search Products</NavDropdown.Item> */}
            {/* <NavDropdown.Item as={Link} to="/viewcart" >Shoping Cart</NavDropdown.Item> */}
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
            <NavDropdown.Item as={Link} to="/displayproducts" >Appoint Store Owner</NavDropdown.Item>
            <NavDropdown.Item as={Link} to="/displayproducts" >Appoint Store Manager</NavDropdown.Item>
            <NavDropdown.Item as={Link} to="/displayproducts" >Edit Manager’s Permissions</NavDropdown.Item>
            <NavDropdown.Item as={Link} to="/displayproducts" >Remove Store Manager</NavDropdown.Item>
            <NavDropdown.Item as={Link} to="/displayproducts" >View Store’s Purchase History</NavDropdown.Item>
          </div>
         </NavDropdown>
}

// function NavStoreManagerDropDown(props){
//   return <NavDropdown id="basic-nav-dropdown" title="Store Manager">
//           <div>
//             <NavDropdown.Item as={Link} to="/allhistory" >Manage Store</NavDropdown.Item>
//           </div>
//          </NavDropdown>
// }


function NavSystemManagerDropDown(props){
  return <NavDropdown id="basic-nav-dropdown" title="System Manager">
          <div>
            <NavDropdown.Item as={Link} to="/allhistory" >View Purchases History</NavDropdown.Item>
          </div>
         </NavDropdown>
}






export default App;
