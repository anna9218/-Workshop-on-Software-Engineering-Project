import unittest

from src.main.DomainLayer.TradeControl import TradeControl
from src.test.WhiteBoxTests.UnitTests.Stubs.StubDelivery import StubDelivery
from src.test.WhiteBoxTests.UnitTests.Stubs.StubUser import StubUser
from src.test.WhiteBoxTests.UnitTests.Stubs.StubPayment import StubPayment


class TradeControlTestCase(unittest.TestCase):
    def setUp(self):
        self.tradeControl = TradeControl.getInstance()
        self.tradeControl.manager = StubUser(self.tradeControl)
        self.tradeControl.delivery_system = StubDelivery()
        self.tradeControl.payment_system = StubPayment()

    def test_init_system(self):
        self.tradeControl.init_system()
        self.assertEqual(len(self.tradeControl.get_managers()), 1)
        self.assertEqual(self.tradeControl.get_delivery_system().isConnected, True)
        self.assertEqual(self.tradeControl.get_payment_system().isConnected, True)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
