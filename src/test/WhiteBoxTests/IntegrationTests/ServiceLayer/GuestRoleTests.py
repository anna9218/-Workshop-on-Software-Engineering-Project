import unittest
from unittest.mock import MagicMock

import jsonpickle

from src.main.DataAccessLayer.ConnectionProxy.Tables import rel_path
from src.main.DataAccessLayer.DataAccessFacade import DataAccessFacade
from src.main.DomainLayer.DeliveryComponent.DeliveryProxy import DeliveryProxy
from src.main.DomainLayer.PaymentComponent.PaymentProxy import PaymentProxy

from src.main.DomainLayer.StoreComponent.StoreAppointment import StoreAppointment

from src.main.DomainLayer.UserComponent.PurchaseType import PurchaseType
from src.main.DomainLayer.StoreComponent.Product import Product
from src.main.DomainLayer.StoreComponent.Store import Store
from src.main.DomainLayer.TradeComponent.TradeControl import TradeControl
from src.main.DomainLayer.UserComponent.DiscountType import DiscountType
from src.main.DomainLayer.UserComponent.ShoppingBasket import ShoppingBasket
from src.main.DomainLayer.UserComponent.User import User
from src.main.ServiceLayer.GuestRole import GuestRole


class GuestRoleTest(unittest.TestCase):
    # @logger
    def setUp(self) -> None:
        if not ("testing" in rel_path):
            raise ReferenceError("The Data Base is not the testing data base.\n"
                                 "\t\t\t\tPlease go to src.main.DataAccessLayer.ConnectionProxy.RealDb.rel_path\n"
                                 "\t\t\t\t and change rel_path to test_rel_path.\n"
                                 "\t\t\t\tThanks :D")
        self.__guest_role = GuestRole()

    # use case 2.2
    def test_register(self):
        # All valid
        self.assertTrue(self.__guest_role.register("Valid", "Valid"))
        user = User()
        user.register("Valid", "Valid")
        self.assertEqual(user, (TradeControl.get_instance()).get_subscriber("Valid"))

        # valid - register second user
        self.assertTrue(self.__guest_role.register("Valid2", "Valid3")['response'])
        user = User()
        user.register("Valid", "Valid")
        self.assertEqual(user, (TradeControl.get_instance()).get_subscriber("Valid"))
        user = User()
        user.register("Valid2", "Valid3")
        self.assertIn(user, (TradeControl.get_instance()).get_subscribers())

        (TradeControl.get_instance()).set_curr_user = User()

        # Invalid - user already exist
        self.assertFalse(self.__guest_role.register("Valid", "Valid")['response'])
        user = User()
        user.register("Valid", "Valid")
        self.assertEqual(user, (TradeControl.get_instance()).get_subscriber("Valid"))

        # Invalid - empty username
        self.assertFalse(self.__guest_role.register("", "Valid")['response'])
        user = User()
        user.register("", "Valid")
        self.assertNotIn(user, (TradeControl.get_instance()).get_subscribers())

        # Invalid - empty password
        self.assertFalse(self.__guest_role.register("Invalid", "")['response'])
        user = User()
        user.register("Invalid", "")
        self.assertNotIn(user, (TradeControl.get_instance()).get_subscribers())

    # use case 2.3
    def test_login(self):
        (TradeControl.get_instance()).register_guest("Valid", "Valid")
        user = (TradeControl.get_instance()).get_subscriber("Valid")

        # All valid
        self.assertTrue(self.__guest_role.login("Valid", "Valid")['response'])
        self.assertTrue(user.is_logged_in())

        # Invalid - user already logged in
        self.assertFalse(self.__guest_role.login("Valid", "Valid")['response'])
        self.assertTrue(user.is_logged_in())

        user.logout()

        # Invalid - incorrect password
        self.assertFalse(self.__guest_role.login("Valid", "Invalid")['response'])
        self.assertFalse(user.is_logged_in())

        # Invalid - user doesn't exist
        self.assertFalse(self.__guest_role.login("user.get_nickname()", "Valid")['response'])
        self.assertFalse(user.is_logged_in())

    # use case 2.4
    def test_display_stores_or_products_info(self):
        product = Product("Eytan's product", 12, "Eytan's category")
        product2 = Product("eytan as product", 10, "Eytan's category")
        user = User()
        user.register("eytan", "eytan's password")
        store: Store = Store("myStore")

        store.get_owners_appointments().append(StoreAppointment(None, user, []))
        store.add_product(user.get_nickname(), "Eytan's product", 12, "Eytan's category", 5,0)
        store.add_product(user.get_nickname(), "eytan as product", 10, "Eytan's category", 100,0)

        (TradeControl.get_instance()).get_stores().append(store)
        product_as_dictionary = {"product_name": product.get_name(), "amount": 100, "store_name": store.get_name(),
                                 "discount_type": DiscountType.DEFAULT, "purchase_type": PurchaseType.DEFAULT}

        product_as_dictionary2 = {"product_name": product2.get_name(), "amount": 10, "store_name": store.get_name(),
                                  "discount_type": DiscountType.DEFAULT, "purchase_type": PurchaseType.DEFAULT}

        self.__guest_role.save_products_to_basket([product_as_dictionary, product_as_dictionary2])

        # flag store

        # All valid
        
