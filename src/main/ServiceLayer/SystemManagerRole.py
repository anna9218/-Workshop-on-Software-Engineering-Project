from src.Logger import logger
from src.main.DomainLayer.Store import Store
from src.main.DomainLayer.User import User
from src.main.DomainLayer.TradeControl import TradeControl


class SystemManagerRole:

    def __init__(self, username):
        user = (TradeControl.get_instance()).get_appointee(username)
        if not user:
            AttributeError(str("The user " + username + " is not a system manager."))
        else:
            self.__user = user

# ---------------------------------------------------- U.C 6.4 ---------------------------------------------------------

    @logger
    def view_user_purchase_history(self, username) -> (list or None):
        """
        This function returns all the purchases that are done by a specific user.

        :param username: the user to view.
        :return: list of user purchases.
        """
        subscriber_to_view: User = (TradeControl.get_instance()).get_subscriber(username)
        if subscriber_to_view:
            return subscriber_to_view.get_accepted_purchases()
        else:
            return None

    @logger
    def view_store_purchases_history(self, store_name: str) -> (list or None):
        """

        :param store_name: the store to view
        :return: list of purchases
        """
        store_to_view: Store = (TradeControl.get_instance()).get_store(store_name)
        if store_to_view:
            return store_to_view.get_purchases("")
        else:
            return None

    def __repr__(self):
        return repr("SystemManagerRole")
