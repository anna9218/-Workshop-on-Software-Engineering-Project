from src.main.DomainLayer.Registration import Registration


class StubRegistration(Registration):

    def __init__(self):
        self.__isRegistered = False
        self.__count = 0

    def register(self, username, password):
        if username == "anna9218" and self.__count == 0:
            self.__isRegistered = True
            self.__count = 1
        else:
            self.__isRegistered = False

    def is_registered(self):
        return self.__isRegistered
