from src.main.DomainLayer.DeliveryComponent.DeliveryProxy import DeliveryProxy


class StubDeliveryProxy(DeliveryProxy):

    def __init__(self):
        self.isConnected = False

    def connect(self):
        self.isConnected = True

