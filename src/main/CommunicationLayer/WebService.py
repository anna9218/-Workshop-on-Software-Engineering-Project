import eventlet
from flask import Flask, request
# import os
from flask_cors import CORS
from flask import jsonify

# from src.main.CommunicationLayer import WebSocketService
from src.main.CommunicationLayer.StorePublisher import StorePublisher
from src.main.DomainLayer.StoreComponent.ManagerPermission import ManagerPermission
from src.main.ServiceLayer.GuestRole import GuestRole
from src.main.ServiceLayer.StoreOwnerOrManagerRole import StoreOwnerOrManagerRole
from src.main.ServiceLayer.SubscriberRole import SubscriberRole
from src.main.ServiceLayer.TradeControlService import TradeControlService
from flask_socketio import SocketIO, join_room, leave_room
import os

app = Flask(__name__)
CORS(app)

socket = SocketIO(app, cors_allowed_origins='*')
# socket = SocketIO(app, logger=True, engineio_logger=True,
#                   cors_allowed_origins='*', async_mode='eventlet')

eventlet.monkey_patch()

app = Flask(__name__)
CORS(app)
app.secret_key = os.environ.get('SECRET')
app.config['WTF_CSRF_SECRET_KEY'] = "\xae\x5c{Xasa\x3b\x8e\x83\x19\xad\x24\x19\asda"
sio = SocketIO(app, logger=True, engineio_logger=True,
               cors_allowed_origins='*', async_mode='eventlet')


# 1 - purchase
# 2 - add+remove manager
# 3 - else


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
        response = GuestRole.search_products_by(search_option, input_str)  # list of Products (Object)
        return jsonify(msg=response["msg"], data=response["response"])
    return jsonify(msg="Oops, communication error.", data=[])


@app.route('/filter_products_by', methods=['POST'])
def filter_products_by():
    if request.is_json:
        request_dict = request.get_json()
        filter_option = request_dict.get('filter_option')  # by name, keyword or category
        products_ls = request_dict.get('products_ls')

        if filter_option == 1:
            min_price = request_dict.get('min_price')
            max_price = request_dict.get('max_price')
            response = GuestRole.filter_products_by(products_ls, filter_option, min_price=min_price,
                                                    max_price=max_price)  # list of Products (Object)
        else:
            if filter_option == 2:
                category = request_dict.get('category')
                response = GuestRole.filter_products_by(products_ls, filter_option,
                                                        category=category)  # list of Products (Object)

        return jsonify(msg=response["msg"], data=response["response"])
    return jsonify(msg="Oops, communication error.", data=[])


@app.route('/get_categories', methods=['GET'])
def get_categories():
    # response = GuestRole.get_categories()
    return jsonify(data=["category1", "category2"])


# @app.route('/filter_products_by', methods=['POST'])
# def filter_products_by():
#     return jsonify(data=["Product1"])
#     # if request.is_json:
#     #     request_dict = request.get_json()
#     #     products = request_dict.get('products')
#     #     filter_option = request_dict.get('filter_option')  # by name, keyword or category
#     #     input = request_dict.get('input')
#     #     if filter_option == 1:
#     #         min = input.min
#     #         max = input.max
#     #         response = GuestRole.search_products_by(products, filter_option, min, max)  # list of Products (Object)
#     #     else:
#     #         response = GuestRole.search_products_by(products, filter_option, input)  # list of Products (Object)


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
def purchase_products():
    response = GuestRole.purchase_products()
    if response:
        # print(response)
        purchases = response["purchases"]
        # print(purchases)
        # print(purchases[0])
        # print(purchases[0]["store_name"])
        # handle_purchase_msg(purchases[0]["store_name"]) TODO
        # print("after handle")
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
        response = StoreOwnerOrManagerRole.get_manager_permissions(store_name)
        numlist = [enum.value for enum in response]
        return jsonify(data=numlist)
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
        response = StoreOwnerOrManagerRole.appoint_store_manager(appointee_nickname, store_name,
                                                                 numbersToEnum(permissions))
        if response:
            return jsonify(msg=response["msg"], data=response["response"])
    return jsonify(msg="Oops, communication error")


@app.route('/remove_manager', methods=['POST'])
def remove_manager():
    if request.is_json:
        request_dict = request.get_json()
        appointee_nickname = request_dict.get('nickname')  # str
        store_name = request_dict.get('store_name')  # str
        response = StoreOwnerOrManagerRole.remove_manager(store_name, appointee_nickname)
        if response:
            return jsonify(msg="Removed manager " + appointee_nickname + " successfully!")
    return jsonify(msg="Oops, communication error")


@app.route('/appoint_store_owner', methods=['POST'])
def appoint_store_owner():
    if request.is_json:
        request_dict = request.get_json()
        appointee_nickname = request_dict.get('appointee_nickname')  # str
        store_name = request_dict.get('store_name')  # str
        response = StoreOwnerOrManagerRole.appoint_additional_owner(appointee_nickname, store_name)
        if response:
            return jsonify(msg=response["msg"], data=response["response"])
    return jsonify(msg="Oops, communication error")


