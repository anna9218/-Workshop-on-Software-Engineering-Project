import unittest

from src.main.DomainLayer.Product import Product
from src.main.DomainLayer.Store import Store


class MyTestCase(unittest.TestCase):

    def test_addProduct0(self):
        u = 1  # TODO User
        s = Store("s_name", u)
        p = Product("p_name", 12)
        # TODO u.AddProduct(s, p) -- which will call to the next line
        s.AddProduct("p_name", 12)
        self.assertEqual(s.get_inventory(), {"p_name": p})
    #
    # def test_addProduct1(self):
    #     self.assertEqual(True, False)
    #
    # def test_removeProduct0(self):
    #     self.assertEqual(True, False)
    #
    # def test_removeProduct1(self):
    #     self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
