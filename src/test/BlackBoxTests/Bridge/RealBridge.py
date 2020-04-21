"""
    class representing the:
                            - concrete implementor in the Bridge pattern
                            - adapter in the the adapter pattern
                            - real subject in the proxy pattern
"""
from src.test.BlackBoxTests.Bridge import Bridge


class RealBridge(Bridge.Bridge):

    def __init__(self):
        pass

    def somefunction(self) -> str:
        return "real"

    def test_sum(self, x, y) -> int:
        pass
        # return junk.junk().sum(x, y)

    def test_wrong_sum(self, x, y) -> int:
        pass
        # return junk.junk().wrongsum(x, y)
