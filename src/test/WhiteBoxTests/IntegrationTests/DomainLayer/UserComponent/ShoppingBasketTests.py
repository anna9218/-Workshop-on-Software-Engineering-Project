import unittest

from src.Logger import logger
from src.main.DomainLayer.StoreComponent.Product import Product
from src.main.DomainLayer.UserComponent.DiscountType import DiscountType
from src.main.DomainLayer.UserComponent.PurchaseType import PurchaseType
from src.main.DomainLayer.UserComponent.ShoppingBasket import ShoppingBasket


class ShoppingBasketTests(unittest.TestCase):
    @logger
    def setUp(self):
        self.__basket = ShoppingBasket()
        self.__product = Product("Eytan's product", 12, "Eytan's category")

    @logger
    # eden
    def test_update_amount(self):
        # def update_amount(self, product_name: str, amount: int):
        self.__basket.add_product(self.__product, 2, DiscountType.DEFAULT, PurchaseType.DEFAULT)

        # All valid
        self.assertTrue(self.__basket.update_amount(self.__product.get_name(), 5))
        self.assertEqual(self.__basket.get_product_amount(self.__product.get_name()), 5)

        # Valid - Edge case - amount is zero
        self.assertTrue(self.__basket.update_amount(self.__product.get_name(), 0))
        self.assertEqual(self.__basket.get_product_amount(self.__product.get_name()), 0)

        # Invalid - Negative amount
        self.assertFalse(self.__basket.update_amount(self.__product.get_name(), -121))
        self.assertEqual(self.__basket.get_product_amount(self.__product.get_name()), 0)

        # Invalid - product doesn't exist
        self.assertFalse(self.__basket.update_amount("self.__product.get_name()", 121))
        self.assertEqual(self.__basket.get_product_amount("self.__product.get_name()"), 0)

    @logger
    def test_is_empty(self):
        # Is empty
        self.assertTrue(self.__basket.is_empty())

        # Is not empty
        self.__basket.add_product(self.__product, 2, DiscountType.DEFAULT, PurchaseType.DEFAULT)
        self.assertFalse(self.__basket.is_empty())

    @logger
    def test_add_product(self):

        # All valid - edge case - amount = 0
        self.__basket.remove_product(self.__product.get_name())
        self.assertFalse(self.__basket.add_product(self.__product, 0, DiscountType.DEFAULT, PurchaseType.DEFAULT))
        self.assertNotIn({"product": self.__product, "amount": 0, "discountType": DiscountType.DEFAULT,
                          "purchaseType": PurchaseType.DEFAULT}, self.__basket.get_products())

        # All valid
        self.assertTrue(self.__basket.add_product(self.__product, 2, DiscountType.DEFAULT, PurchaseType.DEFAULT))
        self.assertIn({"product": self.__product, "amount": 2, "discountType": DiscountType.DEFAULT,
                       "purchaseType": PurchaseType.DEFAULT}, self.__basket.get_products())

        # Invalid - negative amount
        self.assertFalse(self.__basket.add_product(self.__product, -2, DiscountType.DEFAULT, PurchaseType.DEFAULT))
        self.assertIn({"product": self.__product, "amount": 2, "discountType": DiscountType.DEFAULT,
                       "purchaseType": PurchaseType.DEFAULT}, self.__basket.get_products())

    @logger
    def test_remove_product(self):
        # All valid
        self.__basket.add_product(self.__product, 2, DiscountType.DEFAULT, PurchaseType.DEFAULT)
        self.assertTrue(self.__basket.remove_product(self.__product.get_name()))
        self.assertEqual(len(self.__basket.get_products()), 0)

        # Invalid - product doesn't exist
        self.assertFalse(self.__basket.remove_product("self.__product.get_name()"))
        self.assertEqual(len(self.__basket.get_products()), 0)

        # Invalid - product isn't in the basket
        self.assertFalse(self.__basket.remove_product(self.__product.get_name()))
        self.assertEqual(len(self.__basket.get_products()), 0)

        # Invalid - Empty product name
        self.assertFalse(self.__basket.remove_product(""))
        self.assertEqual(len(self.__basket.get_products()), 0)

    @logger
    def test_get_product(self):
        self.__basket.remove_product(self.__product.get_name())
        self.__basket.add_product(self.__product, 12, DiscountType.DEFAULT, PurchaseType.DEFAULT)
        product_as_dictionary = {"product": self.__product,
                                 "amount": self.__basket.get_product_amount(self.__product.get_name()),
                                 "discountType": DiscountType.DEFAULT,
                                 "purchaseType": PurchaseType.DEFAULT}

        # All valid
        self.assertEqual(self.__basket.get_product(self.__product.get_name()), product_as_dictionary)

        # Invalid - product doesn't exist
        self.assertIsNone(self.__basket.get_product("Eytan's very very bad product"))

    @logger
    def test_get_product_amount(self):
        # def get_product_amount(self, product_name: str):
        self.__basket.add_product(self.__product, 12, DiscountType.DEFAULT, PurchaseType.DEFAULT)

        # All valid
        self.assertEqual(self.__basket.get_product_amount(self.__product.get_name()), 12)

        # Invalid - product doesn't exist
        self.assertEqual(self.__basket.get_product_amount("self.__product.get_name()"), 0)

    #@logger
    def test_complete_purchase(self):
        self.__basket.remove_product(self.__product.get_name())
        self.__basket.add_product(self.__product, 12, DiscountType.DEFAULT, PurchaseType.DEFAULT)

        # All valid - one product
        self.__basket.complete_purchase([{"product_name": self.__product.get_name(),
                                          "product_price": self.__product.get_price(),
                                          "amount": 1}])
        self.assertEqual(self.__basket.get_product_amount(self.__product.get_name()), 11)

        product2 = Product("not Eytan's product", 10, "Eytan's category")
        self.__basket.add_product(product2, 6, DiscountType.DEFAULT, PurchaseType.DEFAULT)

        # All valid - two products
        self.__basket.complete_purchase([{"product_name": self.__product.get_name(),
                                          "product_price": self.__product.get_price(),
                                          "amount": 1},
                                         {"product_name": product2.get_name(),
                                          "product_price": product2.get_price(),
                                          "amount": 1}])
        self.assertEqual(self.__basket.get_product_amount(self.__product.get_name()), 10)
        self.assertEqual(self.__basket.get_product_amount(product2.get_name()), 5)

        # All valid - edge case - all amount in the basket
        self.__basket.complete_purchase([{"product_name": self.__product.get_name(),
                                          "product_price": self.__product.get_price(),
                                          "amount": 1},
                                         {"product_name": product2.get_name(),
                                          "product_price": product2.get_price(),
                                          "amount": 5}])
        self.assertEqual(self.__basket.get_product_amount(self.__product.get_name()), 9)
        self.assertNotIn(product2, self.__basket.get_products())

        # All valid - edge case - empty parameter
        self.__basket.complete_purchase([])
        self.assertEqual(self.__basket.get_product_amount(self.__product.get_name()), 9)
        self.assertNotIn(product2, self.__basket.get_products())

        # Invalid - product doesn't exist
        try:
            self.__basket.complete_purchase([{"product_name": product2.get_name(),
                                              "product_price": product2.get_price(),
                                              "amount": 1}])
            self.fail()
        except ValueError:
            pass
        except Exception:
            self.fail()

        self.assertEqual(self.__basket.get_product_amount(self.__product.get_name()), 9)
        self.assertNotIn(product2, self.__basket.get_products())

        # Invalid - more then in the basket
        try:
            self.__basket.complete_purchase([{"product_name": self.__product.get_name(),
                                              "product_price": self.__product.get_price(),
                                              "amount": 100}])
            self.fail()
        except ValueError:
            pass
        except Exception:
            self.fail()

        self.assertEqual(self.__basket.get_product_amount(self.__product.get_name()), 9)
        self.assertNotIn(product2, self.__basket.get_products())

    @logger
    def tearDown(self):
        self.__basket.remove_product(self.__product.get_name())

    if __name__ == '__main__':
        unittest.main()

    def __repr__(self):
        return repr("ShoppingBasketTests")
