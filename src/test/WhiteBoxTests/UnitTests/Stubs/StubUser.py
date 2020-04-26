from src.main.DomainLayer.User import User


class StubUser(User):

    def __init__(self):
        # super().__init__()
        self.__nickname = ""
        self.__password = ""

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
        return True
