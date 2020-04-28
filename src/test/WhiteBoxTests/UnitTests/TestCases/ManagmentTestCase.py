import unittest

# from src.main.DomainLayer import ManagerPermission
from src.main.DomainLayer.ManagerPermission import ManagerPermission
from src.main.DomainLayer.Store import Store
from src.main.DomainLayer.User import User
from src.main.ServiceLayer.StoreManagerRole import StoreManagerRole
from src.main.ServiceLayer.StoreOwnerRole import StoreOwnerRole


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self._store = Store("s_name")
        self._owner = User()
        self._owner.register("username", "1234")
        self._owner.login("username", "1234")
        self._store.add_owner("", self._owner)
        self._owner.get_appointment().appoint_manager(self._store)
        self._manager = User()
        self._manager.register("manager", "1234")
        self._manager.login("manager", "1234")

    def test_add_new_manager(self):
        # ser = StoreOwnerRole()
        # ser.appoint_new_store_manager(self._owner.get_nickname(), self._store.get_name(), self._manager.get_nickname())
        self.assertEqual(True, self._store.add_manager(self._manager))
        self._manager.get_appointment().appoint_manager(self._store)
        self._manager.get_appointment().add_permission(self._store.get_name(), ManagerPermission.USERS_QUESTIONS)
        self._manager.get_appointment().add_permission(self._store.get_name(), ManagerPermission.WATCH_PURCHASE_HISTORY)
        permissions = [ManagerPermission.USERS_QUESTIONS, ManagerPermission.WATCH_PURCHASE_HISTORY]
        self.assertEqual(2, len(self._manager.get_appointment().get_permissions_of_store(self._store.get_name())))
        self.assertEqual(True, self._manager.get_appointment().has_permission(self._store.get_name(), ManagerPermission.USERS_QUESTIONS))
        self.assertEqual(True, self._manager.get_appointment().has_permission(self._store.get_name(), ManagerPermission.WATCH_PURCHASE_HISTORY))
        self.assertEqual(1, len(self._store.get_managers()))
        self.assertEqual(permissions, self._manager.get_appointment().get_permissions_of_store(self._store.get_name()))

    def test_add_new_manager_fail(self):
        # not logged in
        # not owner
        # already a manager on store
        self._store.add_manager(self._manager)
        self.assertEqual(False, self._store.add_manager(self._manager))
        # already a owner on store
        self.assertEqual(False, self._store.add_manager(self._owner))

if __name__ == '__main__':
    unittest.main()
