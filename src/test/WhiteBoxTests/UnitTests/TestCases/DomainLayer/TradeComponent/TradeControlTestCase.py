import unittest

from src.Logger import logger
from src.main.DomainLayer.StoreComponent.Store import Store
from src.main.DomainLayer.TradeComponent.TradeControl import TradeControl
from src.test.WhiteBoxTests.UnitTests.Stubs.StubUser import StubUser


class TradeControlTestCase(unittest.TestCase):
    # @logger
    def setUp(self):
        self.tradeControl = TradeControl.get_instance()
        self.user = StubUser()
        self.user.set_password_and_nickname("nickname", "password")
#         self.tradeControl.manager = StubUser(self.tradeControl)
#         self.tradeControl.delivery_system = StubDelivery()
#         self.tradeControl.payment_system = StubPayment()

    # @logger
    def test_add_sys_manager_success_and_fail(self):
        managers_num = len(self.tradeControl.get_managers())
        self.assertTrue(self.tradeControl.add_system_manager("nickname", "password"))
        self.assertFalse(self.tradeControl.add_system_manager("nickname", "password"))
        self.assertEqual(len(self.tradeControl.get_managers()), managers_num + 1)

    # @logger
    def test_register_guest(self):
        self.assertTrue(self.tradeControl.register_guest("eden", "passwoed"))
        self.assertFalse(self.tradeControl.register_guest("eden", "passwoed"))

    # @logger
    def test_login_guest(self):
        self.assertFalse(self.tradeControl.login_subscriber("eden", "passwoed"))
        self.assertTrue(self.tradeControl.register_guest("eden", "passwoed"))
        self.assertTrue(self.tradeControl.login_subscriber("eden", "passwoed"))
        self.assertFalse(self.tradeControl.login_subscriber("eden", "passwoed"))

    # @logger
    def test_subscribe_success_and_fail(self):
        subscribers_num = len(self.tradeControl.get_subscribers())
        self.assertTrue(self.tradeControl.subscribe(self.user))
        self.assertFalse(self.tradeControl.subscribe(self.user))
        self.assertEqual(len(self.tradeControl.get_subscribers()), subscribers_num + 1)
        self.assertTrue(self.tradeControl.get_subscriber(self.user.get_nickname()))
        self.tradeControl.unsubscribe(self.user)

    # @logger
    def test_unsubscribe_success_and_fail(self):
        self.tradeControl.subscribe(self.user)
        subscribers_num = len(self.tradeControl.get_subscribers())
        self.assertTrue(self.tradeControl.unsubscribe("nickname"))
        self.assertFalse(self.tradeControl.unsubscribe("nickname"))
        self.assertEqual(len(self.tradeControl.get_subscribers()), subscribers_num - 1)

    # @logger
    def test_close_and_open_store(self):
        stores_num = len(self.tradeControl.get_stores())
        self.tradeControl.set_curr_user(self.user)
        self.assertFalse(self.tradeControl.open_store("myFirstStore"))
        self.user.register("name", "213456")
        self.assertFalse(self.tradeControl.open_store("myFirstStore"))
        self.user.login("name", "213456")
        self.assertTrue(self.tradeControl.open_store("myFirstStore"))
        self.assertEqual(len(self.tradeControl.get_stores()), stores_num+1)
        self.assertTrue(self.tradeControl.close_store("myFirstStore"))
        self.assertFalse(self.tradeControl.close_store("myFirstStore"))
        self.assertEqual(len(self.tradeControl.get_stores()), stores_num)

    # @logger
    def test_validate_nickname(self):
        self.assertTrue(self.tradeControl.validate_nickname("nickname"))
        self.tradeControl.subscribe(self.user)
        self.assertFalse(self.tradeControl.validate_nickname("nickname"))
        self.tradeControl.unsubscribe("nickname")

    # @logger
    def test_get_subscriber(self):
        self.assertEqual(self.tradeControl.get_subscriber("nickname"), None)
        self.tradeControl.subscribe(self.user)
        self.assertEqual(self.tradeControl.get_subscriber("nickname"), self.user)
        self.tradeControl.unsubscribe("nickname")

    # @logger
    def test_get_products_by(self):
        self.user.register("eden", "213456")
        self.user.login("eden", "213456")
        self.tradeControl.set_curr_user(self.user)
        self.tradeControl.open_store("myStore")
        self.tradeControl.open_store("myStore2")
        store1 = self.tradeControl.get_store("myStore")
        store2: Store = self.tradeControl.get_store("myStore2")
        store1.add_products("eden", [{"name": "Chair", "price": 100, "category": "Furniture", "amount": 5},
                                     {"name": "Sofa", "price": 100, "category": "Furniture", "amount": 5}])
        store2.add_products("eden", [{"name": "TV", "price": 100, "category": "Electric", "amount": 5},
                                     {"name": "Sofa", "price": 100, "category": "Furniture", "amount": 5}])
        ls = self.tradeControl.get_products_by(1, "Sofa")
        self.assertEqual(len(ls), 2)
        ls = self.tradeControl.get_products_by(2, "o")
        self.assertEqual(len(ls), 2)
        ls = self.tradeControl.get_products_by(2, "a")
        self.assertEqual(len(ls), 3)
        ls = self.tradeControl.get_products_by(3, "Furniture")
        self.assertEqual(len(ls), 3)
        self.tradeControl.close_store("myStore")
        self.tradeControl.close_store("myStore2")

    # @logger
    # def test_next_purchase_id(self):
    #     id1 = (TradeControl.get_instance()).get_next_purchase_id()
    #     id2 = (TradeControl.get_instance()).get_next_purchase_id()
    #
    #     self.assertEqual(id1+1, id2)

    # @logger
    def test_logout_subscriber(self):
        self.assertFalse(self.tradeControl.logout_subscriber())
        self.assertTrue(self.tradeControl.register_guest("eden", "passwoed"))
        self.assertTrue(self.tradeControl.login_subscriber("eden", "passwoed"))
        self.assertTrue(self.tradeControl.logout_subscriber())

    @logger
    def test_view_personal_purchase_history(self):
        pass

    @logger
    def test_view_user_purchase_history(self, nickname):
        pass

    @logger
    def test_view_store_purchases_history(self):
        pass

    # @logger
    def test_add_and_remove_products(self):
        self.user.register("eden", "213456")
        self.user.login("eden", "213456")
        self.tradeControl.set_curr_user(self.user)
        self.tradeControl.open_store("myStore")
        self.tradeControl.open_store("myStore2")
        store1 = self.tradeControl.get_store("myStore")
        self.assertFalse(self.tradeControl.add_products("Store", [{"name": "Chair", "price": 100, "category": "Furniture", "amount": 5},
                                     {"name": "Sofa", "price": 100, "category": "Furniture", "amount": 5}]))
        self.assertTrue(self.tradeControl.add_products("myStore", [
            {"name": "Chair", "price": 100, "category": "Furniture", "amount": 5},
            {"name": "Sofa", "price": 100, "category": "Furniture", "amount": 5}]))
        self.assertNotEqual(store1.get_product("Chair"), None)
        self.assertNotEqual(store1.get_product("Sofa"), None)
        self.assertTrue(self.tradeControl.remove_products("myStore", ["Sofa"]))
        self.assertNotEqual(store1.get_product("Chair"), None)
        self.assertEqual(store1.get_product("Sofa"), None)

    @logger
    def test_edit_product(self):
        pass

    @logger
    def test_appoint_additional_owner(self):
        pass

    @logger
    def test_appoint_store_manager(self):
        pass

    @logger
    def test_edit_manager_permissions(self):
        pass

    @logger
    def test_remove_manager(self):
        pass

    def tearDown(self):
        pass
        # self.tradeControl = TradeControl.get_instance()

    def __repr__(self):
        return repr ("TradeControlTestCase")


if __name__ == '__main__':
    unittest.main()
