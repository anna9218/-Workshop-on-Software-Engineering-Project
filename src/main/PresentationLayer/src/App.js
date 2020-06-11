import React, {useState, useEffect} from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import {Navbar, Nav,Form, FormControl, Button,  NavDropdown, Dropdown} from 'react-bootstrap';
import {BrowserRouter as Router, Switch, Route, Link} from 'react-router-dom'
import './App.css';
import * as theService from './services/communication';


// import Nav from './components/Nav'
// guest
import GuestRoleAPI from './components/GuestRole/GuestRoleAPI'
import RegisterForm from './components/GuestRole/RegisterForm'
import Login from './components/GuestRole/Login'
import DisplayStores from './components/Actions/StoreActions/DisplayStores'
import DisplayProducts from './components/Actions/ShoppingCartActions/DisplayProducts'
import Search from './components/Search'
import ShoppingCart from './components/Actions/ShoppingCartActions/ShoppingCart'
import PurchaseProducts from './components/Actions/ShoppingCartActions/PurchaseProducts'
import StoreDetail from './components/Actions/StoreActions/StoreDetail'
import StoreProducts from './components/Actions/StoreActions/StoreProducts'
import SearchResults from './components/Actions/ShoppingCartActions/SearchResults'

// subscriber
import SubscriberAPI from './components/SubscriberRole/SubscriberAPI'
import OpenStore from './components/SubscriberRole/OpenStore'
import PersonalPurchaseHistory from './components/SubscriberRole/PersonalPurchaseHistory'

// owner or manager
import OwnerAPI from './components/OwnerOrManagerRole/OwnerAPI'
import ManageInventory from './components/OwnerOrManagerRole/ManageInventory'
import ManagerAPI from './components/OwnerOrManagerRole/ManagerAPI'
import AddProductsForm from './components/OwnerOrManagerRole/AddProductsForm'
import AppointStoreManager from './components/OwnerOrManagerRole/AppointStoreManager'

// system manager
import PurchaseHistoryUsersStores from './components/SystemManagerRole/PurchaseHistoryUsersStores'
import SystemManagerAPI from './components/SystemManagerRole/SystemManagerAPI'


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

  useEffect(async () => {
    // init system on startup
    const promise = theService.initSystem();
  });

  return (
    <Router>
      <div className="App">
        {/* Navigation Bar */}
        <Navbar id="navbar" bg="dark" variant="dark">
          <Navbar.Brand as={Link} id="navbar-logo" to="/">Trade Control</Navbar.Brand>
          <Nav id="navbar-nav" className="mr-auto">
             {/* this space is currently only a filer for navbar decoration */}
          </Nav>

          {/* <Nav id="navbar-nav" className="mr-auto" style={{float: "right"}}> */}
          <div style={{marginRight: "1%"}}>
            <Link to='/viewcart'>
              <Button variant="outline-info" id="navbar-shopping-cart">Shopping Cart</Button>
            </Link>
          </div>
                
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
        {/* guest */}
        <Route path="/" exact render={(props) => <GuestRoleAPI screenWidth= {window.innerWidth} screenHeight= {window.innerHeight} {...props} />} />
        <Route path="/register" exact render={(props) => <RegisterForm screenWidth= {window.innerWidth} screenHeight= {window.innerHeight} {...props} />} />
        <Route path="/login" exact render={(props) => <Login screenWidth= {window.innerWidth} screenHeight= {window.innerHeight} {...props} />} />        
        <Route path="/displayproducts" exact render={(props) => <DisplayProducts screenWidth= {window.innerWidth} screenHeight= {window.innerHeight} {...props} />} />
        <Route path="/stores" exact render={(props) => <DisplayStores screenWidth= {window.innerWidth} screenHeight= {window.innerHeight} {...props} />} />
        {/* <Route path="/search" exact component={Search} /> */}
        <Route path="/confirm_purchase" exact render={(props) => <PurchaseProducts screenWidth= {window.innerWidth} screenHeight= {window.innerHeight} {...props} />} />
        <Route path="/viewcart" exact render={(props) => <ShoppingCart screenWidth= {window.innerWidth} screenHeight= {window.innerHeight} {...props} />} />
        <Route path="/stores/:store" exact render={(props) => <StoreDetail screenWidth= {window.innerWidth} screenHeight= {window.innerHeight} {...props} />} />
        <Route path="/stores/:store/products" exact render={(props) => <StoreProducts screenWidth= {window.innerWidth} screenHeight= {window.innerHeight} {...props} />} />
        <Route path="/searchresults" exact render={(props) => <SearchResults screenWidth= {window.innerWidth} screenHeight= {window.innerHeight} {...props} />} />

        {/* subscriber */}
        <Route path="/subscriber" exact render={(props) => <SubscriberAPI screenWidth= {window.innerWidth} screenHeight= {window.innerHeight} {...props} />} />
        <Route path="/openstore" exact render={(props) => <OpenStore screenWidth= {window.innerWidth} screenHeight= {window.innerHeight} {...props} />} />
        <Route path="/history" exact render={(props) => <PersonalPurchaseHistory screenWidth= {window.innerWidth} screenHeight= {window.innerHeight} {...props} />} />
        <Route path="/owner" exact render={(props) => <OwnerAPI screenWidth= {window.innerWidth} screenHeight= {window.innerHeight} {...props} />} />
        <Route path="/manageinventory/:store" exact render={(props) => <ManageInventory screenWidth= {window.innerWidth} screenHeight= {window.innerHeight} {...props} />} />
        <Route path="/manager" exact render={(props) => <ManagerAPI screenWidth= {window.innerWidth} screenHeight= {window.innerHeight} {...props} />} />
        <Route path="/addproduct" exact render={(props) => <AddProductsForm screenWidth= {window.innerWidth} screenHeight= {window.innerHeight} {...props} />} />

        {/* owner */}
        <Route path="/appointmanager" exact render={(props) => <AppointStoreManager screenWidth= {window.innerWidth} screenHeight= {window.innerHeight} {...props} />} />
        
        {/* owner */}
        <Route path="/allhistory" exact render={(props) => <PurchaseHistoryUsersStores screenWidth= {window.innerWidth} screenHeight= {window.innerHeight} {...props} />} />
        <Route path="/systemmanager" exact render={(props) => <SystemManagerAPI screenWidth= {window.innerWidth} screenHeight= {window.innerHeight} {...props} />} />


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
            <NavDropdown.Item as={Link} to="/manageinventory" >Manage Inventory</NavDropdown.Item>
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
