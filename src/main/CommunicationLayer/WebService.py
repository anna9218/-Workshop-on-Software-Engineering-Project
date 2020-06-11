from flask import Flask, request
# import os
from flask_cors import CORS
from flask import jsonify

# from src.main.CommunicationLayer import WebSocketService
from src.main.CommunicationLayer import Websocket
from src.main.ServiceLayer.GuestRole import GuestRole
from src.main.ServiceLayer.StoreOwnerOrManagerRole import StoreOwnerOrManagerRole
from src.main.ServiceLayer.SubscriberRole import SubscriberRole
from src.main.ServiceLayer.TradeControlService import TradeControlService
from flask_socketio import SocketIO, join_room, leave_room

app = Flask(__name__)
CORS(app)
# 1 - purchase
# 2 - add+remove manager
# 3 - else
socket = SocketIO(app, cors_allowed_origins='*')
# socket = SocketIO(app, logger=True, engineio_logger=True,
#                   cors_allowed_origins='*', async_mode='eventlet')


# ------------------------------ GUEST ROLE SERVICES ------------------------------------#


@app.route('/register', methods=['POST'])
def register():
    req = request
    if request.is_json:
        request_dict = request.get_json()
        nickname = request_dict.get('nickname')
        password = request_dict.get('password')
        response = GuestRole.register(nickname, password)  # seems OK, checked
        if response:
            return jsonify(msg=response['msg'], data=response['response'])
        # return jsonify(msg="Registered successfully!")
    return jsonify(msg="Registration failed", data=response['response'], status=400)


@app.route('/login', methods=['POST'])
def login():
    if request.is_json:
        request_dict = request.get_json()
        nickname = request_dict.get('nickname')
        password = request_dict.get('password')
        response = GuestRole.login(nickname, password)  # seems OK, need to verify later
        if response:
            return jsonify(msg=response['msg'], data=response['response'])
    return jsonify(msg="Login failed", data=response['response'], status=400)


@app.route('/display_stores', methods=['GET'])
def display_stores():
    response = GuestRole.display_stores()  # BUG
    return jsonify(data=response)


@app.route('/display_stores_products', methods=['POST'])
def display_stores_products():
    if request.is_json:
        request_dict = request.get_json()
        store_name = request_dict.get('store_name')
        store_info_flag = request_dict.get('store_info_flag')
        products_info_flag = request_dict.get('products_info_flag')
        response = GuestRole.display_stores_or_products_info(store_name, store_info_flag, products_info_flag)
        if response:
            return jsonify(msg=response["msg"], data=response["response"])
        return jsonify(msg="get store products failed", data=response["response"], status=400)


@app.route('/view_shopping_cart', methods=['GET'])
def view_shopping_cart():
    response = GuestRole.view_shopping_cart()
    return jsonify(data=response["response"], msg=response["msg"])


@app.route('/search_products_by', methods=['POST'])
def search_products_by():
    if request.is_json:
        request_dict = request.get_json()
        search_option = request_dict.get('search_option')  # by name, keyword or category
        input_str = request_dict.get('input')
        # response = GuestRole.search_products_by(search_option, input_str)  # list of Products (Object)
        # return jsonify(data=response)
        return jsonify(data=["Product1", "Product2"])


@app.route('/get_categories', methods=['GET'])
def get_categories():
    # response = GuestRole.get_categories()
    return jsonify(data=["category1", "category2"])


@app.route('/filter_products_by', methods=['POST'])
def filter_products_by():
    return jsonify(data=["Product1"])
    # if request.is_json:
    #     request_dict = request.get_json()
    #     products = request_dict.get('products')
    #     filter_option = request_dict.get('filter_option')  # by name, keyword or category
    #     input = request_dict.get('input')
    #     if filter_option == 1:
    #         min = input.min
    #         max = input.max
    #         response = GuestRole.search_products_by(products, filter_option, min, max)  # list of Products (Object)
    #     else:
    #         response = GuestRole.search_products_by(products, filter_option, input)  # list of Products (Object)


@app.route('/add_products_to_cart', methods=['POST'])
def add_products_to_cart():
    if request.is_json:
        request_dict = request.get_json()
        products = request_dict.get('products')
        response = GuestRole.save_products_to_basket(products)
        # if response:
        return jsonify(msg=response['msg'], data=response['response'])
    # return jsonify(msg="Registration failed", data=response['response'], status=400)


@app.route('/update_shopping_cart', methods=['POST'])
def update_shopping_cart():
    return jsonify(msg="Updated successfully!")


@app.route('/purchase_products', methods=['GET'])
async def purchase_products():
    response = GuestRole.purchase_products()
    if response:
        print(response)
        purchases = response["purchases"]
        print(purchases)
        await handle_purchase_msg(purchases[0])  # ["store_name"]
        return jsonify(data=response)
    return jsonify(msg="purchase products failed", data=response["response"], status=400)


@app.route('/confirm_purchase', methods=['POST'])
def confirm_purchase():
    if request.is_json:
        request_dict = request.get_json()
        address = request_dict.get('address')
        details = request_dict.get("purchases")
        response = GuestRole.confirm_payment(address, details)
        if response:
            return jsonify(msg=response['msg'], data=response['response'])
    return jsonify(msg="purchase confirmation failed", data=response["response"], status=400)


# AND MANY MORE OTHER FUNCTIONS ..... TODO

# ------------------------------ STORE OWNER AND MANAGER ROLE SERVICES ------------------------------------#


@app.route('/get_managed_stores', methods=['GET'])
def get_managed_stores():
    response = StoreOwnerOrManagerRole.get_managed_stores()
    return jsonify(data=response)


