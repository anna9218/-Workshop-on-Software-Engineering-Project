import unittest

from src.main.DomainLayer.Product import Product
from src.main.DomainLayer.StoreInventory import StoreInventory


class TradeControlTestCase(unittest.TestCase):
    def setUp(self):
        self.inv = StoreInventory()
        self.product1 = Product("Chair", 100, "Furniture")
        self.product2 = Product("Sofa", 100, "Furniture")
        self.product3 = Product("Guitar", 100, "Musical Instruments")

    def test_add_product(self):
        self.assertTrue(self.inv.add_product(self.product1, 5))
        self.assertEqual(self.inv.get_amount_of_product("Chair"), 5)
        self.assertTrue(self.inv.add_product(self.product1, 5))
        self.assertEqual(self.inv.get_amount_of_product("Chair"), 10)
        self.assertTrue(self.inv.add_product(self.product2, 8))
        self.assertTrue(self.inv.add_product(self.product2, 8))

    def test_get_product(self):
        self.inv.add_product(self.product1, 5)
        product = self.inv.get_product("Chair")
        self.assertNotEqual(product, None)
        self.assertEqual(product.get_name(), "Chair")
        self.assertEqual(product.get_price(), 100)
        self.assertEqual(product.get_category(), "Furniture")
        self.assertEqual(self.inv.get_product("Sofa"), None)

    def test_get_products_by(self):
        self.inv.add_product(self.product1, 4)
        self.inv.add_product(self.product2, 5)
        self.inv.add_product(self.product3, 6)
        # option 1 = search by name
        products_list = self.inv.get_products_by(1, "Chair")
        self.assertEqual(len(products_list), 1)
        self.assertEqual(products_list[0].get_name(), "Chair")
        # option 2 = search by keyword
        products_list = self.inv.get_products_by(2, "r")
        self.assertEqual(len(products_list), 2)
        self.assertEqual(products_list[0].get_name(), "Chair")
        self.assertEqual(products_list[1].get_name(), "Guitar")
        # option 3 = search by category
        products_list = self.inv.get_products_by(3, "Furniture")
        self.assertEqual(len(products_list), 2)
        self.assertEqual(products_list[0].get_name(), "Chair")
        self.assertEqual(products_list[1].get_name(), "Sofa")
        products_list = self.inv.get_products_by(3, "Musical Instruments")
        self.assertEqual(len(products_list), 1)
        self.assertEqual(products_list[0].get_name(), "Guitar")
        products_list = self.inv.get_products_by(3, "Musical Instruments bbbb")
        self.assertEqual(len(products_list), 0)

    def test_remove_product(self):
        self.inv.add_product(self.product1, 4)
        self.inv.add_product(self.product2, 4)
        self.assertTrue(self.inv.remove_product(self.product1.get_name()))
        self.assertEqual(len(self.inv.get_products_by(2, "")), 1)
        self.assertFalse(self.inv.remove_product("eden"))
        self.assertEqual(len(self.inv.get_products_by(2, "")), 1)

    def test_change_amount(self):
        self.inv.add_product(self.product1, 4)
        self.inv.add_product(self.product2, 4)
        self.assertTrue(self.inv.change_amount("Chair", 16))
        self.assertEqual(self.inv.get_amount_of_product("Chair"), 16)
        self.assertEqual(self.inv.get_amount_of_product("Sofa"), 4)

    def test_len(self):
        self.assertEqual(self.inv.len(), 0)
        self.inv.add_product(self.product1, 4)
        self.assertEqual(self.inv.len(), 1)
        self.inv.add_product(self.product2, 4)
        self.assertEqual(self.inv.len(), 2)

    def test_get_amount_of_product(self):
        self.inv.add_product(self.product1, 4)
        self.assertEqual(self.inv.get_amount_of_product("Chair"), 4)
        self.inv.add_product(self.product2, 16)
        self.assertEqual(self.inv.get_amount_of_product("Sofa"), 16)
        self.assertEqual(self.inv.get_amount_of_product("Guitar"), None)


