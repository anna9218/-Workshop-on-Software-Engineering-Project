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
        if TradeControl.get_instance().register_guest("TradeManager", "123456789"):
            if not DeliveryProxy.get_instance().is_connected():
                return {'response': False, 'msg': "Init system failed! connection to delivery system failed"}
            if not PaymentProxy.get_instance().is_connected():
                return {'response': False, 'msg': "Init system failed! connection to delivery system failed"}
            res = TradeControl.get_instance().add_system_manager("TradeManager", "123456789")
            if res['response']:
                return {'response': True, 'msg': "Init system was successful!"}
            return {'response': False, 'msg': "Init system failed! " + res['msg']}
        # if not DeliveryProxy.get_instance().is_connected() and not PaymentProxy.get_instance().is_connected():
        #     if TradeControl.get_instance().register_guest("TradeManager", "123456789"):
        #         if not DeliveryProxy.get_instance().connect():
        #             return {'response': False, 'msg': "Init system failed! connection to delivery system failed"}
        #         if not PaymentProxy.get_instance().connect():
        #             return {'response': False, 'msg': "Init system failed! connection to delivery system failed"}
        #         res = TradeControl.get_instance().add_system_manager("TradeManager", "123456789")
        #         if res['response']:
        #             return {'response': True, 'msg': "Init system was successful!"}
        #         return {'response': False, 'msg': "Init system failed! " + res['msg']}
        # return {'response': False, 'msg': "Init system failed!"}

    @staticmethod
    def get_user_type():
        return TradeControl.get_instance().get_user_type()

    @staticmethod
    def get_product_details(store_name, product_name):
        return TradeControl.get_product_details(store_name, product_name)

    @staticmethod
    def get_curr_username():
        return TradeControl.get_instance().get_curr_username()

    # functions for tests
    @staticmethod
    def remove_user(nickname: str):
        TradeControl.get_instance().unsubscribe(nickname)

    @staticmethod
    def remove_manager(store_name: str, appointee_nickname: str):
        TradeControl.get_instance().remove_manager(store_name, appointee_nickname)

    @staticmethod
    def remove_store(store_name: str):
        TradeControl.get_instance().close_store(store_name)

    # external system tests functions
    @staticmethod
    def is_payment_connected():
        return PaymentProxy.get_instance().is_connected()

    @staticmethod
    def commit_payment( payment_details: {'card_number': str, 'month': str, 'year': str, 'holder': str,
                                               'ccv': str, 'id': str}):
        return PaymentProxy.get_instance().commit_payment(payment_details)

    @staticmethod
    def cancel_payment(transaction_id: str):
        return PaymentProxy.get_instance().cancel_pay(transaction_id)

    def cause_payment_timeout(self):
        PaymentProxy.get_instance().cause_timeout_error()

    def cause_payment_con_error(self):
        PaymentProxy.get_instance().cause_connection_error()

    def set_connection_payment_back(self):
        PaymentProxy.get_instance().set_connection_back()

    @staticmethod
    def is_delivery_connected():
        return DeliveryProxy.get_instance().is_connected()

    @staticmethod
    def deliver(delivery_details: {'name': str, 'address': str, 'city': str, 'country': str,
                                                  'zip': str}):
        return DeliveryProxy.get_instance().deliver_products(delivery_details)

    @staticmethod
    def cancel_delivery(transaction_id: str):
        return DeliveryProxy.get_instance().cancel_supply(transaction_id)

    @staticmethod
    def cause_delivery_timeout():
        DeliveryProxy.get_instance().cause_timeout_error()

    @staticmethod
    def cause_delivery_con_error():
        DeliveryProxy.get_instance().cause_connection_error()

    @staticmethod
    def set_connection_delivery_back():
        DeliveryProxy.get_instance().set_connection_back()
    # end external system tests functions

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
    def get_store(store_name):
        return TradeControl.get_instance().get_store(store_name)

    def __repr__(self):
        return repr("TradeFacadeService")
