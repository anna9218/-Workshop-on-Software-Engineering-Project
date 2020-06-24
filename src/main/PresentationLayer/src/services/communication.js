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

export async function getUserType(){
    return axios.get('http://localhost:5000/get_user_type')
    .then((response) => (response.data), (error) => {console.log(error)});
}

export async function displayStores(){
    return axios.get('http://localhost:5000/display_stores')
    .then((response) => (response.data), (error) => {console.log(error)});
}

export async function displayStoresProducts(store_name){
    return axios.post('http://localhost:5000/display_stores_products', {
        store_name: store_name, 
        store_info_flag: false,
        products_info_flag: true
    })
    .then((response) => (response.data), (error) => {console.log(error)});
}

export async function displayStoresStores(store_name){
    return axios.post('http://localhost:5000/display_stores_products', {
        store_name: store_name, 
        store_info_flag: true,
        products_info_flag: false
    })
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
export async function filterProductsByRange(products_ls, filter_option, min_price, max_price){
    return axios.post('http://localhost:5000/filter_products_by', {
        products_ls: products_ls,
        filter_option: filter_option, 
        min_price: min_price,
        max_price: max_price
    })
    .then((response) => (response.data), (error) => {console.log(error)});
}

export async function filterProductsByCategory(products_ls, filter_option, category){
    return axios.post('http://localhost:5000/filter_products_by', {
        products_ls: products_ls,
        filter_option: filter_option, 
        category: category
    })
    .then((response) => (response.data), (error) => {console.log(error)});
}



export async function addToProductsCart(store_name, product_name, product_amount){
    return axios.post('http://localhost:5000/add_products_to_cart', {
        products: [{"store_name": store_name,
                    "product_name": product_name, 
                    "amount": product_amount}]
    })
    .then((response) => (response.data), (error) => {console.log(error)});
}

export async function updateShoppingCart(action_type, product_name, store_name, amount){
    return axios.post('http://localhost:5000/update_or_remove_from_shopping_cart', {
        action_type: action_type,
        store_name: store_name,
        amount: amount,
        product_name: product_name
    })
    .then((response) => (response.data), (error) => {console.log(error)});
}

export async function purchaseCart(){
    return axios.get('http://localhost:5000/purchase_products')
    .then((response) => (response.data), (error) => {console.log(error)});
}

export async function confirmPurchase(delivery_details, payment_details, purchase_details){
    return axios.post('http://localhost:5000/confirm_purchase', {
        delivery_details: delivery_details,
        payment_details: payment_details,
        purchases: purchase_details
    })
    .then((response) => (response.data), (error) => {console.log(error)});
}

//--------------------------- SUBSCRIBER ROLE ---------------------------------------//


export async function getNickname(){
    return axios.get('http://localhost:5000/get_curr_user_nickname')
    .then((response) => (response.data), (error) => {console.log(error)});
}

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

//--------------------------- INIT SYSTEM --------------------------------------------//
export async function initSystem(){
    return axios.get('http://localhost:5000/init_system')
    .then((response) => (response.data), (error) => {console.log(error)});
}
//--------------------------- END OF INIT SYSTEM -------------------------------------//




//--------------------------- MANAGRT ROLE --------------------------------------------//

export async function fetchManagedStores(){
    return axios.get('http://localhost:5000/get_managed_stores')
    .then((response) => (response.data), (error) => {console.log(error)});
}

export async function fetchManagerPermissions(store_name){
    return axios.post('http://localhost:5000/get_manager_permissions', {
        store_name: store_name,
    })
    .then((response) => (response.data), (error) => {console.log(error)});
}

export async function fetchManagersAppointees(store_name){
    return axios.post('http://localhost:5000/get_managers_appointees', {
        store_name: store_name,
    })
    .then((response) => (response.data), (error) => {console.log(error)});
}

export async function fetchOwnersAppointees(store_name){
    return axios.post('http://localhost:5000/get_owners_appointees', {
        store_name: store_name,
    })
    .then((response) => (response.data), (error) => {console.log(error)});
}
//--------------------------- END OF MANAGRT ROLE -------------------------------------//

//--------------------------- OWNER & MANAGER ROLE --------------------------------------------//

export async function fetchOwnedStores(){
    return axios.get('http://localhost:5000/get_owned_stores')
    .then((response) => (response.data), (error) => {console.log(error)});
}

export async function getPurchasePoliciesOperator(store_name){
    return axios.post('http://localhost:5000/get_purchase_operator', {
        store_name: store_name
    })
    .then((response) => (response.data), (error) => {console.log(error)});
}

export async function setPurchasePoliciesOperator(store_name, operator){
    return axios.post('http://localhost:5000/set_purchase_operator', {
        store_name: store_name,
        operator: operator
    })
    .then((response) => (response.data), (error) => {console.log(error)});
}

export async function addProduct(store_name, product_name, product_price, product_category, product_amount, purchase_type){
    return axios.post('http://localhost:5000/add_product', {
        store_name: store_name,
        products_details:
        [{
            name: product_name,
            price: parseInt(product_price),
            category: product_category,
            amount: parseInt(product_amount),
            purchase_type: purchase_type
        }]
        
    })
    .then((response) => (response.data), (error) => {console.log(error)});
}

export async function editProduct(store_name, product_name, new_product_name, amount, price, category, purchase_type){
    return axios.post('http://localhost:5000/edit_product', {
        store_name: store_name,
        product_name: product_name,
        new_product_name: new_product_name,
        amount: amount,
        price: price,
        category: category,
        purchase_type: purchase_type
    })
    .then((response) => (response.data), (error) => {console.log(error)});
}

export async function deleteProduct(store_name, product_name){
    return axios.post('http://localhost:5000/remove_product', {
        store_name: store_name,
        product_name: product_name
    })
    .then((response) => (response.data), (error) => {console.log(error)});
}

export async function getProductInfo(store_name, product_name){
    return axios.post('http://localhost:5000/get_product_details', {
        store_name: store_name,
        product_name: product_name
    })
    .then((response) => (response.data), (error) => {console.log(error)});
}

export async function appointStoreManager(appointee_nickname, store_name, permissions){
    return axios.post('http://localhost:5000/appoint_store_manager', {
        appointee_nickname: appointee_nickname,
        store_name: store_name,
        permissions: permissions
    })
    .then((response) => (response.data), (error) => {console.log(error)});
}

export async function appointStoreOwner(appointee_nickname, store_name){
    return axios.post('http://localhost:5000/appoint_store_owner', {
        appointee_nickname: appointee_nickname,
        store_name: store_name,
    })
    .then((response) => (response.data), (error) => {console.log(error)});
}


// call anna : handle_appointment_agreement_response(nickname_apointee, store_name, answer: 1= decline, 2 = approve)
// const promise = theService.sendAgreementAnswer(noti['username'], noti['store'], answer ? 2 : 1)
export async function sendAgreementAnswer(appointee_nickname, store_name, answer){
    return axios.post('http://localhost:5000/handle_appointment_agreement_response', {
        appointee_nickname: appointee_nickname,
        store_name: store_name,
        appointment_agreement_response: answer,
    })
    .then((response) => (response.data), (error) => {console.log(error)});
}


export async function removeOwner(store_name, nickname){
    return axios.post('http://localhost:5000/remove_owner', {
        store_name: store_name,
        nickname: nickname
    })
    .then((response) => (response.data), (error) => {console.log(error)});
}

export async function removeManager(store_name, nickname){
    return axios.post('http://localhost:5000/remove_manager', {
        store_name: store_name,
        nickname: nickname
    })
    .then((response) => (response.data), (error) => {console.log(error)});
}



export async function editManagerPermissions(store_name, appointee_nickname, permissions){
    return axios.post('http://localhost:5000/edit_manager_permissions', {
        store_name: store_name,
        appointee_nickname: appointee_nickname,
        permissions: permissions
    })
    .then((response) => (response.data), (error) => {console.log(error)});
}

export async function fetchStorePurchaseHistory(store_name){
    return axios.post('http://localhost:5000/view_store_purchases_history', {
        store_name: store_name,
    })
    .then((response) => (response.data), (error) => {console.log(error)});
}


export async function getPolicies(policy_type, store_name){
    return axios.post('http://localhost:5000/get_policies', {
        store_name: store_name,
        policy_type: policy_type
    })
    .then((response) => (response.data), (error) => {console.log(error)});
}

export async function addAndUpdatePurchasePolicy(action_type, store_name, policy_name, products, min_amount, max_amount, dates, bundle){
        return axios.post('http://localhost:5000/add_and_update_purchase_policy', {
        action_type: action_type,
        store_name: store_name,
        policy_name: policy_name,
        products: products,
        min_amount: min_amount,
        max_amount: max_amount,
        dates: dates,
        bundle: bundle
    })
    .then((response) => (response.data), (error) => {console.log(error)});
}

export async function addAndUpdateDiscountPolicy(action_type, store_name, policy_name, product_name, date, percentage, new_policy_name ,product, min_amount, min_purchase_price){
    return axios.post('http://localhost:5000/add_and_update_dicount_policy', {
        action_type: action_type,
        store_name: store_name,
        policy_name: policy_name,
        product_name: product_name,
        date: date,
        percentage: percentage,
        product: product,
        min_amount: min_amount,
        min_purchase_price: min_purchase_price,
        new_policy_name: new_policy_name
    })
    .then((response) => (response.data), (error) => {console.log(error)});
}

export async function addCompositeDiscountPolicy(store_name, policy1, policy2, operator, percentage, new_policy_name ,date){
    return axios.post('http://localhost:5000/add_composite_dicount_policy', {
        store_name: store_name,
        policy1: policy1,
        policy2: policy2,
        operator: operator,
        percentage: percentage,
        new_policy_name: new_policy_name,
        date: date
    })
    .then((response) => (response.data), (error) => {console.log(error)});
}

export async function deletePolicy(policy_type, store_name, policy_name){
    return axios.post('http://localhost:5000/delete_policy', {
        policy_type: policy_type,
        store_name: store_name,
        policy_name: policy_name,
        
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

export async function SystemManagerfetchStorePurchaseHistory(store_name){
    return axios.post('http://localhost:5000/view_any_store_purchase_history', {
        store_name: store_name
    })
    .then((response) => (response.data), (error) => {console.log(error)});
}

export async function getVisitorsCut(start_date, end_date){
    return axios.post('http://localhost:5000/get_visitors_cut', {
        start_date: start_date,
        end_date: end_date
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
