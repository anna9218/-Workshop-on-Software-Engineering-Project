import unittest
from unittest.mock import MagicMock
from src.main.DomainLayer.TradeComponent.TradeControl import TradeControl
from src.main.DomainLayer.DeliveryComponent.DeliveryProxy import DeliveryProxy
from src.main.DomainLayer.PaymentComponent.PaymentProxy import PaymentProxy
# from Backend.src.main.ServiceLayer.TradeControlService import
from src.main.ServiceLayer.TradeControlService import TradeControlService


class TradeControlServiceTests(unittest.TestCase):
    # @logger
    def setUp(self):
        self.__trade = TradeControlService()

        self.__delivery_proxy_mock = DeliveryProxy.get_instance()
        self.__delivery_proxy_mock.is_connected = MagicMock(return_value=True)
        self.__delivery_proxy_mock.connect = MagicMock(return_value=True)

        self.__payment_proxy_mock = PaymentProxy.get_instance()
        self.__payment_proxy_mock.is_connected = MagicMock(return_value=True)
        self.__payment_proxy_mock.connect = MagicMock(return_value=True)

        # self.__guest_role_mock = GuestRole()
        # self.__guest_role_mock.register = MagicMock(return_value=False)

    # @logger
    def test_init_system(self):
        # test pre conditions:
        res = self.__trade.init_system()  # returns False - payment and delivery already connected
        self.assertFalse(res['response'])

        self.__payment_proxy_mock.is_connected = MagicMock(return_value=False)
        res = self.__trade.init_system()  # returns False - only payment isn't connected
        self.assertFalse(res['response'])

        self.__delivery_proxy_mock.is_connected = MagicMock(return_value=False)
        res = self.__trade.init_system()  # returns True - both aren't connected
        self.assertTrue(res['response'])

        res = self.__trade.init_system()
        self.assertFalse(res['response'])  # should fail - DeliveryProxy & PaymentProxy are already connected

        # test post conditions:
        self.assertTrue(TradeControl.get_instance().get_subscriber("TradeManager").is_registered())
        res = TradeControl.get_instance().get_subscriber("TradeManager") in TradeControl.get_instance().get_managers()
        self.assertTrue(res)
        self.assertEqual(len(TradeControl.get_instance().get_managers()), 1)

    def tearDown(self):
        pass

    def __repr__(self):
        return repr("TradeControlServiceTests")

    if __name__ == '__main__':
        unittest.main()
