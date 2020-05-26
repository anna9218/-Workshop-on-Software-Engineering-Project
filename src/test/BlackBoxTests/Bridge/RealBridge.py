"""
    class representing the:
                            - concrete implementor in the Bridge pattern
                            - adapter in the the adapter pattern
                            - real subject in the proxy pattern
"""
from datetime import datetime

from src.test.BlackBoxTests.Bridge.Bridge import Bridge
from src.main.ServiceLayer.GuestRole import GuestRole
from src.main.ServiceLayer.TradeControlService import TradeControlService
from src.main.ServiceLayer.SubscriberRole import SubscriberRole
from src.main.ServiceLayer.StoreOwnerOrManagerRole import StoreOwnerOrManagerRole
from src.main.ServiceLayer.SystemManagerRole import SystemManagerRole
from src.main.DomainLayer.UserComponent.DiscountType import DiscountType
from src.main.DomainLayer.UserComponent.PurchaseType import PurchaseType
from src.main.DomainLayer.StoreComponent.ManagerPermission import ManagerPermission


class RealBridge(Bridge):

    def __init__(self):
        super().__init__()
        self.__guest_role = GuestRole()
        self.__trade_control_srv = TradeControlService()
        self.__subscriber = SubscriberRole()
        self.__store_owner_or_manager = StoreOwnerOrManagerRole()
        self.__system_manager = SystemManagerRole()

    # uc 1
    def init_sys(self) -> bool:
        self.__trade_control_srv.init_system()
        return self.is_delivery_connected() and self.is_payment_connected()

    def is_payment_connected(self) -> bool:
        return self.__trade_control_srv.is_payment_connected()

    def is_delivery_connected(self) -> bool:
        return self.__trade_control_srv.is_delivery_connected()

    def cause_connection_err_payment(self):
        raise ResourceWarning("System is down!")

    def cause_connection_err_delivery(self):
        raise ResourceWarning("System is down!")

    # uc 2.2
    def register_user(self, nickname: str, password: str) -> bool:
        return self.__guest_role.register(nickname, password)

    def delete_user(self, nickname: str):
        self.__trade_control_srv.remove_user(nickname)

    def delete_manager(self, store_name: str, appointee_nickname: str):
        return self.__trade_control_srv.remove_manager(store_name, appointee_nickname)

    # uc 2.3
    def login(self, nickname: str, password: str) -> bool:
        return self.__guest_role.login(nickname, password)

    # uc 2.4
    def view_stores(self) -> bool:
        res = self.__guest_role.display_stores()
        return res is not None and len(res) != 0

    def display_stores_or_products_info(self, store_name: str, store_info_flag: bool, products_info_flag: bool) -> bool:
        res = self.__guest_role.display_stores_or_products_info(store_name, store_info_flag, products_info_flag)['response']
        return res is not None and len(res) != 0

    # uc 2.5
    def search_product(self, search_option: int, string: str):
        res = self.__guest_role.search_products_by(search_option, string)['response']
        return res is not None and len(res) != 0

    def filter_products(self, filter_details, products):
        res = self.__guest_role.filter_products_by(filter_details, products)
        return res is not None and len(res) != 0

    # uc 2.6
    def add_products_to_cart(self, product_name: str, store_name: str, amount: int, discount_type: int,
                             purchase_type: int) -> bool:
        products_stores_quantity = {"product_name": product_name, "store_name": store_name, "amount": amount}

        for discount in DiscountType:
            if discount.value == discount_type:
                products_stores_quantity["discount_type"] = discount

        for purchase in PurchaseType:
            if purchase.value == purchase_type:
                products_stores_quantity["purchase_type"] = purchase

        return self.__guest_role.save_products_to_basket([products_stores_quantity])

    # uc 2.7
    def view_shopping_cart(self):
        res = self.__guest_role.view_shopping_cart()['response']
        return len(res) != 0

    def update_shopping_cart(self, flag: str,
                             products_details: [{"product_name": str, "store_name": str, "amount": int}]):
        return self.__guest_role.update_shopping_cart(flag, products_details)

    def purchase_products(self) -> dict:
        return self.__guest_role.purchase_products()

    def confirm_purchase(self, address: str, purchase_ls: dict):
        return self.__guest_role.confirm_payment(address, purchase_ls)

    def remove_purchase(self, store_name: str, purchase_date: datetime):
        self.__trade_control_srv.remove_purchase(store_name, purchase_date)

    # uc 3.1
    def logout(self) -> bool:
        return self.__subscriber.logout()

    # uc 3.2
    def open_store(self, store_name: str) -> bool:
        return self.__subscriber.open_store(store_name)

    def delete_store(self, store_name: str):
        self.__trade_control_srv.remove_store(store_name)

    # uc 3.6
    def view_personal_purchase_history(self):
        purchase_ls = self.__subscriber.view_personal_purchase_history()['response']
        return purchase_ls is not None and len(purchase_ls) != 0

    # uc 4.1
    def add_products_to_store(self, store_name: str, products_details:
    [{"name": str, "price": int, "category": str, "amount": int}]) -> bool:
        return self.__store_owner_or_manager.add_products(store_name, products_details)

    def edit_products_in_store(self, store_name: str, product_name: str, op: str, new_value: str):
        return self.__store_owner_or_manager.edit_product(store_name, product_name, op, new_value)

    def remove_products_from_store(self, store_name: str, products_names: list) -> bool:
        return self.__store_owner_or_manager.remove_products(store_name, products_names)

    # 4.2 add and update purchase and discount policies
    def define_and_update_policies(self, type: str, store_name: str) -> [dict] or None:
        return self.__store_owner_or_manager.define_and_update_policies(type, store_name)

    def update_purchase_policy(self, store_name: str, details: {"name": str, "products": [str] or None,
                                                                "min_amount": int or None,
                                                                "max_amount": int or None,
                                                                "dates": [dict] or None, "bundle": bool or None}):
        return self.__store_owner_or_manager.update_purchase_policy(store_name, details)

    def define_purchase_policy(self, store_name: str, details: {"name": str, "products": [str],
                                                                "min_amount": int or None,
                                                                "max_amount": int or None,
                                                                "dates": [dict] or None, "bundle": bool or None}):
        return self.__store_owner_or_manager.define_purchase_policy(store_name, details)

    def update_discount_policy(self):
        pass

    def define_discount_policy(self):
        pass

    # uc 4.3
    def appoint_additional_owner(self, nickname: str, store_name: str) -> {'response': bool, 'msg': str}:
        return self.__store_owner_or_manager.appoint_additional_owner(nickname, store_name)

    # uc 4.5
    def appoint_additional_manager(self, nickname: str, store_name: str, permissions: [int]) -> bool:
        manager_permissions = []
        if permissions:
            for permission in permissions:
                for p in ManagerPermission:
                    if p.value == permission:
                        manager_permissions.append(p)

        return self.__store_owner_or_manager.appoint_store_manager(nickname, store_name, manager_permissions)

    # uc 4.6
    def edit_manager_permissions(self, store_name: str, appointee_nickname: str, permissions: list) -> bool:
        return self.__store_owner_or_manager.edit_manager_permissions(store_name, appointee_nickname, permissions)

    # uc 4.7
    def remove_manager(self, store_name: str, manager_nickname: str) -> bool:
        return self.__store_owner_or_manager.remove_manager(store_name, manager_nickname)

    def view_store_purchase_history(self, store_name: str):
        purchase_ls = self.__store_owner_or_manager.display_store_purchases(store_name)['response']
        return purchase_ls is not None and len(purchase_ls) != 0

    def subscribe_user(self, nickname: str, password: str):
        self.__trade_control_srv.subscribe_user(nickname, password)

    # uc 6.4
    def manager_view_user_purchases(self, nickname: str):
        purchase_ls = self.__system_manager.view_user_purchase_history(nickname)
        return purchase_ls is not None and len(purchase_ls) != 0

    def manager_view_shop_purchase_history(self, store_name: str):
        purchase_ls = self.__system_manager.view_store_purchases_history(store_name)
        return purchase_ls is not None and len(purchase_ls) != 0

    # uc 7
    def connect_payment_sys(self):
        self.__trade_control_srv.connect_payment()

    def disconnect_payment_sys(self):
        self.__trade_control_srv.disconnect_payment()

    def commit_payment(self, product_ls) -> bool:
        return self.__trade_control_srv.commit_payment(product_ls)

    # uc 8
    def connect_delivery_sys(self):
        self.__trade_control_srv.connect_delivery()

    def deliver(self, address: str, products_ls) -> {'response': bool, 'msg': str}:
        return self.__trade_control_srv.deliver(address, products_ls)

    def disconnect_delivery_sys(self):
        self.__trade_control_srv.disconnect_delivery()

    def set_user(self, nickname: str):
        self.__trade_control_srv.set_user(nickname)