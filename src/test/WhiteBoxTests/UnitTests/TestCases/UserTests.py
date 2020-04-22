import unittest

from src.main.DomainLayer.User import User
from src.test.WhiteBoxTests.UnitTests.Stubs.StubLogin import StubLogin
from src.test.WhiteBoxTests.UnitTests.Stubs.StubLogout import StubLogout
from src.test.WhiteBoxTests.UnitTests.Stubs.StubRegistration import StubRegistration


class UserTests(unittest.TestCase):
    def setUp(self):
        self.user = User()
        self.user.registration = StubRegistration()
        self.user.loginState = StubLogin()
        self.user.logoutState = StubLogout()

    def test_register(self):
        self.user.registration.register(self, "anna9218", "password")
        self.assertTrue(self.user.registration.isRegistered)

        # check that it's not possible to register again with same credentials
        self.user.registration.register(self, "anna9218", "password")
        self.assertFalse(self.user.registration.isRegistered)

    def test_login(self):
        # "anna9218", "password" -> registered user, should login successfully
        self.user.loginState.login(self, "anna9218", "password")
        self.assertTrue(self.user.loginState.isLoggedIn)

    def test_login_fail(self):
        # "anna", "password" -> not a registered user, login should fail
        self.assertFalse(self.user.loginState.login(self, "anna", "password"))

    def test_logout(self):
        # "anna9218", "password" -> logged in user, should logout successfully
        self.user.logoutState.logout(self)
        self.assertTrue(self.user.logoutState.isLoggedOut)

    def tearDown(self):
        # maybe delete the registered user resulted from this test
        pass
