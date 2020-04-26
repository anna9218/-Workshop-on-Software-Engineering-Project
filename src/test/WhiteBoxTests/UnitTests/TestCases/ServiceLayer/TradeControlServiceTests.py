import unittest

from src.Logger import logger
from src.main.ServiceLayer.TradeControlService import TradeControlService
from src.test.WhiteBoxTests.UnitTests.Stubs.StubDelivery import StubDelivery


class TradeControlServiceTests(unittest.TestCase):
    @logger
    def setUp(self):
        self.__trade = TradeControlService()

    @logger
    def test_init_system(self):
        self.assertTrue(self.__trade.init_system())

    def tearDown(self):
        pass

    def __repr__(self):
        return repr("TradeControlServiceTests")

    if __name__ == '__main__':
        unittest.main()
