import unittest
from unittest.mock import Mock, patch, MagicMock
from Backend.src.Logger import logger
from Backend.src.main.DomainLayer.TradeComponent.TradeControl import TradeControl
from Backend.src.main.DomainLayer.DeliveryComponent.DeliveryProxy import DeliveryProxy
from Backend.src.main.DomainLayer.PaymentComponent.PaymentProxy import PaymentProxy
from Backend.src.main.ServiceLayer.TradeControlService import TradeFacadeService


class TradeControlServiceTests(unittest.TestCase):
    # @logger
    def setUp(self):
        self.__trade = TradeFacadeService()

        self.__delivery_proxy_mock = DeliveryProxy.get_instance()
        self.__delivery_proxy_mock.is_connected = MagicMock(return_value=True)
        self.__delivery_proxy_mock.connect = MagicMock(return_value=True)

        self.__payment_proxy_mock = PaymentProxy.get_instance()
        self.__payment_proxy_mock.is_connected = MagicMock(return_value=True)
        self.__payment_proxy_mock.connect = MagicMock(return_value=True)

        # self.__guest_role_mock = GuestRole()
        # self.__guest_role_mock.register = MagicMock(return_value=False)

    def test_init_system(self):
        # test pre conditions:
        res = self.__trade.init_system()  # returns False - payment and delivery already connected
        self.assertFalse(res)

        self.__payment_proxy_mock.is_connected = MagicMock(return_value=False)
        res = self.__trade.init_system()  # returns False - only payment isn't connected
        self.assertFalse(res)

        self.__delivery_proxy_mock.is_connected = MagicMock(return_value=False)
        res = self.__trade.init_system()  # returns True - both aren't connected
        self.assertTrue(res)

        res = self.__trade.init_system()
        self.assertFalse(res)  # should fail - DeliveryProxy & PaymentProxy are already connected

        # test post conditions:
        self.assertTrue(TradeControl.get_instance().get_curr_user().is_registered())
        res = TradeControl.get_instance().get_curr_user() in TradeControl.get_instance().get_managers()
        self.assertTrue(res)
        self.assertEqual(len(TradeControl.get_instance().get_managers()), 1)

    def tearDown(self):
        pass

    def __repr__(self):
        return repr("TradeControlServiceTests")

    if __name__ == '__main__':
        unittest.main()
