"""
    test class for use case 2.2 - registration
"""
from src.test.BlackBoxTests.AcceptanceTests.ProjectTest import ProjectTest


class RegisterTest(ProjectTest):

    def setUp(self) -> None:
        super().setUp()
        self.__valid_username = "username"
        self.__valid_pass = "password"
        self.__invalid_input = ""

    def test_success(self):
        res = self.register_user(self.__valid_username, self.__valid_pass)
        self.assertEqual(res, True)

    def test_fail(self):
        res = self.register_user(self.__valid_username, self.__invalid_input)
        self.assertEqual(res, False)

    def tearDown(self) -> None:
        self.remove_user("username")
