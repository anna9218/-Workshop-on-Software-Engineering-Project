class Logout:
    def __init__(self):
        self.isLoggedOut = True

    @classmethod
    def logout(cls, user):
        cls.set_state(True)
        user.loginState.set_state(False)

    @classmethod
    def set_state(cls, state):
        cls.isLoggedOut = state
