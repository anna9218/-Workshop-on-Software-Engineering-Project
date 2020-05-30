import asyncio
import pathlib
import ssl
import websockets

from flask import json

from src.main.CommunicationLayer.Store import Store

# SHOULD SEND ONLY JSON BETWEEN

# add at WebService.purchase_products a connection to websocket func IF COMPLETED SUCCESSFULLY
# maybe the check of success will be here
# MAYBE THIS WILL BE THE STORE-CONTROLLER

_stores = [] # list <Store>


async def handle_login(websocket):
    msg = await websocket.recv()  # {username, (list of) stores, msg, (list of) ids}
    if msg.msg != 'login':
        return
    for s in _stores:
        if s.store_name() in msg.stores:
            index = _stores.index(s)
            id = msg.ids[index]
            while id < s.amount_of_msgs():
                unreadMsg = s.retrieve_msg_by_id(msg.username, id)
                newMsg = unreadMsg  # TODO - create msg as need with the id = id+1
                id += 1
                json.jsonify()
                websocket.send(json.parse(newMsg))


ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
localhost_pem = pathlib.Path(__file__).with_name("localhost.pem")
ssl_context.load_cert_chain(localhost_pem)

sendUnreadMsgs = websockets.serve(  # maybe send instead of serve
    handle_login, "localhost", 8765, ssl=ssl_context  # should be sending the unread msgs
)


async def handle_purchase(websocket, user_name, msg):
    msg = await websocket.recv()  # {username, (list of) stores, msg, (list of) ids}
    if msg.msg != 'logout':
        return
    for s in _stores:
        if s.store_name() in msg.stores:
            index = _stores.index(s)
            id = msg.ids[index]
            while id < s.amount_of_msgs():
                unreadMsg = s.get_msg_by_id(id)
                newMsg = unreadMsg  # TODO - update the id also and create msg
                id += 1
                json.jsonify()
                websocket.send(json.parse(newMsg))

ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
localhost_pem = pathlib.Path(__file__).with_name("localhost.pem")
ssl_context.load_cert_chain(localhost_pem)

notifyPurchase = websockets.serve(
    handle_purchase, "localhost", 8765, ssl=ssl_context
)


# async def handle_logout(websocket):
#     msg = await websocket.recv()  # {username, (list of) stores, msg, (list of) ids}
#     if msg.msg != 'logout':
#         return
#     for s in _stores:
#         if s.store_name() in msg.stores:
#             index = _stores.index(s)
#             client_last_id = msg.ids[index]
            # if (client_last_id < s.get_last_read_msg_id(msg.username)):# TODO ?

# ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
# localhost_pem = pathlib.Path(__file__).with_name("localhost.pem")
# ssl_context.load_cert_chain(localhost_pem)
#
# recieveLogoutMsg = websockets.serve(
#     handle_logout, "localhost", 8765, ssl=ssl_context
# )

asyncio.get_event_loop().run_until_complete(sendUnreadMsgs)
asyncio.get_event_loop().run_until_complete(notifyPurchase) # maybe replace it with store.notify
# asyncio.get_event_loop().run_until_complete(recieveLogoutMsg)
asyncio.get_event_loop().run_forever()  # TODO - delete?


def open_store(store_name, owner_nickname, result):
    if result: # should be true/false if Eden have'nt changed it to dictionary
        _stores.append(Store(store_name, owner_nickname))


def get_store(store_name) -> Store:
    for store in _stores:
        if store.store_name() == store_name:
            return store
    return None


def add_subscriber_to_store(store_name, owner_nickname, result):
    if result: # should be true/false if Eden have'nt changed it to dictionary
        store = get_store(store_name)
        store.subscribe_owner(owner_nickname)


def remove_subscriber_from_store(store_name, owner_nickname, result):
    if result: # should be true/false if Eden have'nt changed it to dictionary
        store = get_store(store_name)
        store.unsubscribe_owner(owner_nickname)