"""
    abstract class responsible for initializing and returning the Bridge
"""
from src.test.BlackBoxTests.Bridge.Bridge import Bridge
from src.test.BlackBoxTests.Bridge.ProxyBridge import ProxyBridge
from src.test.BlackBoxTests.Bridge.RealBridge import RealBridge
from abc import ABC


class Driver(ABC):

    def __init__(self):
        super.__init__()

    @staticmethod
    def get_bridge() -> Bridge:
        real = RealBridge()
        return ProxyBridge(real)

