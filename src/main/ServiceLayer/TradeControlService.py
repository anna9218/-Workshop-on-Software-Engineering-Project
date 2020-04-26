from src.Logger import loggerStaticMethod
from src.main.DomainLayer.FacadeDelivery import FacadeDelivery
from src.main.DomainLayer.FacadePayment import FacadePayment
from src.main.DomainLayer.TradeControl import TradeControl
from src.main.ServiceLayer.GuestRole import GuestRole


class TradeControlService:

    def __init__(self):
        pass

    # use case 1.1
    @staticmethod
    def init_system():
        loggerStaticMethod("init_system",[])
        if not FacadeDelivery.get_instance().is_connected() and not FacadePayment.get_instance().is_connected():
            FacadeDelivery.get_instance().connect()
            FacadePayment.get_instance().connect()
            if GuestRole.register(GuestRole(), "TradeManager", "123456789"):
                return TradeControl.get_instance().add_sys_manager(TradeControl.get_instance().get_subscriber("TradeManager"))
        return False


    def __repr__(self):
        return repr("TradeControlService")