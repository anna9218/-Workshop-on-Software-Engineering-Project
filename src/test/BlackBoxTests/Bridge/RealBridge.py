"""
    class representing the:
                            - concrete implementor in the Bridge pattern
                            - adapter in the the adapter pattern
                            - real subject in the proxy pattern
"""
from src.test.BlackBoxTests.Bridge.Bridge import Bridge
from src.main.DomainLayer.FacadePayment import FacadePayment
from src.main.DomainLayer.User import User


class RealBridge(Bridge):

    def __init__(self):
        self.paymentSys = FacadePayment()

    def register_user(self, username, password) -> str:
        return User().register(username, password)

    def connect_payment_sys(self):
        self.paymentSys.connect()

    def disconnect_payment_sys(self):
        self.paymentSys.disconnect()

    def commit_payment(self, username, amount, credit, date):
        self.paymentSys.commit_payment(username, amount, credit, date)


