from src.main.DomainLayer.Appointment import Appointment
from src.main.DomainLayer.Registration import Registration
from src.main.DomainLayer.Login import Login
from src.main.DomainLayer.ShoppingCart import ShoppingCart
from src.main.DomainLayer.UserType import UserType


class User:
    def __init__(self):
        self.__registrationState = Registration()
        self.__loginState = Login()
        self.__appointment = Appointment()
        self.__shoppingCart = ShoppingCart()
        self.__purchases = []

    def register(self, username, password):
        self.__registrationState.register(username, password)
        return True
           
    def login(self, nickname, password):
        if self.check_nickname(nickname) and self.check_password(password):
            self.__loginState.login()
            return True
        return False

    def logout(self):
        self.__loginState.logout()
        return True

    def check_password(self, password):
        return self.__registrationState.get_password() == password

    def check_nickname(self, nickname):
        return self.__registrationState.get_nickname() == nickname

    def is_logged_in(self):
        return self.__loginState.is_logged_in()

    def is_logged_out(self):
        return not self.__loginState.is_logged_in()

    def get_login(self):
        return self.__loginState

    def is_registered(self):
        return self.__registrationState.is_registered()

    def get_nickname(self):
        return self.__registrationState.get_nickname()

    def get_purchases(self):
        return self.__purchases

    def save_products_to_basket(self, products_stores_quantity_ls):
        return self.__shoppingCart.add_products(products_stores_quantity_ls)

    def view_shopping_cart(self):
        return self.__shoppingCart

    def remove_from_shopping_cart(self, product):
        self.__shoppingCart.remove_product(product)

    def update_quantity_in_shopping_cart(self, product, quantity):
        self.__shoppingCart.update_quantity(product, quantity)

    def get_appointment (self):
        return self.__appointment
      
    def get_user_type(self):
        if self.is_logged_in():
            return UserType.Subscriber
        else:
            return UserType.Guest
