import unittest
from unittest.mock import MagicMock

import jsonpickle

from Backend.src.Logger import logger
from Backend.src.main.DomainLayer.UserComponent.PurchaseType import PurchaseType
from Backend.src.main.DomainLayer.StoreComponent.Product import Product
from Backend.src.main.DomainLayer.StoreComponent.Store import Store
from Backend.src.main.DomainLayer.TradeComponent.TradeControl import TradeControl
from Backend.src.main.DomainLayer.UserComponent.DiscountType import DiscountType
from Backend.src.main.DomainLayer.UserComponent.ShoppingBasket import ShoppingBasket
from Backend.src.main.DomainLayer.UserComponent.User import User
from Backend.src.main.ServiceLayer.GuestRole import GuestRole


class GuestRoleTest(unittest.TestCase):
    # @logger
    def setUp(self) -> None:
        self.__guest_role = GuestRole()

    # @logger
    # use case 2.2
    def test_register(self):
        # All valid
        self.assertTrue(self.__guest_role.register("Valid", "Valid"))
        user = User()
        user.register("Valid", "Valid")
        self.assertEqual(user, (TradeControl.get_instance()).get_subscriber("Valid"))

        # Invalid - user already registered
        self.assertFalse(self.__guest_role.register("Valid2", "Valid3"))
        user = User()
        user.register("Valid", "Valid")
        self.assertEqual(user, (TradeControl.get_instance()).get_subscriber("Valid"))
        user = User()
        user.register("Valid2", "Valid3")
        self.assertNotIn(user, (TradeControl.get_instance()).get_subscribers())

        (TradeControl.get_instance()).set_curr_user = User()

        # Invalid - user already exist
        self.assertFalse(self.__guest_role.register("Valid", "Valid"))
        user = User()
        user.register("Valid", "Valid")
        self.assertEqual(user, (TradeControl.get_instance()).get_subscriber("Valid"))

        # Invalid - empty username
        self.assertFalse(self.__guest_role.register("", "Valid"))
        user = User()
        user.register("", "Valid")
        self.assertNotIn(user, (TradeControl.get_instance()).get_subscribers())

        # Invalid - empty password
        self.assertFalse(self.__guest_role.register("Invalid", ""))
        user = User()
        user.register("Invalid", "")
        self.assertNotIn(user, (TradeControl.get_instance()).get_subscribers())

    # @logger
    # use case 2.3
    def test_login(self):
        (TradeControl.get_instance()).register_guest("Valid", "Valid")
        user = (TradeControl.get_instance()).get_curr_user()

        # All valid
        self.assertTrue(self.__guest_role.login("Valid", "Valid"))
        self.assertTrue(user.is_logged_in())

        # Invalid - user already logged in
        self.assertFalse(self.__guest_role.login("Valid", "Valid"))
        self.assertTrue(user.is_logged_in())

        user.logout()

        # Invalid - incorrect password
        self.assertFalse(self.__guest_role.login("Valid", "Invalid"))
        self.assertFalse(user.is_logged_in())

        # Invalid - user doesn't exist
        self.assertFalse(self.__guest_role.login("user.get_nickname()", "Valid"))
        self.assertFalse(user.is_logged_in())

    # @logger
    # use case 2.4
    def test_display_stores_or_products_info(self):
        product = Product("Eytan's product", 12, "Eytan's category")
        product2 = Product("eytan as product", 10, "Eytan's category")
        store: Store = Store("myStore")
        store.add_product("Eytan's product", 12, "Eytan's category", 5)
        store.add_product("eytan as product", 10, "Eytan's category", 100)
        (TradeControl.get_instance()).get_stores().append(store)
        product_as_dictionary = {"product_name": product.get_name(), "amount": 100, "store_name": store.get_name(),
                                 "discount_type": DiscountType.DEFAULT, "purchase_type": PurchaseType.DEFAULT}

        product_as_dictionary2 = {"product_name": product2.get_name(), "amount": 10, "store_name": store.get_name(),
                                  "discount_type": DiscountType.DEFAULT, "purchase_type": PurchaseType.DEFAULT}

        self.__guest_role.save_products_to_basket([product_as_dictionary, product_as_dictionary2])

        # flag store

        # All valid
        self.assertEqual(store, jsonpickle.decode(self.__guest_role.display_stores_or_products_info(store.get_name(),
                                                                                                    store_info_flag=True
                                                                                                    )))
        # Invalid - store doesn't exist
        self.assertIsNone((self.__guest_role.display_stores_or_products_info("store.get_name()",
                                                                             store_info_flag=True
                                                                             )))

        # flag products

        # All valid
        result_products_in_inventory = [(element['product'], element['amount']) for element in
                                        jsonpickle.decode(self.__guest_role.display_stores_or_products_info
                                                          (store.get_name(),
                                                           products_info_flag=True))]
        expected_products_in_inventory = [(element['product'], element['amount']) for element in
                                          store.get_inventory().get_inventory()]
        self.assertEqual(expected_products_in_inventory, result_products_in_inventory)
        # Invalid - store doesn't exist
        self.assertIsNone((self.__guest_role.display_stores_or_products_info
                           ("store.get_name()",
                            products_info_flag=True)))

        # None flags-
        self.assertIsNone(self.__guest_role.display_stores_or_products_info(store.get_name()))

    # @logger
    # use case 2.5.1
    def test_search_products_by(self):
        user = User()
        user_nickname = "Eytan"
        user_password = "Eytan's password"
        user.register(user_nickname, user_password)

        (TradeControl.get_instance()).set_curr_user(user)
        (TradeControl.get_instance()).login_subscriber(user_nickname, user_password)
        (TradeControl.get_instance()).open_store("myFirstStore")

        store = (TradeControl.get_instance()).get_store("myFirstStore")

        # One store
        store.add_products("Eytan", [{"name": "Chair", "price": 100, "category": "Furniture", "amount": 10},
                                     {"name": "TV", "price": 10, "category": "Electric", "amount": 1},
                                     {"name": "Sofa", "price": 1, "category": "Furniture", "amount": 2}])
        product1: Product = Product("Chair", 100, "Furniture")
        product2: Product = Product("TV", 10, "Electric")
        product3: Product = Product("Sofa", 1, "Furniture")

        # Option 1- All valid
        ls = [result_as_dictionary['product_name'] for result_as_dictionary in
              self.__guest_role.search_products_by(1, "Chair")]
        self.assertEqual(len(ls), 1)
        self.assertTrue(product1.get_name() in ls)

        # Option 1- Not an existing product
        ls = [result_as_dictionary['product_name'] for result_as_dictionary in
              self.__guest_role.search_products_by(1, "EytanIsTheBestEver!!!!")]
        self.assertEqual(len(ls), 0)

        # Option 2- All valid
        ls = [result_as_dictionary['product_name'] for result_as_dictionary in
              self.__guest_role.search_products_by(2, "a")]
        self.assertEqual(len(ls), 2)
        self.assertTrue(product1.get_name() in ls)
        self.assertTrue(product3.get_name() in ls)

        # Option 2- Empty products list
        ls = [result_as_dictionary['product_name'] for result_as_dictionary in
              self.__guest_role.search_products_by(2, "EytanIsTheBestEver!!!!!")]
        self.assertEqual(len(ls), 0)

        # Option 3 - All valid
        ls = [result_as_dictionary['product_name'] for result_as_dictionary in
              self.__guest_role.search_products_by(3, "Furniture")]
        self.assertEqual(len(ls), 2)
        self.assertTrue(product1.get_name() in ls)
        self.assertTrue(product3.get_name() in ls)

        ls = [result_as_dictionary['product_name'] for result_as_dictionary in
              self.__guest_role.search_products_by(3, "Electric")]
        self.assertEqual(len(ls), 1)
        self.assertTrue(product2.get_name() in ls)

        # Option 3 - Not an existing category
        ls = [result_as_dictionary['product_name'] for result_as_dictionary in
              self.__guest_role.search_products_by(3, "EytanIsTheBestEver!!!!!")]
        self.assertEqual(len(ls), 0)

        # Two stores (A.K.A more then one store)
        (TradeControl.get_instance()).open_store("not myFirstStore")

        not_store = (TradeControl.get_instance()).get_store("not myFirstStore")
        not_store.add_products("Eytan", [{"name": "Chair", "price": 100, "category": "Furniture", "amount": 10},
                                         {"name": "TV", "price": 10, "category": "Electric", "amount": 1},
                                         {"name": "Sofa", "price": 1, "category": "Furniture", "amount": 2},
                                         {"name": "Pillow", "price": 5, "category": "Accessories", "amount": 5}])
        product1: Product = Product("Chair", 100, "Furniture")
        product2: Product = Product("TV", 10, "Electric")
        product3: Product = Product("Sofa", 1, "Furniture")
        diff_product: Product = Product("Pillow", 5, "Accessories")

        # Option 1- All valid
        ls = [(result_as_dictionary['store_name'], result_as_dictionary['product_name']) for result_as_dictionary in
              self.__guest_role.search_products_by(1, "Chair")]
        self.assertEqual(len(ls), 2)
        self.assertTrue((store.get_name(), product1.get_name()) in ls)
        self.assertTrue((not_store.get_name(), product1.get_name()) in ls)

        # Option 1- Not an existing product
        ls = [(result_as_dictionary['store_name'], result_as_dictionary['product_name']) for result_as_dictionary in
              self.__guest_role.search_products_by(1, "EytanIsTheBestEver!!!!")]
        self.assertEqual(len(ls), 0)

        # Option 2- All valid
        ls = [(result_as_dictionary['store_name'], result_as_dictionary['product_name']) for result_as_dictionary in
              self.__guest_role.search_products_by(2, "a")]
        self.assertEqual(len(ls), 4)
        self.assertTrue((store.get_name(), product1.get_name()) in ls)
        self.assertTrue((store.get_name(), product3.get_name()) in ls)
        self.assertTrue((not_store.get_name(), product1.get_name()) in ls)
        self.assertTrue((not_store.get_name(), product3.get_name()) in ls)

        # Option 2- Empty products list
        ls = [(result_as_dictionary['store_name'], result_as_dictionary['product_name']) for result_as_dictionary in
              self.__guest_role.search_products_by(2, "EytanIsTheBestEver!!!!!")]
        self.assertEqual(len(ls), 0)

        # Option 3 - All valid
        ls = [(result_as_dictionary['store_name'], result_as_dictionary['product_name']) for result_as_dictionary in
              self.__guest_role.search_products_by(3, "Furniture")]
        self.assertEqual(len(ls), 4)
        self.assertTrue((store.get_name(), product1.get_name()) in ls)
        self.assertTrue((store.get_name(), product3.get_name()) in ls)
        self.assertTrue((not_store.get_name(), product1.get_name()) in ls)
        self.assertTrue((not_store.get_name(), product3.get_name()) in ls)

        ls = [(result_as_dictionary['store_name'], result_as_dictionary['product_name']) for result_as_dictionary in
              self.__guest_role.search_products_by(3, "Electric")]
        self.assertEqual(len(ls), 2)
        self.assertTrue((store.get_name(), product2.get_name()) in ls)
        self.assertTrue((not_store.get_name(), product2.get_name()) in ls)

        # Option 3 - Not an existing category
        ls = [(result_as_dictionary['store_name'], result_as_dictionary['product_name']) for result_as_dictionary in
              self.__guest_role.search_products_by(3, "EytanIsTheBestEver!!!!!")]
        self.assertEqual(len(ls), 0)

        # Valid - product exist only in on store
        ls = [(result_as_dictionary['store_name'], result_as_dictionary['product_name']) for result_as_dictionary in
              self.__guest_role.search_products_by(1, "Pillow")]
        self.assertEqual(len(ls), 1)
        self.assertFalse((store.get_name(), diff_product.get_name()) in ls)
        self.assertTrue((not_store.get_name(), diff_product.get_name()) in ls)

    # @logger
    def test_filter_products_by(self):
        user = User()
        user_nickname = "Eytan"
        user_password = "Eytan's password"
        user.register(user_nickname, user_password)

        (TradeControl.get_instance()).set_curr_user(user)
        (TradeControl.get_instance()).login_subscriber(user_nickname, user_password)
        (TradeControl.get_instance()).open_store("myFirstStore")

        store = (TradeControl.get_instance()).get_store("myFirstStore")

        store.add_products("Eytan", [{"name": "Chair", "price": 100, "category": "Furniture", "amount": 10},
                                     {"name": "TV", "price": 10, "category": "Electric", "amount": 1},
                                     {"name": "Sofa", "price": 1, "category": "Furniture", "amount": 2}])

        # Option 1

        # All valid
        product_ls = (TradeControl.get_instance()).get_products_by(2, "")
        expected = [(product_as_dictionary['store_name'],
                     product_as_dictionary['product_name'],
                     product_as_dictionary['price'],
                     product_as_dictionary['category']) for product_as_dictionary in product_ls]

        result = [(product_as_dictionary['store_name'],
                   product_as_dictionary['product_name'],
                   product_as_dictionary['price'],
                   product_as_dictionary['category']) for product_as_dictionary in
                  self.__guest_role.filter_products_by(product_ls, 1, min_price=0, max_price=101)]
        self.assertListEqual(expected, result)

        product_ls = (TradeControl.get_instance()).get_products_by(2, "")
        expected = [(product_as_dictionary['store_name'],
                     product_as_dictionary['product_name'],
                     product_as_dictionary['price'],
                     product_as_dictionary['category']) for product_as_dictionary in product_ls]

        # All valid - edge case -> min price = some_product price & max price = some_product price
        result = [(product_as_dictionary['store_name'],
                   product_as_dictionary['product_name'],
                   product_as_dictionary['price'],
                   product_as_dictionary['category']) for product_as_dictionary in
                  self.__guest_role.filter_products_by(product_ls, 1, min_price=1, max_price=100)]

        self.assertListEqual(expected, result)

        product_ls = (TradeControl.get_instance()).get_products_by(2, "")
        expected = [(product_as_dictionary['store_name'],
                     product_as_dictionary['product_name'],
                     product_as_dictionary['price'],
                     product_as_dictionary['category']) for product_as_dictionary in product_ls if
                    product_as_dictionary['price'] >= 5]

        # All valid - actually doing some filtering.
        result = [(product_as_dictionary['store_name'],
                   product_as_dictionary['product_name'],
                   product_as_dictionary['price'],
                   product_as_dictionary['category']) for product_as_dictionary in
                  self.__guest_role.filter_products_by(product_ls, 1, min_price=5, max_price=200)]

        self.assertListEqual(expected, result)

        # Invalid - no min price
        result = [(product_as_dictionary['store_name'],
                   product_as_dictionary['product_name'],
                   product_as_dictionary['price'],
                   product_as_dictionary['category']) for product_as_dictionary in
                  self.__guest_role.filter_products_by(product_ls, 1, max_price=200)]

        self.assertListEqual([], result)

        # Invalid - no max price
        result = [(product_as_dictionary['store_name'],
                   product_as_dictionary['product_name'],
                   product_as_dictionary['price'],
                   product_as_dictionary['category']) for product_as_dictionary in
                  self.__guest_role.filter_products_by(product_ls, 1, min_price=0.1)]

        self.assertListEqual([], result)

        # Invalid - empty product_ls
        result = [(product_as_dictionary['store_name'],
                   product_as_dictionary['product_name'],
                   product_as_dictionary['price'],
                   product_as_dictionary['category']) for product_as_dictionary in
                  self.__guest_role.filter_products_by([], 1, min_price=0.1, max_price=200)]

        self.assertListEqual([], result)

        # Option 2

        # All valid
        product_ls = (TradeControl.get_instance()).get_products_by(2, "")
        expected = [(product_as_dictionary['store_name'],
                     product_as_dictionary['product_name'],
                     product_as_dictionary['price'],
                     product_as_dictionary['category']) for product_as_dictionary in product_ls
                    if product_as_dictionary['category'] == "Furniture"]

        result = [(product_as_dictionary['store_name'],
                   product_as_dictionary['product_name'],
                   product_as_dictionary['price'],
                   product_as_dictionary['category']) for product_as_dictionary in
                  self.__guest_role.filter_products_by(product_ls, 2, category="Furniture")]
        self.assertListEqual(expected, result)

        # Invalid - no category
        result = [(product_as_dictionary['store_name'],
                   product_as_dictionary['product_name'],
                   product_as_dictionary['price'],
                   product_as_dictionary['category']) for product_as_dictionary in
                  self.__guest_role.filter_products_by(product_ls, 2)]
        self.assertListEqual([], result)

        # Invalid - category doesn't exist
        result = [(product_as_dictionary['store_name'],
                   product_as_dictionary['product_name'],
                   product_as_dictionary['price'],
                   product_as_dictionary['category']) for product_as_dictionary in
                  self.__guest_role.filter_products_by(product_ls, 2, category="Eytan's category")]
        self.assertListEqual([], result)

        # Invalid - empty product_ls
        result = [(product_as_dictionary['store_name'],
                   product_as_dictionary['product_name'],
                   product_as_dictionary['price'],
                   product_as_dictionary['category']) for product_as_dictionary in
                  self.__guest_role.filter_products_by([], 2, category="Furniture")]
        self.assertListEqual([], result)

        # Neither of the options

        # Invalid - option doesn't exist
        result = [(product_as_dictionary['store_name'],
                   product_as_dictionary['product_name'],
                   product_as_dictionary['price'],
                   product_as_dictionary['category']) for product_as_dictionary in
                  self.__guest_role.filter_products_by([], 3, category="Furniture")]
        self.assertListEqual([], result)

        # Invalid - option doesn't exist
        result = [(product_as_dictionary['store_name'],
                   product_as_dictionary['product_name'],
                   product_as_dictionary['price'],
                   product_as_dictionary['category']) for product_as_dictionary in
                  self.__guest_role.filter_products_by(product_ls, 3, min_price=12.2, max_price=43)]
        self.assertListEqual([], result)

    # @logger
    # use case 2.6
    def test_save_products_to_basket(self):
        # TODO: Maybe add a test to check if try to purchase more amount then the store have.
        product = Product("Eytan's product", 12, "Eytan's category")
        store: Store = Store("myStore")
        store.add_product("Eytan's product", 12, "Eytan's category", 5)
        (TradeControl.get_instance()).get_stores().append(store)
        product_as_dictionary = {"product_name": product.get_name(), "amount": 4, "store_name": store.get_name(),
                                 "discount_type": DiscountType.DEFAULT, "purchase_type": PurchaseType.DEFAULT}
        product_to_add = (product,
                          product_as_dictionary['amount'],
                          product_as_dictionary['discount_type'],
                          product_as_dictionary['purchase_type'])

        basket = ShoppingBasket()
        basket.add_product(*product_to_add)
        expected = (store.get_name(), basket)

        shopping_cart = (TradeControl.get_instance()).get_curr_user().get_shopping_cart()

        # All valid
        self.assertTrue(self.__guest_role.save_products_to_basket([product_as_dictionary]))
        self.assertEqual(len(shopping_cart.get_shopping_baskets()), 1)
        self.assertIn(expected, [(basket['store_name'], basket['basket']) for basket in
                                 shopping_cart.get_shopping_baskets()])

        # Valid - empty basket
        self.assertTrue(self.__guest_role.save_products_to_basket([]))
        self.assertEqual(len(shopping_cart.get_shopping_baskets()), 1)
        self.assertIn(expected, [(basket['store_name'], basket['basket']) for basket in
                                 shopping_cart.get_shopping_baskets()])

        # invalid - basket = None
        self.assertFalse(self.__guest_role.save_products_to_basket([product_as_dictionary, None]))
        self.assertEqual(len(shopping_cart.get_shopping_baskets()), 1)
        self.assertIn(expected, [(basket['store_name'], basket['basket']) for basket in
                                 shopping_cart.get_shopping_baskets()])

        bad_basket = {"product_name": "", "amount": 4, "store_name": store.get_name(),
                      "discount_type": DiscountType.DEFAULT, "purchase_type": PurchaseType.DEFAULT}

        # invalid - product = None
        self.assertFalse(self.__guest_role.save_products_to_basket([bad_basket]))
        self.assertEqual(len(shopping_cart.get_shopping_baskets()), 1)
        self.assertIn(expected, [(basket['store_name'], basket['basket']) for basket in
                                 shopping_cart.get_shopping_baskets()])

        bad_basket = {"product_name": product.get_name(), "amount": -4, "store_name": store.get_name(),
                      "discount_type": DiscountType.DEFAULT, "purchase_type": PurchaseType.DEFAULT}

        # invalid - negative amount
        self.assertFalse(self.__guest_role.save_products_to_basket([bad_basket]))
        self.assertEqual(len(shopping_cart.get_shopping_baskets()), 1)
        self.assertIn(expected, [(basket['store_name'], basket['basket']) for basket in
                                 shopping_cart.get_shopping_baskets()])
        bad_basket = {"product_name": product.get_name(), "amount": -4, "store_name": store.get_name(),
                      "discount_type": DiscountType.DEFAULT, "purchase_type": PurchaseType.DEFAULT}

        bad_basket = {"product_name": product, "amount": 0, "store_name": store.get_name(),
                      "discount_type": DiscountType.DEFAULT, "purchase_type": PurchaseType.DEFAULT}

        # invalid - Edge case - amount = 0
        self.assertFalse(self.__guest_role.save_products_to_basket([bad_basket]))
        self.assertEqual(len(shopping_cart.get_shopping_baskets()), 1)
        self.assertIn(expected, [(basket['store_name'], basket['basket']) for basket in
                                 shopping_cart.get_shopping_baskets()])

    # @logger
    # use case 2.7
    def test_view_shopping_cart(self):
        # Empty shopping_cart
        self.assertListEqual([], self.__guest_role.view_shopping_cart())

        product = Product("Eytan's product", 12, "Eytan's category")
        product2 = Product("eytan as product", 10, "Eytan's category")
        store: Store = Store("myStore")
        store.add_product("Eytan's product", 12, "Eytan's category", 5)
        store.add_product("eytan as product", 10, "Eytan's category", 100)
        (TradeControl.get_instance()).get_stores().append(store)
        product_as_dictionary = {"product_name": product.get_name(), "amount": 100, "store_name": store.get_name(),
                                 "discount_type": DiscountType.DEFAULT, "purchase_type": PurchaseType.DEFAULT}

        product_as_dictionary2 = {"product_name": product2.get_name(), "amount": 10, "store_name": store.get_name(),
                                  "discount_type": DiscountType.DEFAULT, "purchase_type": PurchaseType.DEFAULT}

        product_to_add = (product,
                          product_as_dictionary['amount'],
                          product_as_dictionary['discount_type'],
                          product_as_dictionary['purchase_type'])

        basket = ShoppingBasket()
        basket.add_product(*product_to_add)
        expected = [(store.get_name(), product.get_name(), 100), (store.get_name(), product2.get_name(), 10)]
        self.__guest_role.save_products_to_basket([product_as_dictionary, product_as_dictionary2])

        # Not empty shopping_cart
        self.assertEqual(1, len(self.__guest_role.view_shopping_cart()))
        basket_lst = [element['basket'] for element in self.__guest_role.view_shopping_cart()
                      if element['store_name'] == store.get_name()][0]
        lst = [(store.get_name(), element['product_name'], element['amount']) for element in basket_lst]
        self.assertListEqual(expected, lst)

    # @logger
    # use case 2.7
    def test_update_shopping_cart(self):
        product = Product("Eytan's product", 12, "Eytan's category")
        product2 = Product("eytan as product", 10, "Eytan's category")
        store: Store = Store("myStore")
        store.add_product("Eytan's product", 12, "Eytan's category", 5)
        store.add_product("eytan as product", 10, "Eytan's category", 100)
        (TradeControl.get_instance()).get_stores().append(store)
        product_as_dictionary = {"product_name": product.get_name(), "amount": 100, "store_name": store.get_name(),
                                 "discount_type": DiscountType.DEFAULT, "purchase_type": PurchaseType.DEFAULT}

        product_as_dictionary2 = {"product_name": product2.get_name(), "amount": 100, "store_name": store.get_name(),
                                  "discount_type": DiscountType.DEFAULT, "purchase_type": PurchaseType.DEFAULT}

        self.__guest_role.save_products_to_basket([product_as_dictionary, product_as_dictionary2])

        # flag = update
        flag = "update"

        product_details_as_dictionary = {"product_name": product.get_name(),
                                         "store_name": store.get_name(),
                                         "amount": 15}

        # All valid
        self.assertTrue(self.__guest_role.update_shopping_cart(flag, [product_details_as_dictionary]))
        self.assertEqual(1,
                         len((TradeControl.get_instance()).get_curr_user().get_shopping_cart().get_shopping_baskets()))
        self.assertEqual(15, (TradeControl.get_instance()).get_curr_user().get_shopping_cart().
                         get_store_basket(store.get_name()).get_product_amount
        (product_details_as_dictionary['product_name']))

        product_details_as_dictionary = {"product_name": product.get_name(),
                                         "store_name": store.get_name(),
                                         "amount": 0}

        # All valid - edge case - update by zero
        self.assertTrue(self.__guest_role.update_shopping_cart(flag, [product_details_as_dictionary]))
        self.assertEqual(1,
                         len((TradeControl.get_instance()).get_curr_user().get_shopping_cart().get_shopping_baskets()))
        self.assertEqual(0, (TradeControl.get_instance()).get_curr_user().get_shopping_cart().
                         get_store_basket(store.get_name()).get_product_amount
        (product_details_as_dictionary['product_name']))

        product_details_as_dictionary = {"product_name": product.get_name(),
                                         "store_name": store.get_name(),
                                         "amount": -15}

        # Invalid - negative amount
        self.assertFalse(self.__guest_role.update_shopping_cart(flag, [product_details_as_dictionary]))
        self.assertEqual(1,
                         len((TradeControl.get_instance()).get_curr_user().get_shopping_cart().get_shopping_baskets()))
        self.assertEqual(0, (TradeControl.get_instance()).get_curr_user().get_shopping_cart().
                         get_store_basket(store.get_name()).get_product_amount
        (product_details_as_dictionary['product_name']))

        product_details_as_dictionary = {"product_name": product.get_name(),
                                         "store_name": "store.get_name()",
                                         "amount": 15}

        # Invalid - store doesn't exist
        self.assertFalse(self.__guest_role.update_shopping_cart(flag, [product_details_as_dictionary]))

        product_details_as_dictionary = {"product_name": "product.get_name()",
                                         "store_name": store.get_name(),
                                         "amount": 15}

        # Invalid - product doesn't exist
        self.assertFalse(self.__guest_role.update_shopping_cart(flag, [product_details_as_dictionary]))

        # flag = update
        flag = "remove"

        product_details_as_dictionary = {"product_name": product.get_name(),
                                         "store_name": store.get_name(),
                                         "amount": 15}
        product_details_as_dictionary2 = {"product_name": product2.get_name(),
                                          "store_name": store.get_name(),
                                          "amount": 15}

        # All valid
        self.assertTrue(self.__guest_role.update_shopping_cart(flag, [product_details_as_dictionary]))
        self.assertEqual(1,
                         len((TradeControl.get_instance()).get_curr_user().get_shopping_cart().get_shopping_baskets()))
        self.assertIsNone((TradeControl.get_instance()).get_curr_user().get_shopping_cart().
            get_store_basket(store.get_name()).get_product(
            (product_details_as_dictionary['product_name'])))
        self.assertIsNotNone((TradeControl.get_instance()).get_curr_user().get_shopping_cart().
            get_store_basket(store.get_name()).get_product(
            (product_details_as_dictionary2['product_name'])))

        product_details_as_dictionary = {"product_name": product2.get_name(),
                                         "store_name": "store.get_name()",
                                         "amount": 15}

        # Invalid - store doesn't exist
        self.assertFalse(self.__guest_role.update_shopping_cart(flag, [product_details_as_dictionary]))

        product_details_as_dictionary = {"product_name": "product2.get_name()",
                                         "store_name": store.get_name(),
                                         "amount": 15}

        # Invalid - product doesn't exist
        self.assertFalse(self.__guest_role.update_shopping_cart(flag, [product_details_as_dictionary]))

        product_details_as_dictionary = {"product_name": product2.get_name(),
                                         "store_name": store.get_name(),
                                         "amount": 15}

        # Invalid - incorrect flag
        self.assertFalse(self.__guest_role.update_shopping_cart("Eytan's flag", [product_details_as_dictionary]))

        # Invalid - empty product_details list
        self.assertTrue(self.__guest_role.update_shopping_cart(flag, []))
        self.assertIsNotNone((TradeControl.get_instance()).get_curr_user().get_shopping_cart().
            get_store_basket(store.get_name()).get_product(
            (product_details_as_dictionary2['product_name'])))

    # use case 2.8
    # @logger
    def test_purchase_products(self):
        # TODO: this
        self.assertTrue(False)

    # @logger
    def test_confirm_payment_test(self):
        # TODO: this
        self.assertTrue(False)

    def tearDown(self):
        (TradeControl.get_instance()).__delete__()

    def __repr__(self):
        return repr("GuestRoleTest")

    if __name__ == '__main__':
        unittest.main()
