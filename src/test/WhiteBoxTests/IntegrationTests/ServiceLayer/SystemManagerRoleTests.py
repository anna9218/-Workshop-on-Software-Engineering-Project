import unittest

import jsonpickle

from src.main.DataAccessLayer.ConnectionProxy.Tables import rel_path
from src.main.DataAccessLayer.DataAccessFacade import DataAccessFacade
from src.main.DomainLayer.StoreComponent.Purchase import Purchase
from src.main.DomainLayer.StoreComponent.Store import Store
from src.main.DomainLayer.UserComponent.User import User
from src.main.ServiceLayer.GuestRole import TradeControl
from src.main.ServiceLayer.SystemManagerRole import SystemManagerRole


class SystemManagerRoleTests(unittest.TestCase):
    def setUp(self):
        if not ("testing" in rel_path):
            raise ReferenceError("The Data Base is not the testing data base.\n"
                                 "\t\t\t\tPlease go to src.main.DataAccessLayer.ConnectionProxy.RealDb.rel_path\n"
                                 "\t\t\t\t and change rel_path to test_rel_path.\n"
                                 "\t\t\t\tThanks :D")
        self.nickname = 'eytan'
        self.__system_manager_role = SystemManagerRole()
        (TradeControl.get_instance()).register_guest("eytan", "eytan as password")
        (TradeControl.get_instance()).login_subscriber("eytan", "eytan as password")
        self.__user: User = (TradeControl.get_instance()).get_curr_user()
        (TradeControl.get_instance()).get_managers().append(self.__user)
        (TradeControl.get_instance()).open_store(self.nickname, "eytan as store")
        self.__store: Store = (TradeControl.get_instance()).get_store("eytan as store")
        (TradeControl.get_instance()).add_products(self.nickname, self.__store.get_name(),
                                                   [{"name": "eytan",
                                                     "price": 12,
                                                     "category": "eytan as category",
                                                     "amount": 21, 'purchase_type':0}])

    def test_view_user_purchases_history(self):
        # Empty purchases
        self.assertListEqual([], self.__system_manager_role.view_user_purchase_history(self.nickname, self.__user.get_nickname(), flag_for_tests=True)['response'])

        (TradeControl.get_instance()).get_curr_user().get_purchase_history().append(Purchase(
            [{"product_name": "eytan", "product_price": 12, "amount": 1}], 12, self.__store.get_name(),
            self.__user.get_nickname()))

        # Not empty
        self.assertEqual(1, len(self.__system_manager_role.view_user_purchase_history(self.nickname, self.__user.get_nickname(), flag_for_tests=True)['response']))
        purchases_lst = [jsonpickle.decode(e).get_products() for e in
                         self.__system_manager_role.view_user_purchase_history(self.nickname, self.__user.get_nickname(), flag_for_tests=True)['response']]
        self.assertListEqual([{"product_name": "eytan", "product_price": 12, "amount": 1}], purchases_lst[0])

        (TradeControl.get_instance()).get_managers().remove(self.__user)

        # Not a manager -> return's None
        self.assertIsNone(self.__system_manager_role.view_user_purchase_history(self.nickname, self.__user.get_nickname(), flag_for_tests=True)['response'])

    def test_view_store_purchases_history(self):
        # Empty purchases
        self.assertListEqual([], self.__system_manager_role.view_store_purchases_history(self.nickname, self.__store.get_name(), flag_for_tests=True)['response'])

        (TradeControl.get_instance()).get_store(self.__store.get_name()).add_purchase \
            (Purchase([{"product_name": "eytan", "product_price": 12, "amount": 1}], 12, self.__store.get_name(),
                      self.__user.get_nickname()))

        # Not empty
        lst = self.__system_manager_role.view_store_purchases_history(self.nickname, self.__store.get_name(), flag_for_tests=True)['response']
        self.assertEqual(1, len(lst))
        purchases_lst = [jsonpickle.decode(e).get_products() for e in
                         self.__system_manager_role.view_store_purchases_history(self.nickname, self.__store.get_name(), flag_for_tests=True)['response']]
        self.assertListEqual([{"product_name": "eytan", "product_price": 12, "amount": 1}], purchases_lst[0])

        (TradeControl.get_instance()).get_managers().remove(self.__user)

        # Not a manager -> return's None
        self.assertIsNone((TradeControl.get_instance()).view_store_purchases_history(self.nickname, self.__store.get_name(), flag_for_tests=True)['response'])

    def tearDown(self):
        (DataAccessFacade.get_instance()).delete_purchases()
        # (DataAccessFacade.get_instance()).delete_discount_policies()
        (DataAccessFacade.get_instance()).delete_statistics()
        (DataAccessFacade.get_instance()).delete_store_owner_appointments()
        (DataAccessFacade.get_instance()).delete_products_in_baskets()
        (DataAccessFacade.get_instance()).delete_products()
        (DataAccessFacade.get_instance()).delete_store_manager_appointments()
        (DataAccessFacade.get_instance()).delete_stores()
        (DataAccessFacade.get_instance()).delete_users()
        (TradeControl.get_instance()).__delete__()

    def __repr__(self):
        return repr("SystemManagerRoleTests")

    if __name__ == '__main__':
        unittest.main()
