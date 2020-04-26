from src.Logger import logger, secureLogger
from src.main.DomainLayer.Registration import Registration
from src.main.DomainLayer.Login import Login
from src.main.DomainLayer.ShoppingCart import ShoppingCart
from src.main.DomainLayer.UserType import UserType
from src.main.DomainLayer.Purchase import Purchase


class User:
    def __init__(self):
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
        return self.__shoppingCart

    @logger
    def remove_from_shopping_cart(self, product):
        return self.__shoppingCart.remove_product(product)

    @logger
    def update_quantity_in_shopping_cart(self, product, quantity):
        return self.__shoppingCart.update_quantity(product, quantity)

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
        return repr ("User")