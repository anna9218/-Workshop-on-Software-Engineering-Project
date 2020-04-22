
class FacadeDelivery:

    def __init__(self):
        self.__isConnected = False

    def connect(self):
        if not self.__isConnected:
            self.__isConnected = True

    # need to check address details with system once a system is set
    def deliver_products(self, username, address) -> bool:
        if not self.__isConnected or not self.__check_valid_details(username, address):
            return False
        else:
            return True

    def disconnect(self):
        if self.__isConnected:
            self.__isConnected = False

    def is_connected(self) -> bool:
        return self.__isConnected

    @staticmethod
    def __check_valid_details(username, address) -> bool:
        if len(username) == 0 or len(address) == 0:
            return False
        else:
            return True
