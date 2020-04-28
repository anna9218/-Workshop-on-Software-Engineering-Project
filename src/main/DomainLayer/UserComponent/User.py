from src.Logger import logger, secureLogger
from src.main.DomainLayer.UserComponent.Registration import Registration
from src.main.DomainLayer.UserComponent.Login import Login
from src.main.DomainLayer.UserComponent.ShoppingCart import ShoppingCart
from src.main.DomainLayer.UserComponent.UserType import UserType
from src.main.DomainLayer.StoreComponent.Purchase import Purchase


class User:
    def __init__(self):
        self.guest_id = id
        self.__registrationState = Registration()
        self.__loginState = Login()
        # self.__appointment = StoreManagerAppointment()
        self.__shoppingCart = ShoppingCart()
        self.__accepted_purchases = []
        self.__unaccepted_purchases: [] = []

    @secureLogger
    def register(self, username, password):
        self.__registrationState.register(username, password)
        return True

    @secureLogger
    def login(self, nickname, password):
        if self.check_nickname(nickname) and self.check_password(password):
            self.__loginState.login()
            return True
        return False

    @logger
    def logout(self):
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
    def get_accepted_purchases(self):
        return self.__accepted_purchases

    @logger
    def get_unaccepted_purchases(self):
        return self.__unaccepted_purchases

    @logger
    def save_products_to_basket(self, products_stores_quantity_ls):
        return self.__shoppingCart.add_products(products_stores_quantity_ls)

    @logger
    def view_shopping_cart(self):
        """
        :return: list: [{"store_name": str,
                         "basket": [{"product_name": str
                                     "amount": int}, ...]
                        }, ...]
        """
        return self.__shoppingCart.get_cart_info()

    @logger
    def remove_from_shopping_cart(self, products_details: [{"product_name": str, "store_name": str, "amount": int}]):
        """
        :param products_details: [{"product_name": str,
                                       "store_name": str,
                                       "amount": int}, ...]
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

    @logger
    def set_shopping_cart(self, shopping_cart):
        self.__shoppingCart = shopping_cart
        return True

    @logger
    def set_login_state(self, login_state):
        self.__loginState = login_state

    @logger
    def add_unaccepted_purchase(self, purchase: Purchase):
        self.__unaccepted_purchases.insert(0, purchase)

    @logger
    def remove_unaccepted_purchase(self, purchase: Purchase):
        self.__unaccepted_purchases.remove(purchase)

    @logger
    def add_accepted_purchase(self, purchase: Purchase):
        self.__accepted_purchases.insert(0, purchase)

    def __repr__(self):
        return repr("User")
