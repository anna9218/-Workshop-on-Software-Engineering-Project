"""
    test class for use case 2.3 - login
"""
from Backend.src.Logger import logger
from Backend.src.test.BlackBoxTests.AcceptanceTests.ProjectTest import ProjectTest


class LoginTest(ProjectTest):

    # @logger
    def setUp(self) -> None:
        super().setUp()
        self.register_user(self._username, self._password)

    # @logger
    def test_success(self):
        # valid input + registered user
        res = self.login(self._username, self._password)
        self.assertTrue(res)

    # @logger
    def test_fail(self):
        # registered user + valid username + invalid password
        res = self.login(self._username, "")
        self.assertFalse(res)
        # registered user + invalid username + valid password
        res = self.login("", self._password)
        self.assertFalse(res)
        # not a registered user + valid input
        res = self.login("someOtherUser", "someOtherPassword")
        self.assertFalse(res)

    # @logger
    def tearDown(self) -> None:
        self.delete_user(self._username)

    def __repr__(self):
        return repr("LoginTest")