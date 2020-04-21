
from src.main.DomainLayer.FacadeDelivery import FacadeDelivery
from src.main.DomainLayer.FacadePayment import FacadePayment
# from src.main.DomainLayer.Security import Security
from src.main.DomainLayer.User import User


class TradeControl:

    def __init__(self):
        self.manager = User()
        self.managers = []
        self.stores = []
        self.users = []
        self.delivery_system = FacadeDelivery()
        # self.security_system = Security()
        self.payment_system = FacadePayment()

    # usecase 1.1
    def init_system(self):
        # connect the system to the delivery and payment systems
        # add check for errors
        self.delivery_system.connect()
        self.payment_system.connect()
        # TODO: ANNA: should return true/false and the presentation will send the ack msg
        self.manager.register("TradeManager", "123456789")
        self.managers.append(self.manager)


