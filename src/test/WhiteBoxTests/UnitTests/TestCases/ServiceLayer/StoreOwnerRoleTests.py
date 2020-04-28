import unittest

from src.Logger import logger
from src.main.DomainLayer.Product import Product
from src.main.DomainLayer.Purchase import Purchase
from src.main.ServiceLayer.GuestRole import TradeControl, User, Store
from src.main.ServiceLayer.StoreOwnerRole import StoreOwnerRole
from src.main.ServiceLayer.SystemManagerRole import SystemManagerRole
from src.main.DomainLayer.User import User
from src.test.WhiteBoxTests.UnitTests.Stubs.StubUser import StubUser


class StoreOwnerRoleTests(unittest.TestCase):
    @logger
    def setUp(self):
        self.__nickname = "anna_anna"
        self.__store_name = "Bambook"
        self.__product_details = [("Chair", 100, "Furniture", 5), ("Sofa", 100, "Furniture", 5)]
        self.__product_to_remove = ["Chair"]
        self.__product_name = "Chair"
        self.__anna_as_store_owner = StubUser()
        self.__anna_as_store_owner.register(self.__nickname, "pass")
        (TradeControl.get_instance()).subscribe(self.__anna_as_store_owner)
        self.__store_owner = StoreOwnerRole(self.__anna_as_store_owner)

        self.__additional_owner = StubUser()
        self.__additional_owner.register("Mooncake", "chookity")
        (TradeControl.get_instance()).subscribe(self.__additional_owner)

        self.__additional_manager = StubUser()
        self.__additional_manager.register("Gary", "cookie")
        (TradeControl.get_instance()).subscribe(self.__additional_manager)

        store = TradeControl.get_instance().open_store(self.__store_name)
        if store is not None:
            self.__store: Store = store
            store.add_owner("", self.__anna_as_store_owner)
        else:
            self.__store: Store = (TradeControl.get_instance()).get_store(self.__store_name)

    @logger
    def test_add_products(self):
        # product_details = (product_name, product_price, product_amounts, product_category)
        result = self.__store_owner.add_products(self.__store_name, self.__product_details)
        self.assertTrue(result)

        self.__inventory = self.__store.get_inventory().get_inventory()
        for product_record in self.__product_details:
            inventory_record = (Product(product_record[0], product_record[1], product_record[2]), product_record[3])
            for record in self.__inventory:
                if record[0].get_name() == product_record[0]:
                    self.assertEqual(record[0].get_price(), product_record[1])
                    self.assertEqual(record[0].get_category(), product_record[2])
                    self.assertEqual(record[1], product_record[3])

    @logger
    def test_remove_products(self):
        self.__store_owner.add_products(self.__store_name, self.__product_details)
        result = self.__store_owner.remove_products(self.__store_name, self.__product_to_remove)
        self.assertTrue(result)

        self.__inventory = self.__store.get_inventory()
        self.assertEqual(1, self.__inventory.len())

        self.__store_owner.remove_products(self.__store_name, ["Sofa"])
        self.assertEqual(0, self.__inventory.len())

    @logger
    def test_edit_product(self):
        self.__store_owner.add_products(self.__store_name, self.__product_details)
        result = self.__store_owner.edit_product(self.__store_name, self.__product_name, "name", "Rainbow Chair")
        self.assertTrue(result)

        self.__inventory = self.__store.get_inventory()
        for record in self.__inventory:
            if record[0].get_name() == "Rainbow Chair":
                self.assertEqual(record[0].get_price(), 100)
                self.assertEqual(record[0].get_category(), "Furniture")
                self.assertEqual(record[1], 5)

    # def test_edit_purchase_and_discount_policies(self):
    #     pass

    @logger
    def test_appoint_additional_owner(self):
        result = self.__store_owner.appoint_additional_owner(self.__store_name, )
        self.assertTrue(result)

        result = self.__store_owner.appoint_additional_owner(self.__store_name, )
        self.assertFalse(result)

    @logger
    def test_appoint_store_manager(self):
        result = self.__store_owner.appoint_store_manager(self.__store_name, [9, 10], )
        self.assertTrue(result)

        result = self.__store_owner.appoint_additional_owner(self.__store_name, )
        self.assertFalse(result)

    @logger
    def test_edit_manager_permissions(self):
        result = self.__store_owner.edit_manager_permissions("Gary", [], )
        self.assertTrue(result)

        result = self.__store_owner.edit_manager_permissions("Mooncake", [], )
        self.assertFalse(result)

    @logger
    def test_remove_manager(self):
        self.__store_owner.appoint_store_manager(self.__store_name, [9, 10], )
        result = self.__store_owner.remove_manager(str, str)
        self.assertTrue(result)

        result = self.__store_owner.remove_manager(str, str)
        self.assertFalse(result)

    @logger
    def test_display_store_purchases(self):
        result = self.__store_owner.display_store_purchases(self.__store_name)
        self.assertEqual([], result)  # currently empty

    @logger
    def tearDown(self):
        self.__store.get_inventory().set_inventory([])

    def __repr__(self):
        return repr ("StoreOwnerRoleTests")

    if __name__ == '__main__':
        unittest.main()
