"""
    test class for use case 4.7 - remove store manager
"""
from src.test.BlackBoxTests.AcceptanceTests.ProjectAT import ProjectAT


class RemoveStoreManagerTest(ProjectAT):
    def setUp(self) -> None:
        super().setUp()
        self.__appointee_name = "username2"
        self.__appointee_pass = "password2"
        self.subscribe_user(self.__appointee_name, self.__appointee_pass)
        self.register_user(self._username, self._password)
        self.login(self._username, self._password)
        self.open_store(self._store_name)
        self.appoint_additional_manager(self.__appointee_name, self._store_name, [])

    def test_success(self):
        # valid details
        res = self.remove_manager(self._store_name, self.__appointee_name)
        self.assertTrue(res)

    def test_fail(self):
        # store doesn't exist
        res = self.remove_manager("someOtherStore", self.__appointee_name)
        self.assertFalse(res)
        # appointee doesn't exist
        res = self.remove_manager(self._store_name, "imaginaryAppointee")
        self.assertFalse(res)
        # appointee isn't the manager of the store
        self.remove_manager(self._store_name, self.__appointee_name)
        res = self.remove_manager(self._store_name, self.__appointee_name)
        self.assertFalse(res)

    def tearDown(self) -> None:
        self.remove_store(self._store_name)
        self.delete_user(self._username)
        self.delete_manager(self.__appointee_name, self._store_name)
        self.delete_user(self.__appointee_name)

    def __repr__(self):
        return repr("RemoveStoreManagerTest")