from src.Logger import logger


class Logout:
    def __init__(self):
        self.__isLoggedOut = True

    @classmethod
    @logger
    def logout(cls, user):
        pass
        # cls.set_state(True)
        # user.loginState.set_state(False)

    @classmethod
    @logger
    def set_state(cls, state):
        cls.__isLoggedOut = state
