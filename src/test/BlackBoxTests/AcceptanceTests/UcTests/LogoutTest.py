"""
    test class for use case 3.1 - logout
"""
from src.Logger import logger
from src.test.BlackBoxTests.AcceptanceTests.ProjectTest import ProjectTest


class LogoutTest(ProjectTest):

    @logger
    def setUp(self) -> None:
        super().setUp()
        self.__valid_username = "username"
        self.__valid_password = "password"
        self.__invalid_input = ""

    @logger
    def test_success(self):
        self.register_user(self.__valid_username, self.__valid_password)
        self.login(self.__valid_username, self.__valid_password)
        res = self.logout()
        self.assertEqual(True, res)

    @logger
    def test_fail(self):
        self.register_user(self.__valid_username, self.__valid_password)
        res = self.logout()
        self.assertEqual(False, res)

    @logger
    def tearDown(self) -> None:
        self.remove_user(self.__valid_username)

    def __repr__(self):
        return repr("LogoutTest")