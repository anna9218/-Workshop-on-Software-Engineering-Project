"""
    test class for use case 3.2 - open store
"""
from Backend.src.Logger import logger
from Backend.src.test.BlackBoxTests.AcceptanceTests.ProjectTest import ProjectTest


class OpenStoreTest(ProjectTest):
    # @logger
    def setUp(self) -> None:
        super().setUp()
        self.register_user(self._username, self._password)
        self.login(self._username, self._password)

    # @logger
    def test_success(self):
        # valid store name that doesn't exist in the system
        res = self.open_store(self._store_name)
        self.assertTrue(res)

    # @logger
    def test_fail(self):
        # valid store name + store name already exist in the system
        self.open_store(self._store_name)
        res = self.open_store(self._store_name)
        self.assertFalse(res)
        self.remove_store(self._store_name)
        # invalid store name
        res = self.open_store("")
        self.assertFalse(res)

    # @logger
    def tearDown(self) -> None:
        self.delete_user(self._username)
        self.remove_store(self._store_name)

    def __repr__(self):
        return repr("OpenStoreTest")