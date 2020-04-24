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

    def login(self, username, password):
        return self._realbridge.login(username, password)

    # view stores' products functions
    def view_stores(self):
        return self._realbridge.view_stores()

    def view_store_info(self, store, store_info_flag, products_flag):
        return self._realbridge.view_store_info(store, store_info_flag, products_flag)
