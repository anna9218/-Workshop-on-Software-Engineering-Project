from src.main.DomainLayer.User import User


class StubUser(User):

    def __init__(self, trade_control):
        super().__init__(trade_control)

    def register(self, username, password):
        pass

    def get_trade_control(self):
        return self.get_trade_control()

    def get_login(self):
        return self.get_login()

    def get_logout(self):
        return self.get_logout()

    def get_registration(self):
        return self.get_registration()
