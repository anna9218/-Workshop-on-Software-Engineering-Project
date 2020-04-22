class Login:
    def __init__(self):
        self.__isLoggedIn = False

    # @classmethod
    def login(self):
        if self.__isLoggedIn:
            return False
        self.__isLoggedIn = True
        return True
        # checking if username and password are correct
        # if user.registrationState.is_registered() and user.registrationState.get_name() == username and user.registrationState.get_password() == password:
        #
        #     cls.set_state(True)
        #     user.logoutState.set_state(False)
        #     return True
        # else:
        #     print("login failed")
        #     return False

    def logout(self):
        if not self.__isLoggedIn:
            return False
        self.__isLoggedIn = False
        return False
    # @classmethod
    # def set_state(cls, state):
    #     cls.__isLoggedIn = state

    def is_logged_in(self):
        return self.__isLoggedIn
