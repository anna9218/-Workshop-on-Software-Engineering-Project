"""
    class representing the:
                            - concrete implementor in the Bridge pattern
                            - proxy in the proxy pattern
"""
from src.test.BlackBoxTests.Bridge.Bridge import Bridge
from src.test.BlackBoxTests.Bridge.RealBridge import RealBridge


class ProxyBridge(Bridge):

    def __init__(self, realbridge: RealBridge):
        self.realbridge = realbridge
        # super().__init__()

    def register_user(self, username, password) -> str:
        self.realbridge.register_user(username, password)

    def connect_payment_sys(self):
        self.realbridge.connect_payment_sys()

    def disconnect_payment_sys(self):
        self.realbridge.disconnect_payment_sys()

    def commit_payment(self, username, amount, credit, date):
        self.realbridge.commit_payment(username, amount, credit, date)

    def connect_delivery_sys(self):
        self.realbridge.connect_delivery_sys()

    def deliver(self, username, address):
        self.realbridge.deliver(username, address)

    def disconnect_delivery_sys(self):
        self.realbridge.disconnect_delivery_sys()
