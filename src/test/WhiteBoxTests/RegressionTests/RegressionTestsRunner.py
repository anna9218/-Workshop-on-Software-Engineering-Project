"""
    test suite class - used to test V1 Features.
"""
import unittest
from src.test.WhiteBoxTests.RegressionTests.Version1.SystemManagerRoleTests import SystemManagerRoleTests as \
    SystemManagerRoleTests_V1
from src.test.WhiteBoxTests.RegressionTests.Version1.SubscriberRoleTests import SubscriberRoleTests as \
    SubscriberRoleTests_V1
from src.test.WhiteBoxTests.RegressionTests.Version1.StoreOwnerOrManagerTests import StoreOwnerOrManagerTests \
    as StoreOwnerOrManagerTests_V1
from src.test.WhiteBoxTests.RegressionTests.Version1.GuestRoleTests import GuestRoleTest as \
    GuestRoleTests_V1


class RegressionTestsRunner:
    # Build test suit
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()

    # add individual tests to the test suite for version 1
    suite.addTest(loader.loadTestsFromTestCase(SystemManagerRoleTests_V1))
    suite.addTest(loader.loadTestsFromTestCase(SubscriberRoleTests_V1))
    suite.addTest(loader.loadTestsFromTestCase(StoreOwnerOrManagerTests_V1))
    suite.addTest(loader.loadTestsFromTestCase(GuestRoleTests_V1))

    # pass runner the suite and run it
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)


if __name__ == '__main__':
    unittest.main()


