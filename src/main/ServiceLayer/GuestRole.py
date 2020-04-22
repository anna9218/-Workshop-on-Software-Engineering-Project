from src.main.DomainLayer.Security import Security
from src.main.DomainLayer.TradeControl import TradeControl


class GuestRole:

    def __init__(self):
        pass

    def login(self, nickname, password):
        TradeControl.getInstance().getSubscriber(nickname)

        Security.getInstance().validatedPassword(password)
        TradeControl.getInstance().validateNickName(nickname)

    def logout(self, user_name):
        pass

    def register(self, nickname, password):
        if Security.getInstance().validatedPassword(password) and TradeControl.getInstance().validateNickName(nickname):
            subscriber = TradeControl.getInstance().subscribe()
            subscriber.register(nickname, password)
            return True
        return False

    def search_products(self):
        pass


