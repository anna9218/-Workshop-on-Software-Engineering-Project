import unittest

from src.main.DomainLayer.Purchase import Purchase
from src.main.ServiceLayer.GuestRole import TradeControl, User, Store
from src.main.ServiceLayer.SystemManagerRole import SystemManagerRole


class SystemManagerRoleTests(unittest.TestCase):
    def setUp(self):
        self.__eytan_as_sys_manager = User()
        self.__eytan_as_sys_manager.register("eytan_as_sys_manager", "eytan's password")
        (TradeControl.get_instance()).subscribe(self.__eytan_as_sys_manager)
        (TradeControl.get_instance()).add_sys_manager(self.__eytan_as_sys_manager)

        self.__eytan_as_store_owner = User()
        self.__eytan_as_store_owner.register("eytan_as_store_owner", "eytan's password")
        (TradeControl.get_instance()).subscribe(self.__eytan_as_store_owner)
        self.__system_manager_role = SystemManagerRole(self.__eytan_as_store_owner.get_nickname())

        (TradeControl.get_instance()).open_store("eytan's store")
        self.__store: Store = (TradeControl.get_instance()).get_store("eytan's store")
        self.__store.add_product("eytan's product", 10, "eytan's category", 10)
        self.__purchase: Purchase = Purchase((TradeControl.get_instance()).get_next_purchase_id(),
                                             ["eytan's product", 1], 10, "eytan's store",
                                             self.__eytan_as_store_owner.get_nickname())
        self.__eytan_as_store_owner.add_accepted_purchase(self.__purchase)
        self.__store.add_purchase(self.__purchase)

    def test_view_user_purchases_history(self):
        # All valid
        result = self.__system_manager_role.view_user_purchase_history(self.__eytan_as_store_owner.get_nickname())
        self.assertTrue(result[0].get_purchase_id() == 0)

        # User with no purchases
        result = self.__system_manager_role.view_user_purchase_history(self.__eytan_as_sys_manager.get_nickname())
        self.assertEqual(result, [])

        # Invalid username
        result = self.__system_manager_role.view_user_purchase_history("eytan")
        self.assertIsNone(result)

    def test_view_store_purchases_history(self):
        # All valid
        result = self.__system_manager_role.view_store_purchases_history(self.__store.get_name())
        self.assertTrue(result[0].get_purchase_id() == 0)

        # Store with no purchases
        (TradeControl.get_instance()).open_store("not eytan's store")
        result = self.__system_manager_role.view_store_purchases_history("not eytan's store")
        self.assertEqual(len(result), 0)

        # Invalid store name
        result = self.__system_manager_role.view_store_purchases_history("eytan")
        self.assertIsNone(result)

    if __name__ == '__main__':
        unittest.main()
