"""
    abstract class representing the:
                                    - implementor in the Bridge pattern
                                    - target in the adapter pattern
                                    - subject in the proxy pattern  
"""
# from __future__ import annotations
from abc import ABC, abstractmethod
from datetime import datetime


class Bridge(ABC):

    def __init__(self):
        super().__init__()

    @abstractmethod
    # init system functions
    def init_sys(self) -> bool:
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
    def confirm_purchase(self, delivery_details: {'name': str, 'address': str, 'city': str, 'country': str, 'zip': str},
                        payment_details: {'card_number': str, 'month': str, 'year': str, 'holder': str,
                                          'ccv': str, 'id': str},
                        purchase_ls: []) -> bool:
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
                                            [{"name": str, "price": int, "category": str, "amount": int,
                                              "purchase_type": int}]) -> bool:
        pass

    @abstractmethod
    def edit_products_in_store(self, store_name: str, product_name: str, op: str, new_value: str) -> bool:
        pass

    @abstractmethod
    def remove_products_from_store(self, store_name: str, products_names: list):
        pass

    # 4.2 add and update purchase and discount policies
    def set_purchase_operator(self, store_name: str, operator: str):
        pass

    def get_policies(self, policy_type: str, store_name: str) -> [dict] or None:
        pass

    # 4.4
    def remove_owner(self, appointee_nickname: str, store_name: str) -> {'response': [], 'msg': str}:
        pass

    def get_store(self, store_name):
        pass

    def update_purchase_policy(self, store_name: str, details: {"name": str, "products": [str] or None,
                                                                "min_amount": int or None,
                                                                "max_amount": int or None,
                                                                "dates": [dict] or None, "bundle": bool or None}):
        pass

    def define_purchase_policy(self, store_name: str, details: {"name": str, "products": [str],
                                                                "min_amount": int or None,
                                                                "max_amount": int or None,
                                                                "dates": [dict] or None, "bundle": bool or None}):
        pass

    @abstractmethod
    def update_discount_policy(self, store_name: str, policy_name: str,
                               percentage: float = -999,
                               valid_until: datetime = None,
                               discount_details: {'name': str,
                                                  'product': str} = None,
                               discount_precondition: {'product': str,
                                                       'min_amount': int or None,
                                                       'min_basket_price': str or None} or None = None):
        pass

    @abstractmethod
    def define_composite_policy(self, store_name: str, policy1_name: str, policy2_name: str, flag: str,
                                percentage: float, name: str, valid_until: datetime) -> {}:
        pass

    @abstractmethod
    def define_discount_policy(self, store_name: str,
                               percentage: float,
                               valid_until: datetime,
                               discount_details: {'name': str,
                                                  'product': str},
                               discount_precondition: {'product': str,
                                                       'min_amount': int or None,
                                                       'min_basket_price': str or None} or None = None
                               ):
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
    def is_payment_connected(self) -> bool:
        pass

    @abstractmethod
    def commit_payment(self, payment_details: {'card_number': str, 'month': str, 'year': str, 'holder': str,
                                               'ccv': str, 'id': str}) -> {'response': bool, 'msg': str, "tid": str or None}:
        pass

    @abstractmethod
    def cancel_payment_supply(self, transaction_id: str) -> bool:
        pass

    @abstractmethod
    def cause_payment_timeout(self):
        pass

    @abstractmethod
    def cause_payment_con_error(self):
        pass

    @abstractmethod
    def set_connection_payment_back(self):
        pass

    # delivery System tests bridged functions
    @abstractmethod
    def deliver(self, delivery_details: {'name': str, 'address': str, 'city': str, 'country': str,
                                                  'zip': str}) -> {'response': bool, 'msg': str, "tid": str or None}:
        pass

    @abstractmethod
    def cancel_delivery_supply(self, transaction_id: str) -> bool:
        pass

    @abstractmethod
    def is_delivery_connected(self) -> bool:
        pass

    @abstractmethod
    def cause_delivery_timeout(self):
        pass

    @abstractmethod
    def cause_delivery_con_error(self):
        pass

    @abstractmethod
    def set_connection_delivery_back(self):
        pass

    @abstractmethod
    def set_user(self, nickname: str):
        pass

    def __repr__(self):
        return repr("Bridge")