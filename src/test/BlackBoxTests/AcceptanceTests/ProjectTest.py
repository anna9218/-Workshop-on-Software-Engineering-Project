"""
    abstract class representing the abstraction in the Bridge pattern
"""
from abc import ABC, abstractmethod
from src.test.BlackBoxTests.AcceptanceTests.Driver import Driver
import unittest


class ProjectTest(ABC, unittest.TestCase):

    # setup for all tests
    @abstractmethod
    def setUp(self) -> None:
        self.__bridge = Driver().get_bridge()

    # default functions to be implemented in inheriting classes (not in parent class)
    @abstractmethod
    def test_success(self):
        pass

    @abstractmethod
    def test_fail(self):
        pass

    # bridged functions

    # 1.1 init system functions
    def init_sys(self):
        self.__bridge.init_sys()

    def remove_user(self, username):
        self.__bridge.remove_user(username)

    # 2.2 Register tests functions
    def register_user(self, username, password) -> bool:
        return self.__bridge.register_user(username, password)

    # 2.3 login functions
    def login(self, username, password):
        return self.__bridge.login(username, password)

    # 2.4 view stores' products functions
    def view_stores(self):
        return self.__bridge.view_stores()

    def view_store_info(self, store, store_info_flag, products_flag):
        return self.__bridge.view_store_info(store, store_info_flag, products_flag)

    # 2.5 search products functions
    def search_products_by(self, option, string):
        return self.__bridge.search_product(option, string)
    # TODO

    def filter_products_by(self, filter_details, products):
        return self.__bridge.filter_products(filter_details, products)
    # TODO

    # 2.6 save products to cart
    def add_products_to_cart(self):
        return self.__bridge.add_products_to_cart()
    # TODO

    # 3.1 logout functions
    def logout(self):
        return self.__bridge.logout()

    # 3.3 open store functions
    def open_store(self, name):
        return self.__bridge.open_store(name)

    def teardown_store(self, store):
        self.__bridge.delete_store(store)

    # 3.6 view personal history functions
    def view_personal_purchase_history(self):
        self.__bridge.view_personal_history()
    # TODO

    # 4.1 manage stock functions
    def add_products_to_store(self, user_nickname, store_name, products_details):
        return self.__bridge.add_products_to_store(user_nickname, store_name, products_details)

    def edit_products_in_store(self, nickname, store_name, product_name, op, new_value):
        return self.__bridge.edit_products_in_store(nickname, store_name, product_name, op, new_value)

    def remove_products_from_store(self, user_nickname, store_name, products_names):
        return self.__bridge.remove_products_from_store(user_nickname, store_name, products_names)

    # 4.3 add store owner functions
    def appoint_additional_owner(self, nickname, store_name):
        return self.__bridge.appoint_additional_owner(nickname, store_name)

    # 7 Payment System tests functions
    def connect_payment_sys(self):
        self.__bridge.connect_payment_sys()

    def commit_payment(self, username, amount, credit, date) -> bool:
        return self.__bridge.commit_payment(username, amount, credit, date)

    def disconnect_payment_sys(self):
        self.__bridge.disconnect_payment_sys()

    def is_payment_sys_connected(self):
        return self.__bridge.is_payment_connected()

    # 8 Delivery System tests functions
    def connect_delivery_sys(self):
        self.__bridge.connect_delivery_sys()

    def deliver(self, username, address) -> bool:
        return self.__bridge.deliver(username, address)

    def disconnect_delivery_sys(self):
        self.__bridge.disconnect_delivery_sys()

    def is_delivery_sys_connected(self):
        return self.__bridge.is_delivery_connected()

    # teardown after all tests are run
    @abstractmethod
    def tearDown(self) -> None:
        pass
