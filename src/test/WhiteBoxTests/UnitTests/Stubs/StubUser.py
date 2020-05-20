from src.main.DomainLayer.StoreComponent.Purchase import Purchase
from src.main.DomainLayer.UserComponent.ShoppingCart import ShoppingCart
from src.main.DomainLayer.UserComponent.User import User
from src.test.WhiteBoxTests.UnitTests.Stubs.StubLogin import StubLogin


class StubUser(User):

    def __init__(self):
        # super().__init__()
        self.__nickname = ""
        self.__password = ""
        self.__login = False
        self.__register = False
        self.__accepted_purchases = [Purchase([{"product_name": "Eytan's Product", "product_price": 12.0, "amount": 10}]
                                              , 120.0, "Eytan's store", "eytaniva")]
        self.__shoppingCart = ShoppingCart()

    def login(self, nickname, password):
        self.__login = True
        return True

    def logout(self):
        self.__login = False

    def register(self, username, password):
        self.__register = True
        self.__nickname = username
        self.__password = password

    def unregistered(self):
        self.__register = False
        self.__nickname = None
        self.__password = None

    def is_registered(self):
        return self.__register

    def is_logged_in(self):
        return self.__login

    def get_trade_control(self):
        return self.get_trade_control()

    def get_login(self):
        return self.get_login()

    def get_logout(self):
        return self.get_logout()

    def get_registration(self):
        return self.get_registration()

    def get_nickname(self):
        return self.__nickname

    def set_password_and_nickname(self, name, password):
        self.__nickname = name
        self.__password = password

    def get_accepted_purchases(self):
        return self.__accepted_purchases

