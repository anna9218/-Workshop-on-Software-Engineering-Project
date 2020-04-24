from src.main.DomainLayer import ManagerPermission
from src.main.DomainLayer.User import User
from src.main.DomainLayer.TradeControl import TradeControl
from src.main.DomainLayer.Security import Security
from src.main.ServiceLayer.SubscriberRole import SubscriberRole


class StoreOwnerRole(SubscriberRole):
    def __init__(self, subscriber):
        self.__store_owner = subscriber

    def check_if_ownes_the_store (self, user_name, store_name) -> bool:
        """
        :param user_name: username of the user we want to check
        :param store_name: name of the store which we want to find if the above user owns
        :return: true if the user with user_name owns the store with store_name
        """
        user = self.find_user_by_name(user_name)
        if user is None or not user.is_loggedIn():
            return False
        store = self.get_store(store_name)
        if user in store.get_owners():
            return True

    def add_to_inventory (self, user_name, store_name, products, prices, amounts, categories) -> bool:
        """
        :param user_name: user name of the initializer user- should be owner
        :param store_name: store name of a store which the user with the user_name wants to add products to
        :param products: the names of the new products
        :param prices: a list of the prices of the new products
        :param amounts: a list of the amounts of the new products
        :param categories: a list of the categories of the new products
        :return: true if the inventory contains the new products
        """
        if not self.check_if_ownes_the_store(user_name, store_name):
            return False
        store = self.get_store(store_name)
        return store.add_products(products, prices, amounts, categories)

    def remove_from_inventory(self, user_name, store_name, products) -> bool:
        """
        :param user_name: the user_name of the user that triggered this function
        :param store_name: the store_name of the store we would like to edit its inventory
        :param products: products to delete from inventory - assume they exists on inventory
        :return: True if the inventory updated without the products
        """
        if not self.check_if_ownes_the_store(user_name, store_name):
            return False
        store = self.get_store(store_name)
        return store.remove_products(products)

    def edit_product (self, user_name, store_name, product, new_value, op) -> bool:
        """
        :param user_name: the user_name of the user that triggered this function
        :param store_name: the store_name of the store we would like to edit its inventory
        :param product: product to edit
        :param new_value: the new value to replace with
        :param op: "name" / "price" / "amount" - parameter to edit
        :return: True if the product info updated as need on the inventory if the store
        """
        if not self.check_if_ownes_the_store(user_name, store_name):
            return False
        store = self.get_store(store_name)
        if op is "name":
            return store.change_name(product, new_value)
        elif op is "price":
            return store.change_price(product, new_value)
        elif op is "amount":
            return store.change_amount(product, new_value)
        else:
            return False

    @staticmethod
    def appoint_new_store_manager(self, user_name, store_name, user_name_to_appoint):
        if not self.check_if_ownes_the_store(user_name, store_name):
            return False
        if self.check_if_ownes_the_store(user_name_to_appoint, store_name) or \
                self.check_if_manages_the_store(user_name_to_appoint, store_name):
            return False # check its sure- not possible to have more than 1 appointer
        store = self.get_store(store_name)
        manager = self.find_user_by_name(user_name_to_appoint)
        store.add_manager(manager)
        # the first permissions are 4.9 (not this version) and 4.10 (watch purchase's history)
        self.add_permissions(manager, store_name, ManagerPermission.USERS_QUESTIONS)
        self.add_permissions(manager, store_name, ManagerPermission.WATCH_PURCHASE_HISTORY)

    def check_if_manages_the_store (self, user_name, store_name) -> bool:
        user = self.find_user_by_name(user_name)
        if user is None or not user.is_loggedIn():
            return False
        ap = user.get_appointment()
        return ap.is_manager(store_name)

    @staticmethod
    def get_store(self, store_name):
        return TradeControl.getInstance().get_store(store_name)

    @staticmethod
    def validate_store_name(self, store_name):
        TradeControl.getInstance().validate_store_name(store_name)

    @staticmethod
    def find_user_by_name(self, user_name):
        return TradeControl.getInstance().get_guest(user_name)

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


    def add_permissions (self, manager, store_name, permission):
        manager.get_appointment().add_permission (store_name, permission)

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

    def del_permissions (self, manager, store_name, permission):
        manager.get_appointment().del_permission (store_name, permission)

    pass
