from src.main.DomainLayer.FacadeDelivery import FacadeDelivery


class StubDelivery(FacadeDelivery):

    def __init__(self):
        self.isConnected = False

    def connect(self):
        self.isConnected = True

