"""
    abstract class representing the:
                                    - implementor in the Bridge pattern
                                    - target in the adapter pattern
                                    - subject in the proxy pattern  
"""
# from __future__ import annotations
from abc import ABC, abstractmethod
from datetime import datetime

from Backend.src.Logger import logger


class Bridge(ABC):

    def __init__(self):
        super().__init__()

    @abstractmethod
    # init system functions
    def init_sys(self) -> bool:
        pass

    @abstractmethod
    def is_payment_connected(self) -> bool:
        pass

    @abstractmethod
    def is_delivery_connected(self) -> bool:
        pass

    @abstractmethod
    def cause_connection_err_payment(self):
        pass

    @abstractmethod
    def cause_connection_err_delivery(self):
        pass

    # Register tests bridged functions
    @abstractmethod
    def register_user(self, nickname: str, password: str) -> bool:
        pass

    @abstractmethod
    def delete_user(self, nickname: str):
        pass

    @abstractmethod
    def delete_manager(self, store_name: str, appointee_nickname: str):
        pass

    # login functions
    @abstractmethod
    def login(self, nickname: str, password: str) -> bool:
        pass

    # view stores' products functions
    @abstractmethod
    def view_stores(self) -> bool:
        pass

    @abstractmethod
    def display_stores_or_products_info(self, store_name: str, store_info_flag: bool, products_info_flag: bool) -> bool:
        pass

    # search and filter products functions
    @abstractmethod
    def search_product(self, search_option: int, string: str) -> bool:
        pass

    @abstractmethod
    def filter_products(self, filter_details, products) -> bool:
        pass

    # save products functions
    @abstractmethod
    def add_products_to_cart(self, product_name: str, store_name: str, amount: int, discount_type: int,
                             purchase_type: int) -> bool:
        pass

    # update cart
    @abstractmethod
    def view_shopping_cart(self):
        pass

    @abstractmethod
    def update_shopping_cart(self, flag: str,
                             products_details: [{"product_name": str, "store_name": str, "amount": int}]):
        pass

    # purchase cart
    @abstractmethod
    def purchase_products(self) -> dict:
        pass

    @abstractmethod
    def confirm_purchase(self, address: str, purchase_ls: dict) -> bool:
        pass

    @abstractmethod
    def remove_purchase(self, store_name: str, purchase_date: datetime):
        pass

    # logout functions
    @abstractmethod
    def logout(self) -> bool:
        pass

    # open store functions
    @abstractmethod
    def open_store(self, store_name: str) -> bool:
        pass

    @abstractmethod
    def delete_store(self, store_name: str) -> bool:
        pass

    # view personal purchase history
    @abstractmethod
    def view_personal_purchase_history(self) -> bool:
        pass

    # manage stock functions
    @abstractmethod
    def add_products_to_store(self, store_name: str, products_details:
                                            [{"name": str, "price": int, "category": str, "amount": int}]) -> bool:
        pass

    @abstractmethod
    def edit_products_in_store(self, store_name: str, product_name: str, op: str, new_value: str) -> bool:
        pass

    @abstractmethod
    def remove_products_from_store(self, store_name: str, products_names: list):
        pass

    # add store owner functions
    @abstractmethod
    def appoint_additional_owner(self, nickname: str, store_name: str):
        pass

    # add store manager functions
    @abstractmethod
    def appoint_additional_manager(self, nickname, store_name, permissions: [int]):
        pass

    @abstractmethod
    def edit_manager_permissions(self, store_name: str, appointee_nickname: str, permissions: list) -> bool:
        pass

    @abstractmethod
    # remove manager functions
    def remove_manager(self, store_name: str, manager_nickname: str):
        pass

    @abstractmethod
    def view_store_purchase_history(self, store_name: str):
        pass

    @abstractmethod
    def subscribe_user(self, nickname: str, password: str):
        pass

    # view users' and stores' purchase history
    @abstractmethod
    def manager_view_user_purchases(self, nickname: str):
        pass

    @abstractmethod
    def manager_view_shop_purchase_history(self, store_name: str):
        pass

    # Payment System tests bridged functions
    @abstractmethod
    def connect_payment_sys(self):
        pass

    @abstractmethod
    def commit_payment(self, product_ls) -> bool:
        pass

    @abstractmethod
    def disconnect_payment_sys(self):
        pass

    # delivery System tests bridged functions
    @abstractmethod
    def connect_delivery_sys(self):
        pass

    @abstractmethod
    def deliver(self, address: str, products_ls) -> bool:
        pass

    @abstractmethod
    def disconnect_delivery_sys(self):
        pass

    @abstractmethod
    def set_user(self, nickname: str):
        pass

    def __repr__(self):
        return repr("Bridge")