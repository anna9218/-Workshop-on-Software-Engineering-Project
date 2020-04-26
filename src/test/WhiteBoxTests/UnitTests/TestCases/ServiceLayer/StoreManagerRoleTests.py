import unittest

from src.main.DomainLayer.ManagerPermission import ManagerPermission
from src.main.ServiceLayer.StoreManagerRole import StoreManagerRole
from src.main.ServiceLayer.StoreOwnerRole import StoreOwnerRole
from src.test.WhiteBoxTests.UnitTests.Stubs.StubUser import StubUser
from src.main.ServiceLayer.GuestRole import TradeControl, User, Store


class StoreManagerRoleTests(unittest.TestCase):
    def setUp(self):
        self.__nickname = "Tinka"
        self.__store_name = "Bones"
        self.__product_details = [("Yummy bone", 50, "Pet food", 5), ("Chewy toy", 80, "Pet toy", 10)]
        self.__product_to_remove = ["Chewy toy"]
        self.__product_name = "Chewy toy"
        self.__tinka_as_store_owner = StubUser()
        self.__tinka_as_store_owner.register(self.__nickname, "pass")
        (TradeControl.get_instance()).subscribe(self.__tinka_as_store_owner)
        self.__store_owner = StoreOwnerRole(self.__tinka_as_store_owner)

        store = TradeControl.get_instance().open_store(self.__store_name)
        if store is not None:
            self.__store: Store = store
            store.add_owner(self.__tinka_as_store_owner)
        else:
            self.__store: Store = (TradeControl.get_instance()).get_store(self.__store_name)

        self.__user = StubUser()
        self.__user.register("Anna", "cookie37")
        (TradeControl.get_instance()).subscribe(self.__user)

        self.__store_manager = StoreManagerRole(self.__user, self.__store_name)

        self.__store_owner.appoint_store_manager("Anna", self.__store_name, [ManagerPermission.EDIT_INV])

        # self.__additional_owner = StubUser()
        # self.__additional_owner.register("Mooncake", "chookity")
        # (TradeControl.get_instance()).subscribe(self.__additional_owner)
        # self.__additional_manager = StubUser()
        # self.__additional_manager.register("Gary", "cookie")
        # (TradeControl.get_instance()).subscribe(self.__additional_manager)

    def test_add_products(self):
        result = self.__store_manager.add_products(self.__store_name, self.__product_details)
        self.assertTrue(result)  # bug - need to find a way to compare 2 enums for permission

    # def test_remove_products(self):
    #     # add products (there are 2), remove 1, check amount in inventory, remove another one and check
    #     self.__store_manager.add_products(self.__store_name, self.__product_details)
    #     result = self.__store_manager.remove_products(self.__nickname, self.__store_name, ["Yummy bone"])
    #     self.assertTrue(result)
    #
    #     self.__inventory = self.__store.get_inventory()
    #     self.assertEqual(1, self.__inventory.len())
    #
    #     self.__store_manager.remove_products(self.__nickname, self.__store_name, ["Yummy bone"])
    #     self.assertEqual(0, self.__inventory.len())
    #
    # def test_edit_product(self):
    #     self.__store_manager.add_products(self.__store_name, self.__product_details)
    #     self.__store_manager

    # def test_edit_purchase_and_discount_policies(self):
    #     # TODO
    #     pass
    #
    # def test_appoint_additional_owner(self):
    #     # TODO
    #     pass
    #
    # def test_appoint_store_manager(self):
    #     # TODO
    #     pass
    #
    # def test_edit_manager_permissions(self):
    #     # TODO
    #     pass
    #
    # def test_remove_manager(self):
    #     # TODO
    #     pass
    #
    # def test_display_store_purchases(self):
    #     # TODO
    #     pass

    def tearDown(self):
        self.__store.get_inventory().set_inventory([])

    def __repr__(self):
        return repr ("StoreManagerRoleTests")

    if __name__ == '__main__':
        unittest.main()
