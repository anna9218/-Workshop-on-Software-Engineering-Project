"""
    abstract class representing the abstraction in the Bridge pattern
"""
from abc import ABC, abstractmethod
from src.test.BlackBoxTests.AcceptanceTests.Driver import Driver
from src.test.BlackBoxTests.AcceptanceTests.ReusableTests.ReuableTest import ReusableTests
import unittest


class ProjectTest(ABC, unittest.TestCase):

    # setup for all tests
    @abstractmethod
    def setUp(self) -> None:
        self.bridge = Driver.get_bridge()
        self.reusableTests = ReusableTests()
        super().__init__()

    # default functions to be implemented in inheriting classes
    @abstractmethod
    def test_success(self):
        pass

    @abstractmethod
    def test_fail(self):
        pass

    @abstractmethod
    def test_fatal_error(self):
        pass

    # teardown after all tests are run
    @abstractmethod
    def tearDown(self) -> None:
        pass
