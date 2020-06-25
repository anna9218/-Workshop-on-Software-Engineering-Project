"""
    test class for use case 4.4 - remove store owner
"""
from src.test.BlackBoxTests.AcceptanceTests.ProjectAT import ProjectAT

#TODO: wait for merge with updated add owner


class RemoveStoreOwnerTest(ProjectAT):
    def setUp(self) -> None:
        super().setUp()
        self.__appointee_name = "username2"
        self.__appointee_pass = "password2"
        self.subscribe_user(self.__appointee_name, self.__appointee_pass)
        self.register_user(self._username, self._password)
        self.login(self._username, self._password)
        self.open_store(self._store_name)
        self.appoint_additional_owner(self.__appointee_name, self._store_name)

    def test_success(self):
        # valid details

        # self.user appoints owner1 and manager0
        self.subscribe_user("owner1", "password")
        self.register_user("owner1", "password")
        self.appoint_additional_owner("owner1",  self._store_name)
        self.subscribe_user("manager0", "password")
        self.register_user("manager0", "password")
        self.appoint_additional_manager("manager0", self._store_name, [])

        # owner1 appoints owner2 and manager1
        self.login("owner1", "password")
        self.subscribe_user("owner2", "password")
        self.register_user("owner2", "password")
        self.appoint_additional_owner("owner2",  self._store_name)
        self.subscribe_user("manager1", "password")
        self.register_user("manager1", "password")
        self.appoint_additional_manager("manager1", self._store_name, [])

        # owner2 appoints owner3 and manager2
        self.login("owner2", "password")
        self.subscribe_user("owner3", "password")
        self.register_user("owner3", "password")
        self.appoint_additional_owner("owner3", self._store_name)
        self.subscribe_user("owner5", "password")
        self.register_user("owner5", "password")
        self.appoint_additional_owner("owner5", self._store_name)
        self.subscribe_user("manager2", "password")
        self.register_user("manager2", "password")
        self.appoint_additional_manager("manager2", self._store_name, [])

        # owner3 appoints manager3 and manager4
        self.login("owner3", "password")

        self.subscribe_user("manager3", "password")
        self.register_user("manager3", "password")
        self.subscribe_user("manager4", "password")
        self.register_user("manager4", "password")
        self.appoint_additional_manager("manager3", self._store_name, [])
        self.appoint_additional_manager("manager4", self._store_name, [])

        # self.user removes owner1 as a store owner
        self.login(self._username, self._password)
        res = self.remove_owner("owner1", self._store_name)
        self.assertEqual(res['response'], ['owner1 removed as owner', 'owner2 removed as owner', 'owner3 removed as owner',
                                           'manager3 removed as manager', 'manager4 removed as manager',
                                           'owner5 removed as owner', 'manager2 removed as manager', 'manager1 removed as manager'])
        self.assertEqual(res['msg'], "Store owner owner1 and his appointees were removed successfully.")

        store = self.get_store(self._store_name)
        self.assertTrue(store.is_manager("manager0"))
        self.assertFalse(store.is_manager("manager1"))
        self.assertFalse(store.is_manager("manager2"))
        self.assertFalse(store.is_manager("manager3"))
        self.assertFalse(store.is_manager("manager4"))
        self.assertTrue(store.is_owner(self.__appointee_name))
        self.assertTrue(store.is_owner(self._username))
        self.assertFalse(store.is_owner("owner1"))
        self.assertFalse(store.is_owner("owner2"))
        self.assertFalse(store.is_owner("owner3"))
        self.assertFalse(store.is_owner("owner5"))

    def test_fail(self):
        # appointee doesn't exist
        res = self.remove_owner("ownerDoesntExist", self._store_name)
        self.assertEqual(res['response'], [])
        self.assertEqual(res['msg'], "Error! remove store owner failed.")

        # store doesn't exist
        res = self.remove_owner(self.__appointee_name, "someOtherStore")
        self.assertEqual(res['response'], [])
        self.assertEqual(res['msg'], "Error! remove store owner failed.")

        # appointee isn't the owner of the store
        self.remove_owner(self._store_name, self.__appointee_name)
        res = self.remove_owner(self._store_name, self.__appointee_name)
        self.assertEqual(res['response'], [])
        self.assertEqual(res['msg'], "Error! remove store owner failed.")

    def tearDown(self) -> None:
        self.remove_store(self._store_name)
        self.delete_user(self._username)
        self.delete_manager(self.__appointee_name, self._store_name)
        self.delete_user("owner1")
        self.delete_user("owner2")
        self.delete_user("owner3")
        self.delete_user("owner5")
        self.delete_user("manager0")
        self.delete_user("manager1")
        self.delete_user("manager2")
        self.delete_user("manager3")
        self.delete_user("manager4")
        self.delete_user(self.__appointee_name)

    def __repr__(self):
        return repr("RemoveStoreManagerTest")