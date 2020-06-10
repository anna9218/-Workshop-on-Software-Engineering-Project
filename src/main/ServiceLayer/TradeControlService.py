from datetime import datetime

from src.Logger import loggerStaticMethod
from src.main.DomainLayer.DeliveryComponent.DeliveryProxy import DeliveryProxy
from src.main.DomainLayer.PaymentComponent.PaymentProxy import PaymentProxy
from src.main.DomainLayer.TradeComponent.TradeControl import TradeControl


class TradeControlService:

    def __init__(self):
        pass

    # use case 1.1
    @staticmethod
    def init_system():
        loggerStaticMethod("init_system", [])
        if not DeliveryProxy.get_instance().is_connected() and not PaymentProxy.get_instance().is_connected():
            if TradeControl.get_instance().register_guest("TradeManager", "123456789"):
                if not DeliveryProxy.get_instance().connect():
                    return {'response': False, 'msg': "Init system failed! connection to delivery system failed"}
                if not PaymentProxy.get_instance().connect():
                    return {'response': False, 'msg': "Init system failed! connection to delivery system failed"}
                res = TradeControl.get_instance().add_system_manager("TradeManager", "123456789")
                if res['response']:
                    return {'response': True, 'msg': "Init system was successful!"}
                return {'response': False, 'msg': "Init system failed! " + res['msg']}
        return {'response': False, 'msg': "Init system failed!"}

    @staticmethod
    def get_user_type():
        return TradeControl.get_instance().get_user_type()

    # functions for tests???
    @staticmethod
    def remove_user(nickname: str):
        TradeControl.get_instance().unsubscribe(nickname)

    @staticmethod
    def remove_manager(store_name: str, appointee_nickname: str):
        TradeControl.get_instance().remove_manager(store_name, appointee_nickname)

    @staticmethod
    def is_payment_connected():
        return PaymentProxy.get_instance().is_connected()

    @staticmethod
    def is_delivery_connected():
        return DeliveryProxy.get_instance().is_connected()

    @staticmethod
    def remove_store(store_name: str):
        TradeControl.get_instance().close_store(store_name)

    @staticmethod
    def connect_delivery():
        DeliveryProxy.get_instance().connect()

    @staticmethod
    def connect_payment():
        PaymentProxy.get_instance().connect()

    @staticmethod
    def disconnect_delivery():
        DeliveryProxy.get_instance().disconnect()

    @staticmethod
    def disconnect_payment():
        PaymentProxy.get_instance().disconnect()

    @staticmethod
    def commit_payment(product_ls):
        return PaymentProxy.get_instance().commit_payment(product_ls)

    @staticmethod
    def deliver(address: str, products_ls):
        return DeliveryProxy.get_instance().deliver_products(address, products_ls)

    @staticmethod
    def subscribe_user(nickname: str, password: str):
        TradeControl.get_instance().register_test_user(nickname, password)

    @staticmethod
    def remove_purchase(store_name: str, purchase_date: datetime):
        TradeControl.get_instance().remove_purchase(store_name, purchase_date)

    @staticmethod
    def set_user(nickname: str):
        TradeControl.get_instance().set_curr_user_by_name(nickname)

    @staticmethod
    def get_manager_permissions(store_name: str):
        return TradeControl.get_instance().get_manager_permissions(store_name)

    def __repr__(self):
        return repr("TradeFacadeService")
