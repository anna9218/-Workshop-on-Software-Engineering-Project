"""
    test class for use case 3.3 - open store
"""
from src.test.BlackBoxTests.AcceptanceTests.ProjectTest import ProjectTest


class OpenStoreTest(ProjectTest):

    def setUp(self) -> None:
        super().setUp()
        self.__username = "username"
        self.__password = "password"
        self.__store_name = "store"

    def test_success(self):
        self.register_user(self.__username, self.__password)
        self.login(self.__username, self.__password)
        res = self.open_store(self.__store_name)
        self.assertEqual(True, res)

    def test_fail(self):
        self.register_user(self.__username, self.__password)
        self.login(self.__username, self.__password)
        self.open_store(self.__store_name)
        res = self.open_store(self.__store_name)
        self.assertEqual(False, res)

    def tearDown(self) -> None:
        self.remove_user(self.__username)
        self.teardown_store(self.__store_name)
