"""
    test class for use case 3.1 - logout
"""
from src.test.BlackBoxTests.AcceptanceTests.ProjectAT import ProjectAT


class LogoutTest(ProjectAT):

    # @logger
    def setUp(self) -> None:
        super().setUp()
        self.register_user(self._username, self._password)
        self.login(self._username, self._password)

    # @logger
    def test_success(self):
        res = self.logout()
        self.assertTrue(res)

    # @logger
    def test_fail(self):
        # user not logged in
        self.logout()
        res = self.logout()
        self.assertFalse(res['response'])

    # @logger
    def tearDown(self) -> None:
        self.delete_user(self._username)

    def __repr__(self):
        return repr("LogoutTest")