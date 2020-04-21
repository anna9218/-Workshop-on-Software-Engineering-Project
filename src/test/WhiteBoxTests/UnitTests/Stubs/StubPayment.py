from src.main.DomainLayer.FacadePayment import FacadePayment


class StubPayment(FacadePayment):

    def __init__(self):
        self.isConnected = False

    def connect(self):
        self.isConnected = True

