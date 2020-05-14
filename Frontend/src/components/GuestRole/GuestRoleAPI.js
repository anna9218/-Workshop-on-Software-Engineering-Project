import React, {useState} from 'react';
import {Container, Row, Col, Button, Dropdown, Jumbotron, Form} from 'react-bootstrap'
import {Link} from 'react-router-dom'
import * as registerService from '../../services/register';

// WHAT'S LEFT TO DO HERE:
// Available guest's actions in the Service Layer:
// register - done (except going back, can add a button)
// login - almost done (except going back, can add a button. Need to display new page for logged in user)
// display_stores_or_products_info - need to get handle response and display
// search_products_by,      filter_products_by,     save_products_to_basket
// view_shopping_cart - done, need to decide if products have info to view
// update_shopping_cart
// purchase_products,       confirm_payment



//     // STYLING //
//     btnStyle = {
//         borderRadius: "5px",
//         borderWidth: "1px",
//         borderColor: "rgba(117, 116, 116, 0.3)",
//         margin: "0 5% 0 5%",
//         //backgroundColor: "rgba(84, 148, 103, 0.5)"
//     }


function GuestRoleAPI(){

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
        const promise = registerService.getCategories(); // goes to register.js and sends to backend
    promise.then((data) => {setCategories(data["data"])});
    }
    

    return(
        <Container>
        <Jumbotron fluid>
            <Row>
                <Col />
                <Col xs={7}>
                    <h1 style={{textAlign: "center"}}>Welcome to the Trade Contol Where dreams come true!</h1>
                </Col>
                <Col>
                <Link to='/register'>
                    <Button variant="dark" id="regbtn">Register</Button>
                </Link>
                <Link to='/login'>
                    <Button variant="dark" id="loginbtn">Login</Button>
                </Link>
                </Col>
            </Row>
        </Jumbotron>


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
            </Container>
    );
}


export default GuestRoleAPI;







{/* <Form.Group as={Col} controlId="formGridState">
<Form.Label>State</Form.Label>
<Form.Control as="select" value="Choose...">
    <option>Choose...</option>
    <option>By name</option>
    <option>By name</option>
</Form.Control>
</Form.Group> */}
