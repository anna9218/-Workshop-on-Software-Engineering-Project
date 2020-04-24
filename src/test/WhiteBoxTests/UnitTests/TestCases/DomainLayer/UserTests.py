import unittest

from src.main.DomainLayer.User import User
from src.main.DomainLayer.Store import Store
from src.test.WhiteBoxTests.UnitTests.Stubs.StubLogin import StubLogin
from src.test.WhiteBoxTests.UnitTests.Stubs.StubLogout import StubLogout
from src.test.WhiteBoxTests.UnitTests.Stubs.StubRegistration import StubRegistration
from src.main.DomainLayer.TradeControl import TradeControl
from src.test.WhiteBoxTests.UnitTests.Stubs.StubTradeControl import StubTradeControl
from src.test.WhiteBoxTests.UnitTests.TestCases.ReUsableTests import ReUsableTests


class UserTests(ReUsableTests):

    def setUp(self):
        # self.user.logoutState = StubLogout()
        self.__valid_name = "anna9218"
        self.__valid_pass = "password"
        self.__invalid_input = ""
        super().set_up_user()
        pass

    def test_register(self):
        # register with valid input
        super().test_register(self.__valid_name, self.__valid_pass)




    #     self.user.get_registration().register(self, "anna9218", "password")
    #     self.assertTrue(self.user.get_registration().isRegistered)
    #
    #     # check that it's not possible to register again with same credentials
    #     self.user.get_registration().register(self, "anna9218", "password")
    #     self.assertFalse(self.user.get_registration().isRegistered)
    #
    # def test_login(self):
    #     # "anna9218", "password" -> registered user, should login successfully
    #     self.user.get_login().login(self, "anna9218", "password")
    #     self.assertTrue(self.user.get_login().isLoggedIn)
    #
    # def test_login_fail(self):
    #     # "anna", "password" -> not a registered user, login should fail
    #     self.assertFalse(self.user.get_login().login(self, "anna", "password"))
    #
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
