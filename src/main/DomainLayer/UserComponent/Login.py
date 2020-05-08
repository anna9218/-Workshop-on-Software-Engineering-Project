from src.Logger import logger


class Login:
    def __init__(self):
        self.__isLoggedIn = False

    # @logger
    def login(self):
        self.__isLoggedIn = True

    # @logger
    def logout(self):
        self.__isLoggedIn = False

    # @logger
    def is_logged_in(self):
        return self.__isLoggedIn

    def __repr__(self):
        return repr ("Login")