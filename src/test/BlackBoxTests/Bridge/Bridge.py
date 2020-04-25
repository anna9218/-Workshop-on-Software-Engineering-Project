"""
    abstract class representing the:
                                    - implementor in the Bridge pattern
                                    - target in the adapter pattern
                                    - subject in the proxy pattern  
"""
# from __future__ import annotations
from abc import ABC, abstractmethod


class Bridge(ABC):

    def __init__(self):
        super().__init__()

    # Register tests bridged functions
    @abstractmethod
    def register_user(self, username, password) -> bool:
        pass

    # Payment System tests bridged functions
    @abstractmethod
    def connect_payment_sys(self):
        pass

    @abstractmethod
    def commit_payment(self, username, amount, credit, date) -> bool:
        pass

    @abstractmethod
    def disconnect_payment_sys(self):
        pass

    def is_delivery_connected(self):
        pass

    # delivery System tests bridged functions
    @abstractmethod
    def connect_delivery_sys(self):
        pass

    @abstractmethod
    def deliver(self, username, address) -> bool:
        pass

    @abstractmethod
    def disconnect_delivery_sys(self):
        pass

    def is_payment_connected(self):
        pass

    # init system functions
    def init_sys(self):
        pass

    def remove_user(self, username):
        pass

    # login functions
    def login(self, username, password):
        pass

    # logout functions
    def logout(self):
        pass

    # search products functions
    def search_product(self, option, string):
        pass

    def filter_products(self, filter_details, products):
        pass

    # view stores' products functions
    def view_stores(self):
        pass

    def view_store_info(self, store, store_info_flag, products_flag):
        pass

    # save products functions
    def add_products_to_cart(self):
        pass

    # view personal history functions
    def view_personal_history(self):
        pass

    # open store functions
    def open_store(self, name):
        pass

    def delete_store(self, store):
        pass

    # manage stock functions
    def add_products_to_store(self, user_nickname, store_name, products_details):
        pass

    def edit_products_in_store(self, nickname, store_name, product_name, op, new_value):
        pass

    def remove_products_from_store(self, user_nickname, store_name, products_names):
        pass
