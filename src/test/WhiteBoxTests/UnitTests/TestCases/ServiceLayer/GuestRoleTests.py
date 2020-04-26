import unittest
# from src.main.DomainLayer.TradeControl import TradeControl as TC
from src.Logger import logger
from src.main.DomainLayer.Product import Product
from src.main.DomainLayer.Purchase import Purchase
from src.main.DomainLayer.Store import Store
from src.main.DomainLayer.User import User
from src.main.DomainLayer.TradeControl import TradeControl
from src.main.ServiceLayer.GuestRole import GuestRole
from datetime import datetime as date_time


class GuestRoleTest(unittest.TestCase):

    @logger
    def setUp(self) -> None:
        eytan = User()
        eytan.register("eytan", "isTheBest")
        self.__user = eytan
        self.__store_name = "Eytan's best store"
        self.__store = Store(self.__store_name)
        self.__store.add_product("Eytan's Product", 100, "Eytan Category", 5)
        self.__product1 = Product ("Eytan's Product", 100, "Eytan Category")
        self.__store.add_product("not Eytan's Product", 10, "Eytan Category", 2)
        self.__product2 = Product ("Eytan's Product", 10, "Eytan Category")
        (TradeControl.get_instance()).get_stores().insert(0, self.__store)
        self.__guest_role = GuestRole()

    @logger
    # use case 2.2
    def test_register(self):
        # valid
        self.assertIsNotNone(self.__guest_role.register("name", "password"))
        # not valid (the same username & password)
        self.assertIsNone(self.__guest_role.register("name", "password"))


    @logger
    # use case 2.3
    def login_test(self):
        # valid
        self.assertIsNotNone(self.__guest_role.login(self.__user.get_nickname(), "isTheBest"))
        # not valid (already logged in)
        self.assertIsNone(self.__guest_role.login(self.__user.get_nickname(), "isTheBest"))
        # not valid (not registered)
        self.assertIsNone(self.__guest_role.login("Yarin", "1"))
        # not valid (wrong password)
        self.assertIsNone(self.__guest_role.login(self.__user.get_nickname(), "1"))

    @logger
    # use case 2.4
    def display_stores_test(self):
        self.assertIsNotNone(self.__guest_role.display_stores())

    @logger
    def display_stores_info_test(self):
        self.__guest_role.display_stores_info(self.__store_name, True, False)   # display store info
        # TODO - add checks (return from TradeControl.get_instance().get_store(store_name).get_info())
        self.__guest_role.display_stores_info(self.__store_name, False, True)  # display product info
        # TODO - add checks (return from TradeControl.get_instance().get_store(store_name).get_inventory())

    # use case 2.5.1
    @logger
    def search_products_by_test(self):
        # TODO- add checks
        self.__guest_role.search_products_by(0, 0) # search byName for productName
        self.__guest_role.search_products_by(0, 1) # search byName for string
        self.__guest_role.search_products_by(0, 2) # search byName for category
        self.__guest_role.search_products_by(1, 0) # search byKeyword for productName
        self.__guest_role.search_products_by(1, 1) # search byKeyword for string
        self.__guest_role.search_products_by(1, 2) # search byKeyword for category
        self.__guest_role.search_products_by(2, 0) # search byCategoru for productName
        self.__guest_role.search_products_by(2, 1) # search byCategoru for string
        self.__guest_role.search_products_by(2, 2) # search byCategoru for category

    # use case 2.5.2
    @logger
    def filter_products_by_test(self):
        products = [(self.__product1.get_name, self.__store_name), (self.__product2.get_name, self.__store_name)]

        # byPriceRange
        full_output = self.__guest_role.filter_products_by((1, 9, 101), products)
        self.assertEqual(2, len(full_output)) # contains the range
        self.assertEqual([self.__product1, self.__product2], full_output)
        empty_output = self.__guest_role.filter_products_by((1, 11, 99),
                                                            [(self.__product1.get_name,
                                                              self.__store_name)])  # byPriceRange
        self.assertEqual(0, len(empty_output))

        # byCategory
        self.assertEqual(2, self.__guest_role.filter_products_by((2, "Eytan Category"), products))
        self.assertEqual(0, self.__guest_role.filter_products_by((2, "Category"), products))

    @logger
    # use case 2.6
    # Parameters: nickname of the user,
    #             products_stores_quantity_ls is list of lists: [ [product, quantity, store], .... ]
    def save_products_to_basket_test(self):
        products_stores_quantity_ls = [self.__product1, self.__store, 1]
        self.assertTrue(self.__guest_role.save_products_to_basket(self.__user.get_nickname, products_stores_quantity_ls))
        self.assertTrue(self.__guest_role.save_products_to_basket("yarin", products_stores_quantity_ls))

    @logger
    # use case 2.7
    # Parameter is nickname of the subscriber. If its a guest - None
    def view_shopping_cart_test(self):
        self.assertEquals([], self.__guest_role.view_shopping_cart(self.__user.get_nickname))
        self.__guest_role.update_shopping_cart(self.__user.get_nickname, 0, [self.__product1, 1])
        self.assertEquals(1, len(self.__guest_role.view_shopping_cart(self.__user.get_nickname)))

    @logger
    # Parameters: nickname of the subscriber. If its a guest - None
    #             flag=0 update quantity, flag=1 remove product
    #             product can be a single product or a pair of (product quantity)
    def update_shopping_cart_test(self):
        # update product quantity
        self.assertTrue(self.__guest_role.update_shopping_cart(self.__user.get_nickname, 0, [self.__product1, 1]))
        # update product
        self.assertTrue(self.__guest_role.update_shopping_cart(self.__user.get_nickname, 1, [self.__product1, 1]))
        # remove product that not exists
        self.assertFalse(self.__guest_role.update_shopping_cart(self.__user.get_nickname, 1, [self.__product1, 1]))

    # --------------------------------------------------------------------
    # use case 2.8
    @logger
    def test_calculate_purchase_price_direct_approach(self):
        # All valid
        amount_per_product = [["Eytan's Product", 4], ["not Eytan's Product", 1]]
        result = self.__guest_role.calculate_purchase_price_direct_approach(self.__store_name, amount_per_product,
                                                                            self.__user.get_nickname())
        self.assertEqual(result, 410)

        # store name not valid
        result = self.__guest_role.calculate_purchase_price_direct_approach("Eytan's worst store",
                                                                            amount_per_product,
                                                                            self.__user.get_nickname())
        self.assertEqual(result, -1)

        # amount_per_product name not valid
        result = self.__guest_role.calculate_purchase_price_direct_approach(self.__store_name, [],
                                                                            self.__user.get_nickname())
        self.assertEqual(result, -1)

    @logger
    def test_calculate_purchase_price_walkaround_approach(self):
        amount_per_product_per_store = [[self.__store_name, [["Eytan's Product", 4], ["not Eytan's Product", 1]]]]
        # All valid
        result = self.__guest_role.calculate_purchase_price_walkaround_approach(amount_per_product_per_store,
                                                                                self.__user.get_nickname())
        self.assertEqual(result, 410)

        # Only first store valid valid
        result = self.__guest_role.calculate_purchase_price_walkaround_approach(
            [[self.__store_name, [["Eytan's Product", 4],
                                  ["not Eytan's Product", 20]]]],
            self.__user.get_nickname())

        self.assertEqual(result, -1)

        # store name not valid
        result = self.__guest_role.calculate_purchase_price_walkaround_approach([["Eytan's worst store",
                                                                                  [["Eytan's Product", 4]]]],
                                                                                self.__user.get_nickname())
        self.assertEqual(result, -1)

    @logger
    def test_make_purchase(self):
        amount_per_product = [["Eytan's Product", 4], ["not Eytan's Product", 1]]
        # All valid
        result: Purchase = self.__guest_role.make_purchase(self.__store, amount_per_product,
                                                           self.__user.get_nickname())
        self.assertEqual(result.get_price(), 410)

        # amount_per_product name not valid
        result = self.__guest_role.make_purchase(self.__store, [],
                                                 self.__user.get_nickname())
        self.assertIsNone(result)

    @logger
    def test_accepted_price_purchase(self):
        purchase: Purchase = Purchase((TradeControl.get_instance()).get_next_purchase_id(),
                                      [["Eytan's Product", 4], ["not Eytan's Product", 1]],
                                      410, self.__store_name, self.__user.get_nickname())
        self.__user.add_unaccepted_purchase(purchase)
        # All valid
        date = date_time(2021, 4, 19)
        result = self.__guest_role.accepted_price_purchase(purchase, ["4230014", date])

        # self.assertTrue(result)

        # card not valid
        result = self.__guest_role.accepted_price_purchase(purchase, ["4230014", date])
        self.assertFalse(result)

        # date not valid
        result = self.__guest_role.accepted_price_purchase(purchase, ["4230014", date_time(1999, 4, 19)])
        self.assertFalse(result)

    def __repr__(self):
        return repr ("GuestRoleTest")

if __name__ == '__main__':
    unittest.main()
