import unittest

from src.main.ServiceLayer.TradeControlService import TradeControlService
from src.test.WhiteBoxTests.UnitTests.Stubs.StubDelivery import StubDelivery


class TradeControlServiceTests(unittest.TestCase):
    def setUp(self):
        self.__trade = TradeControlService()

    def test_init_system(self):
        self.assertTrue(self.__trade.init_system())

    def tearDown(self):
        pass

    if __name__ == '__main__':
        unittest.main()
