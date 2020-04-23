import unittest

from src.main.DomainLayer.ManagerPermission import ManagerPermission
from src.main.DomainLayer.Product import Product
from src.main.DomainLayer.Store import Store


class MyTestCase(unittest.TestCase):

    def test_addProduct0(self):
        u = ManagerPermission()
        s = Store("s_name", u)
        p = {"p_name": 12}
        u.AddProducts(s, ["p_name"], [12], [10])
        print (s.get_inventory().get_amount_of_product(p))
        self.assertEqual(10, s.get_inventory().get_amount_of_product(p))
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

