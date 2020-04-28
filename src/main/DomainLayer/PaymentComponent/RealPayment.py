from src.main.DomainLayer.PaymentComponent.PaymentSubject import PaymentSubject


class RealPaymeny(PaymentSubject):
    def connect(self):
        pass

    def commit_payment(self, username, amount, credit, date) -> bool:
        pass

    def disconnect(self):
        pass

    def is_connected(self) -> bool:
        pass