import React, {useState, useEffect} from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import {Navbar, Nav,Form, FormControl, Button,  NavDropdown, Dropdown} from 'react-bootstrap';
import {BrowserRouter as Router, Switch, Route, Link} from 'react-router-dom'
import './App.css';
import * as theService from './services/communication';
import BackToHome from './components/Actions/GeneralActions/Back'

// import Nav from './components/Nav'
// guest
import GuestRoleAPI from './components/GuestRole/GuestRoleAPI'
import RegisterForm from './components/GuestRole/RegisterForm'
import Login from './components/GuestRole/Login'
import DisplayStores from './components/Actions/StoreActions/DisplayStores'
// import DisplayProducts from './components/Actions/ShoppingCartActions/DisplayProducts'
import Search from './components/Search'
import ShoppingCart from './components/Actions/ShoppingCartActions/ShoppingCart'
import PurchaseProducts from './components/Actions/ShoppingCartActions/PurchaseProducts'
import StoreDetail from './components/Actions/StoreActions/StoreDetail'
import StoreProducts from './components/Actions/StoreActions/StoreProducts'
import SearchAndFilterProducts from './components/GuestRole/SearchAndFilterProducts';
// import SearchResults from './components/Actions/ShoppingCartActions/SearchResults'

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
import AppointOwner from './components/OwnerOrManagerRole/AppointOwner'
import RemoveManager from './components/OwnerOrManagerRole/RemoveManager'
import EditPermissions from './components/OwnerOrManagerRole/EditPermissions'

// system manager
import PurchaseHistoryUsersStores from './components/SystemManagerRole/PurchaseHistoryUsersStores'
import SystemManagerAPI from './components/SystemManagerRole/SystemManagerAPI'


class App extends React.Component{
  constructor(props){
    super(props);

    this.state = {
      searchOption: 0,
      searchInput: '',
      categories: [],
      height: window.innerHeight,
      width: window.innerWidth
    }
    this.byNameHandler = this.byNameHandler.bind(this);
    this.byKeywordHandler = this.byKeywordHandler.bind(this);
    this.byCategoryHandler = this.byCategoryHandler.bind(this);
    this.searchInputHandler = this.searchInputHandler.bind(this);
    this.fetchCategories = this.fetchCategories.bind(this);
    this.updateWindowDimensions = this.updateWindowDimensions.bind(this);


  }

  byNameHandler = () =>{
      this.setState({searchOption: 1});
  };
  byKeywordHandler = () =>{
    this.setState({searchOption: 2});
  };
  byCategoryHandler = (input) =>{
    this.setState({searchOption: 2, searchInput: input});
  };
  searchInputHandler = (event) =>{
    this.setState({searchInput: event.target.value});
  };

  componentDidMount = () => {
    // init system on startup
    const promise = theService.initSystem();
    // update window dimentions and set an event listener for resize
    this.updateWindowDimensions();
    window.addEventListener('resize', this.updateWindowDimensions);
  }

  // for the search functionality
  fetchCategories = async () =>{
      const promise = theService.getCategories(); // goes to register.js and sends to backend
      promise.then((data) => {this.setState({categories: data["data"]})});
  };

  updateWindowDimensions = () => {
    this.setState({height: window.innerHeight, width: window.innerWidth})
  }

