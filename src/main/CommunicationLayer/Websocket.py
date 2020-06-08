import asyncio
from typing import Tuple

import jsonpickle
import websockets
from flask_socketio import join_room, leave_room
from jsonpickle import json

from src.main.CommunicationLayer import WebService
from src.main.CommunicationLayer.StorePublisher import Store

from flask import Flask, render_template, jsonify
# class Websocket:
#
# # maybe need to replace the run command at main
# def set_socket(s):
# socket = s
#
# def get_socket():
#     return socket
#
# @socket.on('join')
# async def join(data):
#     join_room(room=data['store'], sid=data['username'])
#
# @socket.on('leave')
# async def leave(data):
#     leave_room(room=data['store'], sid=data['username'])
#
# async def send_notification(event, store_name, msg):
#     # socket.send(msgs, json=True, room=storename)
#     socket.emit(event, msg, room=store_name)  # event = str like 'purchase', 'remove_owner', 'new_owner'
#
# def handle_purchase(user_name, store_name, result):
#     if result:  # should be True or dict - TODO change the call to be inside if (result)
#         msg = f"{user_name} made a purchase on store {store_name}"
#         send_notification('purchase', store_name, msg)

# _stores = []  # (ConnectionLayerStore, list of (username_websocket) of its online subscribers)
# _connections: Tuple = ()  # (username, it's websocket)
#

# async def handle_new_msg(websocket, path):
#     msg = await websocket.recv()
#     content = msg.msg
#     if content is 'openStore':
#         handle_new_connection(msg, path)
#     elif content is 'login':
#         handle_login(msg, path)
#     elif content is 'logout':
#         handle_login(msg, path)
#     else:
#         print(f"unrecognized msg: {content}")  # TODO
#
#
# async def handle_new_connection(msg, path):
#     print(f"new connection! {path}")
#     pass
#
#
# async def handle_login(msg, path):
#     pass
#
#
# async def handle_logout(msg, path):
#     pass
#
#
# # ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
# # localhost_pem = pathlib.Path(__file__).with_name("localhost.pem")
# # ssl_context.load_cert_chain(localhost_pem)
# #
# wait_for_msgs = websockets.serve(
#     handle_new_msg, "localhost", 8765
#     # handle_new_msg, "localhost", 8765, ssl=ssl_context
# )
#
# asyncio.get_event_loop().run_until_complete(wait_for_msgs)
# asyncio.get_event_loop().run_forever()
