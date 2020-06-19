import React, { useState, useEffect } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import {BrowserRouter as Router, Switch, Route, Link} from 'react-router-dom'
import {Button, Jumbotron, Form, Row} from 'react-bootstrap'
import * as theService from '../../../services/communication';
import * as BackOption from '../GeneralActions/Back'


function DisplayStores(props){
  useEffect(() => {
    setCount(count + 1);
    fetchStores();
  }, []);

  const [count, setCount] = useState(1);
  const [selectedStore, setSelectedStore] = useState("");
  const [infoType, setInfoType] = useState("");
  const [stores, setStores] = useState([]); // Declare a new state variable, which we'll call "stores"

  const fetchStores = async () => {
    const promise = theService.displayStores(); // goes to register.js and sends to backend
    promise.then((data) => {
      if(data !== null){
        if (data["data"]["response"].length > 0){   // if there are stores to display
            setStores(data["data"]["response"]);
        }
        else{
          alert(data["data"]["msg"]);      // no stores to display
        }
      }
    });
  };

  return (
    //SET SOME KIND OF COUNTER ID FOR LINK - SOLVED IT WITH STORE NAME
      // <div style={{width: props["screenWidth"], height: props["screenHeight"]}}>
      //   <h1>All Stores</h1>
      //   {stores.map(store => (
      //     <h1>
      //     <Link to={{
      //       pathname:'/stores/'+store, 
      //       state:{
      //         storeName: store
      //       }
      //       }}>
      //       <Button variant="dark">{store}</Button>
      //     </Link>
      //     </h1>
      //   ))}
       
      //   <Button style={{marginTop: "1%"}} variant="dark" id="back-btn" onClick={event => BackOption.BackToHome(props)}>Back</Button>
      // </div>


      <div style={{width: props["screenWidth"], height: props["screenHeight"]}}>
         <div style={{marginTop:"1%"}}>
             <h2>Store and products info: </h2>
         </div>
         <div style={{marginTop:"1%" , marginLeft: "25%", marginRight: "25%", border: "1px solid", borderColor: "#CCCCCC"}}>
             <Form >
                 <fieldset>
                    <Form.Group as={Row} onChange={ event => {setSelectedStore(event.target.value)}}>
                        <Form.Label style={{marginTop:"1%", marginLeft:"0.5%"}} as="legend" column sm={3}>Please choose a store:</Form.Label>
                        <div style={{marginTop:"1%", marginRight:"0%" , marginLeft: "0%"}}>
                          <Form.Control as="select">
                            <option value={""} >Select Store</option>
                            {stores.map(store => (
                                <option value={store}>{store}</option>
                            ))}
                        </Form.Control>
                        </div>
                      </Form.Group>

                      <Form.Group as={Row} >
                                <Form.Label style={{marginLeft:"1%"}} as="legend" column sm={3}>
                                  Choose Display option:
                                </Form.Label>
                                <Form.Check inline onClick={(event => {setInfoType("storeInfo")})} type="radio" label="Store Info" name="formHorizontalRadios" id="Radios1"/>
                                <Form.Check inline onClick={(event => {setInfoType("productsInfo")})} type="radio" label="Store's Products" name="formHorizontalRadios" id="Radios2"/>
                                {/* <Form.Control disabled={!searchType}  style={{marginRight:"2%" , marginLeft: "2%"}} onChange={(event => {setInput(event.target.value)})} placeholder="Enter relevant text..." /> */}
                            </Form.Group>
                     {/* <Form.Group as={Row} >
                         <Form.Label as="legend" column sm={6}>
                             Please enter a unique nickname and password:
                         </Form.Label>
                        <Form.Control style={{marginRight:"3%" , marginLeft: "3%"}} type="text" id="email" name="email" placeholder="Nickname" value={this.state.email} onChange={this.handleEmailChange} />
                         <Form.Control style={{marginTop:"1%", marginRight:"3%" , marginLeft: "3%"}} type="password" id="password" name="password" placeholder="Password" value={this.state.password} onChange={this.handlePasswordChange}/>
                     </Form.Group> */}
                 </fieldset>
                 <Form.Group as={Row} style={{marginRight:"1%" , marginLeft: "1%"}}>
                     {/* <Button type="reset" variant="dark" disabled={this.state.email === "" | this.state.password === ""} onClick={this.handleLogin} to='/'>Login</Button> */}
                     <Link to={{pathname:'/stores/'+selectedStore, 
                                state:{
                                  storeName: selectedStore,
                                  displayOption: infoType}
                                }}>
                                  <Button type="reset" variant="dark" disabled={selectedStore === "" | infoType === ""}>Display</Button>
                     </Link>
                 </Form.Group>
             </Form>
         </div>
         <div style={{marginTop:"1%" , marginLeft: "25%", marginRight: "25%"}}>
             <Form >
                 <Form.Group as={Row} style={{marginRight:"1%" , marginLeft: "1%"}}>
                  <div> <Button variant="dark" id="back-btn" onClick={event => BackOption.BackToHome(props)}>Back</Button></div>
                 </Form.Group>
             </Form>
         </div>

     </div>
  );
}

export default DisplayStores;




          // <h1 key={store.id}>
          //   <Link to={'/stores/${store.id}'}>
          //     <Button variant="dark">{store.name}</Button>
          //   {/* <button type="button" onClick={this.handleRegister}></button> */}
          //   </Link>
          // </h1>