import unittest
from unittest.mock import MagicMock
from src.main.DomainLayer.TradeComponent.TradeControl import TradeControl
from src.main.DomainLayer.DeliveryComponent.DeliveryProxy import DeliveryProxy
from src.main.DomainLayer.PaymentComponent.PaymentProxy import PaymentProxy
from src.main.ServiceLayer.TradeControlService import TradeControlService


class TradeControlServiceTests(unittest.TestCase):
    def setUp(self):
        self.__trade = TradeControlService()

        self.__delivery_proxy_mock = DeliveryProxy.get_instance()
        self.__delivery_proxy_mock.is_connected = MagicMock(return_value=True)
        self.__delivery_proxy_mock.connect = MagicMock(return_value=True)

        self.__payment_proxy_mock = PaymentProxy.get_instance()
        self.__payment_proxy_mock.is_connected = MagicMock(return_value=True)
        self.__payment_proxy_mock.connect = MagicMock(return_value=True)

    def test_init_system(self):
        # test pre conditions:
        self.__payment_proxy_mock.is_connected = MagicMock(return_value=False)
        res = self.__trade.init_system()  # returns False - only payment isn't connected
        self.assertFalse(res['response'])

        self.__delivery_proxy_mock.is_connected = MagicMock(return_value=False)
        res = self.__trade.init_system()  # returns False - both aren't connected
        self.assertFalse(res['response'])

        res = self.__trade.init_system()
        self.assertFalse(res['response'])  # should fail - DeliveryProxy & PaymentProxy are already connected

        # test post conditions:
        self.__delivery_proxy_mock.is_connected = MagicMock(return_value=True)
        self.__payment_proxy_mock.is_connected = MagicMock(return_value=True)
        self.__trade.init_system()
        self.assertTrue(TradeControl.get_instance().get_subscriber("TradeManager").is_registered())
        res = TradeControl.get_instance().get_subscriber("TradeManager") in TradeControl.get_instance().get_managers()
        self.assertTrue(res)
        self.assertEqual(len(TradeControl.get_instance().get_managers()), 1)

    def __repr__(self):
        return repr("TradeControlServiceTests")

    if __name__ == '__main__':
        unittest.main()
