import unittest

from src.main.DomainLayer.StoreComponent.Product import Product
from src.main.DomainLayer.StoreComponent.Store import Store
from src.main.DomainLayer.UserComponent.DiscountType import DiscountType
from src.main.DomainLayer.UserComponent.PurchaseType import PurchaseType
from src.main.DomainLayer.UserComponent.ShoppingBasket import ShoppingBasket
from src.main.DomainLayer.UserComponent.ShoppingCart import ShoppingCart


class ShoppingCartTests(unittest.TestCase):
    def setUp(self):
        self.__shopping_cart = ShoppingCart()
        self.__product = Product("Eytan's product", 12, "Eytan's category")
        self.__store: Store = Store("myStore")
        self.__product_as_dictionary = {"product": self.__product, "amount": 4, "store_name": self.__store.get_name(),
                                        "discount_type": DiscountType.DEFAULT, "purchase_type": PurchaseType.DEFAULT}
        self.__product_to_add = (self.__product_as_dictionary['product'],
                                 self.__product_as_dictionary['amount'])

    def test_add_products(self):
        basket = ShoppingBasket()
        basket.add_product(*self.__product_to_add)
        expected = {"store_name": self.__store.get_name(), "basket": basket}

        # All valid
        self.assertTrue(self.__shopping_cart.add_products([self.__product_as_dictionary])['response'])
        res = self.__shopping_cart.get_shopping_baskets()
        self.assertEqual(len(res), 1)
        res = res[0]
        self.assertTrue(res['store_name'] == self.__store.get_name() and
                        res['basket'].get_products()[0]['product'].get_name() == self.__product.get_name())
        # self.assertIn(expected, self.__shopping_cart.get_shopping_baskets())

        # Valid - empty basket
        self.assertTrue(self.__shopping_cart.add_products([])['response'])
        res = self.__shopping_cart.get_shopping_baskets()
        # [{'store_name', 'basket': ShoppingBasket}]
        # ShoppingBasket.get_products = [{'product', 'amount'}]
        self.assertEqual(len(res), 1)
        res = res[0]
        self.assertTrue(res['store_name'] == self.__store.get_name() and
                        res['basket'].get_products()[0]['product'].get_name() == self.__product.get_name())
        # self.assertIn(expected, self.__shopping_cart.get_shopping_baskets())

        # invalid - basket = None
        self.assertFalse(self.__shopping_cart.add_products([self.__product_as_dictionary, None])['response'])
        res = self.__shopping_cart.get_shopping_baskets()
        # [{'store_name', 'basket': ShoppingBasket}]
        # ShoppingBasket.get_products = [{'product', 'amount'}]
        self.assertEqual(len(res), 1)
        res = res[0]
        self.assertTrue(res['store_name'] == self.__store.get_name() and
                        res['basket'].get_products()[0]['product'].get_name() == self.__product.get_name())
        # self.assertIn(expected, self.__shopping_cart.get_shopping_baskets())

        bad_basket = {"product": None, "amount": 4, "store_name": self.__store.get_name(),
                      "discount_type": DiscountType.DEFAULT, "purchase_type": PurchaseType.DEFAULT}

        # invalid - product = None
        self.assertFalse(self.__shopping_cart.add_products([bad_basket])['response'])
        res = self.__shopping_cart.get_shopping_baskets()
        # [{'store_name', 'basket': ShoppingBasket}]
        # ShoppingBasket.get_products = [{'product', 'amount'}]
        self.assertEqual(len(res), 1)
        res = res[0]
        self.assertTrue(res['store_name'] == self.__store.get_name() and
                        res['basket'].get_products()[0]['product'].get_name() == self.__product.get_name())
        # self.assertIn(expected, self.__shopping_cart.get_shopping_baskets())

        bad_basket = {"product": self.__product, "amount": -4, "store_name": self.__store.get_name(),
                      "discount_type": DiscountType.DEFAULT, "purchase_type": PurchaseType.DEFAULT}

        # invalid - negative amount
        self.assertFalse(self.__shopping_cart.add_products([bad_basket])['response'])
        res = self.__shopping_cart.get_shopping_baskets()
        # [{'store_name', 'basket': ShoppingBasket}]
        # ShoppingBasket.get_products = [{'product', 'amount'}]
        self.assertEqual(len(res), 1)
        res = res[0]
        self.assertTrue(res['store_name'] == self.__store.get_name() and
                        res['basket'].get_products()[0]['product'].get_name() == self.__product.get_name())
        # self.assertIn(expected, self.__shopping_cart.get_shopping_baskets())

        bad_basket = {"product": self.__product, "amount": 0, "store_name": self.__store.get_name(),
                      "discount_type": DiscountType.DEFAULT, "purchase_type": PurchaseType.DEFAULT}

        # invalid - Edge case - amount = 0
        self.assertFalse(self.__shopping_cart.add_products([bad_basket])['response'])
        res = self.__shopping_cart.get_shopping_baskets()
        # [{'store_name', 'basket': ShoppingBasket}]
        # ShoppingBasket.get_products = [{'product', 'amount'}]
        self.assertEqual(len(res), 1)
        res = res[0]
        self.assertTrue(res['store_name'] == self.__store.get_name() and
                        res['basket'].get_products()[0]['product'].get_name() == self.__product.get_name())
        # self.assertIn(expected, self.__shopping_cart.get_shopping_baskets())

    def test_remove_products(self):
        product1: Product = Product("not Eytan's product", 9, "Eytan's category")
        store1: Store = Store("Not my store")
        product2: Product = Product("maybe Eytan's product", 8, "Eytan's category")
        product_as_dictionary_var1 = {"product": product1, "amount": 3, "store_name": self.__store.get_name(),
                                      "discount_type": DiscountType.DEFAULT, "purchase_type": PurchaseType.DEFAULT}
        product_as_dictionary_var2 = {"product": product2, "amount": 5, "store_name": store1.get_name(),
                                      "discount_type": DiscountType.DEFAULT, "purchase_type": PurchaseType.DEFAULT}
        product_as_dictionary_var3 = {"product": product1, "amount": 12, "store_name": store1.get_name(),
                                      "discount_type": DiscountType.DEFAULT, "purchase_type": PurchaseType.DEFAULT}
        self.__shopping_cart.add_products([self.__product_as_dictionary,
                                           product_as_dictionary_var1,
                                           product_as_dictionary_var2,
                                           product_as_dictionary_var3])

        # All valid
        self.assertTrue(self.__shopping_cart.remove_products([{"product_name": self.__product.get_name(),
                                                               "store_name": self.__store.get_name()}]))
        self.assertEqual(len(self.__shopping_cart.get_shopping_baskets()), 2)
        stores = [store_and_basket['store_name'] for store_and_basket in self.__shopping_cart.get_shopping_baskets()]
        self.assertTrue(self.__store.get_name() in stores)
        self.assertTrue(store1.get_name() in stores)
        product_as_dictionary_lst_self_store = self.__shopping_cart.get_store_basket(store1.get_name()).get_products()
        products_self_store = [product_as_dictionary['product'] for product_as_dictionary in
                               product_as_dictionary_lst_self_store]
        product_as_dictionary_lst_store1 = self.__shopping_cart.get_store_basket(store1.get_name()).get_products()
        products_store1 = [product_as_dictionary['product'] for product_as_dictionary in
                           product_as_dictionary_lst_store1]
        self.assertTrue(product1 in products_self_store)
        self.assertTrue(product1 in products_store1)
        self.assertTrue(product2 in products_store1)
        self.assertFalse(self.__product in product_as_dictionary_lst_self_store)

        # Invalid - product isn't in the store
        self.assertFalse(self.__shopping_cart.remove_products([{"product_name": product2.get_name(),
                                                                "store_name": self.__store.get_name()}])['response'])
        self.assertEqual(len(self.__shopping_cart.get_shopping_baskets()), 2)
        stores = [store_and_basket['store_name'] for store_and_basket in self.__shopping_cart.get_shopping_baskets()]
        self.assertTrue(self.__store.get_name() in stores)
        self.assertTrue(store1.get_name() in stores)
        product_as_dictionary_lst_self_store = self.__shopping_cart.get_store_basket(store1.get_name()).get_products()
        products_self_store = [product_as_dictionary['product'] for product_as_dictionary in
                               product_as_dictionary_lst_self_store]
        product_as_dictionary_lst_store1 = self.__shopping_cart.get_store_basket(store1.get_name()).get_products()
        products_store1 = [product_as_dictionary['product'] for product_as_dictionary in
                           product_as_dictionary_lst_store1]
        self.assertTrue(product1 in products_self_store)
        self.assertTrue(product1 in products_store1)
        self.assertTrue(product2 in products_store1)
        self.assertFalse(self.__product in product_as_dictionary_lst_self_store)

        # All valid - make the basket empty
        self.assertTrue(self.__shopping_cart.remove_products([{"product_name": product1.get_name(),
                                                               "store_name": self.__store.get_name()}])['response'])
        self.assertEqual(len(self.__shopping_cart.get_shopping_baskets()), 1)
        stores = [store_and_basket['store_name'] for store_and_basket in self.__shopping_cart.get_shopping_baskets()]
        self.assertFalse(self.__store.get_name() in stores)
        self.assertTrue(store1.get_name() in stores)
        product_as_dictionary_lst = self.__shopping_cart.get_store_basket(store1.get_name()).get_products()
        products = [product_as_dictionary['product'] for product_as_dictionary in product_as_dictionary_lst]
        self.assertTrue(product1 in products)
        self.assertTrue(product2 in products)

        # Invalid - product doesn't exist
        self.assertFalse(self.__shopping_cart.remove_products([{"product_name": "product1.get_name()",
                                                                "store_name": store1.get_name()}])['response'])
        self.assertEqual(len(self.__shopping_cart.get_shopping_baskets()), 1)
        stores = [store_and_basket['store_name'] for store_and_basket in self.__shopping_cart.get_shopping_baskets()]
        self.assertTrue(store1.get_name() in stores)
        product_as_dictionary_lst = self.__shopping_cart.get_store_basket(store1.get_name()).get_products()
        products = [product_as_dictionary['product'] for product_as_dictionary in product_as_dictionary_lst]
        self.assertTrue(product1 in products)
        self.assertTrue(product2 in products)

        # Invalid - store doesn't exist
        self.assertFalse(self.__shopping_cart.remove_products([{"product_name": product1.get_name(),
                                                                "store_name": "store1.get_name()"}])['response'])
        self.assertEqual(len(self.__shopping_cart.get_shopping_baskets()), 1)
        stores = [store_and_basket['store_name'] for store_and_basket in self.__shopping_cart.get_shopping_baskets()]
        self.assertTrue(store1.get_name() in stores)
        product_as_dictionary_lst = self.__shopping_cart.get_store_basket(store1.get_name()).get_products()
        products = [product_as_dictionary['product'] for product_as_dictionary in product_as_dictionary_lst]
        self.assertTrue(product1 in products)
        self.assertTrue(product2 in products)

    def test_update_quantity(self):
        # def update_quantity(products_details: [{"product_name": str, "store_name": str, "amount": int}]):
        product1: Product = Product("not Eytan's product", 9, "Eytan's category")
        store1: Store = Store("Not my store")
        product2: Product = Product("maybe Eytan's product", 8, "Eytan's category")
        product_as_dictionary_var1 = {"product": product1, "amount": 3, "store_name": self.__store.get_name(),
                                      "discount_type": DiscountType.DEFAULT, "purchase_type": PurchaseType.DEFAULT}
        product_as_dictionary_var3 = {"product": product1, "amount": 12, "store_name": store1.get_name(),
                                      "discount_type": DiscountType.DEFAULT, "purchase_type": PurchaseType.DEFAULT}
        product_as_dictionary_var2 = {"product": product2, "amount": 5, "store_name": store1.get_name(),
                                      "discount_type": DiscountType.DEFAULT, "purchase_type": PurchaseType.DEFAULT}
        self.__shopping_cart.add_products([self.__product_as_dictionary,
                                           product_as_dictionary_var1,
                                           product_as_dictionary_var2,
                                           product_as_dictionary_var3])
        # All Valid - product only in one store
        self.assertTrue(self.__shopping_cart.update_quantity([{"product_name": self.__product.get_name(),
                                                               "store_name": self.__store.get_name(),
                                                               "amount": 123}])['response'])
        self.assertEqual(123, self.__shopping_cart.get_store_basket(self.__store.get_name()).get_product_amount(
            self.__product.get_name()))

        # All Valid - product in two stores, but change only in one
        self.assertTrue(self.__shopping_cart.update_quantity([{"product_name": product1.get_name(),
                                                               "store_name": self.__store.get_name(),
                                                               "amount": 234}])['response'])
        self.assertEqual(234,  self.__shopping_cart.get_store_basket(self.__store.get_name()).get_product_amount(
            product1.get_name()))
        self.assertEqual(12,  self.__shopping_cart.get_store_basket(store1.get_name()).get_product_amount(
            product1.get_name()))

        # Invalid - product not in store
        self.assertFalse(self.__shopping_cart.update_quantity([{"product_name": product2.get_name(),
                                                                "store_name": self.__store.get_name(),
                                                                "amount": 234}])['response'])
        self.assertNotEqual(234, self.__shopping_cart.get_store_basket(store1.get_name()).get_product_amount(
            product2.get_name()))

        # Invalid - negative amount
        self.assertFalse(self.__shopping_cart.update_quantity([{"product_name": self.__product.get_name(),
                                                                "store_name": self.__store.get_name(),
                                                                "amount": -999}])['response'])
        self.assertNotEqual(-999, self.__shopping_cart.get_store_basket(self.__store.get_name()).get_product_amount(
            self.__product.get_name()))

    def test_remove_store_basket(self):
        expected_basket = ShoppingBasket()
        expected_basket.add_product(*self.__product_to_add)

        self.__shopping_cart.add_products([self.__product_as_dictionary])

        # All valid - store exist
        self.assertTrue(self.__shopping_cart.remove_store_basket(self.__store.get_name()))
        self.assertEqual(0, len(self.__shopping_cart.get_shopping_baskets()))

        # Invalid - store doesn't exist
        self.assertFalse(self.__shopping_cart.remove_store_basket("self.__store.get_name()"))

    def test_get_store_basket(self):
        expected_basket = ShoppingBasket()
        expected_basket.add_product(*self.__product_to_add)

        self.__shopping_cart.add_products([self.__product_as_dictionary])

        # All valid - store exist
        res = self.__shopping_cart.get_store_basket(self.__store.get_name()).get_products()[0]['product'].get_name()
        self.assertEqual(self.__product.get_name(), res)
        # self.assertEqual(expected_basket, self.__shopping_cart.get_store_basket(self.__store.get_name()))

        # Invalid - store doesn't exist
        self.assertIsNone(self.__shopping_cart.get_store_basket("self.__store.get_name()"))

    def tearDown(self):
        pass

    if __name__ == '__main__':
        unittest.main()

    def __repr__(self):
        return repr("ShoppingCartTests")
