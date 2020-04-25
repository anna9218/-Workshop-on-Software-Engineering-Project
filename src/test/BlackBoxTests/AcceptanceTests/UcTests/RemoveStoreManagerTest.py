"""
    test class for use case 4.7 - remove store manager
"""
from src.test.BlackBoxTests.AcceptanceTests.ProjectTest import ProjectTest


class RemoveStoreManagerTest(ProjectTest):

    def setUp(self) -> None:
        super().setUp()
        self.__appointer_name = "username1"
        self.__appointer_pass = "password1"
        self.__appointee_name = "username2"
        self.__appointee_pass = "password2"
        self.register_user(self.__appointee_name, self.__appointee_pass)
        self.__store = "store"

    def test_success(self):
        self.register_user(self.__appointer_name, self.__appointer_pass)
        self.login(self.__appointer_name, self.__appointer_pass)
        self.open_store(self.__store)
        self.appoint_additional_manager(self.__appointee_name, self.__store, [])
        res = self.remove_manager(self.__store, self.__appointee_name, [])
        self.assertEqual(True, res)

    def test_fail(self):
        self.remove_user(self.__appointee_name)
        self.register_user(self.__appointer_name, self.__appointer_pass)
        self.login(self.__appointer_name, self.__appointer_pass)
        self.open_store(self.__store)
        res = self.remove_manager(self.__store, self.__appointee_name, [])
        self.assertEqual(False, res)

    def tearDown(self) -> None:
        self.remove_user(self.__appointer_name)
        self.teardown_store(self.__store)

