from src.main.DomainLayer.FacadeDelivery import FacadeDelivery
from src.main.DomainLayer.FacadePayment import FacadePayment
from src.main.DomainLayer.TradeControl import TradeControl
from src.main.ServiceLayer.GuestRole import GuestRole


class TradeControlService:

    def __init__(self):
        pass

    # use case 1.1
    @staticmethod
    def init_system(self):
        if FacadeDelivery.connect() and FacadePayment.connect():
            if GuestRole.register("TradeManager", "123456789"):
                return TradeControl.getInstance().add_sys_manager("TradeManager")
        return False
