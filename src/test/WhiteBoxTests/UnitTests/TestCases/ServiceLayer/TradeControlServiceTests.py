import unittest
from unittest.mock import MagicMock

from src.main.DataAccessLayer.ConnectionProxy.Tables import rel_path
from src.main.DomainLayer.TradeComponent.TradeControl import TradeControl
from src.main.DomainLayer.DeliveryComponent.DeliveryProxy import DeliveryProxy
from src.main.DomainLayer.PaymentComponent.PaymentProxy import PaymentProxy
from src.main.ServiceLayer.TradeControlService import TradeControlService


class TradeControlServiceTests(unittest.TestCase):
    def setUp(self):
        if not ("testing" in rel_path):
            raise ReferenceError("The Data Base is not the testing data base.\n"
                                 "\t\t\t\tPlease go to src.main.DataAccessLayer.ConnectionProxy.RealDb.rel_path\n"
                                 "\t\t\t\t and change rel_path to test_rel_path.\n"
                                 "\t\t\t\tThanks :D")
        self.__trade = TradeControlService()

        self.__delivery_proxy_mock = DeliveryProxy.get_instance()
        self.__delivery_proxy_mock.is_connected = MagicMock(return_value=True)
        self.__delivery_proxy_mock.connect = MagicMock(return_value=True)

        self.__payment_proxy_mock = PaymentProxy.get_instance()
        self.__payment_proxy_mock.is_connected = MagicMock(return_value=True)
        self.__payment_proxy_mock.connect = MagicMock(return_value=True)

    def test_new_init_system(self):

        # TODO: For v3
        # result = TradeControlService.init_system()
        # print(result['msg'])
        # self.assertTrue(result['response'])
        # self.assertIsNotNone((TradeControl.get_instance()).get_subscriber("u1"))
        # self.assertIsNotNone((TradeControl.get_instance()).get_subscriber("u2"))
        # self.assertIsNotNone((TradeControl.get_instance()).get_subscriber("u3"))
        # self.assertIsNotNone((TradeControl.get_instance()).get_subscriber("u4"))
        # self.assertIsNotNone((TradeControl.get_instance()).get_subscriber("u5"))
        # self.assertIsNotNone((TradeControl.get_instance()).get_subscriber("u6"))
        # self.assertEqual(len((TradeControl.get_instance()).get_managers()), 1)
        # self.assertIn((TradeControl.get_instance()).get_subscriber("u1"), (TradeControl.get_instance()).get_managers())
        # self.assertIsNotNone((TradeControl.get_instance()).get_store("s1"))
        # self.assertIsNotNone((TradeControl.get_instance()).get_store("s1").get_inventory().get_product("diapers"))
        # self.assertIn((TradeControl.get_instance()).get_subscriber("u3"),
        #               (TradeControl.get_instance()).get_store("s1").get_managers())
        # self.assertIn((TradeControl.get_instance()).get_subscriber("u5"),
        #               (TradeControl.get_instance()).get_store("s1").get_managers())
        # self.assertIn((TradeControl.get_instance()).get_subscriber("u6"),
        #               (TradeControl.get_instance()).get_store("s1").get_managers())

        # TODO: For v4
        self.assertTrue(TradeControlService.init_system()['response'])
        self.assertIsNotNone((TradeControl.get_instance()).get_subscriber("A1"))
        self.assertIsNotNone((TradeControl.get_instance()).get_subscriber("U1"))
        self.assertIsNotNone((TradeControl.get_instance()).get_subscriber("U2"))
        self.assertIsNotNone((TradeControl.get_instance()).get_subscriber("U11"))
        self.assertIsNotNone((TradeControl.get_instance()).get_subscriber("U12"))
        self.assertIsNotNone((TradeControl.get_instance()).get_subscriber("U13"))
        self.assertIn((TradeControl.get_instance()).get_subscriber("A1"), (TradeControl.get_instance()).get_managers())
        self.assertIsNotNone((TradeControl.get_instance()).get_store("S2"))

    def tearDown(self):
        pass

    def __repr__(self):
        return repr("TradeControlServiceTests")

    if __name__ == '__main__':
        unittest.main()
