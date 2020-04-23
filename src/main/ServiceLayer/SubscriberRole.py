from src.main.DomainLayer.TradeControl import TradeControl
from src.main.ServiceLayer.GuestRole import GuestRole


class SubscriberRole(GuestRole):

    def __init__(self):
        pass

    # use case 3.1
    def logout(self, nickname):
        subscriber = TradeControl.getInstance().getSubscriber(nickname)
        if subscriber is not None and subscriber.is_loggedIn():
            subscriber.logout()
            return True
        return False
