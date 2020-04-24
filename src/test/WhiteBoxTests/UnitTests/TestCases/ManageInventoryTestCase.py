import unittest

from src.main.DomainLayer.ManagerPermission import ManagerPermission
from src.main.DomainLayer.Product import Product
from src.main.DomainLayer.Store import Store


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self._store = Store("s_name")
        self._product = Product("p_name", 12, "c")
        # self._owner = user + appoint --> if tests the service

    def test_add_product_true(self):

        self._store.add_products(["p_name"], [12], [10], ["c"])
        self.assertEqual(10, self._store.get_inventory().get_amount_of_product(self._product.get_name()))
        self._store.change_amount(self._product, 1)
        self.assertEqual(1, self._store.get_inventory().get_amount_of_product(self._product.get_name()))
        self._store.remove_product(self._product)
        # print (self._store.get_inventory())
        self.assertEqual(0, self._store.get_inventory().len())
        self.assertEqual(True, self._store.empty_inventory())

    pass

if __name__ == '__main__':
    unittest.main()