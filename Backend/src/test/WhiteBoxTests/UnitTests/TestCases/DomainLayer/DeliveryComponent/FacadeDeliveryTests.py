import unittest

from Backend.src.Logger import logger
from Backend.src.main.DomainLayer.DeliveryComponent.DeliveryProxy import DeliveryProxy


class FacadeDeliveryTests(unittest.TestCase):
    # @logger
    def setUp(self) -> None:
        self.__delivery_sys = DeliveryProxy.get_instance()
        self.__delivery_sys.connect()
        self.__valid_username = "username"
        self.__valid_address = "my awesome address 04/20"
        self.__wrong_input = ""

    # @logger
    def test_connection(self):
        # test that system is connected fine
        self.assertEqual(True, self.__delivery_sys.is_connected())
        # test that the system disconnect fine
        self.__delivery_sys.disconnect()
        self.assertEqual(False, self.__delivery_sys.is_connected())

    # @logger
    def test_wrong_input(self):
        # valid user + invalid address
        res = self.__delivery_sys.deliver_products(self.__valid_username, self.__wrong_input)
        self.assertEqual(False, res)
        # invalid user + valid address
        res = self.__delivery_sys.deliver_products(self.__wrong_input, self.__valid_address)
        self.assertEqual(False, res)
        # invalid user + invalid address
        res = self.__delivery_sys.deliver_products(self.__wrong_input, self.__wrong_input)
        self.assertEqual(False, res)
        # system disconnect + valid input
        self.__delivery_sys.disconnect()
        res = self.__delivery_sys.deliver_products(self.__valid_username, self.__valid_address)
        self.assertEqual(False, res)
        return

    # @logger
    def test_correct_input(self):
        # valid user + valid address
        res = self.__delivery_sys.deliver_products(self.__valid_username, self.__valid_address)
        self.assertEqual(True, res)
        return

    # @logger
    def tearDown(self) -> None:
        self.__delivery_sys.disconnect()

    if __name__ == '__main__':
        unittest.main()

    def __repr__(self):
        return repr ("FacadeDeliveryTests")