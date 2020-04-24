import unittest

from src.main.DomainLayer import ManagerPermission
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
        self._store.add_owner(self._owner)
        self._owner.get_appointment().appoint_manager(self._store)
        self._manager = User()
        self._manager.register("manager", "1234")
        self._manager.login("manager", "1234")

    def test_add_new_manager(self):
        ser = StoreOwnerRole()
        ser.appoint_new_store_manager(self._owner.get_nickname(), self._store.get_name(), self._manager.get_nickname())
        permissions = [ManagerPermission.USERS_QUESTIONS, ManagerPermission.WATCH_PURCHASE_HISTORY]
        self.assertEqual([(self._manager, permissions)], self._store.get_managers())
        # self.assertEqual(1, self._store.get_managers().count())
        # self.assertEqual( permissions, self._store.get_managers().pop(0)[1])

    pass

if __name__ == '__main__':
    unittest.main()
