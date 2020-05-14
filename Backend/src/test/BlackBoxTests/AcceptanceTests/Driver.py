"""
    abstract class responsible for initializing and returning the Bridge
"""
from Backend.src.Logger import loggerStaticMethod
from Backend.src.test.BlackBoxTests.Bridge.Bridge import Bridge
from Backend.src.test.BlackBoxTests.Bridge.ProxyBridge import ProxyBridge
from Backend.src.test.BlackBoxTests.Bridge.RealBridge import RealBridge
from abc import ABC


class Driver(ABC):

    def __init__(self):
        super().__init__()

    @staticmethod
    def get_bridge() -> Bridge:
        loggerStaticMethod("Driver.get_bridge",[])
        real = RealBridge()
        return ProxyBridge(real)

