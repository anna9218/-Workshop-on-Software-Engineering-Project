import unittest

from src.main.DomainLayer.User import User
from src.test.WhiteBoxTests.UnitTests.Stubs.StubLogin import StubLogin
from src.test.WhiteBoxTests.UnitTests.Stubs.StubRegistration import StubRegistration


class UserTests(unittest.TestCase):
    def setUp(self):
        # self.user.logoutState = StubLogout()
        self.__valid_name = "anna9218"
        self.__valid_pass = "password"
        self.__invalid_input = ""
        self.__user = User()
        self.__user.__registration = StubRegistration()
        self.__user.__loginState = StubLogin()

        # self.trade = TradeControl()
        # self.__user = User(self.trade)
        # self.user.logoutState = StubLogout()

    def test_register(self):
        # register with valid input
        self.__user.register(self.__valid_name, self.__valid_pass)
        self.assertTrue(self.__user.is_registered)

    def test_login(self):
        # "anna9218", "password" -> registered user, should login successfully
        self.__user.login(self.__valid_name, self.__valid_pass)
        self.assertTrue(self.__user.is_logged_in())

        self.__user.login(self.__invalid_input, self.__invalid_input)
        self.assertFalse(self.__user.is_logged_in())

    # def test_logout(self):
    #     # "anna9218", "password" -> logged in user, should logout successfully
    #     self.user.get_logout().logout(self)
    #     self.assertTrue(self.user.get_logout().isLoggedOut)
    #
    # def test_open_store_success(self):
    #     self.user.get_registration().register(self, "anna9218", "password")
    #     self.trade.get_stores().append(Store("eden's store"))

    def tearDown(self):
        # maybe delete the registered user resulted from this test
        pass

    if __name__ == '__main__':
        unittest.main()
