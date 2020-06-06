from src.Logger import logger, loggerStaticMethod
from src.main.DomainLayer.TradeComponent.TradeControl import TradeControl


class SubscriberRole:

    def __init__(self):
        pass

    @staticmethod
    @logger
    # use case 3.1
    def logout() -> {'response': bool, 'msg': str}:
        """
        logs the subscriber out of the system
        :return: dict = {'response': bool, 'msg': str}
                 response = True if succeeded, otherwise False
        """
        loggerStaticMethod("SubscriberRole.logout", [])
        return TradeControl.get_instance().logout_subscriber()

    @staticmethod
    @logger
    # 3.2 open store
    def open_store(store_name: str) -> {'response': bool, 'msg': str}:
        """
        Opens a new store with the given store name
        :param store_name: String
        :return: dict = {'response': bool, 'msg': str}
                 response = true if the store is created, else false
        """
        loggerStaticMethod("SubscriberRole.open_store",["store_name"])
        return TradeControl.get_instance().open_store(store_name)

    @staticmethod
    @logger
    # use case 3.7
    def view_personal_purchase_history() -> {'response': list, 'msg': str}:
        """
        View the subscriber's purchase history
        :return: list of json objects containing the subscriber's purchase history or None if none exist
        """
        loggerStaticMethod("SubscriberRole.view_personal_purchase_history", [])
        return TradeControl.get_instance().view_personal_purchase_history()

    def __repr__(self):
        return repr("SubscriberRole")
