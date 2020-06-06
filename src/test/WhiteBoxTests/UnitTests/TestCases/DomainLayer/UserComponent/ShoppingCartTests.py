import unittest

from src.main.DomainLayer.StoreComponent.Product import Product
from src.main.DomainLayer.UserComponent.DiscountType import DiscountType
from src.main.DomainLayer.UserComponent.PurchaseType import PurchaseType
from src.main.DomainLayer.UserComponent.ShoppingCart import ShoppingCart
from src.test.WhiteBoxTests.UnitTests.Stubs.StubProduct import StubProduct
from src.test.WhiteBoxTests.UnitTests.Stubs.StubStore import StubStore


class ShoppingCartTests(unittest.TestCase):
    def setUp(self):
        self.__shopping_cart = ShoppingCart()
        self.__product = StubProduct()
        self.__store = StubStore()
        self.__product_ls_to_add = {"product": self.__product, "amount": 4, "store_name": self.__store.get_name(),
                                    "discount_type": DiscountType.DEFAULT, "purchase_type": PurchaseType.DEFAULT}

    def test_add_products(self):
        self.__shopping_cart.add_products([self.__product_ls_to_add])
        basket_pair = self.__shopping_cart.get_shopping_baskets()[0]
        self.assertEqual(basket_pair["store_name"], "Eytan's best store")
        basket = basket_pair["basket"].get_products()[0]
        self.assertEqual(basket["product"].get_name(), "Alcogel")
        self.assertEqual(basket["amount"], 4)
        self.assertEqual(basket["discountType"], DiscountType.DEFAULT)
        self.assertEqual(basket["purchaseType"], PurchaseType.DEFAULT)

    def test_remove_product(self):
        self.__shopping_cart.add_products([{"product": self.__product, "amount": 4, "store_name": self.__store.get_name(),
                                            "discount_type": DiscountType.DEFAULT, "purchase_type": PurchaseType.DEFAULT},
                                            {"product": Product("TV", 100, "Electric"), "amount": 4,
                                             "store_name": self.__store.get_name(),
                                             "discount_type": DiscountType.DEFAULT, "purchase_type": PurchaseType.DEFAULT}])
        self.assertEqual(len(self.__shopping_cart.get_shopping_baskets()), 1)
        self.__shopping_cart.remove_products([{"product_name": "Alcogel", "store_name": "Eytan's best store"}])
        ls = self.__shopping_cart.get_shopping_baskets()
        self.assertEqual(len(self.__shopping_cart.get_shopping_baskets()), 1)
        self.__shopping_cart.remove_products([{"product_name": "TV", "store_name": "Eytan's best store"}])
        ls = self.__shopping_cart.get_shopping_baskets()
        self.assertEqual(len(self.__shopping_cart.get_shopping_baskets()), 0)

    def test_update_quantity(self):
        self.__shopping_cart.add_products([{"product": self.__product, "amount": 4, "store_name": self.__store.get_name(),
                                            "discount_type": DiscountType.DEFAULT, "purchase_type": PurchaseType.DEFAULT},
                                           {"product": Product("TV", 256, "Electric"), "amount": 4,
                                            "store_name": self.__store.get_name(),
                                            "discount_type": DiscountType.DEFAULT, "purchase_type": PurchaseType.DEFAULT}])
        self.__shopping_cart.update_quantity([{"product_name": self.__product.get_name(), "store_name": self.__store.get_name(), "amount": 16}])
        basket_pair = self.__shopping_cart.get_shopping_baskets()[0]
        self.assertEqual(basket_pair["store_name"], "Eytan's best store")
        basket = basket_pair["basket"].get_products()[0]
        self.assertEqual(basket["product"].get_name(), "Alcogel")
        self.assertEqual(basket["amount"], 16)
        basket = basket_pair["basket"].get_products()[1]
        self.assertEqual(basket["product"].get_name(), "TV")
        self.assertEqual(basket["amount"], 4)

    def tearDown(self):
        pass

    if __name__ == '__main__':
        unittest.main()

    def __repr__(self):
        return repr ("ShoppingCartTests")