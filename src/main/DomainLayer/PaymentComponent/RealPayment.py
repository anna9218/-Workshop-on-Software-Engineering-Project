from src.Logger import logger
from src.main.DomainLayer.PaymentComponent.PaymentSubject import PaymentSubject


class RealPaymeny(PaymentSubject):
    @logger
    def connect(self):
        pass

    @logger
    def commit_payment(self, username, amount, credit, date) -> bool:
        pass

    @logger
    def disconnect(self):
        pass

    @logger
    def is_connected(self) -> bool:
        pass