"""
    test class for use case 4.3 - appoint additional store owner
"""
from src.test.BlackBoxTests.AcceptanceTests.ProjectAT import ProjectAT


class AppointOwnerTest(ProjectAT):

    def setUp(self) -> None:
        super().setUp()
        self.__appointee_name = "username2"
        self.__appointee_pass = "password2"
        self.subscribe_user(self.__appointee_name, self.__appointee_pass)
        self.register_user(self._username, self._password)
        self.login(self._username, self._password)
        self.open_store(self._store_name)

    def test_success(self):
        # valid details
        res = self.appoint_additional_owner(self.__appointee_name, self._store_name)
        self.assertTrue(res)

    def test_fail(self):
        # store doesn't exist
        res = self.appoint_additional_owner(self.__appointee_name, "someOtherStore")
        self.assertFalse(res['response'])
        # appointee doesn't exist
        res = self.appoint_additional_owner("imaginaryAppointee", self._store_name)
        self.assertFalse(res['response'])
        # appointee is already store owner of the shop
        self.appoint_additional_owner(self.__appointee_name, self._store_name)
        res = self.appoint_additional_owner(self.__appointee_name, self._store_name)
        self.assertFalse(res['response'])
        # appointee isn't registered
        self.delete_user(self.__appointee_name)
        res = self.appoint_additional_owner(self.__appointee_name, self._store_name)
        self.assertFalse(res['response'])

    def tearDown(self) -> None:
        self.remove_store(self._store_name)
        self.delete_user(self._username)

    def __repr__(self):
        return repr("AppointOwnerTest")