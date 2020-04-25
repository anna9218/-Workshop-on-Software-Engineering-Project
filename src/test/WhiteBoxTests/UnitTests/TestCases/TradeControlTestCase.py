import unittest

from src.main.DomainLayer.TradeControl import TradeControl
from src.main.DomainLayer.User import User
from src.test.WhiteBoxTests.UnitTests.Stubs.StubDelivery import StubDelivery
from src.test.WhiteBoxTests.UnitTests.Stubs.StubUser import StubUser
from src.test.WhiteBoxTests.UnitTests.Stubs.StubPayment import StubPayment


class TradeControlTestCase(unittest.TestCase):
    def setUp(self):
        self.tradeControl = TradeControl.get_instance()
        self.user = StubUser()
        self.user.set_password_and_nickname("nickname", "password")

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

    # def test_get_products_by(self, search_opt, string):
    #     store1 = self.tradeControl.open_store("myStore")
    #     store1.
    #
    #     ls = map(lambda store: store.get_products_by(search_opt, string), )
    #     return reduce(lambda acc, curr: acc.append(curr), ls)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
