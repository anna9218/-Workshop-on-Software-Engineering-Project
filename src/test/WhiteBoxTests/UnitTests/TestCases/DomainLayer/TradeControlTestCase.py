import unittest

from src.main.DomainLayer.TradeControl import TradeControl
from src.test.WhiteBoxTests.UnitTests.Stubs.StubUser import StubUser


class TradeControlTestCase(unittest.TestCase):
    def setUp(self):
        self.tradeControl = TradeControl.get_instance()
        self.user = StubUser()
        self.user.set_password_and_nickname("nickname", "password")
#         self.tradeControl.manager = StubUser(self.tradeControl)
#         self.tradeControl.delivery_system = StubDelivery()
#         self.tradeControl.payment_system = StubPayment()
# TODO: talk with eitan
#     def test_init_system(self):
#         self.tradeControl.init_system()
#         self.assertEqual(len(self.tradeControl.get_managers()), 1)
#         self.assertEqual(self.tradeControl.get_delivery_system().isConnected, True)
#         self.assertEqual(self.tradeControl.get_payment_system().isConnected, True)
#         self.user = StubUser()
#         self.user.set_password_and_nickname("nickname", "password")

    def test_subscribe_success_and_fail(self):
        subscribers_num = len(self.tradeControl.get_subscribers())
        self.assertTrue(self.tradeControl.subscribe(self.user))
        self.assertFalse(self.tradeControl.subscribe(self.user))
        self.assertEqual(len(self.tradeControl.get_subscribers()), subscribers_num + 1)
        self.assertTrue(self.tradeControl.get_subscriber(self.user.get_nickname()))
        self.tradeControl.unsubscribe(self.user)

    def test_add_sys_manager_success_and_fail(self):
        managers_num = len(self.tradeControl.get_managers())
        self.assertTrue(self.tradeControl.add_sys_manager(self.user))
        self.assertFalse(self.tradeControl.add_sys_manager(self.user))
        self.assertEqual(len(self.tradeControl.get_managers()), managers_num+1)

    def test_unsubscribe_success_and_fail(self):
        self.tradeControl.subscribe(self.user)
        subscribers_num = len(self.tradeControl.get_subscribers())
        self.assertTrue(self.tradeControl.unsubscribe("nickname"))
        self.assertFalse(self.tradeControl.unsubscribe("nickname"))
        self.assertEqual(len(self.tradeControl.get_subscribers()), subscribers_num - 1)

    def test_close_and_open_store(self):
        stores_num = len(self.tradeControl.get_stores())
        self.assertNotEqual(self.tradeControl.open_store("myFirstStore"), None)
        self.assertEqual(self.tradeControl.open_store("myFirstStore"), None)
        self.assertEqual(len(self.tradeControl.get_stores()), stores_num+1)
        self.assertTrue(self.tradeControl.close_store("myFirstStore"))
        self.assertFalse(self.tradeControl.close_store("myFirstStore"))
        self.assertEqual(len(self.tradeControl.get_stores()), stores_num)

    def test_validate_nickname(self):
        self.assertTrue(self.tradeControl.validate_nickname("nickname"))
        self.tradeControl.subscribe(self.user)
        self.assertFalse(self.tradeControl.validate_nickname("nickname"))
        self.tradeControl.unsubscribe("nickname")

    def test_get_subscriber(self):
        self.assertEqual(self.tradeControl.get_subscriber("nickname"), None)
        self.tradeControl.subscribe(self.user)
        self.assertEqual(self.tradeControl.get_subscriber("nickname"), self.user)
        self.tradeControl.unsubscribe("nickname")

    def test_get_store(self):
        self.tradeControl.open_store("myStore")
        store = self.tradeControl.get_store("myStore")
        self.assertNotEqual(store, None)
        self.assertEqual(store.get_name(), "myStore")
        self.assertEqual(self.tradeControl.get_store("blaaa"), None)
        self.tradeControl.close_store("myStore")

    def test_get_products_by(self):
        store1 = self.tradeControl.open_store("myStore")
        store2 = self.tradeControl.open_store("myStore2")
        store1.add_products_to_store([("Chair", 100, "Furniture", 5), ("Sofa", 100, "Furniture", 5)])
        store2.add_products_to_store([("Chair", 125, "Furniture", 5)])
        ls = self.tradeControl.get_products_by(1, "Chair")
        self.assertEqual(len(ls), 2)
        ls = self.tradeControl.get_products_by(2, "o")
        self.assertEqual(len(ls), 1)
        ls = self.tradeControl.get_products_by(3, "Furniture")
        self.assertEqual(len(ls), 3)
        self.tradeControl.close_store("myStore")
        self.tradeControl.close_store("myStore2")

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
