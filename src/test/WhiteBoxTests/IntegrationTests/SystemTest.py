"""
    test suite class - used to test the entire system.
"""
import unittest
from src.test.WhiteBoxTests.IntegrationTests.ServiceLayer.SystemManagerRoleTests import SystemManagerRoleTests
from src.test.WhiteBoxTests.IntegrationTests.ServiceLayer.SubscriberRoleTests import SubscriberRoleTests
from src.test.WhiteBoxTests.IntegrationTests.ServiceLayer.StoreOwnerOrManagerTests import StoreOwnerOrManagerTests
from src.test.WhiteBoxTests.IntegrationTests.ServiceLayer.GuestRoleTests import GuestRoleTest


class SystemTestsRunner:
    # Build test suit
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()

    # add all tests in package UcTests (all acceptance tests) to test suite
    # suite.addTests(loader.loadTestsFromModule(TestCases))

    # add individual tests to the test suite
    suite.addTest(loader.loadTestsFromTestCase(SystemManagerRoleTests))
    suite.addTest(loader.loadTestsFromTestCase(SubscriberRoleTests))
    suite.addTest(loader.loadTestsFromTestCase(StoreOwnerOrManagerTests))
    suite.addTest(loader.loadTestsFromTestCase(GuestRoleTest))

    # pass runner the suite and run it
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)


if __name__ == '__main__':
    unittest.main()


