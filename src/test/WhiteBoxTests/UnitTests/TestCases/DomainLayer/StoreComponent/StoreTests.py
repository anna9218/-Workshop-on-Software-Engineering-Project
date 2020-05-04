import unittest

from src.Logger import logger
from src.main.DomainLayer.StoreComponent.ManagerPermission import ManagerPermission
from src.main.DomainLayer.StoreComponent.Store import Store
from src.main.DomainLayer.StoreComponent.StoreManagerAppointment import StoreManagerAppointment
from src.main.DomainLayer.UserComponent.User import User
from src.test.WhiteBoxTests.UnitTests.Stubs.StubUser import StubUser


class StoreTests(unittest.TestCase):
    @logger
    def setUp(self):
        self.store: Store = Store("myStore")
        self.owner = User()
        self.owner.register("shani", "passwordd45646")
        self.store.get_owners().append(self.owner)
        self.manager = User()
        self.manager.register("dani", "passwordd45646")
        self.store.get_store_manager_appointments().append(StoreManagerAppointment(self.owner, self.manager, [ManagerPermission.EDIT_INV]))

    @logger
    def test_get_products_by(self):
        self.assertTrue(
            self.store.add_products("shani", [{"name": "Chair", "price": 100, "category": "Furniture", "amount": 5},
                                              {"name": "TV", "price": 100, "category": "Electric", "amount": 5},
                                              {"name": "Sofa", "price": 100, "category": "Furniture", "amount": 5}]))
        ls = self.store.get_products_by(1, "Chaer")
        self.assertEqual(ls, [])
        ls = self.store.get_products_by(1, "Chair")
        self.assertEqual(len(ls), 1)
        ls = self.store.get_products_by(2, "a")
        self.assertEqual(len(ls), 2)
        ls = self.store.get_products_by(3, "Furniture")
        self.assertEqual(len(ls), 2)
        ls = self.store.get_products_by(3, "Electric")
        self.assertEqual(len(ls), 1)

    @logger
    def test_add_products(self):
        # self.product3 = Product("Guitar", 100, "Musical Instruments")
        {"name": str, "price": int, "category": str, "amount": int}
        self.assertTrue(self.store.add_products("shani", [{"name": "Chair", "price": 100, "category": "Furniture", "amount": 5},
                                                          {"name": "Sofa", "price": 100, "category": "Furniture", "amount": 5}]))
        self.assertTrue(self.store.add_products("shani", [{"name": "Chair", "price": 100, "category": "Furniture", "amount": 5}]))
        self.assertFalse(self.store.add_products("shani", [{"name": "Chair", "price": -99, "category": "Furniture", "amount": 5},
                                                          {"name": "Sofa", "price": 100, "category": "Furniture", "amount": 5}]))
    @logger
    def test_add_product(self):
        # self.product3 = Product("Guitar", 100, "Musical Instruments")
        self.assertTrue(self.store.add_product("Chair", 100, "Furniture", 5))
        self.assertTrue(self.store.add_product("Sofa", 100, "Furniture", 5))
        self.assertTrue(self.store.add_product("Chair", 100, "Furniture", 5))
        self.assertEqual(self.store.get_inventory().get_amount("Chair"), 10)

    @logger
    def test_remove_products(self):
        self.store.add_product("Chair", 100, "Furniture", 5)
        self.assertFalse(self.store.remove_products("", ["Chair", "Sofa"]))
        self.assertEqual(self.store.get_inventory().len(), 1)
        self.store.add_product("Chair", 100, "Furniture", 5)
        self.store.add_product("Sofa", 100, "Furniture", 3)
        self.assertEqual(self.store.get_inventory().len(), 2)
        self.assertFalse(self.store.remove_products("", ["Chair", "Sofa"]))
        self.assertTrue(self.store.remove_products("shani", ["Chair", "Sofa"]))
        self.store.add_product("Chair", 100, "Furniture", 5)
        self.assertTrue(self.store.remove_products("dani", ["Chair"]))
        self.assertEqual(self.store.get_inventory().len(), 0)

    @logger
    def test_remove_product(self):
        self.assertFalse(self.store.remove_product("Chair"))
        self.store.add_product("Chair", 100, "Furniture", 5)
        self.assertEqual(self.store.get_inventory().len(), 1)
        self.assertTrue(self.store.remove_product("Chair"))
        self.assertEqual(self.store.get_inventory().len(), 0)

    @logger
    def test_change_price(self):
        self.store.add_product("Chair", 100, "Furniture", 5)
        self.assertTrue(self.store.change_price("Chair", 13))
        self.assertEqual(self.store.get_product("Chair").get_price(), 13)
        self.assertTrue(self.store.change_price("Chair", 8))
        self.assertEqual(self.store.get_product("Chair").get_price(), 8)
        self.assertFalse(self.store.change_price("NNNN", 8))
        self.assertFalse(self.store.change_price("Chair", -8))
        self.assertEqual(self.store.get_product("NNNN"), None)

    @logger
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

    @logger
    def test_change_amount(self):
        self.store.add_product("Chair", 100, "Furniture", 5)
        self.assertTrue(self.store.change_amount("Chair", 3))
        self.assertEqual(self.store.get_inventory().get_amount("Chair"), 3)
        self.assertTrue(self.store.change_amount("Chair", 8))
        self.assertFalse(self.store.change_amount("Chair", -8))
        self.assertEqual(self.store.get_inventory().get_amount("Chair"), 8)

    @logger
    def test_add_owner(self):
        user = StubUser()
        user.set_password_and_nickname("eden", "password")
        self.assertTrue(self.store.add_owner("shani", user))
        self.assertEqual(len(self.store.get_owners()), 2)

    @logger
    def test_is_owner(self):
        user = StubUser()
        user.set_password_and_nickname("eden", "password")
        self.assertFalse(self.store.is_owner("eden"))
        self.store.add_owner("shani", user)
        self.assertTrue(self.store.is_owner("eden"))

    @logger
    def test_is_in_store_inventory(self):
        self.store.add_product("Eytan's Product", 100, "Eytan Category", 5)
        self.store.add_product("not Eytan's Product", 10, "Eytan Category", 2)

        # All valid one product
        amount_per_product = [["Eytan's Product", 4]]
        result = self.store.is_in_store_inventory(amount_per_product)
        self.assertTrue(result)

        # All valid two products
        amount_per_product = [["Eytan's Product", 4], ["not Eytan's Product", 1]]
        result = self.store.is_in_store_inventory(amount_per_product)
        self.assertTrue(result)

        # Exactly the same as in stock
        amount_per_product = [["Eytan's Product", 5], ["not Eytan's Product", 2]]
        result = self.store.is_in_store_inventory(amount_per_product)
        self.assertTrue(result)

        # One product not enough in stock
        amount_per_product = [["Eytan's Product", 6], ["not Eytan's Product", 1]]
        result = self.store.is_in_store_inventory(amount_per_product)
        self.assertFalse(result)

        # Two product not enough in stock
        amount_per_product = [["Eytan's Product", 6], ["not Eytan's Product", 10]]
        result = self.store.is_in_store_inventory(amount_per_product)
        self.assertFalse(result)

        # One product doesn't exist
        amount_per_product = [["Eytan's social life", 5], ["not Eytan's Product", 1]]
        result = self.store.is_in_store_inventory(amount_per_product)
        self.assertFalse(result)

        # Two product doesn't exist
        amount_per_product = [["Eytan's social life", 5], ["Liverpool primer league title", 1]]
        result = self.store.is_in_store_inventory(amount_per_product)
        self.assertFalse(result)

    @logger
    def tearDown(self) -> None:
        self.store = None

    def __repr__(self):
        return repr ("StoreTests")