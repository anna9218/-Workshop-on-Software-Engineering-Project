import unittest

from Backend.src.main.DomainLayer.UserComponent.User import User
from Backend.src.test.WhiteBoxTests.UnitTests.Stubs.StubProduct import StubProduct
from Backend.src.test.WhiteBoxTests.UnitTests.Stubs.StubRegistration import StubRegistration
from Backend.src.test.WhiteBoxTests.UnitTests.Stubs.StubShoppingCart import StubShoppingCart
from src.test.WhiteBoxTests.UnitTests.Stubs.StubStore import StubStore


class UserTests(unittest.TestCase):
    # @logger
    def setUp(self):
        # self.user.logoutState = StubLogout()
        self.__valid_name = "anna9218"
        self.__valid_pass = "password"
        self.__invalid_input = ""
        self.__product = StubProduct()
        self.__store = StubStore()
        self.__product_ls_to_add = [[self.__product, self.__store, 1]]  # products_stores_quantity_ls
        self.__user = User()
        self.__user.__registration = self.__user.set_registration_state(StubRegistration())
        # self.__user.__loginState = self.__user.set_login_state(StubLogin())
        self.__user.__shoppingCart = self.__user.set_shopping_cart(StubShoppingCart())

    # @logger
    def test_register(self):
        self.assertTrue(self.__user.register(self.__valid_name, self.__valid_pass))
        self.assertFalse(self.__user.register(self.__valid_name, self.__valid_pass))

    # @logger
    def test_login(self):
        self.__user.register(self.__valid_name, self.__valid_pass)
        self.assertTrue(self.__user.login(self.__valid_name, self.__valid_pass))
        self.assertFalse(self.__user.login(self.__invalid_input, self.__invalid_input))

    # @logger
    def test_logout(self):
        self.__user.register(self.__valid_name, self.__valid_pass)
        self.__user.login(self.__valid_name, self.__valid_pass)
        self.assertTrue(self.__user.logout())

    # @logger
    def test_check_password(self):
        self.__user.register(self.__valid_name, self.__valid_pass)
        self.assertTrue(self.__user.check_password(self.__valid_pass))
        self.assertFalse(self.__user.check_password(self.__invalid_input))

    # @logger
    def test_check_nickname(self):
        self.__user.register(self.__valid_name, self.__valid_pass)
        self.assertTrue(self.__user.check_nickname(self.__valid_name))
        self.assertFalse(self.__user.check_nickname(self.__invalid_input))

    # @logger
    def test_is_logged_in(self):
        self.__user.register(self.__valid_name, self.__valid_pass)
        self.assertFalse(self.__user.is_logged_in())
        self.__user.login(self.__valid_name, self.__valid_pass)
        self.assertTrue(self.__user.is_logged_in())

    # @logger
    def test_is_logged_out(self):
        self.__user.register(self.__valid_name, self.__valid_pass)
        self.assertTrue(self.__user.is_logged_out())
        self.__user.login(self.__valid_name, self.__valid_pass)
        self.assertFalse(self.__user.is_logged_out())

    # @logger
    def test_is_registered(self):
        self.assertFalse(self.__user.is_registered())
        self.__user.register(self.__valid_name, self.__valid_pass)
        self.assertTrue(self.__user.is_registered())

    # @logger
    def test_get_nickname(self):
        self.__user.register(self.__valid_name, self.__valid_pass)
        self.assertEqual(self.__user.get_nickname(), self.__valid_name, "")
        self.assertNotEqual(self.__user.get_nickname(), self.__invalid_input, "")

    # @logger
    def test_save_products_to_basket(self):
        # test for guest
        self.assertTrue(self.__user.save_products_to_basket(self.__product_ls_to_add))
        # test for subscriber
        self.__user.register(self.__valid_name, self.__valid_pass)
        self.assertTrue(self.__user.save_products_to_basket(self.__product_ls_to_add))

    # @logger
    def tearDown(self):
        # maybe delete the registered user resulted from this test
        pass

    def __repr__(self):
        return repr("UserTests")

    if __name__ == '__main__':
        unittest.main()

