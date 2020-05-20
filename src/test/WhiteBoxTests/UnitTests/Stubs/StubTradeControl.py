from Backend.src.main.DomainLayer.TradeComponent.TradeControl import TradeControl
from src.test.WhiteBoxTests.UnitTests.Stubs.StubStore import StubStore
from src.main.DomainLayer.PaymentComponent.PaymentProxy import date_time


class StubTradeControl(TradeControl):
    def __init__(self):
        super().__init__()

    def get_instance(self):
        return self

    def get_stores(self):
        return [StubStore]

    def make_payment(self, username, amount, credit, date) -> bool:
        if type(date) != date_time:
            return False

        if len(username) == 0 or len(credit) == 0 or (date_time.today().date() > date) or amount <= 0:
            return False
        else:
            return True


