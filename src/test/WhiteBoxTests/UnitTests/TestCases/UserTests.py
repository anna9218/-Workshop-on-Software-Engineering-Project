import unittest

from src.main.DomainLayer.User import User
from src.test.WhiteBoxTests.UnitTests.Stubs.StubLogin import StubLogin
from src.test.WhiteBoxTests.UnitTests.Stubs.StubProduct import StubProduct
from src.test.WhiteBoxTests.UnitTests.Stubs.StubRegistration import StubRegistration


class UserTests(unittest.TestCase):
    def setUp(self):
        # self.user.logoutState = StubLogout()
        self.__valid_name = "anna9218"
        self.__valid_pass = "password"
        self.__invalid_input = ""
        self.__product = StubProduct()
        self.__product_ls_to_add = [[]]
        self.__user = User()
        self.__user.__registration = StubRegistration()
        self.__user.__loginState = StubLogin()
        # self.trade = TradeControl()
        # self.__user = User(self.trade)
        # self.user.logoutState = StubLogout()

    def test_register(self):
        self.assertTrue(self.__user.register(self.__valid_name, self.__valid_pass))

    def test_login(self):
        self.__user.register(self.__valid_name, self.__valid_pass)
        self.assertTrue(self.__user.login(self.__valid_name, self.__valid_pass))
        self.assertFalse(self.__user.login(self.__invalid_input, self.__invalid_input))

    def test_logout(self):
        self.__user.register(self.__valid_name, self.__valid_pass)
        self.__user.login(self.__valid_name, self.__valid_pass)
        self.assertTrue(self.__user.logout())

    def test_check_password(self):
        self.__user.register(self.__valid_name, self.__valid_pass)
        self.assertTrue(self.__user.check_password(self.__valid_pass))
        self.assertFalse(self.__user.check_password(self.__invalid_input))

    def test_check_nickname(self):
        self.__user.register(self.__valid_name, self.__valid_pass)
        self.assertTrue(self.__user.check_nickname(self.__valid_name))
        self.assertFalse(self.__user.check_nickname(self.__invalid_input))

    def test_is_logged_in(self):
        self.__user.register(self.__valid_name, self.__valid_pass)
        self.assertFalse(self.__user.is_logged_in())
        self.__user.login(self.__valid_name, self.__valid_pass)
        self.assertTrue(self.__user.is_logged_in())

    def test_is_logged_out(self):
        self.__user.register(self.__valid_name, self.__valid_pass)
        self.assertTrue(self.__user.is_logged_out())
        self.__user.login(self.__valid_name, self.__valid_pass)
        self.assertFalse(self.__user.is_logged_out())

    def test_is_registered(self):
        self.assertFalse(self.__user.is_registered())
        self.__user.register(self.__valid_name, self.__valid_pass)
        self.assertTrue(self.__user.is_registered())

    def test_get_nickname(self):
        self.__user.register(self.__valid_name, self.__valid_pass)
        self.assertEqual(self.__user.get_nickname(), self.__valid_name, "")
        self.assertNotEqual(self.__user.get_nickname(), self.__invalid_input, "")

    # def test_save_products_to_basket(self):
    #     self.__user.register(self.__valid_name, self.__valid_pass)
    #     self.__user.save_products_to_basket()

    # def test_view_shopping_cart(self):
    #
    # def test_remove_from_shopping_cart(self):
    #
    # def test_update_quantity_in_shopping_cart(self):

    def tearDown(self):
        # maybe delete the registered user resulted from this test
        pass

    if __name__ == '__main__':
        unittest.main()
