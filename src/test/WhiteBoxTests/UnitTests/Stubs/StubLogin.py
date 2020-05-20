from Backend.src.main.DomainLayer.UserComponent.Login import Login


class StubLogin(Login):

    def __init__(self):
        self.__isLoggedIn = False

    def login(self, username, password):
        if username == "anna9218" and password == "password":
            self.__isLoggedIn = True
        else:
            self.__isLoggedIn = False

    def is_logged_in(self):
        return self.__isLoggedIn

    def set_login(self, value: bool) -> bool:
        self.__isLoggedIn = value
        return True
