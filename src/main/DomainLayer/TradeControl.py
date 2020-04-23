from functools import reduce

from src.main.DomainLayer.FacadeDelivery import FacadeDelivery
from src.main.DomainLayer.FacadePayment import FacadePayment
from src.main.DomainLayer.Store import Store
from src.main.DomainLayer.User import User


# get a user instance for guest
def get_guest():
    guest = User()
    return guest


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

    def add_sys_manager(self, subscriber):
        self.__managers.append(subscriber)

    def subscribe(self):
        user = User()
        self.__subscribers.append(user)
        return user

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

    def getProductsBy(self, search_opt, string):
        ls = map(lambda store: store.getProductsBy(search_opt, string))
        return reduce(lambda acc, curr: acc.append(curr), ls)

    # def getProduct(self, product_name, store_name):

    def get_users(self):
        return self.__subscribers

    def get_stores(self):
        return self.__stores

    def get_store(self, store_name):
        for s in self.__stores:
            if s.get_name == store_name:
                return s
        return None

    def get_managers(self):
        return self.__managers

    def get_delivery_system(self):
        return self.__delivery_system

    def get_payment_system(self):
        return self.__payment_system
