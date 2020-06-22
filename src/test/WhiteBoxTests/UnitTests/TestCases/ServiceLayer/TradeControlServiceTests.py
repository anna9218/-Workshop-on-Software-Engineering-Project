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
        # # test pre conditions:
        # res = self.__trade.init_system()  # returns False - payment and delivery already connected
        # self.assertFalse(res['response'])
        #
        # self.__payment_proxy_mock.is_connected = MagicMock(return_value=False)
        # res = self.__trade.init_system()  # returns False - only payment isn't connected
        # self.assertFalse(res['response'])
        #
        # self.__delivery_proxy_mock.is_connected = MagicMock(return_value=False)
        # res = self.__trade.init_system()  # returns True - both aren't connected
        # self.assertTrue(res['response'])
        #
        # res = self.__trade.init_system()
        # self.assertFalse(res['response'])  # should fail - DeliveryProxy & PaymentProxy are already connected
        #
        # # test post conditions:
        # self.assertTrue(TradeControl.get_instance().get_subscriber("TradeManager").is_registered())
        # res = TradeControl.get_instance().get_subscriber("TradeManager") in TradeControl.get_instance().get_managers()
        # self.assertTrue(res)
        # self.assertEqual(len(TradeControl.get_instance().get_managers()), 1)
        pass

    def test_new_init_system(self):

        # TODO: For v3
        result = TradeControlService.init_system()
        print(result['msg'])
        self.assertTrue(result['response'])
        self.assertIsNotNone((TradeControl.get_instance()).get_subscriber("u1"))
        self.assertIsNotNone((TradeControl.get_instance()).get_subscriber("u2"))
        self.assertIsNotNone((TradeControl.get_instance()).get_subscriber("u3"))
        self.assertIsNotNone((TradeControl.get_instance()).get_subscriber("u4"))
        self.assertIsNotNone((TradeControl.get_instance()).get_subscriber("u5"))
        self.assertIsNotNone((TradeControl.get_instance()).get_subscriber("u6"))
        self.assertEqual(len((TradeControl.get_instance()).get_managers()), 1)
        self.assertIn((TradeControl.get_instance()).get_subscriber("u1"), (TradeControl.get_instance()).get_managers())
        self.assertIsNotNone((TradeControl.get_instance()).get_store("s1"))
        self.assertIsNotNone((TradeControl.get_instance()).get_store("s1").get_inventory().get_product("diapers"))
        self.assertIn((TradeControl.get_instance()).get_subscriber("u3"),
                      (TradeControl.get_instance()).get_store("s1").get_managers())
        self.assertIn((TradeControl.get_instance()).get_subscriber("u5"),
                      (TradeControl.get_instance()).get_store("s1").get_managers())
        self.assertIn((TradeControl.get_instance()).get_subscriber("u6"),
                      (TradeControl.get_instance()).get_store("s1").get_managers())

        # TODO: For v4
        # self.assertTrue(TradeControlService.init_system()['response'])
        # self.assertIsNotNone((TradeControl.get_instance()).get_subscriber("A1"))
        # self.assertIsNotNone((TradeControl.get_instance()).get_subscriber("U1"))
        # self.assertIsNotNone((TradeControl.get_instance()).get_subscriber("U2"))
        # self.assertIsNotNone((TradeControl.get_instance()).get_subscriber("U11"))
        # self.assertIsNotNone((TradeControl.get_instance()).get_subscriber("U12"))
        # self.assertIsNotNone((TradeControl.get_instance()).get_subscriber("U13"))
        # self.assertIn((TradeControl.get_instance()).get_subscriber("A1"), (TradeControl.get_instance()).get_managers())
        # self.assertIsNotNone((TradeControl.get_instance()).get_store("S2"))

    def tearDown(self):
        pass

    def __repr__(self):
        return repr("TradeControlServiceTests")

    if __name__ == '__main__':
        unittest.main()
