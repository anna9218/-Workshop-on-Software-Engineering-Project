from src.main.DomainLayer.TradeControl import TradeControl
from src.main.ServiceLayer.GuestRole import GuestRole


class SubscriberRole(GuestRole):

    def __init__(self, subscriber):
        self.__subscriber = subscriber

    # use case 3.1
    def logout(self, nickname):
        # subscriber = TradeControl.getInstance().getSubscriber(nickname)
        if self.__subscriber.is_logged_in():
            self.__subscriber.logout()
            return True
        return False

    # 3.2 open store
    def open_store(self, store_name) -> bool:
        # user = TradeControl.getInstance().getUser(user_name)
        if self.__subscriber.is_logged_in():
            return False
        TradeControl.get_instance().validate_store_name(store_name)
        new_store = TradeControl.get_instance().open_store(self.__subscriber, store_name)
        if new_store is None:
            return False
        else:
            # TODO: appoint me as manager of the
            return False
                # new_store.add_owner(self.__subscriber) and appointment.appoint_owner(None, self, new_store)

    # use case 3.7
    def view_personal_purchase_history(self):
        pass

