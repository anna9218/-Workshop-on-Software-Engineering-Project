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
        if FacadeDelivery.get_instance().is_conneced() and FacadePayment.get_instance().is_connected() or\
                FacadeDelivery.get_instance().connect() and FacadePayment.get_instance().connect():
            if GuestRole.register("TradeManager", "123456789"):
                return TradeControl.get_instance().add_sys_manager(TradeControl.get_instance().get_subscriber("TradeManager"))
        return False

