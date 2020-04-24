class FacadeDelivery:
    __instance = None

    @staticmethod
    def get_instance():
        """ Static access method. """
        if FacadeDelivery.__instance is None:
            FacadeDelivery()
        return FacadeDelivery.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if FacadeDelivery.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            self.__isConnected = False
            FacadeDelivery.__instance = self

    def connect(self):
        try:
            if not self.__isConnected:
                self.__isConnected = True
        except Exception:
            raise ResourceWarning("System is down!")

    # need to check address details with system once a system is set
    def deliver_products(self, username, address) -> bool:
        try:
            if not self.__isConnected or not self.__check_valid_details(username, address):
                return False
            else:
                return True
        except Exception:
            raise ResourceWarning("System is down!")

    def disconnect(self):
        try:
            if self.__isConnected:
                self.__isConnected = False
        except Exception:
            raise ResourceWarning("System is down!")

    def is_connected(self) -> bool:
        return self.__isConnected

    @staticmethod
    def __check_valid_details(username, address) -> bool:
        if len(username) == 0 or len(address) == 0:
            return False
        else:
            return True
