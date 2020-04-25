from src.main.DomainLayer.Store import Store


class StubStore(Store):

    def __init__(self, name):
        super().__init__(name)

