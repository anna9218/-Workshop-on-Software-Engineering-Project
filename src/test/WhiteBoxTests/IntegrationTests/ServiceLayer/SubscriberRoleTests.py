import unittest
from unittest.mock import Mock
from unittest.mock import MagicMock

import jsonpickle

from src.Logger import logger
from src.main.DomainLayer.StoreComponent.Purchase import Purchase
from src.main.DomainLayer.StoreComponent.Store import Store
from src.main.DomainLayer.UserComponent.User import User
from src.main.ServiceLayer.SubscriberRole import SubscriberRole
from src.main.DomainLayer.TradeComponent.TradeControl import TradeControl


class SubscriberRoleTests(unittest.TestCase):
    @logger
    def setUp(self):
        self.__subscriber: SubscriberRole = SubscriberRole()
        (TradeControl.get_instance()).register_guest("eytan", "eytan as password")
        (TradeControl.get_instance()).login_subscriber("eytan", "eytan as password")
        self.__user: User = (TradeControl.get_instance()).get_curr_user()
        (TradeControl.get_instance()).get_managers().append(self.__user)
        (TradeControl.get_instance()).open_store("eytan as store")
        self.__store: Store = (TradeControl.get_instance()).get_store("eytan as store")
        (TradeControl.get_instance()).add_products(self.__store.get_name(),
                                                   [{"name": "eytan",
                                                     "price": 12,
                                                     "category": "eytan as category",
                                                     "amount": 21}])

    @logger
    def test_logout(self):
        user = User()
        user_nickname = "Eytan"
        user_password = "Eytan's password"
        user.register(user_nickname, user_password)

        (TradeControl.get_instance()).set_curr_user(user)
        (TradeControl.get_instance()).login_subscriber(user_nickname, user_password)

        # All valid
        self.assertTrue(self.__subscriber.logout())
        self.assertTrue((TradeControl.get_instance()).get_curr_user().is_logged_out())

        # Invalid - user already logged out
        self.assertFalse(self.__subscriber.logout())

    @logger
    def test_open_store(self):
        user = User()
        user_nickname = "Eytan"
        user_password = "Eytan's password"
        user.register(user_nickname, user_password)

        stores_num = len(TradeControl.get_instance().get_stores())
        (TradeControl.get_instance()).set_curr_user(user)
        (TradeControl.get_instance()).login_subscriber(user_nickname, user_password)

        # All valid
        self.assertTrue(self.__subscriber.open_store("myFirstStore"))
        self.assertEqual(stores_num + 1, len((TradeControl.get_instance()).get_stores()))
        store: Store = (TradeControl.get_instance()).get_store("myFirstStore")
        self.assertIsNotNone(store)
        self.assertIn((TradeControl.get_instance()).get_curr_user(), store.get_owners())

        stores_num = stores_num + 1

        # Invalid - store already exist
        self.assertFalse(self.__subscriber.open_store("myFirstStore"))
        self.assertEqual(stores_num, len((TradeControl.get_instance()).get_stores()))
        self.assertIsNotNone((TradeControl.get_instance()).get_store("myFirstStore"))

        bad_user = User()
        (TradeControl.get_instance()).set_curr_user(bad_user)

        # Invalid - curr_user doesn't register
        self.assertFalse(self.__subscriber.open_store("not myFirstStore"))
        self.assertEqual(stores_num, len((TradeControl.get_instance()).get_stores()))
        self.assertIsNone((TradeControl.get_instance()).get_store("not myFirstStore"))

        not_logged_in_user = User()
        not_logged_in_user.register("I am", "Logged out")
        (TradeControl.get_instance()).set_curr_user(not_logged_in_user)

        # Invalid - curr_user doesn't register
        self.assertFalse(self.__subscriber.open_store("not myFirstStore"))
        self.assertEqual(stores_num, len((TradeControl.get_instance()).get_stores()))
        self.assertIsNone((TradeControl.get_instance()).get_store("not myFirstStore"))

        (TradeControl.get_instance()).set_curr_user(user)

        # Invalid - store name is empty
        self.assertFalse(self.__subscriber.open_store("          "))
        self.assertEqual(stores_num, len((TradeControl.get_instance()).get_stores()))
        self.assertIsNone((TradeControl.get_instance()).get_store("          "))

    @logger
    def test_view_personal_purchase_history(self):
        # Empty purchases
        self.assertListEqual([], self.__subscriber.view_personal_purchase_history())

        (TradeControl.get_instance()).get_curr_user().get_purchase_history().append(Purchase(
            [{"product_name": "eytan", "product_price": 12, "amount": 1}], 12, self.__store.get_name(),
            self.__user.get_nickname()))

        # Not empty
        self.assertEqual(1, len(self.__subscriber.view_personal_purchase_history()))
        purchases_lst = [jsonpickle.decode(e).get_products() for e in
                         self.__subscriber.view_personal_purchase_history()]
        self.assertListEqual([{"product_name": "eytan", "product_price": 12, "amount": 1}], purchases_lst[0])

        (TradeControl.get_instance()).get_managers().remove(self.__user)

    @logger
    def tearDown(self):
        (TradeControl.get_instance()).__delete__()
        pass

    def __repr__(self):
        return repr("SubscriberRoleTests")

    if __name__ == '__main__':
        unittest.main()
