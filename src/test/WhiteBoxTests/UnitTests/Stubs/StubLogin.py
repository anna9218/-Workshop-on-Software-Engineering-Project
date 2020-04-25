from src.main.DomainLayer.Login import Login


class StubLogin(Login):

    def __init__(self):
        self.isLoggedIn = False

    def login(self, username, password):
        if username == "anna9218" and password == "password":
            self.isLoggedIn = True
        else:
            self.isLoggedIn = False