@app.route('/get_managers_appointees', methods=['POST'])
def get_managers_appointees():
    if request.is_json:
        request_dict = request.get_json()
        store_name = request_dict.get('store_name')  # str
        response = StoreOwnerOrManagerRole.get_managers_appointees(store_name)
        return jsonify(data=response)
    return jsonify(data=[])


def numbersToEnum(ls):
    enumList: ManagerPermission = []
    for num in ls:
        if num == 1 and (ManagerPermission.EDIT_INV not in enumList):
            enumList.append(ManagerPermission.EDIT_INV)
        if num == 2 and (ManagerPermission.EDIT_POLICIES not in enumList):
            enumList.append(ManagerPermission.EDIT_POLICIES)
        if num == 3 and (ManagerPermission.APPOINT_OWNER not in enumList):
            enumList.append(ManagerPermission.APPOINT_OWNER)
        if num == 4 and (ManagerPermission.DEL_OWNER not in enumList):
            enumList.append(ManagerPermission.DEL_OWNER)
        if num == 5 and (ManagerPermission.APPOINT_MANAGER not in enumList):
            enumList.append(ManagerPermission.APPOINT_MANAGER)
        if num == 6 and (ManagerPermission.EDIT_MANAGER_PER not in enumList):
            enumList.append(ManagerPermission.EDIT_MANAGER_PER)
        if num == 7 and (ManagerPermission.DEL_MANAGER not in enumList):
            enumList.append(ManagerPermission.DEL_MANAGER)
        if num == 8 and (ManagerPermission.CLOSE_STORE not in enumList):
            enumList.append(ManagerPermission.CLOSE_STORE)
        if num == 9 and (ManagerPermission.USERS_QUESTIONS not in enumList):
            enumList.append(ManagerPermission.USERS_QUESTIONS)
        if num == 10 and (ManagerPermission.WATCH_PURCHASE_HISTORY not in enumList):
            enumList.append(ManagerPermission.WATCH_PURCHASE_HISTORY)
    return enumList


@app.route('/edit_manager_permissions', methods=['POST'])
def edit_manager_permissions():
    if request.is_json:
        request_dict = request.get_json()
        store_name = request_dict.get('store_name')  # str
        appointee_nickname = request_dict.get('appointee_nickname')  # str
        permissions = request_dict.get('permissions')  # str
        response = StoreOwnerOrManagerRole.edit_manager_permissions(store_name, appointee_nickname,
                                                                    numbersToEnum(permissions))
        if response:
            return jsonify(msg="Permissions of manager " + appointee_nickname + " were updated successfully!")
        else:
            return jsonify(msg="Oops, update permissions failed.")
    return jsonify(msg="Oops, communication error.")


@app.route('/get_policies', methods=['POST'])
def get_policies():
    if request.is_json:
        request_dict = request.get_json()
        store_name = request_dict.get('store_name')  # str
        policy_name = request_dict.get('policy_name')  # str
        response = StoreOwnerOrManagerRole.get_policies(policy_name, store_name)
        return jsonify(msg=response["msg"], data=response["response"])

    return jsonify(msg="Oops, communication error.")


@app.route('/add_product', methods=['POST'])
def add_product():
    if request.is_json:
        request_dict = request.get_json()
        store_name = request_dict.get('store_name')
        products_details = request_dict.get('products_details')
        response = StoreOwnerOrManagerRole.add_products(store_name, products_details)
        if response["response"]:
            return jsonify(msg="Congrats! Product was added!")
        return jsonify(msg="Oops, product wasn't added")


@app.route('/edit_product', methods=['POST'])
def edit_product():
    if request.is_json:
        errors = []
        request_dict = request.get_json()
        store_name = request_dict.get('store_name')
        product_name = request_dict.get('product_name')
        new_product_name = request_dict.get('new_product_name')
        amount = request_dict.get('amount')
        price = request_dict.get('price')
        category = request_dict.get('category')
        purchase_type = request_dict.get('purchase_type')

        if new_product_name is not None:
            if not StoreOwnerOrManagerRole.edit_product(store_name, product_name, "name", new_product_name)["response"]:
                errors.append("Product Name")
        if amount is not None:
            if not StoreOwnerOrManagerRole.edit_product(store_name, product_name, "amount", amount)["response"]:
                errors.append("Product Amount")
        if price is not None:
            if not StoreOwnerOrManagerRole.edit_product(store_name, product_name, "price", price)["response"]:
                errors.append("Product Price")
        if category is not None:
            if not StoreOwnerOrManagerRole.edit_product(store_name, product_name, "category", category)["response"]:
                errors.append("Category")
        if purchase_type is not None:
            if not StoreOwnerOrManagerRole.edit_product(store_name, product_name, "purchase_type", purchase_type)[
                "response"]:
                errors.append("Purchase Type")

        error_str = ""
        for error in errors:
            error_str += ", " + error

        if len(errors) == 0:
            return jsonify(msg="Congrats! Product was edited successfully!")
        return jsonify(msg="Oops, issue with product edit, couldn't update: " + error_str)


