import unittest
from unittest.mock import Mock
from unittest.mock import MagicMock

from src.main.DataAccessLayer.ConnectionProxy.Tables import rel_path
from src.main.DomainLayer.StoreComponent.Purchase import Purchase
from src.main.ServiceLayer.SubscriberRole import SubscriberRole
from src.main.DomainLayer.TradeComponent.TradeControl import TradeControl


class SubscriberRoleTests(unittest.TestCase):
    def setUp(self):
        if not ("testing" in rel_path):
            raise ReferenceError("The Data Base is not the testing data base.\n"
                                 "\t\t\t\tPlease go to src.main.DataAccessLayer.ConnectionProxy.RealDb.rel_path\n"
                                 "\t\t\t\t and change rel_path to test_rel_path.\n"
                                 "\t\t\t\tThanks :D")
        self.__subscriber: SubscriberRole = SubscriberRole()
        self.__trade_control_mock: TradeControl = TradeControl.get_instance()
        self.name = "eden"

    def test_logout(self):
        self.__trade_control_mock.get_instance().logout_subscriber = MagicMock(return_value=True)
        result = self.__subscriber.logout(self.name)
        self.assertTrue(result)

        self.__trade_control_mock.get_instance().logout_subscriber = MagicMock(return_value=False)
        result = self.__subscriber.logout(self.name)
        self.assertFalse(result)

    def test_open_store(self):
        self.__trade_control_mock.get_instance().open_store = MagicMock(return_value=True)
        store = self.__subscriber.open_store(self.name, "self.__store_name")
        self.assertTrue(store)

        self.__trade_control_mock.get_instance().open_store = MagicMock(return_value=False)
        store = self.__subscriber.open_store(self.name, "self.__store_name")
        self.assertFalse(store)

    def test_view_personal_purchase_history(self):
        purchase: Purchase = Mock()

        self.__trade_control_mock.get_instance().view_personal_purchase_history = MagicMock(return_value=[purchase])
        history = self.__subscriber.view_personal_purchase_history(self.name, True)
        self.assertIsNotNone(history)

        self.__trade_control_mock.get_instance().view_personal_purchase_history = MagicMock(return_value=[])
        history = self.__subscriber.view_personal_purchase_history(self.name, True)
        self.assertIsNotNone(history)

        self.__trade_control_mock.get_instance().view_personal_purchase_history = MagicMock(return_value=None)
        history = self.__subscriber.view_personal_purchase_history(self.name, True)
        self.assertIsNone(history)

    def tearDown(self):
        self.__trade_control_mock.__delete__()

    def __repr__(self):
        return repr("SubscriberRoleTests")

    if __name__ == '__main__':
        unittest.main()
