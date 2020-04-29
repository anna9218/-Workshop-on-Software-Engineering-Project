import unittest

from src.main.DomainLayer.StoreComponent.Product import Product
from src.main.DomainLayer.StoreComponent.Store import Store


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self._store = Store("s_name")
        self._product = Product("p_name", 12, "c")
        # self._owner = user + appoint --> if tests the service

    def test_add_product_true(self):
        self._store.add_products("", ["p_name"])
        self.assertEqual(10, self._store.get_inventory().get_amount(self._product.get_name()))
        self._store.change_amount(self._product, 1)
        self.assertEqual(1, self._store.get_inventory().get_amount(self._product.get_name()))
        self._store.change_name(self._product, "new name")
        self.assertEqual(None, self._store.get_inventory().get_product("p_name"))
        self.assertEqual("new name", self._store.get_inventory().get_product(self._product.get_name()).get_name())
        self._store.change_price(self._product, 1)
        self.assertEqual(1, self._store.get_inventory().get_product(self._product.get_name()).get_price())
        self._store.remove_product(self._product)
        # print (self._store.get_inventory())
        self.assertEqual(0, self._store.get_inventory().len())
        self.assertEqual(True, self._store.empty_inventory())

    def manage_inventory_fail_tests (self):
        self._store.add_products("", ["p_name"])
        self.assertNotEqual(0, self._store.get_inventory().len())
        self.assertNotEqual(None, self._store.get_inventory().get_product("p_name"))
        p = Product("p", 2, "c")
        self.assertNotEqual(True, self._store.change_amount(p, 1))
        self.assertNotEqual(True, self._store.change_name(p, "new name"))
        self.assertNotEqual(True, self._store.change_price(p, 1))
        self._store.remove_product(self._product)
        self.assertNotEqual(False, self._store.empty_inventory())

    if __name__ == '__main__':
        unittest.main()