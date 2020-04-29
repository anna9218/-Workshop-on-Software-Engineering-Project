"""
    test class for use case 2.3 - login
"""
from src.Logger import logger
from src.test.BlackBoxTests.AcceptanceTests.ProjectTest import ProjectTest


class LoginTest(ProjectTest):

    @logger
    def setUp(self) -> None:
        super().setUp()
        self.__username = "username"
        self.__password = "password"

    @logger
    def test_success(self):
        self.register_user("username", "password")
        res = self.login(self.__username, self.__password)
        self.assertEqual(True, res)

    @logger
    def test_fail(self):
        res = self.login(self.__username, self.__password)
        self.assertEqual(False, res)

    @logger
    def tearDown(self) -> None:
        self.remove_user("username")

    def __repr__(self):
        return repr("LoginTest")