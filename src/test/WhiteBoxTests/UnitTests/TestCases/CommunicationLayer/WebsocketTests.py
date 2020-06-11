import unittest
from src.main.CommunicationLayer import WebSocketService

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.__username = "Yarin"
        self.__store_name = "Some Store"
        self.__success = ['TODO'] # TODO

    def test_open_store(self):
        # valid
        WebSocketService.open_store(self.__store_name, self.__username, self.__success)
        self.assertIsNotNone(WebSocketService.get_store(self.__store_name))

        # not valid
        WebSocketService.open_store(self.__store_name, self.__username, self.__success)
        WebSocketService.open_store(self.__store_name, "another user", self.__success)

    def test_add_subscriber(self):
        WebSocketService.open_store(self.__store_name, self.__username, self.__sucsses)
        # valid
        WebSocketService.add_subscriber_to_store(self.__store_name, self.__username, self.__success) # TODO?
        self.assertEqual(True, WebSocketService.is_subscribed_to_store(self.__store_name, self.__username))

        # not valid
        self.assertNotEqual(True, WebSocketService.is_subscribed_to_store(self.__store_name, "Ron"))
        self.assertNotEqual(True, WebSocketService.is_subscribed_to_store("Other Store", self.__username))
        self.assertFalse(WebSocketService.add_subscriber_to_store(self.__store_name, self.__username, self.__success))

        # add another subscriber to same store
        WebSocketService.add_subscriber_to_store(self.__store_name, "new owner", self.__success)
        self.assertEqual(True, WebSocketService.is_subscribed_to_store(self.__store_name, "new owner"))

        # subscribe self.user to another store
        WebSocketService.add_subscriber_to_store("New Store", self.__username, self.__success)
        self.assertEqual(True, WebSocketService.is_subscribed_to_store("New Store", self.__username))

    def test_remove_subscriber(self):
        WebSocketService.open_store(self.__store_name, "first owner", self.__success)
        WebSocketService.add_subscriber_to_store(self.__store_name, self.__username, self.__success)

        # valid
        self.assertEquals(0, WebSocketService.remove_subscriber_from_store(self.__store_name, self.__username, self.__success))
        self.assertEqual(False, WebSocketService.is_subscribed_to_store(self.__store_name, self.__username))
        self.assertEquals(1, len(WebSocketService.get_store(self.__store_name).subscribers()))

        # not valid
        self.assertEquals(-1, WebSocketService.remove_subscriber_from_store(self.__store_name, self.__username, self.__success))
        self.assertEquals(-1, WebSocketService.remove_subscriber_from_store("Store", self.__username, self.__success))
        self.assertEquals(-1, WebSocketService.remove_subscriber_from_store(self.__store_name, "Username", self.__success))

    def test_update_queue_after_purchase(self):
        # WebSocketService.handle_purchase(user_name=self.__username, )
        WebSocketService.open_store(self.__store_name, self.__username, self.__success)

        # valid
        WebSocketService.notifyPurchase(self.__username, self.__store_name, self.__success)
        WebSocketService.notifyPurchase("Other User", self.__store_name, self.__success)

        # not valid - unexist store
        WebSocketService.notifyPurchase("Other User", "Store", self.__success)


    def test_update_queue_after_remove_owner(self):
        # TODO
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