#        Refactoring_v2
#         result = self.__guest_role.display_stores_or_products_info(store.get_name(), store_info_flag=True)['response']
#         owner_names = [user_v.get_nickname() for user_v in store.get_owners()]
#         result_as_tuple = (result['managers'], result['name'], result['owners'])
#         expected = (store.get_managers(), store.get_name(), owner_names)
#         self.assertEqual(expected, result_as_tuple)

        res = self.__guest_role.display_stores_or_products_info(store.get_name(), store_info_flag=True)

        self.assertEqual({"name": 'myStore', "owners": ['eytan'], "managers": []}, res['response'])

        # Invalid - store doesn't exist
        self.assertIsNone((self.__guest_role.display_stores_or_products_info("store.get_name()",
                                                                             store_info_flag=True
                                                                             )['response']))

        # flag products

        # All valid
#        Refactoring_v2
#         result_products_in_inventory = [(element['name'], element['amount']) for element in
#                                         self.__guest_role.display_stores_or_products_info
#                                         (store.get_name(),
#                                          products_info_flag=True)['response']]
        res = (self.__guest_role.display_stores_or_products_info
                                                          (store.get_name(),
                                                           products_info_flag=True)['response'])
        result_products_in_inventory = [(element['name'], element['amount']) for element in res
                                        ]
        expected_products_in_inventory = [(element['product'].get_name(), element['amount']) for element in
                                          store.get_inventory().get_inventory()]
        self.assertEqual(expected_products_in_inventory, result_products_in_inventory)
        # Invalid - store doesn't exist
        self.assertIsNone((self.__guest_role.display_stores_or_products_info
        ("store.get_name()",
         products_info_flag=True)['response']))

        # None flags-
        self.assertIsNone(self.__guest_role.display_stores_or_products_info(store.get_name())['response'])

    # use case 2.5.1
    def test_search_products_by(self):
        user = User()
        user_nickname = "Eytan"
        user_password = "Eytan's password"
        user.register(user_nickname, user_password)

        (TradeControl.get_instance()).register_guest(user_nickname, user_password)
        (TradeControl.get_instance()).login_subscriber(user_nickname, user_password)
        (TradeControl.get_instance()).open_store("myFirstStore")

        store = (TradeControl.get_instance()).get_store("myFirstStore")

        # One store
        store.add_products("Eytan", [{"name": "Chair", "price": 100, "category": "Furniture", "amount": 10, "purchase_type": 0},
                                     {"name": "TV", "price": 10, "category": "Electric", "amount": 1, "purchase_type": 0},
                                     {"name": "Sofa", "price": 1, "category": "Furniture", "amount": 2, "purchase_type": 0}])
        product1: Product = Product("Chair", 100, "Furniture")
        product2: Product = Product("TV", 10, "Electric")
        product3: Product = Product("Sofa", 1, "Furniture")

        # Option 1- All valid
        ls = [result_as_dictionary['product_name'] for result_as_dictionary in
              self.__guest_role.search_products_by(1, "Chair")['response']]
        self.assertEqual(len(ls), 1)
        self.assertTrue(product1.get_name() in ls)

        # Option 1- Not an existing product
        ls = [result_as_dictionary['product_name'] for result_as_dictionary in
              self.__guest_role.search_products_by(1, "EytanIsTheBestEver!!!!")['response']]
        self.assertEqual(len(ls), 0)

        # Option 2- All valid
        ls = [result_as_dictionary['product_name'] for result_as_dictionary in
              self.__guest_role.search_products_by(2, "a")['response']]
        self.assertEqual(len(ls), 2)
        self.assertTrue(product1.get_name() in ls)
        self.assertTrue(product3.get_name() in ls)

        # Option 2- Empty products list
        ls = [result_as_dictionary['product_name'] for result_as_dictionary in
              self.__guest_role.search_products_by(2, "EytanIsTheBestEver!!!!!")['response']]
        self.assertEqual(len(ls), 0)

        # Option 3 - All valid
        ls = [result_as_dictionary['product_name'] for result_as_dictionary in
              self.__guest_role.search_products_by(3, "Furniture")['response']]
        self.assertEqual(len(ls), 2)
        self.assertTrue(product1.get_name() in ls)
        self.assertTrue(product3.get_name() in ls)

        ls = [result_as_dictionary['product_name'] for result_as_dictionary in
              self.__guest_role.search_products_by(3, "Electric")['response']]
        self.assertEqual(len(ls), 1)
        self.assertTrue(product2.get_name() in ls)

        # Option 3 - Not an existing category
        ls = [result_as_dictionary['product_name'] for result_as_dictionary in
              self.__guest_role.search_products_by(3, "EytanIsTheBestEver!!!!!")['response']]
        self.assertEqual(len(ls), 0)

        # Two stores (A.K.A more then one store)
        (TradeControl.get_instance()).open_store("not myFirstStore")

        not_store = (TradeControl.get_instance()).get_store("not myFirstStore")
        not_store.add_products("Eytan", [{"name": "Chair", "price": 100, "category": "Furniture", "amount": 10, "purchase_type": 0},
                                         {"name": "TV", "price": 10, "category": "Electric", "amount": 1, "purchase_type": 0},
                                         {"name": "Sofa", "price": 1, "category": "Furniture", "amount": 2, "purchase_type": 0},
                                         {"name": "Pillow", "price": 5, "category": "Accessories", "amount": 5, "purchase_type": 0}])
        product1: Product = Product("Chair", 100, "Furniture")
        product2: Product = Product("TV", 10, "Electric")
        product3: Product = Product("Sofa", 1, "Furniture")
        diff_product: Product = Product("Pillow", 5, "Accessories")

        # Option 1- All valid
        ls = [(result_as_dictionary['store_name'], result_as_dictionary['product_name']) for result_as_dictionary in
              self.__guest_role.search_products_by(1, "Chair")['response']]
        self.assertEqual(len(ls), 2)
        self.assertTrue((store.get_name(), product1.get_name()) in ls)
        self.assertTrue((not_store.get_name(), product1.get_name()) in ls)

        # Option 1- Not an existing product
        ls = [(result_as_dictionary['store_name'], result_as_dictionary['product_name']) for result_as_dictionary in
              self.__guest_role.search_products_by(1, "EytanIsTheBestEver!!!!")['response']]
        self.assertEqual(len(ls), 0)

        # Option 2- All valid
        ls = [(result_as_dictionary['store_name'], result_as_dictionary['product_name']) for result_as_dictionary in
              self.__guest_role.search_products_by(2, "a")['response']]
        self.assertEqual(len(ls), 4)
        self.assertTrue((store.get_name(), product1.get_name()) in ls)
        self.assertTrue((store.get_name(), product3.get_name()) in ls)
        self.assertTrue((not_store.get_name(), product1.get_name()) in ls)
        self.assertTrue((not_store.get_name(), product3.get_name()) in ls)

        # Option 2- Empty products list
        ls = [(result_as_dictionary['store_name'], result_as_dictionary['product_name']) for result_as_dictionary in
              self.__guest_role.search_products_by(2, "EytanIsTheBestEver!!!!!")['response']]
        self.assertEqual(len(ls), 0)

        # Option 3 - All valid
        ls = [(result_as_dictionary['store_name'], result_as_dictionary['product_name']) for result_as_dictionary in
              self.__guest_role.search_products_by(3, "Furniture")['response']]
        self.assertEqual(len(ls), 4)
        self.assertTrue((store.get_name(), product1.get_name()) in ls)
        self.assertTrue((store.get_name(), product3.get_name()) in ls)
        self.assertTrue((not_store.get_name(), product1.get_name()) in ls)
        self.assertTrue((not_store.get_name(), product3.get_name()) in ls)

        ls = [(result_as_dictionary['store_name'], result_as_dictionary['product_name']) for result_as_dictionary in
              self.__guest_role.search_products_by(3, "Electric")['response']]
        self.assertEqual(len(ls), 2)
        self.assertTrue((store.get_name(), product2.get_name()) in ls)
        self.assertTrue((not_store.get_name(), product2.get_name()) in ls)

        # Option 3 - Not an existing category
        ls = [(result_as_dictionary['store_name'], result_as_dictionary['product_name']) for result_as_dictionary in
              self.__guest_role.search_products_by(3, "EytanIsTheBestEver!!!!!")['response']]
        self.assertEqual(len(ls), 0)

        # Valid - product exist only in on store
        ls = [(result_as_dictionary['store_name'], result_as_dictionary['product_name']) for result_as_dictionary in
              self.__guest_role.search_products_by(1, "Pillow")['response']]
        self.assertEqual(len(ls), 1)
        self.assertFalse((store.get_name(), diff_product.get_name()) in ls)
        self.assertTrue((not_store.get_name(), diff_product.get_name()) in ls)

    def test_filter_products_by(self):
        user = User()
        user_nickname = "Eytan"
        user_password = "Eytan's password"
        user.register(user_nickname, user_password)

        (TradeControl.get_instance()).register_guest(user_nickname, user_password)
        (TradeControl.get_instance()).login_subscriber(user_nickname, user_password)
        (TradeControl.get_instance()).open_store("myFirstStore")

        store = (TradeControl.get_instance()).get_store("myFirstStore")

        store.add_products("Eytan", [{"name": "Chair", "price": 100, "category": "Furniture", "amount": 10, "purchase_type": 0},
                                     {"name": "TV", "price": 10, "category": "Electric", "amount": 1, "purchase_type": 0},
                                     {"name": "Sofa", "price": 1, "category": "Furniture", "amount": 2, "purchase_type": 0}])

        # Option 1

        # All valid
        product_ls = (TradeControl.get_instance()).get_products_by(2, "")['response']
        expected = [(product_as_dictionary['store_name'],
                     product_as_dictionary['product_name'],
                     product_as_dictionary['price'],
                     product_as_dictionary['category']) for product_as_dictionary in product_ls]

        result = [(product_as_dictionary['store_name'],
                   product_as_dictionary['product_name'],
                   product_as_dictionary['price'],
                   product_as_dictionary['category']) for product_as_dictionary in
                  self.__guest_role.filter_products_by(product_ls, 1, min_price=0, max_price=101)['response']]
        self.assertListEqual(expected, result)

        product_ls = (TradeControl.get_instance()).get_products_by(2, "")['response']
        expected = [(product_as_dictionary['store_name'],
                     product_as_dictionary['product_name'],
                     product_as_dictionary['price'],
                     product_as_dictionary['category']) for product_as_dictionary in product_ls]

        # All valid - edge case -> min price = some_product price & max price = some_product price
        result = [(product_as_dictionary['store_name'],
                   product_as_dictionary['product_name'],
                   product_as_dictionary['price'],
                   product_as_dictionary['category']) for product_as_dictionary in
                  self.__guest_role.filter_products_by(product_ls, 1, min_price=1, max_price=100)['response']]

        self.assertListEqual(expected, result)

        product_ls = (TradeControl.get_instance()).get_products_by(2, "")['response']
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
                  self.__guest_role.filter_products_by(product_ls, 1, min_price=5, max_price=200)['response']]

        self.assertListEqual(expected, result)

        # Invalid - no min price
        result = [(product_as_dictionary['store_name'],
                   product_as_dictionary['product_name'],
                   product_as_dictionary['price'],
                   product_as_dictionary['category']) for product_as_dictionary in
                  self.__guest_role.filter_products_by(product_ls, 1, max_price=200)['response']]

        self.assertListEqual([], result)

        # Invalid - no max price
        result = [(product_as_dictionary['store_name'],
                   product_as_dictionary['product_name'],
                   product_as_dictionary['price'],
                   product_as_dictionary['category']) for product_as_dictionary in
                  self.__guest_role.filter_products_by(product_ls, 1, min_price=0.1)['response']]

        self.assertListEqual([], result)

        # Invalid - empty product_ls
        result = [(product_as_dictionary['store_name'],
                   product_as_dictionary['product_name'],
                   product_as_dictionary['price'],
                   product_as_dictionary['category']) for product_as_dictionary in
                  self.__guest_role.filter_products_by([], 1, min_price=0.1, max_price=200)['response']]

        self.assertListEqual([], result)

        # Option 2

        # All valid
        product_ls = (TradeControl.get_instance()).get_products_by(2, "")['response']
        expected = [(product_as_dictionary['store_name'],
                     product_as_dictionary['product_name'],
                     product_as_dictionary['price'],
                     product_as_dictionary['category']) for product_as_dictionary in product_ls
                    if product_as_dictionary['category'] == "Furniture"]

        result = [(product_as_dictionary['store_name'],
                   product_as_dictionary['product_name'],
                   product_as_dictionary['price'],
                   product_as_dictionary['category']) for product_as_dictionary in
                  self.__guest_role.filter_products_by(product_ls, 2, category="Furniture")['response']]
        self.assertListEqual(expected, result)

        # Invalid - no category
        result = [(product_as_dictionary['store_name'],
                   product_as_dictionary['product_name'],
                   product_as_dictionary['price'],
                   product_as_dictionary['category']) for product_as_dictionary in
                  self.__guest_role.filter_products_by(product_ls, 2)['response']]
        self.assertListEqual([], result)

        # Invalid - category doesn't exist
        result = [(product_as_dictionary['store_name'],
                   product_as_dictionary['product_name'],
                   product_as_dictionary['price'],
                   product_as_dictionary['category']) for product_as_dictionary in
                  self.__guest_role.filter_products_by(product_ls, 2, category="Eytan's category")['response']]
        self.assertListEqual([], result)

        # Invalid - empty product_ls
        result = [(product_as_dictionary['store_name'],
                   product_as_dictionary['product_name'],
                   product_as_dictionary['price'],
                   product_as_dictionary['category']) for product_as_dictionary in
                  self.__guest_role.filter_products_by([], 2, category="Furniture")['response']]
        self.assertListEqual([], result)

        # Neither of the options

        # Invalid - option doesn't exist
        result = [(product_as_dictionary['store_name'],
                   product_as_dictionary['product_name'],
                   product_as_dictionary['price'],
                   product_as_dictionary['category']) for product_as_dictionary in
                  self.__guest_role.filter_products_by([], 3, category="Furniture")['response']]
        self.assertListEqual([], result)

        # Invalid - option doesn't exist
        result = [(product_as_dictionary['store_name'],
                   product_as_dictionary['product_name'],
                   product_as_dictionary['price'],
                   product_as_dictionary['category']) for product_as_dictionary in
                  self.__guest_role.filter_products_by(product_ls, 3, min_price=12.2, max_price=43)['response']]
        self.assertListEqual([], result)

    # use case 2.6
    def test_save_products_to_basket(self):

        # # TODO: Maybe add a test to check if try to purchase more amount then the store have.
        # product = Product("Eytan's product", 12, "Eytan's category")
        # user = User()
        # user.register("eytan", "eytan's password")
        # store: Store = Store("myStore")
        # store.get_owners().append(user)
        # store.add_product(user.get_nickname(), "Eytan's product", 12, "Eytan's category", 5, 0)
        # (TradeControl.get_instance()).get_stores().append(store)
        # product_as_dictionary = {"product_name": product.get_name(), "amount": 4, "store_name": store.get_name(),
        #                          "discount_type": DiscountType.DEFAULT, "purchase_type": PurchaseType.DEFAULT}
        # product_to_add = (product,
        #                   product_as_dictionary['amount'])
        #
        # basket = ShoppingBasket()
        # basket.add_product(*product_to_add)
        # expected = (store.get_name(), basket.get_basket_info())
        #
        # shopping_cart = (TradeControl.get_instance()).get_curr_user().get_shopping_cart()
        #
        # # All valid
        # self.assertTrue(self.__guest_role.save_products_to_basket([product_as_dictionary])['response'])
        # self.assertEqual(len(shopping_cart.get_shopping_baskets()), 1)
        # self.assertListEqual([expected], [(basket['store_name'], basket['basket'].get_basket_info()) for basket in
        #                          shopping_cart.get_shopping_baskets()])
        #
        # # Valid - empty basket
        # self.assertTrue(self.__guest_role.save_products_to_basket([])['response'])
        # self.assertEqual(len(shopping_cart.get_shopping_baskets()), 1)
        # self.assertIn(expected, [(basket['store_name'], basket['basket']) for basket in
        #                          shopping_cart.get_shopping_baskets()])
        #
        # # invalid - basket = None
        # self.assertFalse(self.__guest_role.save_products_to_basket([product_as_dictionary, None])['response'])
        # self.assertEqual(len(shopping_cart.get_shopping_baskets()), 1)
        # self.assertIn(expected, [(basket['store_name'], basket['basket']) for basket in
        #                          shopping_cart.get_shopping_baskets()])
        #
        # bad_basket = {"product_name": "", "amount": 4, "store_name": store.get_name(),
        #               "discount_type": DiscountType.DEFAULT, "purchase_type": PurchaseType.DEFAULT}
        #
        # # invalid - product = None
        # self.assertFalse(self.__guest_role.save_products_to_basket([bad_basket])['response'])
        # self.assertEqual(len(shopping_cart.get_shopping_baskets()), 1)
        # self.assertIn(expected, [(basket['store_name'], basket['basket']) for basket in
        #                          shopping_cart.get_shopping_baskets()])
        #
        # bad_basket = {"product_name": product.get_name(), "amount": -4, "store_name": store.get_name(),
        #               "discount_type": DiscountType.DEFAULT, "purchase_type": PurchaseType.DEFAULT}
        #
        # # invalid - negative amount
        # self.assertFalse(self.__guest_role.save_products_to_basket([bad_basket])['response'])
        # self.assertEqual(len(shopping_cart.get_shopping_baskets()), 1)
        # self.assertIn(expected, [(basket['store_name'], basket['basket']) for basket in
        #                          shopping_cart.get_shopping_baskets()])
        # bad_basket = {"product_name": product.get_name(), "amount": -4, "store_name": store.get_name(),
        #               "discount_type": DiscountType.DEFAULT, "purchase_type": PurchaseType.DEFAULT}
        #
        # bad_basket = {"product_name": product, "amount": 0, "store_name": store.get_name(),
        #               "discount_type": DiscountType.DEFAULT, "purchase_type": PurchaseType.DEFAULT}
        #
        # # invalid - Edge case - amount = 0
        # self.assertFalse(self.__guest_role.save_products_to_basket([bad_basket])['response'])
        # self.assertEqual(len(shopping_cart.get_shopping_baskets()), 1)
        # self.assertIn(expected, [(basket['store_name'], basket['basket']) for basket in
        #                          shopping_cart.get_shopping_baskets()])
       
        # TODO: Maybe add a test to check if try to purchase more amount then the store have.
        product = Product("Eytan's product", 12, "Eytan's category")
        user = User()
        user.register("eytan", "eytan's password")
        store: Store = Store("myStore")
        store.get_owners_appointments().append(StoreAppointment(None, user, []))
        store.add_product(user.get_nickname(), "Eytan's product", 12, "Eytan's category", 5)
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
        self.assertTrue(self.__guest_role.save_products_to_basket([product_as_dictionary])['response'])
        self.assertEqual(len(shopping_cart.get_shopping_baskets()), 1)
        self.assertIn(expected, [(basket['store_name'], basket['basket']) for basket in
                                 shopping_cart.get_shopping_baskets()])

        # Valid - empty basket
        self.assertTrue(self.__guest_role.save_products_to_basket([])['response'])
        self.assertEqual(len(shopping_cart.get_shopping_baskets()), 1)
        self.assertIn(expected, [(basket['store_name'], basket['basket']) for basket in
                                 shopping_cart.get_shopping_baskets()])

        # invalid - basket = None
        self.assertFalse(self.__guest_role.save_products_to_basket([product_as_dictionary, None])['response'])
        self.assertEqual(len(shopping_cart.get_shopping_baskets()), 1)
        self.assertIn(expected, [(basket['store_name'], basket['basket']) for basket in
                                 shopping_cart.get_shopping_baskets()])

        bad_basket = {"product_name": "", "amount": 4, "store_name": store.get_name(),
                      "discount_type": DiscountType.DEFAULT, "purchase_type": PurchaseType.DEFAULT}

        # invalid - product = None
        self.assertFalse(self.__guest_role.save_products_to_basket([bad_basket])['response'])
        self.assertEqual(len(shopping_cart.get_shopping_baskets()), 1)
        self.assertIn(expected, [(basket['store_name'], basket['basket']) for basket in
                                 shopping_cart.get_shopping_baskets()])

        bad_basket = {"product_name": product.get_name(), "amount": -4, "store_name": store.get_name(),
                      "discount_type": DiscountType.DEFAULT, "purchase_type": PurchaseType.DEFAULT}

        # invalid - negative amount
        self.assertFalse(self.__guest_role.save_products_to_basket([bad_basket])['response'])
        self.assertEqual(len(shopping_cart.get_shopping_baskets()), 1)
        self.assertIn(expected, [(basket['store_name'], basket['basket']) for basket in
                                 shopping_cart.get_shopping_baskets()])
        bad_basket = {"product_name": product.get_name(), "amount": -4, "store_name": store.get_name(),
                      "discount_type": DiscountType.DEFAULT, "purchase_type": PurchaseType.DEFAULT}

        bad_basket = {"product_name": product, "amount": 0, "store_name": store.get_name(),
                      "discount_type": DiscountType.DEFAULT, "purchase_type": PurchaseType.DEFAULT}

        # invalid - Edge case - amount = 0
        self.assertFalse(self.__guest_role.save_products_to_basket([bad_basket])['response'])
        self.assertEqual(len(shopping_cart.get_shopping_baskets()), 1)
        self.assertIn(expected, [(basket['store_name'], basket['basket']) for basket in
                                 shopping_cart.get_shopping_baskets()])

    # use case 2.7
    def test_view_shopping_cart(self):
        # Empty shopping_cart
        self.assertListEqual([], self.__guest_role.view_shopping_cart()['response'])

        product = Product("Eytan's product", 12, "Eytan's category")
        product2 = Product("eytan as product", 10, "Eytan's category")
        user = User()
        user.register("eytan", "eytan's password")
        store: Store = Store("myStore")

        store.get_owners_appointments().append(StoreAppointment(None, user, []))
        store.add_product(user.get_nickname(), "Eytan's product", 12, "Eytan's category", 5,0)
        store.add_product(user.get_nickname(), "eytan as product", 10, "Eytan's category", 100,0)

        (TradeControl.get_instance()).get_stores().append(store)
        product_as_dictionary = {"product_name": product.get_name(), "amount": 100, "store_name": store.get_name(),
                                 "discount_type": DiscountType.DEFAULT, "purchase_type": PurchaseType.DEFAULT}

        product_as_dictionary2 = {"product_name": product2.get_name(), "amount": 10, "store_name": store.get_name(),
                                  "discount_type": DiscountType.DEFAULT, "purchase_type": PurchaseType.DEFAULT}

        product_to_add = (product,
                          product_as_dictionary['amount'])

        basket = ShoppingBasket()
        basket.add_product(*product_to_add)
        expected = [(store.get_name(), product.get_name(), 100), (store.get_name(), product2.get_name(), 10)]
        self.__guest_role.save_products_to_basket([product_as_dictionary, product_as_dictionary2])

        # Not empty shopping_cart
        self.assertEqual(1, len(self.__guest_role.view_shopping_cart()['response']))
        basket_lst = [element['basket'] for element in self.__guest_role.view_shopping_cart()['response']
                      if element['store_name'] == store.get_name()][0]
        lst = [(store.get_name(), element['product_name'], element['amount']) for element in basket_lst]
        self.assertListEqual(expected, lst)

    # use case 2.7
    def test_update_shopping_cart(self):
        product = Product("Eytan's product", 12, "Eytan's category")
        product2 = Product("eytan as product", 10, "Eytan's category")
        user = User()
        user.register("eytan", "eytan's password")
        store: Store = Store("myStore")

        store.get_owners_appointments().append(StoreAppointment(None, user, []))
        store.add_product(user.get_nickname(), "Eytan's product", 12, "Eytan's category", 5, 0)
        store.add_product(user.get_nickname(), "eytan as product", 10, "Eytan's category", 100, 0)

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
        self.assertTrue(self.__guest_role.update_shopping_cart(flag, [product_details_as_dictionary])['response'])
        self.assertEqual(1,
                         len((TradeControl.get_instance()).get_curr_user().get_shopping_cart().get_shopping_baskets()))
        self.assertEqual(15, (TradeControl.get_instance()).get_curr_user().get_shopping_cart().
                         get_store_basket(store.get_name()).get_product_amount
        (product_details_as_dictionary['product_name']))

        product_details_as_dictionary = {"product_name": product.get_name(),
                                         "store_name": store.get_name(),
                                         "amount": 0}

        # All valid - edge case - update by zero
        self.assertTrue(self.__guest_role.update_shopping_cart(flag, [product_details_as_dictionary])['response'])
        self.assertEqual(1,
                         len((TradeControl.get_instance()).get_curr_user().get_shopping_cart().get_shopping_baskets()))
        self.assertEqual(0, (TradeControl.get_instance()).get_curr_user().get_shopping_cart().
                         get_store_basket(store.get_name()).get_product_amount
        (product_details_as_dictionary['product_name']))

        product_details_as_dictionary = {"product_name": product.get_name(),
                                         "store_name": store.get_name(),
                                         "amount": -15}

        # Invalid - negative amount
        self.assertFalse(self.__guest_role.update_shopping_cart(flag, [product_details_as_dictionary])['response'])
        self.assertEqual(1,
                         len((TradeControl.get_instance()).get_curr_user().get_shopping_cart().get_shopping_baskets()))
        self.assertEqual(0, (TradeControl.get_instance()).get_curr_user().get_shopping_cart().
                         get_store_basket(store.get_name()).get_product_amount
        (product_details_as_dictionary['product_name']))

        product_details_as_dictionary = {"product_name": product.get_name(),
                                         "store_name": "store.get_name()",
                                         "amount": 15}

        # Invalid - store doesn't exist
        self.assertFalse(self.__guest_role.update_shopping_cart(flag, [product_details_as_dictionary])['response'])

        product_details_as_dictionary = {"product_name": "product.get_name()",
                                         "store_name": store.get_name(),
                                         "amount": 15}

        # Invalid - product doesn't exist
        self.assertFalse(self.__guest_role.update_shopping_cart(flag, [product_details_as_dictionary])['response'])

        # flag = update
        flag = "remove"

        product_details_as_dictionary = {"product_name": product.get_name(),
                                         "store_name": store.get_name(),
                                         "amount": 15}
        product_details_as_dictionary2 = {"product_name": product2.get_name(),
                                          "store_name": store.get_name(),
                                          "amount": 15}

        # All valid
        self.assertTrue(self.__guest_role.update_shopping_cart(flag, [product_details_as_dictionary])['response'])
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
        self.assertFalse(self.__guest_role.update_shopping_cart(flag, [product_details_as_dictionary])['response'])

        product_details_as_dictionary = {"product_name": "product2.get_name()",
                                         "store_name": store.get_name(),
                                         "amount": 15}

        # Invalid - product doesn't exist
        self.assertFalse(self.__guest_role.update_shopping_cart(flag, [product_details_as_dictionary])['response'])

        product_details_as_dictionary = {"product_name": product2.get_name(),
                                         "store_name": store.get_name(),
                                         "amount": 15}

        # Invalid - incorrect flag
        self.assertFalse(
            self.__guest_role.update_shopping_cart("Eytan's flag", [product_details_as_dictionary])['response'])

        # Invalid - empty product_details list
        self.assertTrue(self.__guest_role.update_shopping_cart(flag, [])['response'])
        self.assertIsNotNone((TradeControl.get_instance()).get_curr_user().get_shopping_cart().
            get_store_basket(store.get_name()).get_product(
            (product_details_as_dictionary2['product_name'])))

    # use case 2.8
    def test_purchase_products(self):
        product = Product("Eytan's product", 12, "Eytan's category")
        product2 = Product("eytan as product", 10, "Eytan's category")
        user = User()
        user.register("eytan", "eytan's password")
        store: Store = Store("myStore")
        store.get_owners().append(user)
        store1: Store = Store("not myStore")
        store1.get_owners().append(user)
        store.add_product(user.get_nickname(), "Eytan's product", 12, "Eytan's category", 5, 0)
        store1.add_product(user.get_nickname(), "eytan as product", 10, "Eytan's category", 100, 0)
        (TradeControl.get_instance()).get_stores().append(store)
        (TradeControl.get_instance()).get_stores().append(store1)
        product_as_dictionary = {"product_name": product.get_name(), "amount": 1, "store_name": store.get_name(),
                                 "discount_type": DiscountType.DEFAULT, "purchase_type": PurchaseType.DEFAULT}
        product_as_dictionary2 = {"product_name": product2.get_name(), "amount": 10,
                                  "store_name": store1.get_name(),
                                  "discount_type": DiscountType.DEFAULT, "purchase_type": PurchaseType.DEFAULT}

        (TradeControl.get_instance()).set_curr_user(user)
        self.__guest_role.save_products_to_basket([product_as_dictionary, product_as_dictionary2])

        expected_list = [(store.get_name(), 12, 1),
                         (store1.get_name(), 100, 1)]
        # All valid
        result_as_dictionary = self.__guest_role.purchase_products()
        result_basket_list = [(basket['store_name'], basket['basket_price'], len(basket['products'])) for basket in
                              result_as_dictionary['purchases']]

        result_as_tuple: tuple = (result_as_dictionary['total_price'], result_basket_list)
        self.assertEqual(result_as_tuple[0], 112)
        self.assertListEqual(result_basket_list, expected_list)

        # Init cart again
        product_as_dictionary = {"product_name": product.get_name(), "amount": 1000, "store_name": store.get_name(),
                                 "discount_type": DiscountType.DEFAULT, "purchase_type": PurchaseType.DEFAULT}
        self.__guest_role.save_products_to_basket([product_as_dictionary])

        expected_list = [(store1.get_name(), 100, 1)]

        # Invalid - one basket have more then store have.
        result_as_dictionary = self.__guest_role.purchase_products()
        result_basket_list = [(basket['store_name'], basket['basket_price'], len(basket['products'])) for basket in
                              result_as_dictionary['purchases']]

        result_as_tuple: tuple = (result_as_dictionary['total_price'], result_basket_list)
        self.assertEqual(result_as_tuple[0], 100)
        self.assertListEqual(result_basket_list, expected_list)

        product_as_dictionary2 = {"product_name": product2.get_name(), "amount": 1000,
                                  "store_name": store1.get_name(),
                                  "discount_type": DiscountType.DEFAULT, "purchase_type": PurchaseType.DEFAULT}
        self.__guest_role.save_products_to_basket([product_as_dictionary2])

        # Invalid two baskets have more then store have.
        self.assertListEqual([], self.__guest_role.purchase_products())

        # TODO: Add tests for legal/illegal policies(4.2), a test with discount and a test without discount.
        # More TODO: A test for Public auction, a test for secret sale and for known sale.

    def test_purchase_basket(self):
        product = Product("Eytan's product", 12, "Eytan's category")
        product2 = Product("eytan as product", 10, "Eytan's category")
        user = User()
        user.register("eytan", "eytan's password")
        store: Store = Store("myStore")
        store.get_owners().append(user)
        store1: Store = Store("not myStore")
        store1.get_owners().append(user)
        store.add_product(user.get_nickname(), "Eytan's product", 12, "Eytan's category", 5, 0)
        store1.add_product(user.get_nickname(), "eytan as product", 10, "Eytan's category", 100, 0)
        (TradeControl.get_instance()).get_stores().append(store)
        (TradeControl.get_instance()).get_stores().append(store1)
        product_as_dictionary = {"product_name": product.get_name(), "amount": 1, "store_name": store.get_name(),
                                 "discount_type": DiscountType.DEFAULT, "purchase_type": PurchaseType.DEFAULT}
        product_as_dictionary2 = {"product_name": product2.get_name(), "amount": 10, "store_name": store1.get_name(),
                                  "discount_type": DiscountType.DEFAULT, "purchase_type": PurchaseType.DEFAULT}

        (TradeControl.get_instance()).set_curr_user(user)
        self.__guest_role.save_products_to_basket([product_as_dictionary, product_as_dictionary2])

        expected_list = [(store.get_name(), 12, 1)]
        # All valid
        result_as_dictionary = self.__guest_role.purchase_basket(store.get_name())['response']
        result_basket_list = [(basket['store_name'], basket['basket_price'], len(basket['products'])) for basket in
                              result_as_dictionary['purchases']]

        result_as_tuple: tuple = (result_as_dictionary['total_price'], result_basket_list)
        self.assertEqual(result_as_tuple[0], 12)
        self.assertListEqual(result_basket_list, expected_list)

        # Init cart again
        product_as_dictionary = {"product_name": product.get_name(), "amount": 1000, "store_name": store.get_name(),
                                 "discount_type": DiscountType.DEFAULT, "purchase_type": PurchaseType.DEFAULT}
        self.__guest_role.save_products_to_basket([product_as_dictionary])

        # Invalid - try to purchase more than store have
        result_as_dictionary = self.__guest_role.purchase_basket(store.get_name())['response']
        self.assertIsNone(result_as_dictionary)

        # Invalid - basket doesn't exist
        result_as_dictionary = self.__guest_role.purchase_basket("store.get_name()")['response']
        self.assertIsNone(result_as_dictionary)

        # Init cart again
        self.__guest_role.update_shopping_cart("remove", [{"product_name": product.get_name(), "amount": 1000,
                                                           "store_name": store.get_name()}])
        product_as_dictionary = {"product_name": product.get_name(), "amount": 1, "store_name": store.get_name(),
                                 "discount_type": DiscountType.DEFAULT, "purchase_type": PurchaseType.DEFAULT}
        self.__guest_role.save_products_to_basket([product_as_dictionary])

        # TODO: Add tests for legal/illegal policies(4.2), a test with discount and a test without discount.
        # More TODO: A test for Public auction, a test for secret sale and for known sale.

    def test_confirm_payment(self):
        product = Product("Eytan's product", 12, "Eytan's category")
        product2 = Product("eytan as product", 10, "Eytan's category")
        user = User()
        user.register("eytan", "eytan's password")
        store: Store = Store("myStore")
        store.get_owners().append(user)
        store1: Store = Store("not myStore")
        store1.get_owners().append(user)
        store.add_product(user.get_nickname(), "Eytan's product", 12, "Eytan's category", 5, 0)
        store1.add_product(user.get_nickname(), "eytan as product", 10, "Eytan's category", 100, 0)
        (TradeControl.get_instance()).get_stores().append(store)
        (TradeControl.get_instance()).get_stores().append(store1)
        product_as_dictionary = {"product_name": product.get_name(), "amount": 1, "store_name": store.get_name(),
                                 "discount_type": DiscountType.DEFAULT, "purchase_type": PurchaseType.DEFAULT}
        product_as_dictionary2 = {"product_name": product2.get_name(), "amount": 10, "store_name": store1.get_name(),
                                  "discount_type": DiscountType.DEFAULT, "purchase_type": PurchaseType.DEFAULT}

        (TradeControl.get_instance()).set_curr_user(user)
        self.__guest_role.save_products_to_basket([product_as_dictionary, product_as_dictionary2])

        DeliveryProxy.get_instance().deliver_products = MagicMock(return_value={'response': True, 'msg': 'Good'})
        PaymentProxy.get_instance().commit_payment = MagicMock(return_value={'response': True, 'msg': 'Good'})

        # Assuming GuestRole.purchase_products() is working fine.
        purchase_result = self.__guest_role.purchase_products()

        # All valid
        self.assertTrue(self.__guest_role.confirm_payment("Eytan's address", purchase_result)['response'])
        # check post condition - purchase in purchase history
        self.assertEqual(2, len(user.get_purchase_history()))
        # # check post-condition: after purchase, shopping cart should be empty
        # self.assertEqual(0, len(user.get_shopping_cart().get_shopping_baskets()))
        # check post-condition: after purchase, amount in store should be decreased
        self.assertEqual(4, (TradeControl.get_instance()).get_store(store.get_name()).get_inventory().
                         get_amount(product.get_name()))
        self.assertEqual(90, (TradeControl.get_instance()).get_store(store1.get_name()).get_inventory().
                         get_amount(product2.get_name()))

        DeliveryProxy.get_instance().deliver_products = MagicMock(return_value={'response': True, 'msg': 'Good'})
        PaymentProxy.get_instance().commit_payment = MagicMock(return_value={'response': False, 'msg': 'Bad'})

        # Invalid  - can't make the payment
        self.assertFalse(self.__guest_role.confirm_payment("Eytan's address", purchase_result)['response'])
        # check post condition - purchase in not in purchase history
        self.assertEqual(2, len(user.get_purchase_history()))
        # check post condition - amount in stores not change
        self.assertEqual(4, (TradeControl.get_instance()).get_store(store.get_name()).get_inventory().
                         get_amount(product.get_name()))
        self.assertEqual(90, (TradeControl.get_instance()).get_store(store1.get_name()).get_inventory().
                         get_amount(product2.get_name()))

        DeliveryProxy.get_instance().deliver_products = MagicMock(return_value={'response': False, 'msg': 'Bad'})
        PaymentProxy.get_instance().commit_payment = MagicMock(return_value={'response': True, 'msg': 'Good'})

        # Invalid  - can't make the Delivery
        self.assertFalse(self.__guest_role.confirm_payment("Eytan's address", purchase_result)['response'])
        # check post condition - inventory amount do not decrease
        self.assertEqual(4, (TradeControl.get_instance()).get_store(store.get_name()).get_inventory().
                         get_amount(product.get_name()))
        # check post condition - purchase in not in  purchase history
        self.assertEqual(2, len(user.get_purchase_history()))


    def tearDown(self):
        (DataAccessFacade.get_instance()).delete_purchases()
        # (DataAccessFacade.get_instance()).delete_discount_policies()
        (DataAccessFacade.get_instance()).delete_statistics()
        (DataAccessFacade.get_instance()).delete_store_owner_appointments()
        (DataAccessFacade.get_instance()).delete_products_in_baskets()
        (DataAccessFacade.get_instance()).delete_products()
        (DataAccessFacade.get_instance()).delete_store_manager_appointments()
        (DataAccessFacade.get_instance()).delete_stores()
        (DataAccessFacade.get_instance()).delete_users()
        (TradeControl.get_instance()).__delete__()

    def __repr__(self):
        return repr("GuestRoleTest")

    if __name__ == '__main__':
        unittest.main()
