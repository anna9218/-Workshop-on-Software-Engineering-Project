import React, {useState} from 'react';
import {Container, Row, Col, Button, Dropdown, Jumbotron, Form} from 'react-bootstrap'
import {Link} from 'react-router-dom'
import * as theService from '../../services/communication';


// WHAT'S LEFT TO DO HERE:
// Available guest's actions in the Service Layer:
// register - done
// login - almost done (except going back, can add a button. Need to display new page for logged in user)
// display_stores_or_products_info 
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


function GuestRoleAPI(props){

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
    
    return(

        <Container style={{width: props["screenWidth"], height: props["screenHeight"]}}>
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

            
                {/*
                        // for guest only
                        1. register - > now button -> redirect to ./register -> ok
                        2. login - > now button -> redirect to ./login -> ok 

                        // guest and up
                        3. display stores and products info, display stores ->  redirect to ./stores
                        4. search products by + filter products by -> in navbar
                        5. save products to basket -> in shopping cart
                        6. view and update shopping cart -> in shopping cart
                    */}

             
        <Row>
            <Button variant="secondary" size="lg" block as={Link} to="/stores">
                Display Stores And Products Information
            </Button>

            {/* <Link to='/stores'>
                <Button variant="dark" id="displaystores">Display Stores</Button>
            </Link> */}
                    
            {/* <Link to='/purchase'>
                <Button variant="dark" id="purchasesbtn">Purchase Products</Button>
            </Link> */}
                    
            {/* <Link to='/viewcart'>
                <Button variant="dark" id="viewcartbtn">View Shopping Cart</Button>
            </Link> */}



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




//SEARCH
{/* <Form inline>
<Form.Control type="text" placeholder="Search" className="search" onChange={searchInputHandler}/>
<Dropdown>
<Dropdown.Toggle variant="dark" id="dropdown-searchby">
    By
</Dropdown.Toggle>
<Dropdown.Menu variant="dark">
    <Link to='/search'>
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

</Form> */}
