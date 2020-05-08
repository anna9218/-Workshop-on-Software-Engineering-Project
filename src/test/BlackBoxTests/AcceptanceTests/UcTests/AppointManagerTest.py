"""
    test class for use case 4.5 - appoint additional store manager
"""
from src.Logger import logger
from src.test.BlackBoxTests.AcceptanceTests.ProjectTest import ProjectTest


class AppointManagerTest(ProjectTest):

    # @logger
    def setUp(self) -> None:
        super().setUp()
        self.__appointee_name = "otherUsername"
        self.__appointee_pass = "otherPassword"
        self.subscribe_user(self.__appointee_name, self.__appointee_pass)
        self.register_user(self._username, self._password)
        self.login(self._username, self._password)
        self.open_store(self._store_name)

    # @logger
    def test_success(self):
        # all valid details
        res = self.appoint_additional_manager(self.__appointee_name, self._store_name, [])
        self.assertTrue(res)

    # @logger
    def test_fail(self):
        # store doesn't exist
        res = self.appoint_additional_manager(self.__appointee_name, "someStoreName", [])
        self.assertFalse(res)
        # user doesn't exist
        res = self.appoint_additional_manager("someUser", self._store_name, [])
        self.assertFalse(res)
        # user isn't registered
        self.delete_user(self.__appointee_name)
        res = self.appoint_additional_manager(self.__appointee_name, self._store_name, [])
        self.assertFalse(res)

    # @logger
    def tearDown(self) -> None:
        self.delete_user(self._username)
        self.remove_store(self._store_name)

    def __repr__(self):
        return repr("AppointManagerTest")