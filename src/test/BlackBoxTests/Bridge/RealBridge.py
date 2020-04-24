"""
    class representing the:
                            - concrete implementor in the Bridge pattern
                            - adapter in the the adapter pattern
                            - real subject in the proxy pattern
"""
from src.main.DomainLayer.FacadeDelivery import FacadeDelivery
from src.test.BlackBoxTests.Bridge.Bridge import Bridge
from src.main.DomainLayer.FacadePayment import FacadePayment
from src.main.ServiceLayer.TradeControlService import TradeControlService
from src.main.ServiceLayer.GuestRole import GuestRole


class RealBridge(Bridge):

    def __init__(self):
        super().__init__()
        self.__paymentSys = FacadePayment.get_instance()
        self.__deliverySys = FacadeDelivery.get_instance()
        self.__trade_control_srv = TradeControlService()
        self.__guest_role = GuestRole()
        # self.user = User()

    def register_user(self, username, password) -> bool:
        return self.__guest_role.register(username, password)

    def connect_payment_sys(self):
        self.__paymentSys.connect()

    def disconnect_payment_sys(self):
        self.__paymentSys.disconnect()

    def commit_payment(self, username, amount, credit, date) -> bool:
        return self.__paymentSys.commit_payment(username, amount, credit, date)

    def connect_delivery_sys(self):
        self.__deliverySys.connect()

    def deliver(self, username, address) -> bool:
        return self.__deliverySys.deliver_products(username, address)

    def disconnect_delivery_sys(self):
        self.__deliverySys.disconnect()

    def is_delivery_connected(self):
        return self.__deliverySys.is_connected()

    def init_sys(self):
        self.__trade_control_srv.init_system()

    def login(self, username, password):
        return self.__guest_role.login(username, password)

    def search_product(self, option, string):
        return self.__guest_role.search_products_by(option, string)

    def filter_products(self, filter_details, products):
        self.__guest_role.filter_products_by(filter_details, products)

    # view stores' products functions
    def view_stores(self):
        return self.__guest_role.display_stores()

    def view_store_info(self, store, store_info_flag, products_flag):
        return self.__guest_role.display_stores_info(store, store_info_flag, products_flag)
