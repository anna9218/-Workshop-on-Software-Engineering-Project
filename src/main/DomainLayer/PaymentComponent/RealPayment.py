from src.Logger import logger
from src.main.DomainLayer.PaymentComponent.PaymentSubject import PaymentSubject


class RealPayment(PaymentSubject):
    # @logger
    def connect(self):
        pass

    # @logger
    def commit_payment(self, products_ls: {"total_price": float, "products": [dict]}) -> bool:
        pass

    # @logger
    def disconnect(self):
        pass

    # @logger
    def is_connected(self) -> bool:
        pass