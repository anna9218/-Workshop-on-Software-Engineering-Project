from Backend.src.Logger import logger
from Backend.src.main.DomainLayer.TradeComponent.TradeControl import TradeControl


class SystemManagerRole:

    def __init__(self):
        pass

# ---------------------------------------------------- U.C 6.4 ---------------------------------------------------------

    # @logger
    def view_user_purchase_history(self, viewed_user: str):
        """
        This function returns all the purchases that are done by a specific user.
        :param viewed_user: the user to view.
        :return: list of json objects containing the users' purchases or None if none exist
        """
        return TradeControl.get_instance().view_user_purchase_history(viewed_user)

    # @logger
    def view_store_purchases_history(self, store_name: str):
        """
        :param store_name: the store to view
        :return: list of purchases
        """
        return TradeControl.get_instance().view_store_purchases_history(store_name)

    def __repr__(self):
        return repr("SystemManagerRole")
