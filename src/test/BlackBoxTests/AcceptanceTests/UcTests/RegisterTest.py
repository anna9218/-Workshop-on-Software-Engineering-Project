"""
    test class for use case 2.2 - registration
"""
from src.Logger import logger
from src.test.BlackBoxTests.AcceptanceTests.ProjectTest import ProjectTest


class RegisterTest(ProjectTest):
    # @logger
    def setUp(self) -> None:
        super().setUp()

    # @logger
    def test_success(self):
        # valid input details
        res = self.register_user(self._username, self._password)
        self.assertTrue(res)

    # @logger
    def test_fail(self):
        # valid username + invalid password
        res = self.register_user(self._username, "")
        self.assertFalse(res)
        # invalid username + valid password
        res = self.register_user("", self._password)
        self.assertFalse(res)
        # username already registered in the system
        self.register_user(self._username, self._password)
        res = self.register_user(self._username, "somePassword")
        self.assertFalse(res)

    # @logger
    def tearDown(self) -> None:
        self.delete_user(self._username)

    def __repr__(self):
        return repr("RegisterTest")