import unittest

from src.Logger import logger
from src.main.ServiceLayer.TradeControlService import TradeControlService
from src.test.WhiteBoxTests.UnitTests.Stubs.StubDelivery import StubDeliveryProxy


class TradeControlServiceTests(unittest.TestCase):
    @logger
    def setUp(self):
        self.__trade = TradeControlService()

    @logger
    def test_init_system(self):
        self.assertTrue(self.__trade.init_system())

    # TODO:
    #     def test_init_system(self):
    #         self.tradeControl.init_system()
    #         self.assertEqual(len(self.tradeControl.get_managers()), 1)
    #         self.assertEqual(self.tradeControl.get_delivery_system().isConnected, True)
    #         self.assertEqual(self.tradeControl.get_payment_system().isConnected, True)
    #         self.user = StubUser()
    #         self.user.set_password_and_nickname("nickname", "password")

    def tearDown(self):
        pass

    def __repr__(self):
        return repr("TradeControlServiceTests")

    if __name__ == '__main__':
        unittest.main()
