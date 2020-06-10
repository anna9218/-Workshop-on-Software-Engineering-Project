"""
    class representing the:
                            - concrete implementor in the Bridge pattern
                            - proxy in the proxy pattern
"""
from datetime import datetime

from src.test.BlackBoxTests.Bridge.Bridge import Bridge
from src.test.BlackBoxTests.Bridge.RealBridge import RealBridge


class ProxyBridge(Bridge):

    def __init__(self, bridge: RealBridge):
        super().__init__()
        self._realbridge = bridge

    # 1.1
    # @logger
    def init_sys(self) -> bool:
        return self._realbridge.init_sys()

    # @logger
    def is_payment_connected(self) -> bool:
        return self._realbridge.is_payment_connected()

    # @logger
    def is_delivery_connected(self) -> bool:
        return self._realbridge.is_delivery_connected()

    def cause_connection_err_payment(self):
        self.cause_connection_err_payment()

    def cause_connection_err_delivery(self):
        self.cause_connection_err_delivery()

    # 2.2
    # @logger
    def register_user(self, nickname: str, password: str) -> bool:
        return self._realbridge.register_user(nickname, password)

    # @logger
    def delete_user(self, nickname: str):
        self._realbridge.delete_user(nickname)

    def delete_manager(self, store_name: str, appointee_nickname: str):
        self._realbridge.delete_manager(store_name, appointee_nickname)

    # 2.3
    # @logger
    def login(self, nickname: str, password: str) -> bool:
        return self._realbridge.login(nickname, password)

    # 2.4
    # @logger
    def view_stores(self):
        return self._realbridge.view_stores()

    def display_stores_or_products_info(self, store_name: str, store_info_flag: bool, products_info_flag: bool) -> bool:
        return self._realbridge.display_stores_or_products_info(store_name, store_info_flag, products_info_flag)

    # 2.5
    # @logger
    def search_product(self, search_option: int, string: str):
        return self._realbridge.search_product(search_option, string)

    # @logger
    def filter_products(self, filter_details, products):
        return self._realbridge.filter_products(filter_details, products)

    # 2.6
    # @logger

    def add_products_to_cart(self, product_name: str, store_name: str, amount: int, discount_type: int,
                             purchase_type: int) -> bool:
        return self._realbridge.add_products_to_cart(product_name, store_name, amount, discount_type, purchase_type)

    # 2.7
    def view_shopping_cart(self):
        return self._realbridge.view_shopping_cart()

    def update_shopping_cart(self, flag: str,
                             products_details: [{"product_name": str, "store_name": str, "amount": int}]):
        return self._realbridge.update_shopping_cart(flag, products_details)

    # 2.8
    def purchase_products(self) -> dict:
        return self._realbridge.purchase_products()

    def confirm_purchase(self, address: str, purchase_ls: dict):
        return self._realbridge.confirm_purchase(address, purchase_ls)

    def remove_purchase(self, store_name: str, purchase_date: datetime):
        self._realbridge.remove_purchase(store_name, purchase_date)

    # 3.1
    # @logger
    def logout(self) -> bool:
        return self._realbridge.logout()

    # 3.2
    # @logger
    def open_store(self, store_name: str) -> bool:
        return self._realbridge.open_store(store_name)

    # @logger
    def delete_store(self, store_name: str):
        self._realbridge.delete_store(store_name)

    # 3.6
    def view_personal_purchase_history(self):
        return self._realbridge.view_personal_purchase_history()

    # 4.1
    # @logger
    def add_products_to_store(self, store_name: str, products_details:
                                            [{"name": str, "price": int, "category": str, "amount": int}]) -> bool:
        return self._realbridge.add_products_to_store(store_name, products_details)

    # @logger
    def edit_products_in_store(self, store_name: str, product_name: str, op: str, new_value: str):
        return self._realbridge.edit_products_in_store(store_name, product_name, op, new_value)

    # @logger
    def remove_products_from_store(self, store_name: str, products_names: list):
        return self._realbridge.remove_products_from_store(store_name, products_names)

    # 4.2
    def set_purchase_operator(self, store_name: str, operator: str):
        self._realbridge.set_purchase_operator(store_name, operator)

    def get_policies(self, policy_type: str, store_name: str) -> [dict] or None:
        return self._realbridge.define_and_update_policies(policy_type, store_name)

    def update_purchase_policy(self, store_name: str, details: {"name": str, "products": [str] or None,
                                                                "min_amount": int or None,
                                                                "max_amount": int or None,
                                                                "dates": [dict] or None, "bundle": bool or None}):
        return self._realbridge.update_purchase_policy(store_name, details)

    def define_purchase_policy(self, store_name: str, details: {"name": str, "products": [str],
                                                                "min_amount": int or None,
                                                                "max_amount": int or None,
                                                                "dates": [dict] or None, "bundle": bool or None}):
        return self._realbridge.define_purchase_policy(store_name, details)

    def update_discount_policy(self):
        return self._realbridge.update_discount_policy()

    def define_discount_policy(self):
        return self._realbridge.define_discount_policy()

    # 4.3
    # @logger
    def appoint_additional_owner(self, nickname, store_name):
        return self._realbridge.appoint_additional_owner(nickname, store_name)

    # 4.4 remove store owner functions
    def remove_owner(self, appointee_nickname: str, store_name: str) -> {'response': [], 'msg': str}:
        return self._realbridge.remove_owner(appointee_nickname, store_name)

    def get_store(self, store_name):
        return self._realbridge.get_store(store_name)

    # 4.5
    # @logger
    def appoint_additional_manager(self, nickname, store_name, permissions: [int]):
        return self._realbridge.appoint_additional_manager(nickname, store_name, permissions)

    # 4.6
    def edit_manager_permissions(self, store_name: str, appointee_nickname: str, permissions: list) -> bool:
        return self._realbridge.edit_manager_permissions(store_name, appointee_nickname, permissions)

    # 4.7
    # @logger
    def remove_manager(self, store_name, manager_nickname):
        return self._realbridge.remove_manager(store_name, manager_nickname)

    def view_store_purchase_history(self, store_name: str):
        return self._realbridge.view_store_purchase_history(store_name)

    def subscribe_user(self, nickname: str, password: str):
        self._realbridge.subscribe_user(nickname, password)

    # 6.4
    def manager_view_user_purchases(self, nickname: str):
        return self._realbridge.manager_view_user_purchases(nickname)

    def manager_view_shop_purchase_history(self, store_name: str):
        return self._realbridge.manager_view_shop_purchase_history(store_name)

    # 7
    # @logger
    def connect_payment_sys(self):
        self._realbridge.connect_payment_sys()

    # @logger
    def disconnect_payment_sys(self):
        self._realbridge.disconnect_payment_sys()

    # @logger
    def commit_payment(self, product_ls) -> bool:
        return self._realbridge.commit_payment(product_ls)

    # 8
    # @logger
    def connect_delivery_sys(self):
        self._realbridge.connect_delivery_sys()

    # @logger
    def deliver(self, address: str, products_ls) -> bool:
        return self._realbridge.deliver(address, products_ls)

    # @logger
    def disconnect_delivery_sys(self):
        self._realbridge.disconnect_delivery_sys()

    def set_user(self, nickname: str):
        return self._realbridge.set_user(nickname)

    def __repr__(self):
        return repr("ProxyBridge")