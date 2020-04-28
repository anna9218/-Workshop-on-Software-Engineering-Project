import unittest

from src.Logger import logger
from src.main.DomainLayer.StoreComponent.ManagerPermission import ManagerPermission
from src.main.ServiceLayer.StoreManagerRole import StoreManagerOrManagerRole
from src.main.ServiceLayer.StoreOwnerOrManagerRole import StoreOwnerOrManagerRole
from src.test.WhiteBoxTests.UnitTests.Stubs.StubUser import StubUser
from src.main.ServiceLayer.GuestRole import TradeControl, User, Store


class StoreManagerRoleTests(unittest.TestCase):
    @logger
    def setUp(self):
        self.__nickname = "Tinka"
        self.__store_name = "Bones"
        self.__product_details = [("Yummy bone", 50, "Pet food", 5), ("Chewy toy", 80, "Pet toy", 10)]
        self.__product_to_remove = ["Chewy toy"]
        self.__product_name = "Chewy toy"
        self.__tinka_as_store_owner = StubUser()
        self.__tinka_as_store_owner.register(self.__nickname, "pass")
        (TradeControl.get_instance()).subscribe(self.__tinka_as_store_owner)
        self.__store_owner = StoreOwnerOrManagerRole(self.__tinka_as_store_owner)

        store = TradeControl.get_instance().open_store(self.__store_name)
        if store is not None:
            self.__store: Store = store
            store.add_owner("", self.__tinka_as_store_owner)
        else:
            self.__store: Store = (TradeControl.get_instance()).get_store(self.__store_name)

        self.__user = StubUser()
        self.__user.register("Anna", "cookie37")
        (TradeControl.get_instance()).subscribe(self.__user)

        self.__store_manager = StoreManagerOrManagerRole(self.__user, self.__store_name)

        self.__store_owner.appoint_store_manager(self.__store_name, [n for n in ManagerPermission], )

        (TradeControl.get_instance()).get_subscribers().insert(0, self.__user)

        self.__additional_manager = StubUser()
        self.__additional_manager.register("Gary", "cookie")
        (TradeControl.get_instance()).subscribe(self.__additional_manager)
        self.__store_manager.appoint_store_manager(self.__store_name, [n for n in ManagerPermission], )

    @logger
    def test_add_products(self):
        result = self.__store_manager.add_products(self.__product_details, )
        self.assertTrue(result)  # bug - need to find a way to compare 2 enums for permission


    @logger
    def test_remove_products(self):
        # add products (there are 2), remove 1, check amount in inventory, remove another one and check
        self.__store_manager.add_products(self.__product_details, )
        result = self.__store_manager.remove_products(self.__store_name, ["Yummy bone"])
        self.assertTrue(result)

        self.__inventory = self.__store.get_inventory()
        self.assertEqual(1, self.__inventory.len())

        result = self.__store_manager.remove_products(self.__store_name, ["Chewy toy"])
        self.assertTrue(result)
        self.assertEqual(0, self.__inventory.len())

        result = self.__store_manager.remove_products(self.__store_name, ["Chewy toy"])
        self.assertFalse(result)

    @logger
    def test_edit_product(self):
        self.__store_manager.add_products(self.__product_details, )
        result = self.__store_manager.edit_product(self.__store_name, self.__product_name, "name", "Rainbow Chair")

        self.assertTrue(result)

        self.__inventory = self.__store.get_inventory()
        for record in self.__inventory:
            if record[0].get_name() == "Rainbow Chair":
                self.assertEqual(record[0].get_price(), 80)
                self.assertEqual(record[0].get_category(), "Pet toy")
                self.assertEqual(record[1], 10)

    def test_appoint_store_manager(self):
        eytan: User = User()
        eytan.register("eytan", "eytan's password")
        TradeControl.get_instance().get_subscribers().insert(0, eytan)

        # All Valid.
        result = self.__store_manager.appoint_store_manager(self.__store_name,
                                                            [ManagerPermission.WATCH_PURCHASE_HISTORY], )
        # self.assertTrue(result)

        # store_name unValid.
        result = self.__store_manager.appoint_store_manager("self.__store_name",
                                                            [ManagerPermission.WATCH_PURCHASE_HISTORY], )
        self.assertFalse(result)

        # username unValid.
        result = self.__store_manager.appoint_store_manager(self.__store_name,
                                                            [ManagerPermission.WATCH_PURCHASE_HISTORY], )
        self.assertFalse(result)

    def test_edit_manager_permissions(self):
        result = self.__store_manager.edit_manager_permissions("Gary", [], )
        #self.assertTrue(result)

        result = self.__store_manager.edit_manager_permissions("Mooncake", [], )
        self.assertFalse(result)

    def test_remove_manager(self):
        self.__store_owner.appoint_store_manager(self.__store_name, [9, 10], )

        result = self.__store_manager.remove_manager(str, str)
        #self.assertTrue(result)

        result = self.__store_manager.remove_manager(str, str)
        self.assertFalse(result)

    def test_display_store_purchases(self):
        result = self.__store_manager.display_store_purchases(self.__store_name)
        self.assertEqual([], result)  # currently empty

    def tearDown(self):
        self.__store.get_inventory().set_inventory([])

    def __repr__(self):
        return repr ("StoreManagerRoleTests")

    if __name__ == '__main__':
        unittest.main()
