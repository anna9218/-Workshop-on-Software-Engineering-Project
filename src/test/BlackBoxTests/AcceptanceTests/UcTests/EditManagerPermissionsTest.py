"""
    test class for use case 4.6 - edit managers' permissions
"""
from src.test.BlackBoxTests.AcceptanceTests.ProjectTest import ProjectTest


class EditManagerPermissionsTest(ProjectTest):

    # @logger
    def setUp(self) -> None:
        super().setUp()
        self.__appointee_name = "username2"
        self.__appointee_pass = "password2"
        self.subscribe_user(self.__appointee_name, self.__appointee_pass)
        self.register_user(self._username, self._password)
        self.login(self._username, self._password)
        self.open_store(self._store_name)
        self.appoint_additional_manager(self.__appointee_name, self._store_name, [])

    # @logger
    def test_success(self):
        res = self.edit_manager_permissions(self._store_name, self.__appointee_name, [])
        self.assertTrue(res)

    # @logger
    def test_fail(self):
        # store doesn't exist
        res = self.edit_manager_permissions("anotherStoreName", self.__appointee_name, [])
        self.assertFalse(res)
        # user doesn't exist
        res = self.edit_manager_permissions(self._store_name, "anotherUserName", [])
        self.assertFalse(res)
        # user isn't a manager of the store
        self.remove_manager(self._store_name, self.__appointee_name)
        res = self.edit_manager_permissions(self._store_name, self.__appointee_name, [])
        self.assertFalse(res)

    # @logger
    def tearDown(self) -> None:
        self.remove_store(self._store_name)
        self.delete_user(self._username)
        self.delete_manager(self.__appointee_name, self._store_name)
        self.delete_user(self.__appointee_name)

    def __repr__(self):
        return repr("EditManagerPermissionsTest")