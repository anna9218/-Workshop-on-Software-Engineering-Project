from src.Logger import logger
from src.main.DomainLayer.DeliveryComponent.DeliverySubject import DeliverySubject


class RealPayment(DeliverySubject):
    @logger
    def connect(self):
        pass

    @logger
    def deliver_products(self, username, address) -> bool:
        pass

    @logger
    def disconnect(self):
        pass

    @logger
    def is_connected(self) -> bool:
        pass