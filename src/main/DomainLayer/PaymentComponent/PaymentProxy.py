from datetime import datetime as date_time

from src.Logger import logger, loggerStaticMethod, errorLogger
from src.main.DomainLayer.PaymentComponent.PaymentSubject import PaymentSubject


class PaymentProxy(PaymentSubject):
    __instance = None
    __realSubject = None

    @staticmethod
    def get_instance():
        """ Static access method. """
        loggerStaticMethod("FacadePayment.get_instance", [])
        if PaymentProxy.__instance is None:
            PaymentProxy()
        return PaymentProxy.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if PaymentProxy.__instance is not None:
            errorLogger("This class is a singleton!")
            raise Exception("This class is a singleton!")
        else:
            self.__isConnected = False
            if PaymentProxy.__realSubject:
                PaymentProxy.__instance = self.__realSubject
            else:
                PaymentProxy.__instance = self

    @logger
    def connect(self):
        try:
            if not self.__isConnected:
                self.__isConnected = True
        except Exception:
            errorLogger("System is down!")
            raise ResourceWarning("System is down!")

    @logger
    # need to check payment details with system once a system is set
    def commit_payment(self, username, amount, credit, date) -> bool:
        try:
            if not self.__isConnected or not self.__check_valid_details(username, amount, credit, date):
                return False
            else:
                return True
        except Exception:
            errorLogger("System is down!")
            raise ResourceWarning("System is down!")

    @logger
    def disconnect(self):
        try:
            if self.__isConnected:
                self.__isConnected = False
        except Exception:
            errorLogger("System is down!")
            raise ResourceWarning("System is down!")

    @logger
    def is_connected(self) -> bool:
        return self.__isConnected

    @staticmethod
    def __check_valid_details(name, amount, credit, date) -> bool:
        loggerStaticMethod("__check_valid_details", [name, amount, credit, date])
        if type(date) != date_time:
            return False

        if len(name) == 0 or len(credit) == 0 or (date_time.today().date() > date.date()) or amount <= 0:
            return False
        else:
            return True

    def __repr__(self):
        return repr ("FacadePayment")