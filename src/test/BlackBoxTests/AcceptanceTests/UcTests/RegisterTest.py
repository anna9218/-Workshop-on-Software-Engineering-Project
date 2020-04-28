"""
    test class for use case 2.2 - registration
"""
from src.Logger import logger
from src.test.BlackBoxTests.AcceptanceTests.ProjectTest import ProjectTest


class RegisterTest(ProjectTest):
    @logger
    def setUp(self) -> None:
        super().setUp()
        self.__valid_username = "username"
        self.__valid_pass = "password"
        self.__invalid_input = ""

    @logger
    def test_success(self):
        res = self.register_user(self.__valid_username, self.__valid_pass)
        self.assertEqual(res, True)

    @logger
    def test_fail(self):
        res = self.register_user(self.__valid_username, self.__invalid_input)
        self.assertEqual(res, False)

    @logger
    def tearDown(self) -> None:
        self.remove_user("username")
