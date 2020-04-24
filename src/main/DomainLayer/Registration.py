# from src.main.DomainLayer.User import User


class Registration:
    def __init__(self):
        self.__isRegistered = False
        self.__username = None
        self.__password = None

    def register(self, username, password):
        self.__isRegistered = True
        self.__username = username
        self.__password = password

    # @classmethod
    # def checkUsername(self, user, username):
    #     isValid = True
    #     for u in user.get_trade_control().get_users():
    #         if u.registrationState.get_username() == username:
    #             isValid = False
    #     return isValid

    # @classmethod
    # def checkPassword(self, password):
    #     return True

    def get_nickname(self):
        return self.__username

    def get_password(self):
        return self.__password

    def is_registered(self):
        return self.__isRegistered
