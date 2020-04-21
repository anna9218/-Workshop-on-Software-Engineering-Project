class Login:
    def __init__(self):
        self.isLoggedIn = False

    @classmethod
    def login(cls, user, username, password):
        # checking if username and password are correct
        if user.registrationState.username == username and user.registrationState.password == password:
            cls.set_state(True)
            user.logoutState.set_state(False)
            return True
        else:
            print("login failed")
            return False

    @classmethod
    def set_state(cls, state):
        cls.isLoggedIn = state
