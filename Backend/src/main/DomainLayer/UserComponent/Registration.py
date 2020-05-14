# from src.main.DomainLayer.User import User
from Backend.src.Logger import logger, secureLogger


class Registration:
    def __init__(self):
        self.__isRegistered = False
        self.__username = None
        self.__password = None

    # @secureLogger
    def register(self, username, password):
        self.__isRegistered = True
        self.__username = username
        self.__password = password

    # @logger
    def get_nickname(self):
        return self.__username

    # @secureLogger
    def get_password(self):
        return self.__password

    # @logger
    def is_registered(self):
        return self.__isRegistered

    def __repr__(self):
        return repr("Registration")