from functools import reduce

from src.Logger import loggerStaticMethod, errorLogger, logger
from src.main.DomainLayer.StoreComponent.Store import Store
from src.main.DomainLayer.UserComponent.DiscountType import DiscountType
from src.main.DomainLayer.UserComponent.PurchaseType import PurchaseType
from src.main.DomainLayer.UserComponent.User import User
import jsonpickle


class TradeControl:
    __instance = None

    @staticmethod
    def get_instance():
        """ Static access method. """
        loggerStaticMethod("TradeControl.get_instance", [])
        if TradeControl.__instance is None:
            TradeControl()
        return TradeControl.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if TradeControl.__instance is not None:
            errorLogger("This class is a singleton!")
            raise Exception("This class is a singleton!")
        else:
            self.__curr_user = User()
            self.__managers = []
            self.__stores = []
            self.__subscribers = []
            TradeControl.__instance = self

    @logger
    # ------- TradeControlService function
    def add_system_manager(self, nickname, password):
        for s in self.__managers:
            if s.get_nickname() == nickname:
                return False
        if self.get_subscriber(nickname):
            self.__managers.append(self.__curr_user)
            return True
        else:
            self.register_guest(nickname, password)
            self.__managers.append(self.__curr_user)
            return True
        # if self.register_guest(nickname, password):
        #     self.__managers.append(self.__curr_user)
        return False

    @logger
    # ----   Guest functions   ----
    def register_guest(self, nickname, password):
        return (self.validate_nickname(nickname) and \
                self.__curr_user.register(nickname, password) and \
                self.subscribe(self.__curr_user))

    @logger
    def login_subscriber(self, nickname, password):
        # subscriber: User = self.get_subscriber(nickname)
        return (self.__curr_user.is_registered() and \
               self.__curr_user.is_logged_out() and \
               self.__curr_user.login(nickname, password))

    @logger
    def subscribe(self, user: User):
        if self.validate_nickname(user.get_nickname()):
            self.__subscribers.append(user)
            return True
        return False

    @logger
    def unsubscribe(self, nickname):
        for s in self.__subscribers:
            if s.get_nickname() == nickname:
                self.__subscribers.remove(s)
                return True
        return False

    @logger
    def close_store(self, store_name) -> bool:
        for s in self.__stores:
            if s.get_name() == store_name:
                self.__stores.remove(s)
                return True
        return False

    @logger
    def validate_nickname(self, nickname):
        for u in self.__subscribers:
            if u.get_nickname() == nickname:
                return False
        return True

    @logger
    def get_subscriber(self, nickname):
        for u in self.__subscribers:
            if u.get_nickname() == nickname:
                return u
        return None

    @logger
    def get_products_by(self, search_opt: int, string: str):
        list_of_lists = list(map(lambda store: store.get_products_by(search_opt, string), self.__stores))
        list_ = reduce(lambda acc, curr: acc + curr, list_of_lists)
        return list_

    @logger
    def filter_products_by(self, filter_details, products_ls):
        """
        :param filter_details: list of filter details = "byPriceRange" (1, min_num, max_num)
                                                        "byCategory" (2, category)
        :param products_ls: list of string: [(product_name, store_name), ...]
        :return: list of filtered products
        """
        if products_ls is []:
            return []
        else:
            # convert all products
            products_list = list(map(lambda pair: self.get_store(pair[1]).get_product(pair[0]), products_ls))
            # filter by Price Range
            if filter_details[0] == 1:
                return list(filter(lambda p: filter_details[1] <= p.get_price() <= filter_details[2], products_list))
            else:
                # filter by Category
                if filter_details[0] == 2:
                    return list(filter(lambda p: filter_details[1] == p.get_category(), products_list))

    @logger
    def get_store_info(self, store_name):
        return jsonpickle.encode(self.get_store(store_name))

    @logger
    def get_store_inventory(self, store_name):
        return jsonpickle.encode(self.get_store(store_name).get_inventory())

    @logger
    def save_products_to_basket(self, products_stores_quantity_ls: [{"product_name": str, "store_name": str,
                                                                     "amount": int, "discount_type": DiscountType,
                                                                     "purchase_type": PurchaseType}]):
        ls = list(map(lambda x: {"product": self.get_store(x["store_name"]).get_product(x["product_name"]),
                                 "store": x["store_name"],
                                 "amount": x["amount"],
                                 "discount_type": x["discount_type"],
                                 "purchase_type": x["purchase_type"]},
                      products_stores_quantity_ls))
        return self.__curr_user.save_products_to_basket(ls)

    @logger
    def view_shopping_cart(self):
        return self.__curr_user.view_shopping_cart()

    @logger
    def remove_from_shopping_cart(self, products_details: [{"product_name": str, "store_name": str, "amount": int}]):
        """
        :param products_details: [{"product_name": str,
                                       "store_name": str,
                                       "amount": int}, ...]
        :return: True on success, False when one of the products doesn't exist in the shopping cart
        """
        return self.__curr_user.remove_from_shopping_cart(products_details)

    @logger
    def update_quantity_in_shopping_cart(self, products_details: [{"product_name": str, "store_name": str, "amount": int}]):
        """
        :param flag: action option - "remove"/"update"
        :param products_details: [{"product_name": str,
                                       "store_name": str,
                                       "amount": int}, ...]
        :return: True on success, False when one of the products doesn't exist in the shopping cart
        """
        return self.__curr_user.update_quantity_in_shopping_cart(products_details)

    @logger
    def get_store(self, store_name):
        for s in self.__stores:
            if s.get_name() == store_name:
                return s
        return None
    # ---------------------------------------------------

    # --------------   subscriber functions   --------------
    @logger
    def logout_subscriber(self):
        if self.__curr_user.is_registered() and self.__curr_user.is_logged_in():
            self.__curr_user.logout()
            return True
        return False

    @logger
    def open_store(self, store_name) -> bool:
        if self.__curr_user.is_registered() and self.__curr_user.is_logged_in():
            for s in self.__stores:
                if s.get_name() == store_name:
                    return False
            store = Store(store_name)
            store.get_owners().append(self.__curr_user)
            self.__stores.append(store)
            return True
        return False

    @logger
    def view_personal_purchase_history(self):
        if self.__curr_user.is_registered() and self.__curr_user.is_logged_in():
            purchases = self.__curr_user.get_accepted_purchases()
            return reduce(lambda acc, curr_product: acc + jsonpickle.encode(curr_product), purchases)
        return None
    # ----------------------------------

    # ---- system manager functions ----
    @logger
    def view_user_purchase_history(self, nickname):
        if self.is_manager(self.__curr_user.get_nickname()):
            viewed_user = self.get_subscriber(nickname)
            if viewed_user:
                return reduce(lambda acc, curr_product: acc + jsonpickle.encode(curr_product),
                              viewed_user.get_accepted_purchases())
        else:
            return None

    @logger
    def view_store_purchases_history(self, store_name):
        if self.is_manager(self.__curr_user.get_nickname()):
            viewed_store = self.get_store(store_name)
            if viewed_store:
                return reduce(lambda acc, curr_product: acc + jsonpickle.encode(curr_product),
                              viewed_store.get_purchases())
        else:
            return None

    @logger
    def is_manager(self, nickname):
        for m in self.__managers:
            if m.get_nickname() == nickname:
                return True
        return False
    # ----------------------------------

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ANNA ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
    @logger
    def add_products(self, store_name: str, products_details: [{"name": str, "price": int, "category": str, "amount": int}]) -> bool:
        """
        :param store_name: store's name
        :param products_details: list of JSONs, each JSON is one details record, for one product
        :return: True if products were added, False otherwise
        """
        store: Store = self.get_store(store_name)
        if store is not None and \
                (store.is_owner(self.__curr_user.get_nickname()) or
                 store.is_manager(self.__curr_user.get_nickname())) and \
                self.__curr_user.is_registered() and \
                self.__curr_user.is_logged_in():
            store.add_products(self.__curr_user.get_nickname(), products_details)
            return True
        return False

    @logger
    def remove_products(self, store_name: str, products_names: list) -> bool:
        """
        :param store_name: store's name
        :param products_names: list of product's names to remove
        :return: True if products were removed, False otherwise
        """
        store: Store = self.get_store(store_name)
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

    @logger
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

    @logger
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

    @logger
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

    @logger
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

    @logger
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

    @logger
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
            # TODO - check if the jsonpickle.encode convert to json works
            return jsonpickle.encode(store.get_purchases(self.__curr_user.get_nickname()))
        return []

    # ----------- Getters & Setters --------------
    @logger
    def get_subscribers(self):
        return self.__subscribers

    @logger
    def get_stores(self):
        return self.__stores

    @logger
    def get_managers(self):
        return self.__managers

    @logger
    def get_guest(self):
        guest = User()
        return guest

    @logger
    def set_curr_user(self, curr: User):
        self.__curr_user = curr

    def get_curr_user(self):
        return self.__curr_user

    def __repr__(self):
        return repr("TradeControl")