@app.route('/get_manager_permissions', methods=['POST'])
def get_manager_permissions():
    if request.is_json:
        request_dict = request.get_json()
        store_name = request_dict.get('store_name')  # str
        response = TradeControlService.get_manager_permissions(store_name)
        return jsonify(data=response)
    return jsonify(data=[])


@app.route('/get_owned_stores', methods=['GET'])
def get_owned_stores():
    response = StoreOwnerOrManagerRole.get_owned_stores()
    return jsonify(data=response["response"], msg=response["msg"])


@app.route('/appoint_store_manager', methods=['POST'])
def appoint_store_manager():
    if request.is_json:
        request_dict = request.get_json()
        appointee_nickname = request_dict.get('appointee_nickname')  # str
        store_name = request_dict.get('store_name')  # str
        permissions = request_dict.get('permissions')  # list of tuples
        response = StoreOwnerOrManagerRole.appoint_store_manager(appointee_nickname, store_name, permissions)
        if response:
            return jsonify(msg=response["msg"], data=response["response"])
    return jsonify(msg="Oops, communication error")


@app.route('/add_product', methods=['POST'])
def add_product():
    if request.is_json:
        request_dict = request.get_json()
        store_name = request_dict.get('store_name')  # str
        products_details = request_dict.get('products_details')  # list of tuples
        response = StoreOwnerOrManagerRole.add_products(store_name, products_details)
        if response:
            return jsonify(msg="Congrats! Product was added!")
    return jsonify(msg="Oops, product wasn't added")


# ------------------------------ SUBSCRIBER ROLE SERVICES -------------------------------------------------#


@app.route('/logout', methods=['GET'])
def logout():
    response = SubscriberRole.logout()
    if response:
        return jsonify(msg="Logged out successfully")
    return jsonify(msg="Logout failed")


@app.route('/open_store', methods=['POST'])
def open_store():
    if request.is_json:
        request_dict = request.get_json()
        store_name = request_dict.get('store_name')
        result = SubscriberRole.open_store(store_name)
        #   Websocket.open_store(store_name, SubscriberRole.username, result)
        # TODO - add some func at websocket that registers the owner
        # WebSocketService.open_store(store_name, SubscriberRole.username, result)
        # if response:
        return jsonify(data=result['response'], msg=result['msg'])
    return jsonify(msg="Oops, store wasn't opened")


@app.route('/view_personal_purchase_history', methods=['GET'])
def view_personal_purchase_history():
    # response = SubscriberRole.view_personal_purchase_history()
    # return jsonify(msg="Logged out successfully", data=response) # NEED TO BE CHEKED, STAM ASITI

    return jsonify(data=["purchase1", "purchase2"])


# ------------------------------ SYSTEM MANAGER ROLE SERVICES ---------------------------------------------#

# @app.route('/system_initialized', methods=['POST'])
# def system_initialized():
#     result = TradeControlService.is_sys_initialized()
#     return jsonify(data=result)

@app.route('/view_user_purchase_history', methods=['POST'])
def view_user_purchase_history():
    if request.is_json:
        request_dict = request.get_json()
        viewed_user = request_dict.get('nickname')
    #     response = SystemManagerRole.view_user_purchase_history(viewed_user)
    #     if response:  # if not None
    #         return jsonify(msg="success", data=response)
    # return jsonify(msg="fail", data=response)
    return jsonify(data=["user_purchase1", "user_purchase2"])


@app.route('/view_store_purchases_history', methods=['POST'])
def view_store_purchases_history():
    if request.is_json:
        request_dict = request.get_json()
        store_name = request_dict.get('store_name')
    #     response = SystemManagerRole.view_store_purchases_history(store_name)
    #     if response:  # if not None
    #         return jsonify(msg="success", data=response)
    # return jsonify(msg="fail", data=response)
    return jsonify(data=["store_purchase1", "store_purchase2"])


# ------------------------------ TRADE CONTROL SERVICE ----------------------------------------------------#

@app.route('/init_system', methods=['GET'])
def init_system():
    result = TradeControlService.init_system()
    return jsonify(data=result['response'], msg=result['msg'])


@app.route('/get_user_type', methods=['GET'])
def get_user_type():
    result = TradeControlService.get_user_type()
    return jsonify(data=result)


# ------------------------------ WEBSOCKET ----------------------------------------------------#

_users = {}  # dict of <username>: <its session ID>


@socket.on('connect')
def connect():
    print(f"connect event. sid --> {request.sid}")
    _users[TradeControlService.get_curr_username] = request.sid


@socket.on('subscribe')
def join(data):
    print("recieved join request")
    _users[data['username']] = request.sid
    join_room(room=data['store'], sid=_users[data['username']])
    print(f"{data['username']} has been subscribed to store {data['storename']}")


@socket.on('unsbscribe')
def leave(data):
    # TODO - add check that exists
    leave_room(room=data['store'], sid=_users[data['username']])
    print(f"{data['username']} has been removed as subscriber of store {data['storename']}")


def send_notification(store_name, msg):
    # socket.send(msgs, json=True, room=storename)
    # TODO - does it sends even if not logged in? maybe use the written store-funcs
    print(f"room = {store_name}")
    socket.emit('message', msg, room=store_name)  # event = str like 'purchase', 'remove_owner', 'new_owner'


def handle_purchase_msg(store_name):
    # if result:  # should be True or dict - TODO change the call to be inside if (result)
    msg = f"a purchase have been done at store {store_name}"
    send_notification(store_name, jsonify(messages=msg, store=store_name))
    print(f"send msg: {msg}")


def handle_remove_owner_msg(user_name, store_name):
    # if result:  # should be True or dict - TODO change the call to be inside if (result)
    msg = f"{user_name} was removed as owner from store {store_name}"
    send_notification(store_name, jsonify(username=user_name, messages=msg, store=store_name))
    print(f"send msg: {msg}")
