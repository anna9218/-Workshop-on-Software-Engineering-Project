
from src.main.DomainLayer.FacadeDelivery import FacadeDelivery
from src.main.DomainLayer.FacadePayment import FacadePayment
from src.main.DomainLayer.Store import Store
from src.main.DomainLayer.User import User


class TradeControl:
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if TradeControl.__instance is None:
            TradeControl()
        return TradeControl.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if TradeControl.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            self.__manager = User(self)
            self.__managers = []
            self.__stores = []
            self.__subscribers = []
            self.__delivery_system = FacadeDelivery()
            self.__payment_system = FacadePayment()
            TradeControl.__instance = self

    # usecase 1.1
    def init_system(self):
        # connect the system to the delivery and payment systems
        # add check for errors
        self.__delivery_system.connect()
        self.__payment_system.connect()
        # TODO: ANNA: should return true/false and the presentation will send the ack msg
        self.__manager.register("TradeManager", "123456789")
        self.__managers.append(self.manager)

    def subscribe(self):
        user = User()
        self.__subscribers.append(user)
        return user
        # TODO - maybe send to Security?

    def open_store(self, user, store_name) -> Store:
        for s in self.__stores:
            if s.get_name() == store_name:
                return None
        store = Store(store_name)
        self.__stores.append(store)
        return store

    def validateNickName(self, nickname):
        for u in self.__subscribers:
            if u.getName() == nickname:
                return False
        return True

    def get_subscriber(self, nickname):
        for u in self.__subscribers:
            if u.getName() == nickname:
                return u
        return None

    def get_users(self):
        return self.__subscribers

    def get_stores(self):
        return self.__stores

    def get_managers(self):
        return self.__managers

    def get_delivery_system(self):
        return self.__delivery_system

    def get_payment_system(self):
        return self.__payment_system

