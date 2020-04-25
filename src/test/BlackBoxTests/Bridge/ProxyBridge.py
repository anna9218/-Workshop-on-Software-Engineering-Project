"""
    class representing the:
                            - concrete implementor in the Bridge pattern
                            - proxy in the proxy pattern
"""
from src.test.BlackBoxTests.Bridge.Bridge import Bridge
from src.test.BlackBoxTests.Bridge.RealBridge import RealBridge


class ProxyBridge(Bridge):

    def __init__(self, bridge: RealBridge):
        super().__init__()
        self._realbridge = bridge

    def register_user(self, username, password) -> bool:
        return self._realbridge.register_user(username, password)

    def connect_payment_sys(self):
        self._realbridge.connect_payment_sys()

    def disconnect_payment_sys(self):
        self._realbridge.disconnect_payment_sys()

    def commit_payment(self, username, amount, credit, date) -> bool:
        return self._realbridge.commit_payment(username, amount, credit, date)

    def is_payment_connected(self):
        return self._realbridge.is_payment_connected()

    def connect_delivery_sys(self):
        self._realbridge.connect_delivery_sys()

    def deliver(self, username, address) -> bool:
        return self._realbridge.deliver(username, address)

    def disconnect_delivery_sys(self):
        self._realbridge.disconnect_delivery_sys()

    def is_delivery_connected(self):
        return self._realbridge.is_delivery_connected()

    def init_sys(self):
        self._realbridge.init_sys()

    def remove_user(self, username):
        self._realbridge.remove_user(username)

    def login(self, username, password):
        return self._realbridge.login(username, password)

    def view_stores(self):
        return self._realbridge.view_stores()

    def logout(self):
        return self._realbridge.logout()

    def search_product(self, option, string):
        return self._realbridge.search_product(option, string)

    def filter_products(self, filter_details, products):
        return self._realbridge.filter_products(filter_details, products)

    def add_products_to_cart(self, nickname, products_stores_quantity_ls):
        return self._realbridge.add_products_to_cart(nickname, products_stores_quantity_ls)

    def view_personal_history(self):
        return self._realbridge.view_personal_history()

    def open_store(self, name):
        return self._realbridge.open_store(name)

    def delete_store(self, store):
        self._realbridge.delete_store(store)

    def add_products_to_store(self, user_nickname, store_name, products_details):
        return self._realbridge.add_products_to_store(user_nickname, store_name, products_details)

    def edit_products_in_store(self, nickname, store_name, product_name, op, new_value):
        return self._realbridge.edit_products_in_store(nickname, store_name, product_name, op, new_value)

    def remove_products_from_store(self, user_nickname, store_name, products_names):
        return self._realbridge.remove_products_from_store(user_nickname, store_name, products_names)

    def appoint_additional_owner(self, nickname, store_name):
        return self._realbridge.appoint_additional_owner(nickname, store_name)

    def appoint_additional_manager(self, nickname, store_name, permissions):
        return self._realbridge.appoint_additional_manager(nickname, store_name, permissions)

    def remove_manager(self, store_name, manager_nickname, permissions):
        return self._realbridge.remove_manager(store_name, manager_nickname, permissions)
