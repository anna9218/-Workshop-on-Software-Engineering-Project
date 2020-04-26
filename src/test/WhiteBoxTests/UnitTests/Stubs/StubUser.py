from src.main.DomainLayer.Purchase import Purchase
from src.main.DomainLayer.User import User
from src.test.WhiteBoxTests.UnitTests.Stubs.StubLogin import StubLogin
from datetime import datetime as date_time


class StubUser(User):

    def __init__(self):
        # super().__init__()
        self.__nickname = ""
        self.__password = ""
        self.__loginState = StubLogin()
        self.__accepted_purchases = [Purchase(35, 1, 29.99, "Some Store", "anna9218")]

    def login(self, nickname, password):
        return self.__loginState.login(nickname, password)

    def logout(self):
        if self.is_logged_in():
            self.__loginState.set_login(False)
            return True
        return False

    def register(self, username, password):
        self.__nickname = username
        self.__password = password

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

    def is_registered(self):
        return True

    def is_logged_in(self):
        return self.__loginState.is_logged_in()

    def get_accepted_purchases(self):
        return self.__accepted_purchases

