import unittest

from Backend.src.Logger import logger
from Backend.src.main.DomainLayer.StoreComponent.Product import Product
from Backend.src.main.DomainLayer.StoreComponent.Store import Store
from Backend.src.main.DomainLayer.UserComponent.DiscountType import DiscountType
from Backend.src.main.DomainLayer.UserComponent.PurchaseType import PurchaseType
from Backend.src.main.DomainLayer.UserComponent.User import User


class UserTests(unittest.TestCase):
    # @logger
    def setUp(self):
        self.__valid_name = "anna9218"
        self.__valid_password = "password"
        self.__user = User()
        self.__user.register(self.__valid_name, self.__valid_password)

        self.__product = Product("Eytan's product", 12, "Eytan's category")
        self.__store: Store = Store("myStore")
        self.__products_to_add = [{"product": self.__product, "store_name": self.__store.get_name(),
                                   "amount": 1, "discount_type": DiscountType.DEFAULT,
                                   "purchase_type": PurchaseType.DEFAULT}]  # products_stores_quantity_ls

    # @logger
    def test_register(self):
        # All valid
        guest1 = User()
        self.assertTrue(guest1.register("valid", "valid"))
        self.assertTrue(guest1.is_registered())
        self.assertTrue(guest1.is_logged_out())
        self.assertFalse(guest1.is_logged_in())

        # All valid -username has white spaces but not empty
        guest11 = User()
        self.assertTrue(guest11.register("valid validovich", "valid"))
        self.assertTrue(guest11.is_registered())
        self.assertTrue(guest11.is_logged_out())
        self.assertFalse(guest11.is_logged_in())

        # Invalid - username is empty
        guest2 = User()
        self.assertFalse(guest2.register("", "valid"))
        self.assertFalse(guest2.is_registered())
        self.assertTrue(guest2.is_logged_out())
        self.assertFalse(guest2.is_logged_in())

        # Invalid - password is empty
        self.assertFalse(guest2.register("valid", ""))
        self.assertFalse(guest2.is_registered())
        self.assertTrue(guest2.is_logged_out())
        self.assertFalse(guest2.is_logged_in())

        # Invalid - user already exist
        self.assertFalse(guest1.register("not valid", "not valid"))
        self.assertEqual(guest1.get_nickname(), "valid")

    # @logger
    def test_login(self):
        # All Valid
        self.assertTrue(self.__user.login(self.__valid_name, self.__valid_password))
        self.assertTrue(self.__user.is_logged_in())
        self.assertFalse(self.__user.is_logged_out())

        self.__user.logout()

        # Invalid - username + whitespaces, valid password
        self.assertFalse(self.__user.login(self.__valid_name + " ", self.__valid_password))
        self.assertFalse(self.__user.is_logged_in())
        self.assertTrue(self.__user.is_logged_out())

        # Invalid - valid username, password + whitespaces
        self.assertFalse(self.__user.login(self.__valid_name, self.__valid_password + " "))
        self.assertFalse(self.__user.is_logged_in())
        self.assertTrue(self.__user.is_logged_out())

        # Invalid -username doesn't exist
        self.assertFalse(self.__user.login("self.__valid_name", self.__valid_password))
        self.assertFalse(self.__user.is_logged_in())
        self.assertTrue(self.__user.is_logged_out())

        # Invalid - incorrect password
        self.assertFalse(self.__user.login(self.__valid_name, "self.__valid_password"))
        self.assertFalse(self.__user.is_logged_in())
        self.assertTrue(self.__user.is_logged_out())

        registered = User()
        registered.register("Eytan", "Eytan's password")

        # Invalid - password of different registered user
        self.assertFalse(self.__user.login(self.__valid_name, "Eytan's password"))
        self.assertFalse(self.__user.is_logged_in())
        self.assertTrue(self.__user.is_logged_out())

        self.__user.login(self.__valid_name, self.__valid_password)

        # Invalid - user already logged in
        self.assertFalse(self.__user.login(self.__valid_name, self.__valid_password))
        self.assertTrue(self.__user.is_logged_in())
        self.assertFalse(self.__user.is_logged_out())

    # @logger
    def test_logout(self):
        self.__user.login(self.__valid_name, self.__valid_password)

        # All valid
        self.assertTrue(self.__user.logout())
        self.assertTrue(self.__user.is_logged_out())
        self.assertFalse(self.__user.is_logged_in())

        # Invalid - user is already logged out
        self.assertFalse(self.__user.logout())
        self.assertTrue(self.__user.is_logged_out())
        self.assertFalse(self.__user.is_logged_in())

        guest = User()

        # Invalid - user isn't register
        self.assertFalse(guest.logout())
        self.assertTrue(guest.is_logged_out())
        self.assertFalse(guest.is_logged_in())

    # @logger
    def test_check_password(self):
        # All valid
        self.assertTrue(self.__user.check_password(self.__valid_password))

        # Invalid password doesn't exist
        self.assertFalse(self.__user.check_password("self.__valid_password"))

        registered = User()
        registered.register("Eytan", "Eytan's password")

        # Invalid - password exist but isn't corresponding with the username
        self.assertFalse(registered.check_password(self.__valid_password))

    # @logger
    def test_check_nickname(self):
        # All valid
        self.assertTrue(self.__user.check_nickname(self.__valid_name))

        # Invalid password doesn't exist
        self.assertFalse(self.__user.check_nickname("self.__valid_password"))

        registered = User()
        registered.register("Eytan", "Eytan's password")

        # Invalid - password exist but isn't corresponding with the username
        self.assertFalse(registered.check_nickname(self.__valid_name))

    # @logger
    def test_is_logged_in(self):
        guest = User()
        subscriber = User()
        subscriber.register("Sub", "scriber")
        self.__user.login(self.__valid_name, self.__valid_password)

        # All valid
        self.assertTrue(self.__user.is_logged_in())

        # Not valid - user is logged out
        self.assertFalse(subscriber.is_logged_in())

        # Not valid - user isn't registered
        self.assertFalse(guest.is_logged_in())

    # @logger
    def test_is_logged_out(self):
        guest = User()
        subscriber = User()
        subscriber.register("Sub", "scriber")
        subscriber.login("Sub", "scriber")
        self.__user.logout()

        # All valid
        self.assertTrue(self.__user.is_logged_out())

        # Not valid - user is logged out
        self.assertFalse(subscriber.is_logged_out())

        # Not valid - user isn't registered
        self.assertTrue(guest.is_logged_out())

    # @logger
    def test_is_registered(self):
        guest = User()
        self.__user.logout()

        # All valid - user is registered
        self.assertTrue(self.__user.is_registered())

        # All valid - user isn't registered
        self.assertFalse(guest.is_registered())

    # @logger
    def test_get_nickname(self):
        guest = User()
        self.__user.logout()

        # All valid - user is registered
        self.assertEqual(self.__user.get_nickname(), self.__valid_name)

        # All valid - user isn't registered
        self.assertIsNone(guest.get_nickname())

    # @logger
    def test_save_products_to_basket(self):
        guest = User()

        # All valid- guest
        self.assertTrue(guest.save_products_to_basket(self.__products_to_add))
        self.assertEqual(1, len(guest.get_shopping_cart().get_store_basket(self.__store.get_name()).get_products()))
        products = [product_as_dictionary['product'] for product_as_dictionary in
                    guest.get_shopping_cart().get_store_basket(self.__store.get_name()).get_products()]
        self.assertIn(self.__product, products)

        # Valid - empty products
        self.assertTrue(guest.save_products_to_basket([]))
        self.assertEqual(1, len(guest.get_shopping_cart().get_store_basket(self.__store.get_name()).get_products()))
        products = [product_as_dictionary['product'] for product_as_dictionary in
                    guest.get_shopping_cart().get_store_basket(self.__store.get_name()).get_products()]
        self.assertIn(self.__product, products)

        # Invalid - product is None
        self.assertFalse(
            guest.save_products_to_basket([{"product": None, "store_name": self.__store.get_name(),
                                            "amount": 1, "discount_type": DiscountType.DEFAULT,
                                            "purchase_type": PurchaseType.DEFAULT}]))
        self.assertEqual(1, len(guest.get_shopping_cart().get_store_basket(self.__store.get_name()).get_products()))
        products = [product_as_dictionary['product'] for product_as_dictionary in
                    guest.get_shopping_cart().get_store_basket(self.__store.get_name()).get_products()]
        self.assertIn(self.__product, products)

        # Invalid - Edge case - quantity is zero
        self.assertFalse(
            guest.save_products_to_basket([{"product": self.__product, "store_name": self.__store.get_name(),
                                            "amount": 0, "discount_type": DiscountType.DEFAULT,
                                            "purchase_type": PurchaseType.DEFAULT}]))
        self.assertEqual(1, len(guest.get_shopping_cart().get_store_basket(self.__store.get_name()).get_products()))
        products = [product_as_dictionary['product'] for product_as_dictionary in
                    guest.get_shopping_cart().get_store_basket(self.__store.get_name()).get_products()]
        self.assertIn(self.__product, products)

        # Invalid - Negative quantity
        self.assertFalse(
            guest.save_products_to_basket([{"product": self.__product, "store_name": self.__store.get_name(),
                                            "amount": -11, "discount_type": DiscountType.DEFAULT,
                                            "purchase_type": PurchaseType.DEFAULT}]))
        self.assertEqual(1, len(guest.get_shopping_cart().get_store_basket(self.__store.get_name()).get_products()))
        products = [product_as_dictionary['product'] for product_as_dictionary in
                    guest.get_shopping_cart().get_store_basket(self.__store.get_name()).get_products()]
        self.assertIn(self.__product, products)

    # @logger
    def tearDown(self):
        # maybe delete the registered user resulted from this test
        pass

    def __repr__(self):
        return repr("UserTests")

    if __name__ == '__main__':
        unittest.main()
