from flask import Flask, escape, request
# import os
from flask_cors import CORS
from flask import jsonify
from src.main.ServiceLayer.GuestRole import GuestRole

app = Flask(__name__)
CORS(app)


# ------------------------------ GUEST ROLE SERVICES ------------------------------------#
@app.route('/register', methods=['POST'])
def register():
    if request.is_json:
        request_dict = request.get_json()
        nickname = request_dict.get('nickname')
        password = request_dict.get('password')
        response = GuestRole.register(nickname, password)  # BUG - returns None (instead of True/False)
        return jsonify(msg="Registered successfully!")
    return jsonify(msg="Registration failed", status=400)


@app.route('/login', methods=['POST'])
def login():
    if request.is_json:
        request_dict = request.get_json()
        nickname = request_dict.get('nickname')
        password = request_dict.get('password')
        response = GuestRole.login(nickname, password)  # MAYBE BUG - returns None (instead of True/False)
        return jsonify(msg="Logged in successfully!")
    return jsonify(msg="Login failed", status=400)


@app.route('/display_stores', methods=['GET'])
def display_stores():
    # response = GuestRole.display_stores()  # BUG
    return jsonify(data=["success"])


@app.route('/view_shopping_cart', methods=['GET'])
def view_shopping_cart():
    # response = GuestRole.view_shopping_cart()
    return jsonify(data=["success"])


# AND MANY MORE OTHER FUNCTIONS ..... TODO

# ------------------------------ STORE OWNER AND MANAGER ROLE SERVICES ------------------------------------#

# ------------------------------ SUBSCRIBER ROLE SERVICES -------------------------------------------------#

# ------------------------------ SYSTEM MANAGER ROLE SERVICES ---------------------------------------------#

# ------------------------------ TRADE CONTROL SERVICE ----------------------------------------------------#

