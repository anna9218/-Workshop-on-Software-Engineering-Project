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
            self.__curr_user = User()

    def register_guest(self, nickname, password):
        if self.validate_nickname(nickname):
            guest = User()
            guest.register(nickname, password)
            self.subscribe(guest)
            return True
        return False

    def login_subsceiber(self, nickname, password):
        subscriber: User = self.get_subscriber(nickname)
        if subscriber and subscriber.is_registered() and subscriber.is_logged_out():
            return subscriber.login(nickname, password)

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
        list_of_lists = list(map(lambda store: store.get_products_by(search_opt, string), self.__stores))
        list_ = reduce(lambda acc, curr: acc + curr, list_of_lists)
        return list_

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

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ANNA ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
    def add_products(self, store_name: str, products_details: list) -> bool:
        """
        :param store_name: store's name
        :param products_details: list of JSONs, each JSON is one details record, for one product
        :return: True if products were added, False otherwise
        """
        store = self.get_store(store_name)
        if store is not None and \
                (store.is_owner(self.__curr_user.get_nickname()) or
                 store.is_manager(self.__curr_user.get_nickname())) and \
                self.__curr_user.is_registered() and \
                self.__curr_user.is_logged_in():
            store.add_products(self.__curr_user.get_nickname(), products_details)
            return True
        return False

    def remove_products(self, store_name: str, products_names: list) -> bool:
        """
        :param store_name: store's name
        :param products_names: list of product's names to remove
        :return: True if products were removed, False otherwise
        """
        store = self.get_store(store_name)
        for product_name in products_names:
            if store is not None and not store.get_product(product_name):
                return False

        if store is not None and \
                self.__curr_user.is_registered() and \
                self.__curr_user.is_logged_in() and \
                (store.is_owner(self.__curr_user.get_nickname()) or
                 store.is_manager(self.__curr_user.get_nickname())):
            store.remove_products(self.__curr_user.get_nickname(), products_names)
            return True
        return False

    def edit_product(self, store_name: str, product_name: str, op: str, new_value) -> bool:
        """
        :param store_name: store's name
        :param product_name: product's name to edit
        :param op: edit options - name, price, amount
        :param new_value: new value to set to
        :return: True if all products were removed, else return False
        """
        store = self.get_store(store_name)
        if store is not None and \
                self.__curr_user.is_registered() and \
                self.__curr_user.is_logged_in() and \
                (store.is_owner(self.__curr_user.get_nickname()) or
                 store.is_manager(self.__curr_user.get_nickname())):
            return store.edit_product(self.__curr_user.get_nickname(), product_name, op, new_value)
        return False

    def appoint_additional_owner(self, appointee_nickname: str, store_name: str) -> bool:
        """
        :param appointee_nickname: nickname of the new owner that will be appointed
        :param store_name: store the owner will be added to
        :return: True on success, else False
        """
        appointee = self.get_subscriber(appointee_nickname)
        store = self.get_store(store_name)

        if appointee is not None and \
                store is not None and \
                self.__curr_user.is_registered() and \
                appointee.is_registered() and \
                self.__curr_user.is_logged_in() and \
                not store.is_owner(appointee_nickname) and \
                (store.is_owner(self.__curr_user.get_nickname()) or
                 store.is_manager(self.__curr_user.get_nickname())):
            store.add_owner(self.__curr_user.get_nickname(), appointee)
            return True
        return False

    def appoint_store_manager(self, appointee_nickname: str, store_name: str, permissions: list) -> bool:
        """
        :param appointee_nickname: nickname of the new manager that will be appointed
        :param store_name: store's name
        :param permissions: ManagerPermission[] -> list of permissions (list of Enum)
        :return: True on success, else False
        """
        appointee = self.get_subscriber(appointee_nickname)
        store = self.get_store(store_name)

        if appointee is not None and \
                store is not None and \
                self.__curr_user.is_registered() and \
                appointee.is_registered() and \
                self.__curr_user.is_logged_in() and \
                (store.is_owner(self.__curr_user.get_nickname()) or store.is_manager(self.__curr_user.get_nickname())) and \
                not store.is_manager(appointee_nickname) and \
                not store.is_owner(appointee_nickname):
            store.add_manager(self.__curr_user, appointee, permissions)
            return True
        return False

    def edit_manager_permissions(self, store_name: str, appointee_nickname: str, permissions: list) -> bool:
        """
        :param store_name: store's name
        :param appointee_nickname: manager's nickname who's permissions will be edited
        :param permissions: ManagerPermission[] ->list of permissions (list of Enum)
        :return: True on success, else False
        """
        appointee = self.get_subscriber(appointee_nickname)
        store = self.get_store(store_name)
        if appointee is not None and \
                store is not None and \
                self.__curr_user.is_registered() and \
                appointee.is_registered() and \
                self.__curr_user.is_logged_in() and \
                (store.is_owner(self.__curr_user.get_nickname()) or store.is_manager(self.__curr_user.get_nickname())) and \
                store.is_manager(appointee):
            store.edit_manager_permissions(self.__curr_user, appointee_nickname, permissions)
            return True
        return False

    def remove_manager(self, store_name: str, appointee_nickname: str) -> bool:
        """
        :param store_name: store's name
        :param appointee_nickname: manager's nickname who's will be removed
        :return: True if removed successfully, else False
        """
        store = self.get_store(store_name)
        appointee = self.get_subscriber(appointee_nickname)
        if appointee is not None and \
                store is not None and \
                self.__curr_user.is_registered() and \
                appointee.is_registered() and \
                self.__curr_user.is_logged_in() and \
                (store.is_owner(self.__curr_user.get_nickname()) or store.is_manager(self.__curr_user.get_nickname())) and \
                store.is_manager(appointee):
            store.remove_manager(self.__curr_user.get_nickname(), appointee_nickname)
            return True
        return False

    def display_store_purchases(self, store_name: str) -> list:
        """
        :param store_name: store's name
        :return: purchases list
        """
        store = self.get_store(store_name)
        if store is not None and \
                self.__curr_user.is_registered() and \
                self.__curr_user.is_logged_in() and \
                (store.is_owner(self.__curr_user.get_nickname()) or store.is_manager(self.__curr_user.get_nickname())):
            return store.get_purchases(self.__curr_user.get_nickname())
        return []
