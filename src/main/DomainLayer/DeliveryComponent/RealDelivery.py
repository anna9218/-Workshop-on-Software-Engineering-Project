from src.main.DomainLayer.DeliveryComponent.DeliverySubject import DeliverySubject


class RealPayment(DeliverySubject):
    def connect(self):
        pass

    def deliver_products(self, username, address) -> bool:
        pass

    def disconnect(self):
        pass

    def is_connected(self) -> bool:
        pass