  render(){
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
              <Link to={{pathname:'/viewcart', history: this.props}}>
                <Button variant="outline-info" id="navbar-shopping-cart">Shopping Cart</Button>
              </Link>
            </div>

            <Form inline id="form">
              {/* <Form.Control id="form-search-text" type="text" placeholder="Search" className="search" value={searchInput} onChange={searchInputHandler}/> */}
             {/* <Dropdown>
                  <Dropdown.Toggle variant="outline-info" id="dropdown-searchby">
                      By
                  </Dropdown.Toggle>
                  <Dropdown.Menu variant="outline-info" id="form-dropdown-menu">
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
               </Dropdown> */}

          <Link to={{
            pathname:'/searchandfilter',
            state: {
                searchOption: this.state.searchOption,
                input: this.state.searchInput,
                categories: this.state.categories
            }
            }}>
              <Button id="form-search-button" variant="outline-info">Search</Button>
            </Link>

          </Form>
        </Navbar>

        <Switch>
          {/* guest */}
          <Route path="/" exact render={(props) => <GuestRoleAPI screenWidth= {this.state.width} screenHeight= {this.state.height-100} {...props} />} />
          <Route path="/register" exact render={(props) => <RegisterForm screenWidth= {this.state.width} screenHeight= {this.state.height-100} {...props} />} />
          <Route path="/login" exact render={(props) => <Login screenWidth= {this.state.width} screenHeight= {this.state.height-100} {...props} />} />
          {/* <Route path="/displayproducts" exact render={(props) => <DisplayProducts screenWidth= {width} screenHeight= {height-100} {...props} />} /> */}
          <Route path="/stores" exact render={(props) => <DisplayStores screenWidth= {this.state.width} screenHeight= {this.state.height-100} {...props} />} />
          {/* <Route path="/search" exact component={Search} /> */}
          <Route path="/confirm_purchase" exact render={(props) => <PurchaseProducts screenWidth= {this.state.width} screenHeight= {this.state.height-100} {...props} />} />
          <Route path="/viewcart" exact render={(props) => <ShoppingCart screenWidth= {this.state.width} screenHeight= {this.state.height-100} {...props} />} />
          <Route path="/stores/:store" exact render={(props) => <StoreDetail screenWidth= {this.state.width} screenHeight= {this.state.height-100} {...props} />} />
          <Route path="/stores/:store/products" exact render={(props) => <StoreProducts screenWidth= {this.state.width} screenHeight= {this.state.height-100} {...props} />} />
          // <Route path="/searchresults" exact render={(props) => <SearchResults screenWidth= {this.state.width} screenHeight= {this.state.height-100} {...props} />} />
          <Route path="/searchandfilter" exact render={(props) => <SearchAndFilterProducts screenWidth= {window.innerWidth} screenHeight= {window.innerHeight} {...props} />} />

          {/* subscriber */}
          <Route path="/subscriber" exact render={(props) => <SubscriberAPI screenWidth= {this.state.width} screenHeight= {this.state.height-100} {...props} />} />
          <Route path="/openstore" exact render={(props) => <OpenStore screenWidth= {this.state.width} screenHeight= {this.state.height-100} {...props} />} />
          <Route path="/history" exact render={(props) => <PersonalPurchaseHistory screenWidth= {this.state.width} screenHeight= {this.state.height-100} {...props} />} />
          <Route path="/owner" exact render={(props) => <OwnerAPI screenWidth= {this.state.width} screenHeight= {this.state.height-100} {...props} />} />
          <Route path="/manageinventory/:store" exact render={(props) => <ManageInventory screenWidth= {this.state.width} screenHeight= {this.state.height-100} {...props} />} />
          <Route path="/manager" exact render={(props) => <ManagerAPI screenWidth= {this.state.width} screenHeight= {this.state.height-100} {...props} />} />
          <Route path="/addproduct" exact render={(props) => <AddProductsForm screenWidth= {this.state.width} screenHeight= {this.state.height-100} {...props} />} />

          {/* owner */}
          <Route path="/appointowner" exact render={(props) => <AppointOwner screenWidth= {window.innerWidth} screenHeight= {window.innerHeight} {...props} />} />
        <Route path="/appointmanager" exact render={(props) => <AppointStoreManager screenWidth= {window.innerWidth} screenHeight= {window.innerHeight} {...props} />} />
        <Route path="/editpermissions" exact render={(props) => <EditPermissions screenWidth= {window.innerWidth} screenHeight= {window.innerHeight} {...props} />} />
        <Route path="/removemanager" exact render={(props) => <RemoveManager screenWidth= {window.innerWidth} screenHeight= {window.innerHeight} {...props} />} />

          {/* owner */}
          <Route path="/allhistory" exact render={(props) => <PurchaseHistoryUsersStores screenWidth= {this.state.width} screenHeight= {this.state.height-100} {...props} />} />
          <Route path="/systemmanager" exact render={(props) => <SystemManagerAPI screenWidth= {this.state.width} screenHeight= {this.state.height-100} {...props} />} />


          <Route path="/back" exact render={(props) => <BackToHome screenWidth= {this.state.width} screenHeight= {this.state.height-100} history={this.props} {...props} />} />


          {/* <Route path="/history" exact component={PersonalPurchaseHistory} />
          <Route path="/history" exact component={PersonalPurchaseHistory} />
          <Route path="/history" exact component={PersonalPurchaseHistory} />
          <Route path="/history" exact component={PersonalPurchaseHistory} /> */}
        </Switch>
        </div>
      </Router>
    );
  }
}




