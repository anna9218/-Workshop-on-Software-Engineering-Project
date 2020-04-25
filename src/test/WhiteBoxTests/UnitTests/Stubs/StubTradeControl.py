from src.main.DomainLayer.TradeControl import TradeControl
from src.test.WhiteBoxTests.UnitTests.Stubs.StubStore import StubStore


class StubTradeControl(TradeControl):
    def __init__(self):
        super().__init__()

    def get_instance(self):
        return self

    def get_stores(self):
        return [StubStore]

