"""
    test suite class - used to organize the tests and run them together
"""
import unittest
from src.test.BlackBoxTests.AcceptanceTests import JunkTests


class AllTests:
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    runner = unittest.TextTestRunner()

    # add tests to test suite
    suite.addTest(loader.loadTestsFromModule(JunkTests.JunkTest()))

    # pass runner the suite and run it
    result = runner.run(suite)
