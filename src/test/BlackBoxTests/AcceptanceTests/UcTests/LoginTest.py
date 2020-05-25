"""
    test class for use case 2.3 - login
"""
from src.test.BlackBoxTests.AcceptanceTests.ProjectTest import ProjectTest


class LoginTest(ProjectTest):

    # @logger
    def setUp(self) -> None:
        super().setUp()
        self.register_user(self._username, self._password)

    # @logger
    def test_success(self):
        # valid input + registered user
        res = self.login(self._username, self._password)
        self.assertTrue(res['response'])

    # @logger
    def test_fail(self):
        # registered user + valid username + invalid password
        res = self.login(self._username, "")
        self.assertFalse(res['response'])
        # registered user + invalid username + valid password
        res = self.login("", self._password)
        self.assertFalse(res['response'])
        # not a registered user + valid input
        res = self.login("someOtherUser", "someOtherPassword")
        self.assertFalse(res['response'])

    # @logger
    def tearDown(self) -> None:
        self.delete_user(self._username)

    def __repr__(self):
        return repr("LoginTest")