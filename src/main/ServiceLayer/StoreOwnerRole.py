from src.main.DomainLayer.User import User
from src.main.DomainLayer.TradeControl import TradeControl
from src.main.DomainLayer.Security import Security


class StoreOwnerRole:
    def __init__(self):
        pass

    def open_store_func(self, user_name, store_name) -> bool:
        user = TradeControl.getInstance().getUser(user_name)
        if user is None or not user.is_loggedIn():
            return False
        TradeControl.getInstance().validate_store_name(store_name)
        new_store = TradeControl.getInstance().open_store(self, store_name)
        if new_store is None:
            return False
        else:

            return new_store.add_owner(user) and appointment.appoint_owner(None, self, new_store)

