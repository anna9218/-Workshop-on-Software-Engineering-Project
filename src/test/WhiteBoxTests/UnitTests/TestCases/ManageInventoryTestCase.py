import unittest

from src.main.DomainLayer.ManagerPermission import ManagerPermission
from src.main.DomainLayer.Product import Product
from src.main.DomainLayer.Store import Store


class MyTestCase(unittest.TestCase):

    def test_addProduct0(self):
        u = ManagerPermission()
        s = Store("s_name", u)
        p = {"p_name": 12}
        u.add_products(s, p)
        self.assertEqual(Product("p_name", 12), s.get_inventory().get("p_name"))
    #
    # def test_addProduct1(self):
    #     self.assertEqual(True, False)
    #
    # def test_removeProduct0(self):
    #     self.assertEqual(True, False)
    #
    # def test_removeProduct1(self):
    #     self.assertEqual(True, False)
    pass

if __name__ == '__main__':
    unittest.main()