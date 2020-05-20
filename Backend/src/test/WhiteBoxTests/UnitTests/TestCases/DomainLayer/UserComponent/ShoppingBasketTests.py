import unittest

from Backend.src.Logger import logger
from Backend.src.main.DomainLayer.UserComponent.DiscountType import DiscountType
from Backend.src.main.DomainLayer.UserComponent.PurchaseType import PurchaseType
from Backend.src.main.DomainLayer.UserComponent.ShoppingBasket import ShoppingBasket
from Backend.src.test.WhiteBoxTests.UnitTests.Stubs.StubProduct import StubProduct


class ShoppingBasketTests(unittest.TestCase):
    # @logger
    def setUp(self):
        self.__basket = ShoppingBasket()
        self.__product = StubProduct()

    # @logger
    # eden
    def test_update_amount(self):
        self.__basket.add_product(self.__product, 2, DiscountType.DEFAULT, PurchaseType.DEFAULT)
        self.assertEqual(self.__basket.get_product_amount("Alcogel"), 2)
        self.__basket.update_amount(self.__product.get_name(), 5)
        self.assertEqual(self.__basket.get_product_amount("Alcogel"), 5)
        self.__basket.update_amount(self.__product.get_name(), 1)
        self.assertEqual(self.__basket.get_product_amount("Alcogel"), 1)

    # @logger
    def test_is_empty(self):
        self.assertTrue(self.__basket.is_empty())
        self.__basket.add_product(self.__product, 2, DiscountType.DEFAULT, PurchaseType.DEFAULT)
        self.assertFalse(self.__basket.is_empty())

    # @logger
    def test_add_product(self):
        self.assertTrue(self.__basket.add_product(self.__product, 2, DiscountType.DEFAULT, PurchaseType.DEFAULT))
        self.assertIn({"product": self.__product, "amount": 2, "discountType": DiscountType.DEFAULT,
                       "purchaseType": PurchaseType.DEFAULT}, self.__basket)

    # @logger
    def test_remove_product(self):
        self.__basket.add_product(self.__product, 2, DiscountType.DEFAULT, PurchaseType.DEFAULT)
        self.assertTrue(self.__basket.remove_product(self.__product.get_name()))
        self.assertFalse(self.__basket.get_products())
        self.assertNotIn([self.__product, 2], self.__basket)

    # @logger
    def tearDown(self):
        pass

    if __name__ == '__main__':
        unittest.main()

    def __repr__(self):
        return repr ("ShoppingBasketTests")