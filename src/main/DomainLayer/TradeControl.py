from functools import reduce

from src.main.DomainLayer.FacadeDelivery import FacadeDelivery
from src.main.DomainLayer.FacadePayment import FacadePayment
from src.main.DomainLayer.Store import Store
from src.main.DomainLayer.User import User


class TradeControl:
    __instance = None

    @staticmethod
    def get_instance():
        """ Static access method. """
        if TradeControl.__instance is None:
            TradeControl()
        return TradeControl.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if TradeControl.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            self.__managers = []
            self.__stores = []
            self.__subscribers = []
            TradeControl.__instance = self

    def add_sys_manager(self, subscriber: User):
        for s in self.__managers:
            if s.get_nickname() == subscriber.get_nickname():
                return False
        self.__managers.append(subscriber)
        return True

    def subscribe(self, user: User):
        for s in self.__subscribers:
            if s.get_nickname() == user.get_nickname():
                return False
        self.__subscribers.append(user)
        return True

    def unsubscribe(self, nickname):
        for s in self.__subscribers:
            if s.get_nickname() == nickname:
                self.__subscribers.remove(s)
                return True
        return False

    def open_store(self, store_name) -> Store:
        for s in self.__stores:
            if s.get_name() == store_name:
                return None
        store = Store(store_name)
        self.__stores.append(store)
        return store

    def close_store(self, store_name) -> bool:
        for s in self.__stores:
            if s.get_name() == store_name:
                self.__stores.remove(s)
                return True
        return False

    def validate_nickname(self, nickname):
        for u in self.__subscribers:
            if u.get_nickname() == nickname:
                return False
        return True

    def get_subscriber(self, nickname):
        for u in self.__subscribers:
            if u.get_nickname() == nickname:
                return u
        return None

    def get_products_by(self, search_opt, string):
        ls = map(lambda store: store.get_products_by(search_opt, string), self.__stores)
        return reduce(lambda acc, curr: acc.append(curr), ls)

    def get_store(self, store_name):
        for s in self.__stores:
            if s.get_name() == store_name:
                return s
        return None



    def get_subscribers(self):
        return self.__subscribers

    def get_stores(self):
        return self.__stores

    def get_managers(self):
        return self.__managers

    # get a user instance for guest
    def get_guest(self):
        guest = User()
        return guest