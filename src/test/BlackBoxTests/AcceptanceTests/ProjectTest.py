"""
    abstract class representing the abstraction in the Bridge pattern
"""
from abc import ABC, abstractmethod
from src.test.BlackBoxTests.AcceptanceTests.Driver import Driver
import unittest


class ProjectTest(ABC, unittest.TestCase):

    # setup for all tests
    @abstractmethod
    def setUp(self) -> None:
        self.__bridge = Driver().get_bridge()

    # default functions to be implemented in inheriting classes (not in parent class)
    @abstractmethod
    def test_success(self):
        pass

    @abstractmethod
    def test_fail(self):
        pass

    # bridged functions

    # Register tests functions
    def register_user(self, username, password) -> bool:
        return self.__bridge.register_user(username, password)

    # Payment System tests functions
    def connect_payment_sys(self):
        self.__bridge.connect_payment_sys()

    def commit_payment(self, username, amount, credit, date) -> bool:
        return self.__bridge.commit_payment(username, amount, credit, date)

    def disconnect_payment_sys(self):
        self.__bridge.disconnect_payment_sys()

    # Delivery System tests functions
    def connect_delivery_sys(self):
        self.__bridge.connect_delivery_sys()

    def deliver(self, username, adress) -> bool:
        return self.__bridge.deliver(username, adress)

    def disconnect_delivery_sys(self):
        self.__bridge.disconnect_delivery_sys()

    # teardown after all tests are run
    @abstractmethod
    def tearDown(self) -> None:
        pass
