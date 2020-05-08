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
            super().__init__()
            self.__isConnected = False
            if PaymentProxy.__realSubject:
                PaymentProxy.__instance = self.__realSubject
            else:
                PaymentProxy.__instance = self

    # @logger
    def connect(self):
        try:
            if not self.__isConnected:
                self.__isConnected = True
                return True
            else:
                return False
        except Exception:
            errorLogger("System is down!")
            raise ResourceWarning("System is down!")

    # @logger
    # need to check payment details with system once a system is set
    def commit_payment(self, products_ls: {"total_price": float, "purchases": [dict]}) -> bool:
        try:
            if not self.__isConnected or not self.__check_valid_details(products_ls):
                return False
            else:
                return True
        except Exception:
            errorLogger("System is down!")
            raise ResourceWarning("System is down!")

    # @logger
    def disconnect(self):
        try:
            if self.__isConnected:
                self.__isConnected = False
                return True
            else:
                return False
        except Exception:
            errorLogger("System is down!")
            raise ResourceWarning("System is down!")

    def cancel_payment(self, purchase_ls):
        return True

    # @logger
    def is_connected(self) -> bool:
        return self.__isConnected

    @staticmethod
    def __check_valid_details(products_ls) -> bool:
        loggerStaticMethod("__check_valid_details", [products_ls])
        if len(products_ls["purchases"]) == 0 or products_ls["total_price"] == 0:
            return False
        else:
            return True

    def __delete__(self):
        PaymentProxy.__instance = None

    def __repr__(self):
        return repr("FacadePayment")