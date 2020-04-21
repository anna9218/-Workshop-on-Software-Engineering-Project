"""
    abstract class representing the abstraction in the Bridge pattern
"""
from abc import ABC, abstractmethod
from src.test.BlackBoxTests.AcceptanceTests import Driver
import unittest


class ProjectTest(ABC, unittest.TestCase):

    # setup for all tests
    @abstractmethod
    def setUp(self) -> None:
        self.bridge = Driver.Driver.get_bridge()
        super().__init__()

    # TODO:add functions for tests
    def test_sum(self, x, y) -> int:
        return self.bridge.test_sum(x, y)

    def test_wrong_sum(self, x, y) -> int:
        return self.bridge.test_wrong_sum(x, y)

    # teardown after all tests are run
    @abstractmethod
    def tearDown(self) -> None:
        pass
