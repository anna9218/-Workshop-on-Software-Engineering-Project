from src.Logger import logger
from src.main.DomainLayer.Store import Store
from src.main.DomainLayer.User import User
from src.main.DomainLayer.TradeControl import TradeControl


class SystemManagerRole:

    def __init__(self):
        pass

# ---------------------------------------------------- U.C 6.4 ---------------------------------------------------------

    @logger
    def view_user_purchase_history(self, nickname):
        """
        This function returns all the purchases that are done by a specific user.
        :param nickname: the user to view.
        :return: list of json objects containing the users' purchases or None if none exist
        """
        return TradeControl.get_instance().view_user_purchase_history(nickname)

    @logger
    def view_store_purchases_history(self, store_name: str):
        """

        :param store_name: the store to view
        :return: list of purchases
        """
        return TradeControl.get_instance().view_store_purchases_history(store_name)

    def __repr__(self):
        return repr("SystemManagerRole")
