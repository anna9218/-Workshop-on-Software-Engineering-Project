"""
    abstract class representing the abstraction in the Bridge pattern
"""
from abc import ABC, abstractmethod
from datetime import datetime

from src.Logger import logger
from src.test.BlackBoxTests.AcceptanceTests.Driver import Driver
import unittest


class ProjectTest(ABC, unittest.TestCase):

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

    # @logger
    # 1.1 init system functions
    def init_sys(self) -> bool:
        return self.__bridge.init_sys()

    # @logger
    def is_payment_sys_connected(self):
        return self.__bridge.is_payment_connected()

    # @logger
    def is_delivery_sys_connected(self):
        return self.__bridge.is_delivery_connected()

    # @logger
    def cause_connection_err_payment(self):
        raise ResourceWarning("System is down!")

    # @logger
    def cause_connection_err_delivery(self):
        raise ResourceWarning("System is down!")

    # @logger
    def delete_user(self, nickname: str):
        self.__bridge.delete_user(nickname)

    def delete_manager(self, store_name: str, appointee_nickname: str):
        self.__bridge.delete_manager(store_name, appointee_nickname)

    # @logger
    # 2.2 Register tests functions
    def register_user(self, nickname: str, password: str) -> bool:
        return self.__bridge.register_user(nickname, password)

    # @logger
    # 2.3 login functions
    def login(self, nickname: str, password: str) -> bool:
        return self.__bridge.login(nickname, password)

    # @logger
    # 2.4 view stores' products functions
    def view_stores(self) -> bool:
        return self.__bridge.view_stores()

    def display_stores_or_products_info(self, store_name: str, store_info_flag: bool, products_info_flag: bool) -> bool:
        return self.__bridge.display_stores_or_products_info(store_name, store_info_flag, products_info_flag)

    # @logger
    # 2.5 search products functions
    def search_products_by(self, search_option: int, string: str):
        return self.__bridge.search_product(search_option, string)

    # @logger
    def filter_products_by(self, filter_details, products):
        return self.__bridge.filter_products(filter_details, products)

    # @logger
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

    def confirm_purchase(self, address: str, purchase_ls: dict) -> bool:
        return self.__bridge.confirm_purchase(address, purchase_ls)

    def remove_purchase(self, store_name: str, purchase_date: datetime):
        self.__bridge.remove_purchase(store_name, purchase_date)

    # @logger
    # 3.1 logout functions
    def logout(self) -> bool:
        return self.__bridge.logout()

    # @logger
    # 3.2 open store functions
    def open_store(self, store_name: str) -> bool:
        return self.__bridge.open_store(store_name)

    # @logger
    def remove_store(self, store_name: str):
        self.__bridge.delete_store(store_name)

    # @logger
    # 3.7 view personal history functions
    def view_personal_purchase_history(self):
        return self.__bridge.view_personal_purchase_history()

    # @logger
    # 4.1 manage stock functions
    def add_products_to_store(self, store_name: str, products_details:
                                            [{"name": str, "price": int, "category": str, "amount": int}]) -> bool:
        return self.__bridge.add_products_to_store(store_name, products_details)

    # @logger
    def edit_products_in_store(self, store_name: str, product_name: str, op: str, new_value: str) -> bool:
        return self.__bridge.edit_products_in_store(store_name, product_name, op, new_value)

    # @logger
    def remove_products_from_store(self, store_name: str, products_names: list) -> bool:
        return self.__bridge.remove_products_from_store(store_name, products_names)

    # @logger
    # 4.3 add store owner functions
    def appoint_additional_owner(self, nickname: str, store_name: str) -> bool:
        return self.__bridge.appoint_additional_owner(nickname, store_name)

    # @logger
    # 4.5 appoint store manager functions
    def appoint_additional_manager(self, nickname: str, store_name: str, permissions: [int]) -> bool:
        return self.__bridge.appoint_additional_manager(nickname, store_name, permissions)

    # 4.6 edit manager permissions
    def edit_manager_permissions(self, store_name: str, appointee_nickname: str, permissions: list) -> bool:
        return self.__bridge.edit_manager_permissions(store_name, appointee_nickname, permissions)

    # @logger
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

    # @logger
    # 7 Payment System tests functions
    def connect_payment_sys(self):
        self.__bridge.connect_payment_sys()

    # @logger
    def commit_payment(self, product_ls) -> bool:
        return self.__bridge.commit_payment(product_ls)

    # @logger
    def disconnect_payment_sys(self):
        self.__bridge.disconnect_payment_sys()

    # @logger
    # 8 Delivery System tests functions
    def connect_delivery_sys(self):
        self.__bridge.connect_delivery_sys()

    # @logger
    def deliver(self, address: str, products_ls) -> bool:
        return self.__bridge.deliver(address, products_ls)

    # @logger
    def disconnect_delivery_sys(self):
        self.__bridge.disconnect_delivery_sys()

    def set_user(self, nickname: str):
        return self.__bridge.set_user(nickname)

    # teardown after all tests are run
    @abstractmethod
    def tearDown(self) -> None:
        pass

    def __repr__(self):
        return repr("ProjectTest")