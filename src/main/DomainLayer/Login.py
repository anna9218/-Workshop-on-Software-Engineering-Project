class Login:
    def __init__(self):
        self.__isLoggedIn = False

    def login(self):
        self.__isLoggedIn = True

    def logout(self):
        self.__isLoggedIn = False

    def is_logged_in(self):
        return self.__isLoggedIn
