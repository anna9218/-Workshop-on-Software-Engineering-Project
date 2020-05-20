import unittest
from unittest.mock import MagicMock

import jsonpickle

from Backend.src.Logger import logger
from Backend.src.main.DomainLayer.StoreComponent.Purchase import Purchase
from Backend.src.main.DomainLayer.StoreComponent.Store import Store
from Backend.src.main.DomainLayer.UserComponent.User import User
from Backend.src.main.ServiceLayer.GuestRole import TradeControl
from Backend.src.main.ServiceLayer.SystemManagerRole import SystemManagerRole


class SystemManagerRoleTests(unittest.TestCase):
    @logger
    def setUp(self):
        self.__system_manager_role = SystemManagerRole()
        (TradeControl.get_instance()).register_guest("eytan", "eytan as password")
        (TradeControl.get_instance()).login_subscriber("eytan", "eytan as password")
        self.__user: User = (TradeControl.get_instance()).get_curr_user()
        (TradeControl.get_instance()).get_managers().append(self.__user)
        (TradeControl.get_instance()).open_store("eytan as store")
        self.__store: Store = (TradeControl.get_instance()).get_store("eytan as store")
        (TradeControl.get_instance()).add_products(self.__store.get_name(),
                                                   [{"name": "eytan",
                                                     "price": 12,
                                                     "category": "eytan as category",
                                                     "amount": 21}])

    @logger
    def test_view_user_purchases_history(self):
        # Empty purchases
        self.assertListEqual([], self.__system_manager_role.view_user_purchase_history(self.__user.get_nickname()))

        (TradeControl.get_instance()).get_curr_user().get_purchase_history().append(Purchase(
            [{"product_name": "eytan", "product_price": 12, "amount": 1}], 12, self.__store.get_name(),
            self.__user.get_nickname()))

        # Not empty
        self.assertEqual(1, len(self.__system_manager_role.view_user_purchase_history(self.__user.get_nickname())))
        purchases_lst = [jsonpickle.decode(e).get_products() for e in
                         self.__system_manager_role.view_user_purchase_history(self.__user.get_nickname())]
        self.assertListEqual([{"product_name": "eytan", "product_price": 12, "amount": 1}], purchases_lst[0])

        (TradeControl.get_instance()).get_managers().remove(self.__user)

        # Not a manager -> return's None
        self.assertIsNone(self.__system_manager_role.view_user_purchase_history(self.__user.get_nickname()))

    @logger
    def test_view_store_purchases_history(self):
        # Empty purchases
        self.assertListEqual([], self.__system_manager_role.view_store_purchases_history(self.__store.get_name()))

        (TradeControl.get_instance()).get_store(self.__store.get_name()).add_purchase \
            (Purchase([{"product_name": "eytan", "product_price": 12, "amount": 1}], 12, self.__store.get_name(),
                      self.__user.get_nickname()))

        # Not empty
        lst = self.__system_manager_role.view_store_purchases_history(self.__store.get_name())
        self.assertEqual(1, len(lst))
        purchases_lst = [jsonpickle.decode(e).get_products() for e in
                         self.__system_manager_role.view_store_purchases_history(self.__store.get_name())]
        self.assertListEqual([{"product_name": "eytan", "product_price": 12, "amount": 1}], purchases_lst[0])

        (TradeControl.get_instance()).get_managers().remove(self.__user)

        # Not a manager -> return's None
        self.assertIsNone((TradeControl.get_instance()).view_store_purchases_history(self.__store.get_name()))

    @logger
    def tearDown(self):
        (TradeControl.get_instance()).__delete__()

    def __repr__(self):
        return repr("SystemManagerRoleTests")

    if __name__ == '__main__':
        unittest.main()
