import unittest

from src.main.DomainLayer.ManagerPermission import ManagerPermission
from src.main.DomainLayer.Store import Store
from src.test.WhiteBoxTests.UnitTests.Stubs.StubUser import StubUser


class StoreTests(unittest.TestCase):
    def setUp(self):
        self.store = Store("myStore")

    def test_add_products(self):
        # self.product3 = Product("Guitar", 100, "Musical Instruments")
        self.assertTrue(self.store.add_products([("Chair", 100, "Furniture", 5), ("Sofa", 100, "Furniture", 5)]))
        self.assertTrue(self.store.add_products([("Chair", 100, "Furniture", 5), ("Sofa", 100, "Furniture", 5)]))
        self.assertFalse(self.store.add_products([("Chair", -999, "Furniture", 5), ("Sofa", -999, "Furniture", 5)]))
        self.assertFalse(self.store.add_products([("Chair", 100, "Furniture", -100), ("Sofa", 100, "Furniture", -100)]))

    def test_add_product(self):
        # self.product3 = Product("Guitar", 100, "Musical Instruments")
        self.assertTrue(self.store.add_product("Chair", 100, "Furniture", 5))
        self.assertFalse(self.store.add_product("Chair", -999, "Furniture", 5))
        self.assertTrue(self.store.add_product("Sofa", 100, "Furniture", 5))
        self.assertFalse(self.store.add_product("Sofa", 100, "Furniture", -5))

    def test_remove_products(self):
        self.store.add_product("Chair", 100, "Furniture", 5)
        self.assertFalse(self.store.remove_products(["Chair", "Sofa"]))
        self.assertEqual(self.store.get_inventory().len(), 0)
        self.store.add_product("Chair", 100, "Furniture", 5)
        self.store.add_product("Sofa", 100, "Furniture", 3)
        self.assertEqual(self.store.get_inventory().len(), 2)
        self.assertTrue(self.store.remove_products(["Chair", "Sofa"]))
        self.assertEqual(self.store.get_inventory().len(), 0)

    def test_remove_product(self):
        self.assertFalse(self.store.remove_product("Chair"))
        self.store.add_product("Chair", 100, "Furniture", 5)
        self.assertEqual(self.store.get_inventory().len(), 1)
        self.assertTrue(self.store.remove_product("Chair"))
        self.assertEqual(self.store.get_inventory().len(), 0)

    def test_change_price(self):
        self.store.add_product("Chair", 100, "Furniture", 5)
        self.assertTrue(self.store.change_price("Chair", 13))
        self.assertEqual(self.store.get_product("Chair").get_price(), 13)
        self.assertTrue(self.store.change_price("Chair", 8))
        self.assertEqual(self.store.get_product("Chair").get_price(), 8)
        self.assertFalse(self.store.change_price("NNNN", 8))
        self.assertFalse(self.store.change_price("Chair", -8))
        self.assertEqual(self.store.get_product("NNNN"), None)

    def test_change_name(self):
        self.store.add_product("Chair", 100, "Furniture", 5)
        self.assertTrue(self.store.change_name("Chair", "Chair222"))
        self.assertNotEqual(self.store.get_product("Chair222"), None)
        self.assertEqual(self.store.get_product("Chair"), None)
        self.assertTrue(self.store.change_name("Chair222", "Blaaaa"))
        self.assertNotEqual(self.store.get_product("Blaaaa"), None)
        self.assertEqual(self.store.get_product("Chair222"), None)
        self.assertFalse(self.store.change_name("NNNN", "blaaa"))
        self.assertEqual(self.store.get_product("NNNN"), None)
        self.assertEqual(self.store.get_product("blaaa"), None)

    def test_change_amount(self):
        self.store.add_product("Chair", 100, "Furniture", 5)
        self.assertTrue(self.store.change_amount("Chair", 3))
        self.assertEqual(self.store.get_inventory().get_amount_of_product("Chair"), 3)
        self.assertTrue(self.store.change_amount("Chair", 8))
        self.assertFalse(self.store.change_amount("Chair", -8))
        self.assertEqual(self.store.get_inventory().get_amount_of_product("Chair"), 8)

    def test_add_owner(self):
        user = StubUser()
        user.set_password_and_nickname("eden", "password")
        self.assertTrue(self.store.add_owner(user))
        self.assertEqual(len(self.store.get_owners()), 1)

    def test_is_owner(self):
        user = StubUser()
        user.set_password_and_nickname("eden", "password")
        self.assertFalse(self.store.is_owner("eden"))
        self.store.add_owner(user)
        self.assertTrue(self.store.is_owner("eden"))

    def test_is_in_store_inventory(self):
        self.store.add_product("Eytan's Product", 100, "Eytan Category", 5)
        self.store.add_product("not Eytan's Product", 10, "Eytan Category", 2)

        # All valid one product
        amount_per_product = [["Eytan's Product", 4]]
        result = self.store.is_in_store_inventory(amount_per_product)
        self.assertTrue(result)

        # All valid two products
        amount_per_product = [["Eytan's Product", 4], ["not Eytan's Product", 1]]
        result = self.store.is_in_store_inventory(amount_per_product)
        self.assertTrue(result)

        # Exactly the same as in stock
        amount_per_product = [["Eytan's Product", 5], ["not Eytan's Product", 2]]
        result = self.store.is_in_store_inventory(amount_per_product)
        self.assertTrue(result)

        # One product not enough in stock
        amount_per_product = [["Eytan's Product", 6], ["not Eytan's Product", 1]]
        result = self.store.is_in_store_inventory(amount_per_product)
        self.assertFalse(result)

        # Two product not enough in stock
        amount_per_product = [["Eytan's Product", 6], ["not Eytan's Product", 10]]
        result = self.store.is_in_store_inventory(amount_per_product)
        self.assertFalse(result)

        # One product doesn't exist
        amount_per_product = [["Eytan's social life", 5], ["not Eytan's Product", 1]]
        result = self.store.is_in_store_inventory(amount_per_product)
        self.assertFalse(result)

        # Two product doesn't exist
        amount_per_product = [["Eytan's social life", 5], ["Liverpool primer league title", 1]]
        result = self.store.is_in_store_inventory(amount_per_product)
        self.assertFalse(result)


