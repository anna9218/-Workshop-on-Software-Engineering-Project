import unittest

from src.Logger import logger
from src.main.ServiceLayer.SubscriberRole import SubscriberRole
from src.test.WhiteBoxTests.UnitTests.Stubs.StubUser import StubUser
from src.main.ServiceLayer.GuestRole import TradeControl


class SubscriberRoleTests(unittest.TestCase):
    @logger
    def setUp(self):
        self.__nickname = "anna9218"
        self.__password = "password"
        self.__store_name = "Bambook"
        self.__anna_as_subscriber = StubUser()
        self.__anna_as_subscriber.register(self.__nickname, self.__password)
        (TradeControl.get_instance()).subscribe(self.__anna_as_subscriber)
        self.__subscriber = SubscriberRole(self.__anna_as_subscriber)
        self.__anna_as_subscriber.login(self.__nickname, self.__password)

    @logger
    def test_logout(self):
        result = self.__subscriber.logout()
        self.assertTrue(result)
        # check that can't logout if already logged out
        result = self.__subscriber.logout()
        self.assertFalse(result)

    @logger
    def test_open_store(self):
        store = self.__subscriber.open_store(self.__store_name)
        self.assertIsNotNone(store)
        # check that can't open store if logged out
        self.__subscriber.logout()
        store = self.__subscriber.open_store(self.__store_name)
        self.assertIsNone(store)

    @logger
    def test_view_personal_purchase_history(self):
        history = self.__subscriber.view_personal_purchase_history()
        self.assertIsNotNone(history)
        # check history wasn't changed
        self.assertEqual(self.__anna_as_subscriber.get_accepted_purchases(), history)

    @logger
    def tearDown(self):
        self.__subscriber.logout()

    def __repr__(self):
        return repr ("SubscriberRoleTests")

    if __name__ == '__main__':
        unittest.main()
