import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import {BrowserRouter as Router, Switch, Route} from 'react-router-dom'
import './App.css';

import Nav from './components/Nav'

import GuestRoleAPI from './components/GuestRole/GuestRoleAPI'
import RegisterForm from './components/GuestRole/RegisterForm'
import Login from './components/GuestRole/Login'
import DisplayStores from './components/DisplayStores'
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
        {/* <Nav /> */}
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


