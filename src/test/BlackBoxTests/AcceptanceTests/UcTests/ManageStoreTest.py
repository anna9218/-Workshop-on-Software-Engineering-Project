"""
    test class for use case 5.1 - check that manager can activated actions he has permissions to
"""
from src.test.BlackBoxTests.AcceptanceTests.ProjectTest import ProjectTest


class ManageStoreTest(ProjectTest):

    def setUp(self) -> None:
        super().setUp()
        self.subscribe_user("newManager", "newPassword")
        self.register_user(self._username, self._password)
        self.login(self._username, self._password)
        self.open_store(self._store_name)
        self.add_products_to_store(self._store_name,
                                   [{"name": "product", "price": 10, "category": "general", "amount": 10}])
        self.appoint_additional_manager("newManager", self._store_name, [3])
        self.logout()
        self.set_user("newManager")
        self.login("newManager", "newPassword")

    def test_success(self):
        self.subscribe_user("newUser", "newerPassword")
        # manager with permission to add owner
        res = self.appoint_additional_owner("newUser", self._store_name)
        self.assertTrue(res)

    def test_fail(self):
        # manager without permissions
        self.edit_manager_permissions(self._store_name, self._username, [])
        res = self.edit_products_in_store(self._store_name, "product", "price", "100")
        self.assertFalse(res['response'])

    def tearDown(self) -> None:
        self.logout()
        self.update_shopping_cart("remove",
                                  [{"product_name": "product", "store_name": self._store_name, "amount": 10}])
        self.remove_products_from_store(self._store_name, ["product"])
        self.remove_store("store")
        self.delete_user(self._username)
        self.delete_manager("newManager", self._store_name)
        # self.delete_user("newManager")
        # self.delete_user("newUser")

    def __repr__(self):
        return repr("ManageStoreTest")