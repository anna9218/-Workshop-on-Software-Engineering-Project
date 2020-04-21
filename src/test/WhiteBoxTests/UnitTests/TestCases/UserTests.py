import unittest

from src.main.DomainLayer.User import User
from src.test.WhiteBoxTests.UnitTests.Stubs.StubRegistration import StubRegistration


class UserTests(unittest.TestCase):
    def setUp(self):
        self.user = User()
        self.user.registration = StubRegistration()

    def test_register(self):
        self.user.registration.register(self, "anna9218", "password")
        self.assertTrue(self.user.registration.isRegistered)

        # check that it's not possible to register again with same credentials
        self.user.registration.register(self, "anna9218", "password")
        self.assertFalse(self.user.registration.isRegistered)

    def tearDown(self):
        pass
