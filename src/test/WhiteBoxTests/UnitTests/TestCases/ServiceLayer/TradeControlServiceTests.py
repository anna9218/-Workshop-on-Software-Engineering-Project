import unittest

from src.Logger import logger
from src.main.DomainLayer.DeliveryComponent.DeliveryProxy import DeliveryProxy
from src.main.DomainLayer.PaymentComponent.PaymentProxy import PaymentProxy
from src.main.DomainLayer.TradeComponent.TradeControl import TradeControl
from src.main.ServiceLayer.TradeControlService import TradeControlService


class TradeControlServiceTests(unittest.TestCase):
    # @logger
    def setUp(self):
        self.__trade = TradeControlService()

    # @logger
    def test_init_system(self):
        # test pre conditions:
        self.assertFalse(DeliveryProxy.get_instance().is_connected())
        self.assertFalse(PaymentProxy.get_instance().is_connected())

        res = self.__trade.init_system()
        self.assertTrue(res)  # should succeed

        res = self.__trade.init_system()
        self.assertFalse(res)  # should fail - DeliveryProxy & PaymentProxy are already connected

        # test post conditions:
        self.assertTrue(DeliveryProxy.get_instance().is_connected())
        self.assertTrue(PaymentProxy.get_instance().is_connected())
        self.assertTrue(TradeControl.get_instance().get_curr_user().is_registered())
        res = TradeControl.get_instance().get_curr_user() in TradeControl.get_instance().get_managers()
        self.assertTrue(res)
        self.assertEqual(len(TradeControl.get_instance().get_managers()), 1)

    # TODO:
    #     def test_init_system(self):
    #         self.tradeControl.init_system() -> done
    #         self.assertEqual(len(self.tradeControl.get_managers()), 1) -> done
    #         self.assertEqual(self.tradeControl.get_delivery_system().isConnected, True) -> done
    #         self.assertEqual(self.tradeControl.get_payment_system().isConnected, True) -> done
    #         self.user = StubUser() -> ?
    #         self.user.set_password_and_nickname("nickname", "password") ----> why? (Anna)

    def tearDown(self):
        pass

    def __repr__(self):
        return repr("TradeControlServiceTests")

    if __name__ == '__main__':
        unittest.main()
