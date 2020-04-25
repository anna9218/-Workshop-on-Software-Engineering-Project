from src.main.DomainLayer.TradeControl import TradeControl
from src.main.ServiceLayer.StoreOwnerRole import StoreOwnerRole


class SubscriberRole:

    def __init__(self, subscriber):
        self.__subscriber = subscriber

    # use case 3.1
    def logout(self):
        # subscriber = TradeControl.getInstance().getSubscriber(nickname)
        if self.__subscriber.is_registered() and self.__subscriber.is_logged_in():
            self.__subscriber.logout()
            return True
        return False

    # 3.2 open store
    def open_store(self, store_name):
        # user = TradeControl.getInstance().getUser(user_name)
        if not self.__subscriber.is_registered() or not self.__subscriber.is_logged_in():
            return None
        # TradeControl.get_instance().validate_store_name(store_name)
        new_store = TradeControl.get_instance().open_store(store_name)

        if new_store is None:
            return None
        else:
            new_store.add_owner(self.__subscriber)
            return StoreOwnerRole(self.__subscriber)

    # use case 3.7
    def view_personal_purchase_history(self):
        if self.__subscriber.is_registered and self.__subscriber.is_logged_in():
            return self.__subscriber.get_purchases()