// function NavGuestDropDown(props){
//   // return <NavDropdown style={{position: "absolute"}} id="basic-nav-dropdown" title={}
//   //         <div>
//   //            <NavDropdown.Item as={Link} to="/stores" >Stores</NavDropdown.Item>
//   //            <NavDropdown.Item as={Link} to="/displayproducts" >Products</NavDropdown.Item>
//   //            <NavDropdown.Item as={Link} to="/viewcart" >Shoping Cart</NavDropdown.Item>
//   //         </div>
//   //       </NavDropdown>
//   return <NavDropdown id="basic-nav-dropdown" title="Guest">
//           <div>
//             <NavDropdown.Item as={Link} to="/stores" >Display Stores</NavDropdown.Item>
//             {/* <NavDropdown.Item as={Link} to="/displayproducts">Search Products</NavDropdown.Item> */}
//             {/* <NavDropdown.Item as={Link} to="/viewcart" >Shoping Cart</NavDropdown.Item> */}
//             {/* <NavDropdown.Item as={Link} to="/PurchaseProducts" >Purchase Products</NavDropdown.Item> */}
//           </div>
//          </NavDropdown>
// }

// function NavSubscriberDropDown(props){
//   return <NavDropdown id="basic-nav-dropdown" title="Subscriber">
//           <div>
//             <NavDropdown.Item as={Link} to="/openstore">Open Store</NavDropdown.Item>
//             <NavDropdown.Item as={Link} to="/history" >Personal Purchase History</NavDropdown.Item>
//           </div>
//          </NavDropdown>
// }

// function NavStoreOwnerDropDown(props){
//   return <NavDropdown id="basic-nav-dropdown" title="Store Owner">
//           <div>
//             <NavDropdown.Item as={Link} to="/manageinventory" >Manage Inventory</NavDropdown.Item>
//             <NavDropdown.Item as={Link} to="/displayproducts" >Manage Policies</NavDropdown.Item>
//             <NavDropdown.Item as={Link} to="/displayproducts" >Appoint Store Owner</NavDropdown.Item>
//             <NavDropdown.Item as={Link} to="/displayproducts" >Appoint Store Manager</NavDropdown.Item>
//             <NavDropdown.Item as={Link} to="/displayproducts" >Edit Manager’s Permissions</NavDropdown.Item>
//             <NavDropdown.Item as={Link} to="/displayproducts" >Remove Store Manager</NavDropdown.Item>
//             <NavDropdown.Item as={Link} to="/displayproducts" >View Store’s Purchase History</NavDropdown.Item>
//           </div>
//          </NavDropdown>
// }



// function NavSystemManagerDropDown(props){
//   return <NavDropdown id="basic-nav-dropdown" title="System Manager">
//           <div>
//             <NavDropdown.Item as={Link} to="/allhistory" >View Purchases History</NavDropdown.Item>
//           </div>
//          </NavDropdown>
// }






export default App;
