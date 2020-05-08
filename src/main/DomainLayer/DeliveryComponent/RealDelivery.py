from src.Logger import logger
from src.main.DomainLayer.DeliveryComponent.DeliverySubject import DeliverySubject


class RealDelivery(DeliverySubject):
    # @logger
    def connect(self):
        pass

    # @logger
    def deliver_products(self, address: str, products_ls: []) -> bool:
        pass

    # @logger
    def disconnect(self):
        pass

    # @logger
    def is_connected(self) -> bool:
        pass
