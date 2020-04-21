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

    def somefunction(self) -> str:
        return "proxy"

    def test_sum(self, x, y) -> int:
        return self.realbridge.test_sum(x, y)

    def test_wrong_sum(self, x, y) -> int:
        return self.realbridge.test_wrong_sum(x, y)
