from datetime import datetime

from src.Logger import logger, secureLogger
from src.main.DomainLayer.StoreComponent.Product import Product
from src.main.DomainLayer.StoreComponent.Purchase import Purchase
from src.main.DomainLayer.UserComponent.Login import Login
from src.main.DomainLayer.UserComponent.Registration import Registration
from src.main.DomainLayer.UserComponent.ShoppingCart import ShoppingCart, DiscountType, PurchaseType
from src.main.DomainLayer.UserComponent.UserType import UserType
# from src.main.DomainLayer.StoreComponent.Purchase import Purchase


class User:
    def __init__(self):
        self.guest_id = id
        self.__registrationState = Registration()
        self.__loginState = Login()
        # self.__appointment = StoreManagerAppointment()
        self.__shoppingCart = ShoppingCart()
        self.__purchase_history = []

    @secureLogger
    def register(self, username: str, password: str):
        if self.__registrationState.get_nickname() is not None:
            return False

        if username.strip() == "" or password.strip() == "":
            return False
        self.__registrationState.register(username, password)
        return True

    @secureLogger
    def login(self, nickname: str, password: str):
        if self.check_nickname(nickname) and self.check_password(password) and not self.is_logged_in():
            self.__loginState.login()
            return True
        return False

    @logger
    def logout(self):
        if not self.is_logged_in():
            return False

        # Else
        self.__loginState.logout()
        return True

    @secureLogger
    def check_password(self, password):
        return self.__registrationState.get_password() == password

    @logger
    def check_nickname(self, nickname):
        return self.__registrationState.get_nickname() == nickname

    @logger
    def is_logged_in(self):
        return self.__loginState.is_logged_in()

    @logger
    def is_logged_out(self):
        return not self.__loginState.is_logged_in()

    @logger
    def get_login(self):
        return self.__loginState

    @logger
    def is_registered(self):
        return self.__registrationState.is_registered()

    @logger
    def get_nickname(self):
        return self.__registrationState.get_nickname()

    @logger
    def get_purchase_history(self):
        return self.__purchase_history

    @logger
    def save_products_to_basket(self, products_stores_quantity_ls: [{"store_name": str,
                                                                     "product": Product,
                                                                     "amount": int, "discount_type": DiscountType,
                                                                     "purchase_type": PurchaseType}]):
        return self.__shoppingCart.add_products(products_stores_quantity_ls)

    @logger
    def view_shopping_cart(self):
        """
        :return: list: [{"store_name": str,
                         "basket": [{"product_name": str
                                     "amount": int}, ...]
                        }, ...]
        """
        return self.__shoppingCart.view_shopping_cart()

    @logger
    def remove_from_shopping_cart(self, products_details: [{"product_name": str, "store_name": str}]):
        """
        :param products_details: [{"product_name": str,
                                       "store_name": str}, ...]
        :return: True on success, False when one of the products doesn't exist in the shopping cart
        """
        return self.__shoppingCart.remove_products(products_details)

    @logger
    def update_quantity_in_shopping_cart(self, products_details: [{"product_name": str, "store_name": str, "amount": int}]):
        """
        :param flag: action option - "remove"/"update"
        :param products_details: [{"product_name": str,
                                       "store_name": str,
                                       "amount": int}, ...]
        :return: True on success, False when one of the products doesn't exist in the shopping cart
        """
        return self.__shoppingCart.update_quantity(products_details)

    # def get_appointment (self):
    #     return self.__appointment

    @logger
    def get_user_type(self):
        if self.is_logged_in():
            return UserType.Subscriber
        else:
            return UserType.Guest

    @logger
    def set_registration_state(self, registration):
        self.__registrationState = registration
        return True

    # --- Do we need this ?? ---

    @logger
    def set_shopping_cart(self, shopping_cart):
        self.__shoppingCart = shopping_cart
    #
    # @logger
    # def set_login_state(self, login_state):
    #     self.__loginState = login_state

    @logger
    def complete_purchase(self, purchase: Purchase):
        # add purchase to purchase history
        self.__purchase_history.append(purchase)
        # delete purchase from shopping cart
        self.__shoppingCart.get_store_basket(purchase.get_store_name()).complete_purchase(purchase.get_products())

    @logger
    def remove_purchase(self, store_name: str, date: datetime):
        for p in self.__purchase_history:
            if p.get_store_name() == store_name and p.get_date() == date:
                self.__purchase_history.remove(p)

    @logger
    def get_shopping_cart(self) -> ShoppingCart:
        return self.__shoppingCart

    def __repr__(self):
        return repr("User")

    def __eq__(self, other):
        try:
            return self.get_nickname() == other.get_nickname()
        except Exception:
            return False
