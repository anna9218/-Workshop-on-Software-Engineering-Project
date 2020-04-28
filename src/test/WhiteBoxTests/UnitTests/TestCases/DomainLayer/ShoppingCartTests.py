import unittest

from src.Logger import logger
from src.main.DomainLayer.UserComponent.ShoppingCart import ShoppingCart
from src.test.WhiteBoxTests.UnitTests.Stubs.StubProduct import StubProduct
from src.test.WhiteBoxTests.UnitTests.Stubs.StubStore import StubStore


class ShoppingCartTests(unittest.TestCase):
    @logger
    def setUp(self):
        self.__shopping_cart = ShoppingCart()
        self.__product = StubProduct()
        self.__store = StubStore()
        self.__product_ls_to_add = [self.__product, self.__store, 1]  # products_stores_quantity_ls

    @logger
    def test_add_products(self):
        self.__shopping_cart.add_products([self.__product_ls_to_add])
        # check products were added
        for store_basket in self.__shopping_cart.get_shopping_baskets():
            if store_basket[0].get_name() == self.__store.get_name():  # if its the same store
                tmp_result = False
                for prod in store_basket[1]:
                    tmp_prod = prod[0]
                    if self.__product.get_name() == tmp_prod.get_name():
                        tmp_result = True
                self.assertTrue(tmp_result)

    @logger
    def test_remove_product(self):
        self.__shopping_cart.add_products([self.__product_ls_to_add])
        self.__shopping_cart.remove_product(self.__product)
        for store_basket in self.__shopping_cart.get_shopping_baskets():  # check product was removed
            if store_basket[0].get_name() == self.__store.get_name():  # if its the same store
                self.assertNotIn(self.__product, store_basket[1])

    @logger
    def test_update_quantity(self):
        self.__shopping_cart.add_products([self.__product_ls_to_add])
        self.__shopping_cart.update_quantity(self.__product, 5)
        for store_basket in self.__shopping_cart.get_shopping_baskets():  # check product was removed
            if store_basket[0].get_name() == self.__store.get_name():
                for product_amount in store_basket[1]:
                    if product_amount[0].get_name() == self.__product.get_name():
                        self.assertEqual(5, product_amount[1])

    def tearDown(self):
        pass

    if __name__ == '__main__':
        unittest.main()

    def __repr__(self):
        return repr ("ShoppingCartTests")