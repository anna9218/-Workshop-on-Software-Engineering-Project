"""
    class representing the:
                            - concrete implementor in the Bridge pattern
                            - adapter in the the adapter pattern
                            - real subject in the proxy pattern
"""
from src.test.BlackBoxTests.Bridge.Bridge import Bridge
from src.main.DomainLayer.User import User


class RealBridge(Bridge):

    def __init__(self):
        pass

    def register_user(self, username, password) -> str:
        return User().register(username, password)


