class FacadePayment:
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if FacadePayment.__instance is None:
            FacadePayment()
        return FacadePayment.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if FacadePayment.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            self.__isConnected = False
            FacadePayment.__instance = self

    def connect(self):
        if not self.__isConnected:
            self.__isConnected = True

    # need to check payment details with system once a system is set
    def commit_payment(self, username, amount, credit, date) -> bool:
        if not self.__isConnected or not self.__check_valid_details(username, amount, credit, date):
            return False
        else:
            return True

    def disconnect(self):
        if self.__isConnected:
            self.__isConnected = False

    def is_connected(self) -> bool:
        return self.__isConnected

    @staticmethod
    def __check_valid_details(name, amount, credit, date) -> bool:
        if len(name) == 0 or len(credit) == 0 or len(date) == 0 or amount <= 0:
            return False
        else:
            return True
