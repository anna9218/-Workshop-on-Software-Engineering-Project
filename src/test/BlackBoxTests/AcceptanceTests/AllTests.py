"""
    test suite class - used to organize the tests and run them together
"""
import unittest
from src.test.BlackBoxTests.AcceptanceTests.UcTests.DeliverySystemTest import DeliverySystemTest
from src.test.BlackBoxTests.AcceptanceTests.UcTests.PaymentSystemTest import PaymentSystemTest
from src.test.BlackBoxTests.AcceptanceTests.UcTests.RegisterTest import RegisterTest


class AllTests:
    # Build test suit
    suite = unittest.TestSuite()

    # add tests to test suite
    suite.addTest(DeliverySystemTest())
    suite.addTest(PaymentSystemTest())
    # suite.addTest(RegisterTest())

    runner = unittest.TextTestRunner()
    # pass runner the suite and run it
    runner.run(suite)




