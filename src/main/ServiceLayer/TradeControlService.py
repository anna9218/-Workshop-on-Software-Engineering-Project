from src.Logger import loggerStaticMethod
from src.main.DomainLayer.DeliveryComponent.DeliveryProxy import DeliveryProxy
from src.main.DomainLayer.PaymentComponent.PaymentProxy import PaymentProxy
from src.main.DomainLayer.TradeComponent.TradeControl import TradeControl
from src.main.ServiceLayer.GuestRole import GuestRole


class TradeControlService:

    def __init__(self):
        pass

    # use case 1.1
    @staticmethod
    def init_system():
        loggerStaticMethod("init_system",[])
        if not DeliveryProxy.get_instance().is_connected() and not PaymentProxy.get_instance().is_connected():
            DeliveryProxy.get_instance().connect()
            PaymentProxy.get_instance().connect()
            if GuestRole.register(GuestRole(), "TradeManager", "123456789"):
                return TradeControl.get_instance().add_sys_manager(TradeControl.get_instance().get_subscriber("TradeManager"))
        return False

    def __repr__(self):
        return repr("TradeControlService")