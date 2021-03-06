"""
    abstract class representing the abstraction in the Bridge pattern
"""
from abc import ABC, abstractmethod
from datetime import datetime

from src.test.BlackBoxTests.AcceptanceTests.Driver import Driver
import unittest


class ProjectAT(ABC, unittest.TestCase):

    # setup for all tests
    @abstractmethod
    def setUp(self) -> None:
        self.__bridge = Driver().get_bridge()
        self._username = "username"
        self._password = "password"
        self._store_name = "store"

    # default functions to be implemented in inheriting classes (not in parent class)
    @abstractmethod
    def test_success(self):
        pass

    @abstractmethod
    def test_fail(self):
        pass

    # bridged functions

    # 1.1 init system functions
    def init_sys(self) -> bool:
        return self.__bridge.init_sys()

    def delete_user(self, nickname: str):
        self.__bridge.delete_user(nickname)

    def delete_manager(self, store_name: str, appointee_nickname: str):
        self.__bridge.delete_manager(store_name, appointee_nickname)

    # 2.2 Register tests functions
    def register_user(self, nickname: str, password: str) -> bool:
        return self.__bridge.register_user(nickname, password)

    # 2.3 login functions
    def login(self, nickname: str, password: str) -> bool:
        return self.__bridge.login(nickname, password)

    # 2.4 view stores' products functions
    def view_stores(self) -> bool:
        return self.__bridge.view_stores()

    def display_stores_or_products_info(self, store_name: str, store_info_flag: bool, products_info_flag: bool) -> bool:
        return self.__bridge.display_stores_or_products_info(store_name, store_info_flag, products_info_flag)

    # 2.5 search products functions
    def search_products_by(self, search_option: int, string: str):
        return self.__bridge.search_product(search_option, string)

    def filter_products_by(self, filter_details, products):
        return self.__bridge.filter_products(filter_details, products)

    # 2.6 save products to cart
    def add_products_to_cart(self, product_name: str, store_name: str, amount: int, discount_type: int,
                             purchase_type: int) -> bool:
        return self.__bridge.add_products_to_cart(product_name, store_name, amount, discount_type,  purchase_type)

    # 2.7 update cart
    def view_shopping_cart(self):
        return self.__bridge.view_shopping_cart()

    def update_shopping_cart(self, flag: str,
                             products_details: [{"product_name": str, "store_name": str, "amount": int}]):
        return self.__bridge.update_shopping_cart(flag, products_details)

    # 2.8 purchase products
    def purchase_products(self) -> dict:
        return self.__bridge.purchase_products()

    def confirm_purchase(self, delivery_details: {'name': str, 'address': str, 'city': str, 'country': str, 'zip': str},
                         payment_details: {'card_number': str, 'month': str, 'year': str, 'holder': str,
                                           'ccv': str, 'id': str},
                         purchase_ls: []) -> bool:
        return self.__bridge.confirm_purchase(delivery_details, payment_details, purchase_ls)

    def remove_purchase(self, store_name: str, purchase_date: datetime):
        self.__bridge.remove_purchase(store_name, purchase_date)

    # 3.1 logout functions
    def logout(self) -> bool:
        return self.__bridge.logout()

    # 3.2 open store functions
    def open_store(self, store_name: str) -> bool:
        return self.__bridge.open_store(store_name)

    def remove_store(self, store_name: str):
        self.__bridge.delete_store(store_name)

    # 3.7 view personal history functions
    def view_personal_purchase_history(self):
        return self.__bridge.view_personal_purchase_history()

    # 4.1 manage stock functions
    def add_products_to_store(self, store_name: str, products_details:
                                            [{"name": str, "price": int, "category": str, "amount": int,
                                              "purchase_type": int}]) -> bool:
        return self.__bridge.add_products_to_store(store_name, products_details)

    def edit_products_in_store(self, store_name: str, product_name: str, op: str, new_value: str) -> bool:
        return self.__bridge.edit_products_in_store(store_name, product_name, op, new_value)

    def remove_products_from_store(self, store_name: str, products_names: list) -> bool:
        return self.__bridge.remove_products_from_store(store_name, products_names)

    # 4.2 add and update purchase and discount policies
    def set_purchase_operator(self, store_name: str, operator: str):
        self.__bridge.set_purchase_operator(store_name, operator)

    def get_policies(self, policy_type: str, store_name: str) -> [dict] or None:
        return self.__bridge.get_policies(policy_type, store_name)

    def update_purchase_policy(self, store_name: str, details: {"name": str, "products": [str] or None,
                                                                "min_amount": int or None, "max_amount": int or None,
                                                                "dates": [dict] or None, "bundle": bool or None}):
        return self.__bridge.update_purchase_policy(store_name, details)

    def define_purchase_policy(self, store_name: str, details: {"name": str, "products": [str],
                                                                "min_amount": int or None, "max_amount": int or None,
                                                                "dates": [dict] or None, "bundle": bool or None}):
        return self.__bridge.define_purchase_policy(store_name, details)

    def update_discount_policy(self, store_name: str, policy_name: str,
                               percentage: float = -999,
                               valid_util: datetime = None,
                               discount_details: {'name': str,
                                                  'product': str} = None,
                               discount_precondition: {'product': str,
                                                       'min_amount': int or None,
                                                       'min_basket_price': str or None} or None = None):
        return self.__bridge.update_discount_policy(store_name, policy_name, percentage, valid_util,
                                                    discount_details, discount_precondition)

    def define_composite_policy(self, store_name: str, policy1_name: str, policy2_name: str, flag: str,
                                percentage: float, name: str, valid_until: datetime) -> {}:
        return self.__bridge.define_composite_policy(store_name, policy1_name, policy2_name, flag, percentage, name,
                                                     valid_until)

    def define_discount_policy(self, store_name: str,
                               percentage: float,
                               valid_until: datetime,
                               discount_details: {'name': str,
                                                  'product': str},
                               discount_precondition: {'product': str,
                                                       'min_amount': int or None,
                                                       'min_basket_price': str or None} or None = None
                               ):
        return self.__bridge.define_discount_policy(store_name, percentage, valid_until, discount_details,
                                                    discount_precondition)

    # 4.3 add store owner functions
    def appoint_additional_owner(self, nickname: str, store_name: str) -> bool:
        return self.__bridge.appoint_additional_owner(nickname, store_name)

    # 4.4 remove store owner
    def remove_owner(self, appointee_nickname: str, store_name: str) -> {'response': [], 'msg': str}:
        return self.__bridge.remove_owner(appointee_nickname, store_name)

    def get_store(self, store_name):
        return self.__bridge.get_store(store_name)

    # 4.5 appoint store manager functions
    def appoint_additional_manager(self, nickname: str, store_name: str, permissions: [int]) -> bool:
        return self.__bridge.appoint_additional_manager(nickname, store_name, permissions)

    # 4.6 edit manager permissions
    def edit_manager_permissions(self, store_name: str, appointee_nickname: str, permissions: list) -> bool:
        return self.__bridge.edit_manager_permissions(store_name, appointee_nickname, permissions)

    # 4.7 remove manager functions
    def remove_manager(self, store_name: str, manager_nickname: str) -> bool:
        return self.__bridge.remove_manager(store_name, manager_nickname)

    def subscribe_user(self, nickname: str, password: str):
        self.__bridge.subscribe_user(nickname, password)

    # 4.10 view store purchase history
    def view_store_purchase_history(self, store_name: str):
        return self.__bridge.view_store_purchase_history(store_name)

    # 6.4 view users' and stores' purchase history
    def manager_view_user_purchases(self, nickname: str):
        return self.__bridge.manager_view_user_purchases(nickname)

    def manager_view_shop_purchase_history(self, store_name: str):
        return self.__bridge.manager_view_shop_purchase_history(store_name)

    # 7 payment system
    def commit_payment(self, payment_details: {'card_number': str, 'month': str, 'year': str, 'holder': str,
                                               'ccv': str, 'id': str}) -> bool:
        return self.__bridge.commit_payment(payment_details)

    def is_payment_sys_connected(self):
        return self.__bridge.is_payment_connected()

    def cancel_payment_supply(self, transaction_id: str) -> bool:
        return self.__bridge.cancel_payment_supply(transaction_id)

    def cause_payment_timeout(self):
        self.__bridge.cause_payment_timeout()

    def cause_payment_con_error(self):
        self.__bridge.cause_payment_con_error()

    def set_connection_payment_back(self):
        self.__bridge.set_connection_payment_back()

    # 8 delivery system
    def deliver(self, delivery_details: {'name': str, 'address': str, 'city': str, 'country': str,
                                                  'zip': str}) -> bool:
        return self.__bridge.deliver(delivery_details)

    def is_delivery_sys_connected(self):
        return self.__bridge.is_delivery_connected()

    def cancel_delivery_supply(self, transaction_id: str) -> bool:
        return self.__bridge.cancel_delivery_supply(transaction_id)

    def cause_delivery_timeout(self):
        self.__bridge.cause_delivery_timeout()

    def cause_delivery_con_error(self):
        self.__bridge.cause_delivery_con_error()

    def set_connection_delivery_back(self):
        self.__bridge.set_connection_delivery_back()

    def set_user(self, nickname: str):
        return self.__bridge.set_user(nickname)

    # teardown after all tests are run
    @abstractmethod
    def tearDown(self) -> None:
        pass

    def __repr__(self):
        return repr("ProjectAT")
