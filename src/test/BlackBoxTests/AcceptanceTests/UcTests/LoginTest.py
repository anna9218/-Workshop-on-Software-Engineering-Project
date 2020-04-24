"""
    test class for use case 2.3 - login
"""
from src.test.BlackBoxTests.AcceptanceTests.ProjectTest import ProjectTest


class LoginTest(ProjectTest):

    def setUp(self) -> None:
        super().setUp()
        self.__valid_username = "username"
        self.__valid_pass = "password"
        self.__invalid_input = ""

    def test_success(self):
        res = self.login(self.__valid_username, self.__valid_pass)
        self.assertEqual(True, res)

    def test_fail(self):
        res = self.login(self.__valid_username, self.__invalid_input)
        self.assertEqual(False, res)

    def tearDown(self) -> None:
        pass
