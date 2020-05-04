import unittest

from src.Logger import logger
from src.main.DomainLayer.StoreComponent.Purchase import Purchase
from src.main.ServiceLayer.GuestRole import TradeControl, User, Store
from src.main.ServiceLayer.SystemManagerRole import SystemManagerRole


class SystemManagerRoleTests(unittest.TestCase):
    # @logger
    def setUp(self):
        self.__system_manager_role = SystemManagerRole()

        self.__manager = User()
        self.__manager.register("manager", "password")
        (TradeControl.get_instance()).subscribe(self.__manager)
        (TradeControl.get_instance()).add_system_manager(self.__manager)

        self.__store_owner = User()
        self.__store_owner.register("store_owner", "password")
        (TradeControl.get_instance()).subscribe(self.__store_owner)

        TradeControl.get_instance().set_curr_user(self.__store_owner)

        self.__store_owner.login("store_owner", "password")
        res = (TradeControl.get_instance()).open_store("Some Store")
        self.__store: Store = (TradeControl.get_instance()).get_store("Some Store")
        self.__store.add_products("store_owner", [{"name": "Chair", "price": 100, "category": "Furniture", "amount": 5},
                                                          {"name": "Sofa", "price": 100, "category": "Furniture", "amount": 5}])
        self.__purchase: Purchase = Purchase(777, ["some product", 1], 10, "Some Store", "manager")

        self.__store_owner.add_accepted_purchase(self.__purchase)
        self.__store.add_purchase(self.__purchase)

        TradeControl.get_instance().set_curr_user(self.__system_manager_role)

    # @logger
    def test_view_user_purchases_history(self):
        # purchases = self.__store_owner.get_accepted_purchases()

        # All valid - store_owner has a single purchase
        result = self.__system_manager_role.view_user_purchase_history("store_owner")  # BUGBUG
        self.assertTrue(result[0].get_purchase_id() == 777)
        self.assertTrue(len(result) == 1)

        # User with no purchases
        result = self.__system_manager_role.view_user_purchase_history(self.__manager.get_nickname())
        self.assertEqual(result, [])

        # Invalid username
        result = self.__system_manager_role.view_user_purchase_history("invalid_username")
        self.assertIsNone(result)

        self.assertEqual(self.__store_owner.get_accepted_purchases(), purchases)

    # @logger
    def test_view_store_purchases_history(self):
        purchases = self.__store.get_purchases("store_owner")

        # All valid
        result = self.__system_manager_role.view_store_purchases_history(self.__store.get_name())
        self.assertTrue(result[0].get_purchase_id() == 0)

        # Store with no purchases
        (TradeControl.get_instance()).open_store("Other Store")
        result = self.__system_manager_role.view_store_purchases_history("Other Store")
        self.assertEqual(len(result), 0)

        # Invalid store name
        result = self.__system_manager_role.view_store_purchases_history("invalid_username")
        self.assertIsNone(result)

        self.assertEqual(self.store_owner.get_accepted_purchases(), purchases)

    def __repr__(self):
        return repr("SystemManagerRoleTests")

    if __name__ == '__main__':
        unittest.main()
