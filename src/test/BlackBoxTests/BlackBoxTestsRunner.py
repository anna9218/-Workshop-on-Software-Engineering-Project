"""
    test suite class - used to organize the tests and run them together
"""
import unittest
from Backend.src.test.BlackBoxTests.AcceptanceTests.UcTests.InitSystemTest import InitSystemTest
from Backend.src.test.BlackBoxTests.AcceptanceTests.UcTests.RegisterTest import RegisterTest
from Backend.src.test.BlackBoxTests.AcceptanceTests.UcTests.LoginTest import LoginTest
from Backend.src.test.BlackBoxTests.AcceptanceTests.UcTests.LogoutTest import LogoutTest
from Backend.src.test.BlackBoxTests.AcceptanceTests.UcTests.OpenStoreTest import OpenStoreTest
from Backend.src.test.BlackBoxTests.AcceptanceTests.UcTests.ManageStockTest import ManageStockTest
from Backend.src.test.BlackBoxTests.AcceptanceTests.UcTests.AppointOwnerTest import AppointOwnerTest
from src.test.BlackBoxTests.AcceptanceTests.UcTests.AppointManagerTest import AppointManagerTest
from Backend.src.test.BlackBoxTests.AcceptanceTests.UcTests.RemoveStoreManagerTest import RemoveStoreManagerTest
from Backend.src.test.BlackBoxTests.AcceptanceTests.UcTests.DeliverySystemTest import DeliverySystemTest
from Backend.src.test.BlackBoxTests.AcceptanceTests.UcTests.PaymentSystemTest import PaymentSystemTest
# from Backend.src.test.BlackBoxTests.AcceptanceTests import UcTests


class BlackBoxTestsRunner:
    # Build test suit
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()

    # add all tests in package UcTests (all acceptance tests) to test suite
    # suite.addTests(loader.loadTestsFromModule(UcTests))

    # add individual tests to the test suite
    suite.addTest(loader.loadTestsFromTestCase(InitSystemTest))
    suite.addTest(loader.loadTestsFromTestCase(RegisterTest))
    suite.addTest(loader.loadTestsFromTestCase(LoginTest))
    suite.addTest(loader.loadTestsFromTestCase(LogoutTest))
    suite.addTest(loader.loadTestsFromTestCase(OpenStoreTest))
    suite.addTest(loader.loadTestsFromTestCase(ManageStockTest))
    suite.addTest(loader.loadTestsFromTestCase(AppointOwnerTest))
    suite.addTest(loader.loadTestsFromTestCase(AppointManagerTest))
    suite.addTest(loader.loadTestsFromTestCase(RemoveStoreManagerTest))
    suite.addTest(loader.loadTestsFromTestCase(DeliverySystemTest))
    suite.addTest(loader.loadTestsFromTestCase(PaymentSystemTest))

    # pass runner the suite and run it
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

    if __name__ == '__main__':
        unittest.main()


