"""
    test class for use case 2.2 - registration
"""
from src.test.BlackBoxTests.AcceptanceTests.ProjectAT import ProjectAT


class RegisterTest(ProjectAT):
    def setUp(self) -> None:
        super().setUp()

    def test_success(self):
        # valid input details
        res = self.register_user(self._username, self._password)
        self.assertTrue(res['response'])

    def test_fail(self):
        # valid username + invalid password
        res = self.register_user(self._username, "")
        self.assertFalse(res['response'])
        # invalid username + valid password
        res = self.register_user("", self._password)
        self.assertFalse(res['response'])
        # username already registered in the system
        self.register_user(self._username, self._password)
        res = self.register_user(self._username, "somePassword")
        self.assertFalse(res['response'])

    def tearDown(self) -> None:
        self.delete_user(self._username)

    def __repr__(self):
        return repr("RegisterTest")