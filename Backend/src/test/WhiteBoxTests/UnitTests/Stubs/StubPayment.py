from Backend.src.main.DomainLayer.PaymentComponent.PaymentProxy import PaymentProxy


class StubPaymentProxy(PaymentProxy):

    def __init__(self):
        self.isConnected = False

    def connect(self):
        self.isConnected = True

