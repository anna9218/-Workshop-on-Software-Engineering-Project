from src.main.DomainLayer.Appointment import Appointment
from src.main.DomainLayer.Registration import Registration
from src.main.DomainLayer.Login import Login
from src.main.DomainLayer.Logout import Logout
from src.main.DomainLayer.ShoppingCart import ShoppingCart


class User:
    def __init__(self):
        self.__registrationState = Registration()
        self.__loginState = Login()
        # self.__logoutState = Logout()
        self.__appointment = Appointment()
        self.__shoppingCart = ShoppingCart()

    def register(self, username, password):
        self.__registrationState.register(username, password)
        # if ackMSG:
        #     print("registered successfully")
        # else:
        #     print("something failed, please try again")
            
    def login(self, nickname, password):
        if self.check_nickname(nickname) and self.check_password(password):
            return self.__loginState.login()
        return False

    def logout(self):
        return self.__loginState.logout()
        # ackMSG = self.__loginState.login(self, username, password)
        # if ackMSG:
        #     print("logged in successfully")
        # else:
        #     print("error while logging in")

    # def logout(self):
    #     ackMSG = self.__logoutState.logout(self)
    #     print("logged out successfully")

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

    # def get_logout(self):
    #     return self.__logoutState

    def is_registered(self):
        return self.__registrationState.is_registered()

    def get_nickname(self):
        return self.__registrationState.get_nickname()

    # def get_name(self):
    #     return self.__name
    #
    # def set_price(self, new_price):
    #     self.__price = new_price
    #
    # def set_name(self, new_name):
    #     self.__name = new_name

    def save_products_to_basket(self, products_stores_quantity_ls):
        self.__shoppingCart.add_products(products_stores_quantity_ls)

    def view_shopping_cart(self):
        return self.__shoppingCart

    def remove_from_shopping_cart(self, product):
        self.__shoppingCart.remove_product(product)

    def update_quantity_in_shopping_cart(self, product, quantity):
        self.__shoppingCart.update_quantity(product, quantity)

