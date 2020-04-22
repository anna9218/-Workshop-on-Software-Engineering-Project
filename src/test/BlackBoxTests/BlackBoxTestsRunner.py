"""
    test suite class - used to organize the tests and run them together
"""
import unittest
from src.test.BlackBoxTests.AcceptanceTests.UcTests.DeliverySystemTest import DeliverySystemTest
from src.test.BlackBoxTests.AcceptanceTests.UcTests.PaymentSystemTest import PaymentSystemTest
# from src.test.BlackBoxTests.AcceptanceTests.UcTests.RegisterTest import RegisterTest
# from src.test.BlackBoxTests.AcceptanceTests import UcTests


class BlackBoxTestsRunner:
    # Build test suit
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()

    # add all tests in package UcTests (all acceptance tests) to test suite
    # suite.addTests(loader.loadTestsFromModule(UcTests))

    # add individual tests to the test suite
    suite.addTest(loader.loadTestsFromTestCase(DeliverySystemTest))
    suite.addTest(loader.loadTestsFromTestCase(PaymentSystemTest))

    # pass runner the suite and run it
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

    if __name__ == '__main__':
        unittest.main()


