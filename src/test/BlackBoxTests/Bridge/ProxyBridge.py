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
