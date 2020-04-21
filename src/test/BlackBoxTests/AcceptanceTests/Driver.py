"""
    abstract class responsible for initializing and returning the Bridge
"""
from src.test.BlackBoxTests.Bridge import Bridge, ProxyBridge, RealBridge
from abc import ABC


class Driver(ABC):

    def __init__(self):
        super.__init__()

    @staticmethod
    def get_bridge() -> Bridge:
        real = RealBridge.RealBridge()
        return ProxyBridge.ProxyBridge(real)