@app.route('/remove_product', methods=['POST'])
def remove_product():
    if request.is_json:
        request_dict = request.get_json()
        store_name = request_dict.get('store_name')
        products_name = request_dict.get('product_name')
        response = StoreOwnerOrManagerRole.remove_products(store_name, [products_name])
        if response:
            return jsonify(msg="Congrats! Product was removed!")
    return jsonify(msg="Oops, product wasn't removed")


@app.route('/get_product_details', methods=['POST'])
def get_product_details():
    if request.is_json:
        request_dict = request.get_json()
        store_name = request_dict.get('store_name')  # str
        products_details = request_dict.get('product_name')
        response = TradeControlService.get_product_details(store_name, products_details)
    return jsonify(data=response)


# ------------------------------ SUBSCRIBER ROLE SERVICES -------------------------------------------------#


@app.route('/logout', methods=['GET'])
def logout():
    response = SubscriberRole.logout()
    if response:
        return jsonify(msg="Logged out successfully!")
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
        websocket_open_store(TradeControlService.get_curr_username(), store_name)
        return jsonify(data=result['response'], msg=result['msg'])
    return jsonify(msg="Oops, store wasn't opened.")


@app.route('/view_personal_purchase_history', methods=['GET'])
def view_personal_purchase_history():
    response = SubscriberRole.view_personal_purchase_history()
    return jsonify(msg=response["msg"], data=response["response"])  # NEED TO BE CHEKED, STAM ASITI


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
_stores: [StorePublisher] = []  # list of StorePublisher


# @socket.on('')
@socket.on('connect')
def connect():
    print(f"connect event. sid --> {request.sid}")
    owner_username = TradeControlService.get_curr_username()
    print(f"curr_nickname = {owner_username}")
    if (owner_username is not None):
        _users[owner_username] = request.sid
        # print ("in if")
        for store in _stores:
            # print ("in for")
            if store.is_subscribed_to_store(owner_username):
                # print("before join")
                join_room(room=store.store_name(), sid=_users[owner_username])
                print(f"username {owner_username} is added as a subscriber to store {store.store_name()} publisher")

    print(f"users list: {_users}")


# @socket.on('join')
# def join(data):
#     print("recieved join request")
#     _users[data['username']] = request.sid
#     join_room(room=data['store'], sid=_users[data['username']])
#     print(f"{data['username']} has been subscribed to store {data['storename']}")

def websocket_open_store(username, storename):
    if get_store(storename) is None:
        # print(f"open store (name = {storename}) msg from {username} ")
        if _users:
            append_user_to_room(storename, username)
            print (f"append user {username} to store {storename}")
        create_new_publisher(storename, username)
        return True
    return False


def create_new_publisher(storename, username):
    if get_store(storename) is None:
        store = StorePublisher(storename, username)
        # print(f"store = {store}")
        _stores.append(store)
        # print(f"{storename} has been added by {username}")
        store.subscribe_owner(username)
        return True
    return False


def append_user_to_room(storename, username):
    _users[username] = request.sid
    # print(f"users = {_users}")
    join_room(room=storename, sid=_users[username])
    # print(f"{username} has been subscribed to store {storename}")


@socket.on('unsubscribe')
def leave(data):
    # TODO - add check that exists
    leave_room(room=data['store'], sid=_users[data['username']])
    print(f"{data['username']} has been removed as subscriber of store {data['storename']}")


# TODO - add a call from remove_owner func
def unsbscribe(username, storename):
    leave_room(room=storename, sid=_users[username])
    # print(f"{username} has been removed as subscriber of store {storename}")


def notify_all(store_name, msg):
    # socket.send(msgs, json=True, room=storename)
    print(f"room = {store_name}, msg = {msg}")
    socket.emit('message', msg, room=store_name)  # event = str like 'purchase', 'remove_owner', 'new_owner'
    # socket.send({
    #         'messages': [msg]
    #     }, room=store_name)


def handle_purchase_msg(store_name):
    # msg = f"a purchase has been done at store {store_name}"
    # print(f"send msg: {msg}")
    notify_all(store_name, jsonify(messages=msg, store=store_name))


def handle_remove_owner_msg(user_name, store_name):
    msg = f"{user_name} was removed as owner from store {store_name}"
    notify_all(store_name, jsonify(username=user_name, messages=msg, store=store_name))
    # print(f"send msg: {msg}")


def get_store(store_name) -> StorePublisher:
    for store in _stores:
        if store.store_name() == store_name:
            return store
    return None


def add_subscriber_to_store(store_name, owner_nickname):
    store = get_store(store_name)
    if store is None:
        # print(f"store {store_name} is none, owner is {owner_nickname}")
        return False
    if store.is_subscribed_to_store(owner_nickname):
        return False
    store.subscribe_owner(owner_nickname)
    return True


def remove_subscriber_from_store(store_name, owner_nickname):
    store = get_store(store_name)
    if store is None:
        return -2
    return store.unsubscribe_owner(owner_nickname)


def is_subscribed_to_store(store_name, nickname):
    store = get_store(store_name)
    if store is not None:
        return store.is_subscribed_to_store(nickname)
    # print(f"store {store_name} is none. nickname is {nickname}")
    return False
