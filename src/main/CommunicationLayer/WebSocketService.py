import asyncio
import pathlib
import ssl
from collections import Set
from typing import Tuple

import websockets
from jsonpickle import json

from src.main.CommunicationLayer.Store import Store

# SHOULD SEND ONLY JSON BETWEEN

_stores = []  # (ConnectionLayerStore, list of (username_websocket) of its online subscribers)
_connections : Tuple = () # (username, it's websocket)

def open_store(store_name, owner_nickname, result):
    if result and get_store(store_name) is None:  # should be true/false if Eden have'nt changed it to dictionary
        _stores.append (Store(store_name, owner_nickname))  # TODO - add ws? how?
        # maybe replace with registration msg and open new websocket in first store ownership
        # maybe even replace websockets of subscribers in each login/logout
        # still keep some logic with the service so there will be no hacks


def in_connections(username_to_check):
    for username, ws in _connections:
        if username == username_to_check:
            return True
    return False


async def handle_new_connection(websocket):
    msg = await websocket.recv()  # {username, (list of) stores, msg, (list of) ids}
    if msg.msg != 'connect':  # new - {username, msg}
        return
    for store in _stores:
        # for username, ws in username_ws_tuple:
        if store.is_subscribed_to_store(msg.username) and not in_connections(msg.username):
            _connections.append((msg.username, websocket))
            msgs = store.notify(msg.username)

        # if s.store_name() in msg.stores:
        #     index = _stores.index(s)
        #     id = msg.ids[index]
        #     while id < s.amount_of_msgs():
        #         unreadMsg = s.retrieve_msg_by_id(msg.username, id)
        #         newMsg = unreadMsg  # TODO - create msg as need with the id = id+1
        #         id += 1
        #         json.jsonify()
        #         websocket.send(json.parse(newMsg))


# ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
# localhost_pem = pathlib.Path(__file__).with_name("localhost.pem")
# ssl_context.load_cert_chain(localhost_pem)

sendUnreadMsgs = websockets.serve(  # maybe send instead of serve
    # handle_login, "localhost", 8765, ssl=ssl_context  # should be sending the unread msgs
    handle_new_connection, "localhost", 8765  # should be sending the unread msgs
)


async def handle_purchase(user_name, store_name, result):
    # msg = await websocket.recv()  # {username, (list of) stores, msg, (list of) ids}
    # if msg.msg != 'logout':
    #     return
    if result:  # should be True or dict
        store = get_store(store_name)
        if store is not None:
            # index = _stores.index(store)
            # id = msg.ids[index]
            # while id < store.amount_of_msgs():
            #     unreadMsg = store.get_msg_by_id(id)
            #     newMsg = unreadMsg  # TODO - update the id also and create msg
            #     id += 1
            #     json.jsonify()
            #     websocket.send(json.parse(newMsg))
            store.add_msg(user_name + ' made a purchase on store ' + store_name)
            store.notifyAll()

async def send_msg (send_to_username, msg):
    for username, ws in _connections:
        if send_to_username == username:
           json.jsonify()
           ws.send(json.parse(msg))

#
# ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
# localhost_pem = pathlib.Path(__file__).with_name("localhost.pem")
# ssl_context.load_cert_chain(localhost_pem)

# notifyPurchase = websockets.serve(
#     handle_purchase, "localhost", 8765
#     # handle_purchase, "localhost", 8765, ssl=ssl_context
# )


async def handle_logout(websocket):
    msg = await websocket.recv()  # {username, (list of) stores, msg, (list of) ids}
    if msg.msg != 'logout':  # new - {username, msg}
        return
    for username, ws in _connections:
        if username == msg.username:
            _connections.remove((username, ws))
        # if s.store_name() in msg.stores:


#             index = _stores.index(s)
#             client_last_id = msg.ids[index]
# if (client_last_id < s.get_last_read_msg_id(msg.username)):# TODO ?

# ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
# localhost_pem = pathlib.Path(__file__).with_name("localhost.pem")
# ssl_context.load_cert_chain(localhost_pem)
#
recieveLogoutMsg = websockets.serve(
    handle_logout, "localhost", 8765
    # handle_logout, "localhost", 8765, ssl=ssl_context
)

asyncio.get_event_loop().run_until_complete(sendUnreadMsgs)


# asyncio.get_event_loop().run_until_complete(notifyPurchase) # maybe replace it with store.notify
# asyncio.get_event_loop().run_until_complete(recieveLogoutMsg)
# asyncio.get_event_loop().run_forever()  # TODO - delete?

def get_store(store_name) -> Store:
    for store in _stores:
        if store.store_name() == store_name:
            return store
    return None


def add_subscriber_to_store(store_name, owner_nickname, result):
    if result:  # should be true/false if Eden have'nt changed it to dictionary
        store = get_store(store_name)
        store.subscribe_owner(owner_nickname)


def remove_subscriber_from_store(store_name, owner_nickname, result):
    if result:  # should be true/false if Eden have'nt changed it to dictionary
        store = get_store(store_name)
        store.unsubscribe_owner(owner_nickname)


def is_subscribed_to_store(store_name, nickname):
    store = get_store(store_name)
    return store.is_subscribed_to_store(nickname)
