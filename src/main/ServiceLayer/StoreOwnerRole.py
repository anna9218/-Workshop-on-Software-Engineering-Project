from src.main.DomainLayer.User import User
from src.main.DomainLayer.TradeControl import TradeControl
from src.main.DomainLayer.Security import Security


class StoreOwnerRole:
    def __init__(self, user):
        self.__user = user

    # def open_store_func(self, user_name, store_name):
        # user = TradeControl.getInstance().getUser(user_name)
        # if user
        # TradeControl.getInstance().validate_store_name(self.store_name)

