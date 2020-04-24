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
