import unittest

from src.main.DomainLayer.StoreComponent.Product import Product
from src.main.DomainLayer.StoreComponent.StoreInventory import StoreInventory


class StoreInventoryTests(unittest.TestCase):
    def setUp(self):
        self.inv = StoreInventory()
        self.product1 = Product("Chair", 100, "Furniture")
        self.product1.set_purchase_type(0)
        self.product2 = Product("Sofa", 10, "Furniture")
        self.product2.set_purchase_type(0)
        self.product3 = Product("Guitar", 1000, "Musical Instruments")
        self.product3.set_purchase_type(0)

    def test_add_product(self):
        # All valid - None existing product
        self.assertTrue(self.inv.add_product(self.product1, 5))
        self.assertEqual(self.inv.get_amount("Chair"), 5)

        # All valid - Existing product
        self.assertTrue(self.inv.add_product(self.product1, 5))
        self.assertEqual(self.inv.get_amount("Chair"), 10)

        # Invalid - Illegal amount
        self.assertFalse(self.inv.add_product(self.product2, -8))

    def test_get_product(self):
        self.inv.add_product(self.product1, 5)

        # All valid
        product = self.inv.get_product("Chair")
        self.assertIsNotNone(product)
        self.assertEqual(product.get_name(), "Chair")
        self.assertEqual(product.get_price(), 100)
        self.assertEqual(product.get_category(), "Furniture")

        # Invalid -> none existing product
        self.assertIsNone(self.inv.get_product("Sofa"))

    def test_get_products_by(self):
        self.inv.add_product(self.product1, 4)
        self.inv.add_product(self.product2, 5)
        self.inv.add_product(self.product3, 6)

        # option 1 = search by name

        # All valid
        products_list = self.inv.get_products_by(1, "Chair")
        self.assertEqual(len(products_list), 1)
        self.assertTrue(self.product1 in products_list)

        # Invalid -> none existing product
        products_list = self.inv.get_products_by(1, "Eytan")
        self.assertEqual(len(products_list), 0)

        # option 2 = search by keyword
        products_list = self.inv.get_products_by(2, "r")
        self.assertEqual(len(products_list), 2)
        self.assertTrue(self.product1 in products_list)
        self.assertTrue(self.product3 in products_list)

        # Invalid -> none existing keyword
        products_list = self.inv.get_products_by(2, "Eytan")
        self.assertEqual(len(products_list), 0)

        # option 3 = search by category
        products_list = self.inv.get_products_by(3, "Furniture")
        self.assertEqual(len(products_list), 2)
        self.assertTrue(self.product1 in products_list)
        self.assertTrue(self.product2 in products_list)

        products_list = self.inv.get_products_by(3, "Musical Instruments")
        self.assertEqual(len(products_list), 1)
        self.assertTrue(self.product3 in products_list)

        # Invalid -> none existing category
        products_list = self.inv.get_products_by(3, "Eytan")
        self.assertEqual(len(products_list), 0)

    # @logger
    def test_remove_product(self):
        self.inv.add_product(self.product1, 4)
        self.inv.add_product(self.product2, 2)

        # All valid
        self.assertTrue(self.inv.remove_product(self.product1.get_name()))
        self.assertEqual(len(self.inv.get_products_by(2, "")), 1)
        self.assertTrue(self.product2 in self.inv.get_products_by(2, ""))

        # Invalid -> None existing product
        self.assertFalse(self.inv.remove_product("eden"))
        self.assertEqual(len(self.inv.get_products_by(2, "")), 1)

    def test_change_amount(self):
        self.inv.add_product(self.product1, 4)
        self.inv.add_product(self.product2, 2)

        # All valid
        self.assertTrue(self.inv.change_amount("Chair", 16))
        self.assertEqual(self.inv.get_amount("Sofa"), 2)

        #  All valid -> 0 amount
        self.assertTrue(self.inv.change_amount("Chair", 0))
        self.assertEqual(self.inv.get_amount("Chair"), 0)
        self.assertEqual(self.inv.get_amount("Sofa"), 2)

        # Invalid -> negative amount
        self.assertFalse(self.inv.change_amount("Chair", -16))
        self.assertEqual(self.inv.get_amount("Chair"), 0)
        self.assertEqual(self.inv.get_amount("Sofa"), 2)

        # Invalid -> none existing product name
        self.assertFalse(self.inv.change_amount("Eytan", 12))
        self.assertEqual(self.inv.get_amount("Chair"), 0)
        self.assertEqual(self.inv.get_amount("Sofa"), 2)

        product_names = [p.get_name() for p in self.inv.get_products_by(2, "")]
        self.assertFalse("Eytan" in product_names)

    # @logger
    def test_len(self):

        # All valid -> Empty inventory
        self.assertEqual(self.inv.len(), 0)

        self.inv.add_product(self.product1, 4)

        # All valid -> Not empty inventory  -> one product.
        self.assertEqual(self.inv.len(), 1)

        self.inv.add_product(self.product2, 4)

        # All valid -> Not empty inventory  -> more then one product.
        self.assertEqual(self.inv.len(), 2)

        # All valid -> Check that the inventory doesn't change while adding an invalid product.
        try:
            self.inv.add_product(Product("Eytan", -100, "Different Eytan"), 12)
        except ValueError:
            ""
        self.assertEqual(self.inv.len(), 2)

        self.inv.add_product(Product("Eytan", 100, "Different Eytan"), -12)
        self.assertEqual(self.inv.len(), 2)

    # @logger
    def test_get_amount_of_product(self):
        # All valid -> none existing product
        self.assertEqual(self.inv.get_amount("Chair"), 0)

        self.inv.add_product(self.product1, 4)

        # All valid -> amount > 0
        self.assertEqual(self.inv.get_amount("Chair"), 4)

        self.inv.change_amount(self.product1.get_name(), 0)

        # All valid -> amount = 0
        self.assertEqual(self.inv.get_amount("Chair"), 0)

    # @logger
    def test_is_in_stock(self):
        self.inv.add_product(self.product1, 10)

        # All valid
        result = self.inv.is_in_stock(self.product1.get_name(), 9)
        self.assertTrue(result)

        # All valid - Edge case
        result = self.inv.is_in_stock(self.product1.get_name(), 10)
        self.assertTrue(result)

        # All valid - Edge case 2
        result = self.inv.is_in_stock(self.product1.get_name(), 0)
        self.assertTrue(result)

        # product name not valid
        result = self.inv.is_in_stock("self.product1", 10)
        self.assertFalse(result)

        # amount not valid
        result = self.inv.is_in_stock(self.product1.get_name(), -10)
        self.assertFalse(result)

    def __repr__(self):
        return repr("StoreInventoryTests")