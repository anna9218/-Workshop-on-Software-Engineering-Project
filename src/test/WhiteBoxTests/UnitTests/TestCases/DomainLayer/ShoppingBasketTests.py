import unittest

from src.main.DomainLayer.ShoppingBasket import ShoppingBasket
from src.test.WhiteBoxTests.UnitTests.Stubs.StubProduct import StubProduct


class ShoppingBasketTests(unittest.TestCase):
    def setUp(self):
        self.__basket = ShoppingBasket()
        self.__product = StubProduct()

    def test_add_product(self):
        self.assertTrue(self.__basket.add_product([self.__product, 2]))
        self.assertIn([self.__product, 2], self.__basket)

    def test_remove_product(self):
        self.__basket.add_product([self.__product, 2])
        self.assertTrue(self.__basket.remove_product(self.__product))
        self.assertFalse(self.__basket.get_products())
        self.assertNotIn([self.__product, 2], self.__basket)

    def tearDown(self):
        pass

    if __name__ == '__main__':
        unittest.main()
