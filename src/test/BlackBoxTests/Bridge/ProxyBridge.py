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

    def register_user(self, username, password) -> str:
        return self._realbridge.register_user(username, password)

    def connect_payment_sys(self):
        self._realbridge.connect_payment_sys()

    def disconnect_payment_sys(self):
        self._realbridge.disconnect_payment_sys()

    def commit_payment(self, username, amount, credit, date) -> bool:
        return self._realbridge.commit_payment(username, amount, credit, date)

    def connect_delivery_sys(self):
        self._realbridge.connect_delivery_sys()

    def deliver(self, username, address) -> bool:
        return self._realbridge.deliver(username, address)

    def disconnect_delivery_sys(self):
        self._realbridge.disconnect_delivery_sys()
