from src.main.DomainLayer.Security import Security
from src.main.DomainLayer.TradeControl import TradeControl


class GuestRole:

    def __init__(self):
        pass

    # use case 2.2
    @staticmethod
    def register(self, nickname, password):
        if Security.getInstance().validatedPassword(password) and TradeControl.getInstance().validateNickName(nickname):
            subscriber = TradeControl.getInstance().subscribe()
            subscriber.register(nickname, password)
            return True
        return False

    # use case 2.3
    @staticmethod
    def login(self, nickname, password):
        subscriber = TradeControl.getInstance().getSubscriber(nickname)
        if subscriber is not None and subscriber.is_loggedOut() and subscriber.checkPassword(password):
            subscriber.login()
            return True
        return False

        # if user.registrationState.is_registered() and
        #    user.registrationState.get_name() == username and
        #    user.registrationState.get_password() == password:
        #
        #     cls.set_state(True)
        #     user.logoutState.set_state(False)
        #     return True
        # else:
        #     print("login failed")
        #     return False

    # use case 2.4
    def display_stores_info(self):
        pass

    # use case 2.5
    @staticmethod
    def search_products(self):
        pass


