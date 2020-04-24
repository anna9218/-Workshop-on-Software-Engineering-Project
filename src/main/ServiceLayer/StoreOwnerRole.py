from src.main.DomainLayer.User import User
from src.main.DomainLayer.TradeControl import TradeControl
from src.main.DomainLayer.Security import Security
from src.main.ServiceLayer.SubscriberRole import SubscriberRole


class StoreOwnerRole(SubscriberRole):
    def __init__(self, subscriber):
        self.__store_owner = subscriber

    # def open_store_func(self, user_name, store_name) -> bool:
    #     user = self.find_user_by_name(user_name)
    #     if user is None or not user.is_loggedIn():
    #         return False
    #     self.validate_store_name(store_name)
    #     new_store = TradeControl.getInstance().open_store(self, store_name)
    #     if new_store is None:
    #         return False
    #     else:
    #         return new_store.add_owner(user) and appointment.appoint_owner(None, self, new_store)

    def check_if_owns_the_store(self, user_name, store_name) -> bool:
        user = self.find_user_by_name(user_name)
        if user is None or not user.is_loggedIn():
            return False
        store = self.get_store(store_name)
        if user in store.get_owners():
            return True

    def add_to_inventory(self, user_name, store_name, products, prices, amounts, categories) -> bool:
        if not self.check_if_owns_the_store(user_name, store_name):
            return False
        store = self.get_store(store_name)
        store.add_products(products, prices, amounts, categories)
        return True

    def remove_from_inventory(self, user_name, store_name, products) -> bool:
        if not self.check_if_owns_the_store(user_name, store_name):
            return False
        store = self.get_store(store_name)
        store.remove_products(products)
        return True

    def edit_product(self, user_name, store_name, product, new_value, op) -> bool:
        if not self.check_if_owns_the_store(user_name, store_name):
            return False
        store = self.get_store(store_name)
        if op is "name":
            store.change_name(product, new_value)
        elif op is "price":
            store.change_price(product, new_value)
        elif op is "amount":
            store.change_amount(product, new_value)
        else:
            return False
        return True

    @staticmethod
    def get_store(self, store_name):
        return TradeControl.getInstance().get_store(store_name)

    @staticmethod
    def validate_store_name(self, store_name):
        TradeControl.getInstance().validate_store_name(store_name)

    @staticmethod
    def find_user_by_name(self, user_name):
        return TradeControl.getInstance().getUser(user_name)

    # use case 4.10 - View store’s purchase history
    @staticmethod
    def display_store_purchases(self, nickname, store):
        """
        :param self:
        :param nickname: of the store owner
        :param store: name of the store - (string?)
        :return:
        """
        subscriber = TradeControl.getInstance().getSubscriber(nickname)
        # checking preconditions
        if subscriber.is_registered() and subscriber.is_logged_in() and self.check_if_owns_the_store(nickname, store):
            store = TradeControl.getInstance().get_store(store)
            if store in None:
                return False
            else:
                return store.get_purchases()

    @staticmethod
    def display_purchase_info(self, purchase, store):
        """
        :param self:
        :param purchase:
        :param store: name of the store - (string?)
        :return: returns a Purchase object
        """
        store = TradeControl.getInstance().get_store(store)
        store.get_purchase_info(purchase)
