import React, {useState} from 'react';
import {Container, Row, Col, Button, Dropdown, Jumbotron, Form} from 'react-bootstrap'
import {Link, Redirect, Router} from 'react-router-dom'
import * as theService from '../../services/communication';


// WHAT A SUBSCRIBER CAN DO?
// Guest actions - display_stores_or_products_info, search_products_by, view_shopping_cart, update_shopping_cart, purchase_products
//
// Logout (3.1)
// Open store (3.2)
// View personal purchase history (3.7)


function SubscriberAPI(){


    const [searchOption, setSearchOption] = useState(0);
    const [searchInput, setSearchInput] = useState('');
    const [categories, setCategories] = useState([])

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
    }

    // for the search functionality
    const fetchCategories = async () =>{
        const promise = theService.getCategories(); // goes to register.js and sends to backend
    promise.then((data) => {setCategories(data["data"])});
    }




    const logoutHandler = async () =>{
        const promise = theService.logout(); // goes to register.js and sends to backend
        promise.then((data) => {
          alert(data["msg"]);

        //   <Router>
        //   <Redirect to='/subscriber' />
        //   </Router>
              {/* </Redirect> */}



        });
    };




    return(
        <Container>
            <div>
                <h1>Welcome Dear Subscriber!</h1>
            </div>

            



            <Row>
            <Link to='/stores'>
                <Button variant="dark" id="displaystores">Display Stores</Button>
            </Link>
    
            <Link to='/purchase'>
                <Button variant="dark" id="purchasesbtn">Purchase Products</Button>
            </Link>
                    
            <Link to='/viewcart'>
                <Button variant="dark" id="viewcartbtn">View Shopping Cart</Button>
            </Link>


            <Form inline>
                <Form.Control type="text" placeholder="Search" className="search" onChange={searchInputHandler}/>
                <Dropdown>
                <Dropdown.Toggle variant="dark" id="dropdown-searchby">
                    By
                </Dropdown.Toggle>
                <Dropdown.Menu variant="dark">
                    {/* <Link to='/search'> */}
                    <Dropdown.Item href="#/action-1" onClick={byNameHandler} variant="dark">By Name</Dropdown.Item>
                    <Dropdown.Item href="#/action-2" onClick={byKeywordHandler} variant="dark">By Keyword</Dropdown.Item>
                            

                    <Dropdown drop='right' onClick={fetchCategories}>
                    <Dropdown.Toggle variant="dark" id="dropdown-searchby">
                        By Category
                    </Dropdown.Toggle>

                    <Dropdown.Menu variant="dark">
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
                        <Button variant="dark">Search</Button>
                    </Link>

                </Form>
            </Row>
 










    
            <Link to='/openstore'>
                <Button variant="dark" id="open_store">Open Store</Button>
            </Link>

            <Link to='/history'>
                <Button variant="dark" id="view_personal_history">View personal purchase history</Button>
            </Link>

            {/* <Link to='/'> */}
                <Button variant="dark" id="logout" onClick={logoutHandler}>Logout</Button>
            {/* </Link> */}

        </Container>
    );

}

export default SubscriberAPI;