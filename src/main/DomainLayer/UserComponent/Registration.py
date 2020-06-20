# from src.main.DomainLayer.User import User
from src.Logger import secureLogger, logger
import hashlib, binascii, os


class Registration:
    def __init__(self):
        self.__isRegistered = False
        self.__username = None
        self.__password = None

    @secureLogger
    def register(self, username, password):
        self.__isRegistered = True
        self.__username = username
        # self.__password = password
        self.__password = self.make_password_hash(password)

    @logger
    def unregistered(self):
        self.__isRegistered = False
        self.__username = None
        self.__password = None

    @logger
    def get_nickname(self):
        return self.__username

    @secureLogger
    def get_password(self):
        return self.__password

    @logger
    def is_registered(self):
        return self.__isRegistered

    @logger
    def make_password_hash(self, password):
        """
        Hash the received password for safely storing in the DB
        :param password: the received password
        :return: hashed password
        """""
        salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
        pass_hash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 100000)
        pass_hash = binascii.hexlify(pass_hash)
        return (salt + pass_hash).decode('ascii')

    def __repr__(self):
        return repr("Registration")