from Backend.src.main.DomainLayer.UserComponent.Registration import Registration


class StubRegistration(Registration):
    def __init__(self):
        self.__isRegistered = False
        self.count = 0

    def register(self, username, password):
        if username == "anna9218" and self.count == 0:
            self.__isRegistered = True
            self.count = 1
        else:
            self.__isRegistered = False

    def get_nickname(self):
        return "anna9218"

    def get_password(self):
        return "password"

    def is_registered(self):
        return self.__isRegistered
