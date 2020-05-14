import unittest
from unittest.mock import MagicMock

from Backend.src.Logger import logger
from Backend.src.main.ServiceLayer.GuestRole import TradeControl
from Backend.src.main.ServiceLayer.SystemManagerRole import SystemManagerRole


class SystemManagerRoleTests(unittest.TestCase):
    # @logger
    def setUp(self):
        self.__system_manager_role = SystemManagerRole()
        self.__trade_control_mock = TradeControl().get_instance()
        self.__viewed_user = "anna9218"
        self.__store_name = "Some Store"

    # @logger
    def test_view_user_purchases_history(self):
        self.__trade_control_mock.get_instance().view_user_purchase_history = MagicMock(return_value=True)
        res = self.__system_manager_role.view_user_purchase_history(self.__viewed_user)
        self.assertTrue(res)

        self.__trade_control_mock.get_instance().view_user_purchase_history = MagicMock(return_value=False)
        res = self.__system_manager_role.view_user_purchase_history(self.__viewed_user)
        self.assertFalse(res)

    # @logger
    def test_view_store_purchases_history(self):
        self.__trade_control_mock.get_instance().view_store_purchases_history = MagicMock(return_value=True)
        res = self.__system_manager_role.view_store_purchases_history(self.__store_name)
        self.assertTrue(res)

        self.__trade_control_mock.get_instance().view_store_purchases_history = MagicMock(return_value=False)
        res = self.__system_manager_role.view_store_purchases_history(self.__store_name)
        self.assertFalse(res)

    # @logger
    def tearDown(self):
        self.__trade_control_mock.__delete__()

    def __repr__(self):
        return repr("SystemManagerRoleTests")

    if __name__ == '__main__':
        unittest.main()
