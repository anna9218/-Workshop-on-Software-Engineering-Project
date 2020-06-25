"""
    test class for use case 4.5 - appoint additional store manager
"""
from src.test.BlackBoxTests.AcceptanceTests.ProjectAT import ProjectAT


class AppointManagerTest(ProjectAT):

    def setUp(self) -> None:
        super().setUp()
        self.__appointee_name = "otherUsername"
        self.__appointee_pass = "otherPassword"
        self.subscribe_user(self.__appointee_name, self.__appointee_pass)
        self.register_user(self._username, self._password)
        self.login(self._username, self._password)
        self.open_store(self._store_name)

    def test_success(self):
        # all valid details
        res = self.appoint_additional_manager(self.__appointee_name, self._store_name, [])
        self.assertTrue(res)

    def test_fail(self):
        # store doesn't exist
        res = self.appoint_additional_manager(self.__appointee_name, "someStoreName", [])
        self.assertFalse(res['response'])
        # user doesn't exist
        res = self.appoint_additional_manager("someUser", self._store_name, [])
        self.assertFalse(res['response'])
        # user isn't registered
        self.delete_user(self.__appointee_name)
        res = self.appoint_additional_manager(self.__appointee_name, self._store_name, [])
        self.assertFalse(res['response'])

    def tearDown(self) -> None:
        self.remove_store(self._store_name)
        self.delete_user(self._username)
        self.delete_user(self.__appointee_name)

    def __repr__(self):
        return repr("AppointManagerTest")
