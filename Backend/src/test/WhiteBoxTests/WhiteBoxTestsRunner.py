"""
    test suite class - used to organize the tests and run them together
"""
import unittest
from Backend.src.test.WhiteBoxTests.UnitTests.TestCases.DomainLayer.PaymentComponent.FacadePaymentTests import FacadePaymentTests
from Backend.src.test.WhiteBoxTests.UnitTests.TestCases.DomainLayer.DeliveryComponent.FacadeDeliveryTests import FacadeDeliveryTests


class WhiteBoxTestsRunner:
    # Build test suit
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()

    # add all tests in package UcTests (all acceptance tests) to test suite
    # suite.addTests(loader.loadTestsFromModule(TestCases))

    # add individual tests to the test suite
    suite.addTest(loader.loadTestsFromTestCase(FacadePaymentTests))
    suite.addTest(loader.loadTestsFromTestCase(FacadeDeliveryTests))

    # pass runner the suite and run it
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

    if __name__ == '__main__':
        unittest.main()


