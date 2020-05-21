import axios from "axios";
//Responsible for sending requests to the back-end

export async function register(nickname, password) {
    return axios.post('http://localhost:5000/register', {
        nickname: nickname, 
        password: password
    })
    .then((response) => (response.data), (error) => {console.log(error)});
}

export async function login(nickname, password) {
    return axios.post('http://localhost:5000/login', {
        nickname: nickname, 
        password: password
    })
    .then((response) => (response.data), (error) => {console.log(error)});
}

export async function displayStores(){
    return axios.get('http://localhost:5000/display_stores')
    .then((response) => (response.data), (error) => {console.log(error)});
}

export async function displayShoppingCart(){
    return axios.get('http://localhost:5000/view_shopping_cart')
    .then((response) => (response.data), (error) => {console.log(error)});
}

export async function searchProductsBy(search_option, input){
    return axios.post('http://localhost:5000/search_products_by', {
        search_option: search_option, 
        input: input
    })
    .then((response) => (response.data), (error) => {console.log(error)});
}

export async function getCategories(){
    return axios.get('http://localhost:5000/get_categories')
    .then((response) => (response.data), (error) => {console.log(error)});
}

//input is ["min": 2, "max": 5] or "category"
export async function filterProductsBy(products, filter_option, input){
    return axios.post('http://localhost:5000/filter_products_by', {
        products: products,
        filter_option: filter_option, 
        input: input
    })
    .then((response) => (response.data), (error) => {console.log(error)});
}

export async function addToProductsCart(products){
    return axios.post('http://localhost:5000/add_products_to_cart', {
        products: products
    })
    .then((response) => (response.data), (error) => {console.log(error)});
}

export async function updateShoppingCart(option_flag, product){
    return axios.post('http://localhost:5000/update_shopping_cart', {
        option_flag: option_flag,
        product: product
    })
    .then((response) => (response.data), (error) => {console.log(error)});
}



//--------------------------- SUBSCRIBER ROLE ---------------------------------------//

export async function openStore(store_name){
    return axios.post('http://localhost:5000/open_store', {
        store_name: store_name
    })
    .then((response) => (response.data), (error) => {console.log(error)});
}

export async function logout(){
    return axios.get('http://localhost:5000/logout')
    .then((response) => (response.data), (error) => {console.log(error)});
}

export async function fetchPersonalPurchaseHistory(){
    return axios.get('http://localhost:5000/view_personal_purchase_history')
    .then((response) => (response.data), (error) => {console.log(error)});
}

//--------------------------- END OF SUBSCRIBER ROLE --------------------------------//

//--------------------------- OWNER ROLE --------------------------------------------//

export async function addProduct(product_name, product_price, product_category, product_amount){
    return axios.post('http://localhost:5000/add_product', {
        product_name: product_name,
        product_price: product_price,
        product_category: product_category,
        product_amount: product_amount
    })
    .then((response) => (response.data), (error) => {console.log(error)});
}

//--------------------------- END OF OWNER ROLE -------------------------------------//


//--------------------------- SYSTEM MANAGER ROLE -----------------------------------//

export async function fetchUserPurchaseHistory(nickname){
    return axios.post('http://localhost:5000/view_user_purchase_history', {
        nickname: nickname
    })
    .then((response) => (response.data), (error) => {console.log(error)});
}

export async function fetchStorePurchaseHistory(store_name){
    return axios.post('http://localhost:5000/view_store_purchases_history', {
        store_name: store_name
    })
    .then((response) => (response.data), (error) => {console.log(error)});
}

//--------------------------- END OF SYSTEM MANAGE ----------------------------------//


//TODO
export async function getManagerPermissions(){
    return axios.post('http://localhost:5000/XXXXXXXX', {
    })
    .then((response) => (response.data), (error) => {console.log(error)});
}







    // result.then(res => {if (res.status == 200) 
    //     {let json = await res.json();
    //     return json;}})
    // if (result.status == 200){
    //     return result.then('A');

    // result.then(function(response)
    // {
    //     return(response.resolved);
    // })
    // const result = await axios.post('https://localhost:5000/register', {nickname: nickname, password: password})
    // return result.data;
    // if(result.status !== 200){

    // }
    // body = await result.json();
    // return body;


    // when you write: `{ username, password }` JS will format it to be `{ username: username, password: password }`
    // When running Flask -> "Running on http://127.0.0.1:5000/", it may vary
