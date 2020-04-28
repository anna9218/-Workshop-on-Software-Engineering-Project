from src.Logger import logger, errorLogger, loggerStaticMethod
from src.main.DomainLayer.DeliveryComponent.DeliverySubject import DeliverySubject


class DeliveryProxy(DeliverySubject):
    __instance = None
    __realSubject = None

    @staticmethod
    def get_instance():
        """ Static access method. """
        loggerStaticMethod("FacadeDelivery.get_instance",[])
        if DeliveryProxy.__instance is None:
            DeliveryProxy()
        return DeliveryProxy.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if DeliveryProxy.__instance is not None:
            errorLogger("This class is a singleton!")
            raise Exception("This class is a singleton!")
        else:
            self.__isConnected = False
            if DeliveryProxy.__realSubject:
                DeliveryProxy.__instance = self.__realSubject
            else:
                DeliveryProxy.__instance = self

    @logger
    def connect(self):
        try:
            if not self.__isConnected:
                self.__isConnected = True
        except Exception:
            errorLogger("System is down!")
            raise ResourceWarning("System is down!")

    @logger
    # need to check address details with system once a system is set
    def deliver_products(self, username, address) -> bool:
        try:
            if not self.__isConnected or not self.__check_valid_details(username, address):
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
    def __check_valid_details(username, address) -> bool:
        loggerStaticMethod("__check_valid_details", [username, address])
        if len(username) == 0 or len(address) == 0:
            return False
        else:
            return True

    def __repr__(self):
        return repr("FacadeDelivery")