import unittest
from unittest.mock import MagicMock

from src.main.DataAccessLayer.ConnectionProxy.Tables import rel_path
from src.main.ServiceLayer.GuestRole import TradeControl
from src.main.ServiceLayer.SystemManagerRole import SystemManagerRole


class SystemManagerRoleTests(unittest.TestCase):
    def setUp(self):
        if not ("testing" in rel_path):
            raise ReferenceError("The Data Base is not the testing data base.\n"
                                 "\t\t\t\tPlease go to src.main.DataAccessLayer.ConnectionProxy.RealDb.rel_path\n"
                                 "\t\t\t\t and change rel_path to test_rel_path.\n"
                                 "\t\t\t\tThanks :D")
        self.__system_manager_role = SystemManagerRole()
        self.__trade_control_mock = TradeControl().get_instance()
        self.__viewed_user = "anna9218"
        self.__store_name = "Some Store"
        self.__sys_manager_name = "eden"

    def test_view_user_purchases_history(self):
        self.__trade_control_mock.get_instance().view_user_purchase_history = MagicMock(return_value=[])
        res = self.__system_manager_role.view_user_purchase_history(self.__sys_manager_name, self.__viewed_user)
        self.assertListEqual(res, [])

        self.__trade_control_mock.get_instance().view_user_purchase_history = \
            MagicMock(return_value=[{"product_name": "Eytan's product",
                                     "store_name": "Eytan's store",
                                     "amount": 1}])
        res = self.__system_manager_role.view_user_purchase_history(self.__sys_manager_name, self.__viewed_user)
        res_as_tuples = [(result['product_name'], result['store_name'], result['amount']) for result in res]
        self.assertListEqual(res_as_tuples, [("Eytan's product", "Eytan's store", 1)])

    def test_view_store_purchases_history(self):
        self.__trade_control_mock.get_instance().view_store_purchases_history = MagicMock(return_value=[])
        res = self.__system_manager_role.view_store_purchases_history(self.__sys_manager_name, self.__store_name)
        self.assertListEqual(res, [])

        self.__trade_control_mock.get_instance().view_store_purchases_history = \
            MagicMock(return_value=[{"product_name": "Eytan's product",
                                     "store_name": "Eytan's store",
                                     "amount": 1}])
        res = self.__system_manager_role.view_store_purchases_history(self.__sys_manager_name, self.__store_name)
        res_as_tuples = [(result['product_name'], result['store_name'], result['amount']) for result in res]
        self.assertListEqual(res_as_tuples, [("Eytan's product", "Eytan's store", 1)])

    def tearDown(self):
        self.__trade_control_mock.__delete__()

    def __repr__(self):
        return repr("SystemManagerRoleTests")

    if __name__ == '__main__':
        unittest.main()
