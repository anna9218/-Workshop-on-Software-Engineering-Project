import unittest

from src.main.DomainLayer.ManagerPermission import ManagerPermission
from src.main.DomainLayer.Store import Store
from src.test.WhiteBoxTests.UnitTests.Stubs.StubUser import StubUser


class StoreTests(unittest.TestCase):
    def setUp(self):
        self.store = Store("myStore")

    def test_add_products(self):
        # self.product3 = Product("Guitar", 100, "Musical Instruments")
        self.assertTrue(self.store.add_products([("Chair", 100, "Furniture", 5), ("Sofa", 100, "Furniture", 5)]))
        self.assertTrue(self.store.add_products([("Chair", 100, "Furniture", 5), ("Sofa", 100, "Furniture", 5)]))

    def test_add_product(self):
        # self.product3 = Product("Guitar", 100, "Musical Instruments")
        self.assertTrue(self.store.add_product("Chair", 100, "Furniture", 5))
        self.assertTrue(self.store.add_product("Chair", 100, "Furniture", 5))
        self.assertTrue(self.store.add_product("Sofa", 100, "Furniture", 5))

    def test_edit_manager_permissions(self):
        manager = StubUser()
        owner = StubUser()
        owner2 = StubUser()
        manager.set_password_and_nickname("manager", "sdf")
        owner.set_password_and_nickname("owner", "123")
        owner2.set_password_and_nickname("owner2", "123")
        self.store.add_owner(owner)
        self.store.add_manager(manager,
                               [ManagerPermission.APPOINT_MAMAGER, ManagerPermission.DEL_MANAGER], owner)
        self.assertTrue(self.store.edit_manager_permissions(manager, [ManagerPermission.CLOSE_STORE], owner))
        self.assertFalse(self.store.edit_manager_permissions(manager, [ManagerPermission.APPOINT_MAMAGER], owner2))

    def test_remove_products(self):
        self.store.add_product("Chair", 100, "Furniture", 5)
        self.assertFalse(self.store.remove_products(["Chair", "Sofa"]))
        self.assertEqual(self.store.get_inventory().len(), 0)
        self.store.add_product("Chair", 100, "Furniture", 5)
        self.store.add_product("Sofa", 100, "Furniture", 3)
        self.assertEqual(self.store.get_inventory().len(), 2)
        self.assertTrue(self.store.remove_products(["Chair", "Sofa"]))
        self.assertEqual(self.store.get_inventory().len(), 0)

    def test_remove_product(self):
        self.assertFalse(self.store.remove_product("Chair"))
        self.store.add_product("Chair", 100, "Furniture", 5)
        self.assertEqual(self.store.get_inventory().len(), 1)
        self.assertTrue(self.store.remove_product("Chair"))
        self.assertEqual(self.store.get_inventory().len(), 0)

    def test_change_price(self):
        self.store.add_product("Chair", 100, "Furniture", 5)
        self.assertTrue(self.store.change_price("Chair", 13))
        self.assertEqual(self.store.get_product("Chair").get_price(), 13)
        self.assertTrue(self.store.change_price("Chair", 8))
        self.assertEqual(self.store.get_product("Chair").get_price(), 8)
        self.assertFalse(self.store.change_price("NNNN", 8))
        self.assertEqual(self.store.get_product("NNNN"), None)

    def test_change_name(self):
        self.store.add_product("Chair", 100, "Furniture", 5)
        self.assertTrue(self.store.change_name("Chair", "Chair222"))
        self.assertNotEqual(self.store.get_product("Chair222"), None)
        self.assertEqual(self.store.get_product("Chair"), None)
        self.assertTrue(self.store.change_name("Chair222", "Blaaaa"))
        self.assertNotEqual(self.store.get_product("Blaaaa"), None)
        self.assertEqual(self.store.get_product("Chair222"), None)
        self.assertFalse(self.store.change_name("NNNN", "blaaa"))
        self.assertEqual(self.store.get_product("NNNN"), None)
        self.assertEqual(self.store.get_product("blaaa"), None)

    def test_change_amount(self):
        self.store.add_product("Chair", 100, "Furniture", 5)
        self.assertTrue(self.store.change_amount("Chair", 3))
        self.assertEqual(self.store.get_inventory().get_amount_of_product("Chair"), 3)
        self.assertTrue(self.store.change_amount("Chair", 8))
        self.assertEqual(self.store.get_inventory().get_amount_of_product("Chair"), 8)

    def test_add_owner(self):
        user = StubUser()
        user.set_password_and_nickname("eden", "password")
        self.assertTrue(self.store.add_owner(user))
        self.assertEqual(len(self.store.get_owners()), 1)

    def test_add_manager(self):
        manager = StubUser()
        owner = StubUser()
        manager.set_password_and_nickname("eden", "password")
        owner.set_password_and_nickname("dana", "password123")
        self.store.add_owner(owner)
        self.assertTrue(self.store.add_manager(manager, [ManagerPermission.APPOINT_MAMAGER, ManagerPermission.DEL_MANAGER], owner))
        _tuple = self.store.get_managers_tuple()
        self.assertEqual(len(_tuple), 1)
        self.assertEqual(_tuple[0][0], manager)
        self.assertEqual(_tuple[0][1], [ManagerPermission.APPOINT_MAMAGER, ManagerPermission.DEL_MANAGER])
        self.assertEqual(_tuple[0][2], owner)

    def test_is_owner(self):
        user = StubUser()
        user.set_password_and_nickname("eden", "password")
        self.assertFalse(self.store.is_owner("eden"))
        self.store.add_owner(user)
        self.assertTrue(self.store.is_owner("eden"))

