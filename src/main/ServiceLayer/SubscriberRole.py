from src.Logger import logger
from src.main.DomainLayer.TradeControl import TradeControl
from src.main.ServiceLayer.StoreOwnerRole import StoreOwnerRole


class SubscriberRole:

    def __init__(self, subscriber):
        self.__subscriber = subscriber

    # @logger
    # use case 3.1
    def logout(self):
        """
        logs the subscriber out of the system
        :return: True if succeeded, otherwise False
        """
        # subscriber = TradeControl.getInstance().getSubscriber(nickname)
        if self.__subscriber.is_registered() and self.__subscriber.is_logged_in():
            self.__subscriber.logout()
            return True
        return False

    @logger
    # 3.2 open store
    def open_store(self, store_name: str):
        """
        Opens a new store with the given store name
        :param store_name: String
        :return: the Store created, or None
        """
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

    @logger
    # use case 3.7
    def view_personal_purchase_history(self):
        """
        View the subscriber's purchase history
        :return: the subscriber's purchase history or None
        """
        if self.__subscriber.is_registered and self.__subscriber.is_logged_in():
            # return self.__subscriber.get_purchases()
            return self.__subscriber.get_accepted_purchases()
        return None

    def __repr__(self):
        return repr("SubscriberRole")