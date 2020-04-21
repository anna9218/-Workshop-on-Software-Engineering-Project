import unittest

from src.main.DomainLayer.TradeControl import TradeControl
from src.test.WhiteBoxTests.UnitTests.Stubs.StubDelivery import StubDelivery
from src.test.WhiteBoxTests.UnitTests.Stubs.StubUser import StubUser
from src.test.WhiteBoxTests.UnitTests.Stubs.StubPayment import StubPayment


class TradeControlTestCase(unittest.TestCase):
    def setUp(self):
        self.tradeControl = TradeControl()
        self.tradeControl.manager = StubUser()
        self.tradeControl.delivery_system = StubDelivery()
        self.tradeControl.payment_system = StubPayment()

    def test_init_system(self):
        self.tradeControl.init_system()
        self.assertEqual(len(self.tradeControl.managers), 1)
        self.assertEqual(self.tradeControl.delivery_system.isConnected, True)
        self.assertEqual(self.tradeControl.payment_system.isConnected, True)

    def tearDown(self):
        pass
