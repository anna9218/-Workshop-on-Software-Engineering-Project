from src.main.DomainLayer.DeliveryComponent.DeliveryProxy import DeliveryProxy


class StubDeliveryProxy(DeliveryProxy):
    __instance = None
    __realSubject = None

    def __init__(self):
        self.isConnected = False

    def connect(self):
        self.isConnected = True

    def is_connect(self):
        self.isConnected = True

    @staticmethod
    def get_instance():

        if DeliveryProxy.__instance is None:
            DeliveryProxy()
        return DeliveryProxy.__instance

