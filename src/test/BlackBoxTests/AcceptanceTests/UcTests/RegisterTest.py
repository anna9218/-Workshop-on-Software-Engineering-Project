"""
    test class for use case 2.2 - registration
"""
from src.test.BlackBoxTests.AcceptanceTests.ProjectTest import ProjectTest


class RegisterTest(ProjectTest):

    def setUp(self) -> None:
        self.username = "username"
        self.good_pass = "pass1234"
        self.bad_pass = " "

    # register function should be checked with DB or stub
    def test_success(self):
        res = self.register_user(self.username, self.good_pass)
        self.assertEqual(res, "registered successfully")

    def test_fail(self):
        res = self.register_user(self.username, self.bad_pass)
        self.assertEqual(res, "something failed, please try again")

    def test_fatal_error(self):
        self.reusableTests.test_server_error()

    def tearDown(self) -> None:
        pass
