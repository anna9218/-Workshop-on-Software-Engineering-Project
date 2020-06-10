"""
    test suite class - used to organize the tests and run them together
"""
import unittest
from src.test.BlackBoxTests.AcceptanceTests import UcTests
from src.test.BlackBoxTests.AcceptanceTests.UcTests.AppointManagerTest import AppointManagerTest as Test6
from src.test.BlackBoxTests.AcceptanceTests.UcTests.AppointOwnerTest import AppointOwnerTest as Test2
from src.test.BlackBoxTests.AcceptanceTests.UcTests.DefineAndEditPoliciesTest import DefineAndUpdatePoliciesTest as Test3
from src.test.BlackBoxTests.AcceptanceTests.UcTests.DeliverySystemTest import DeliverySystemTest as Test4
from src.test.BlackBoxTests.AcceptanceTests.UcTests.EditManagerPermissionsTest import EditManagerPermissionsTest as Test5
from src.test.BlackBoxTests.AcceptanceTests.UcTests.InitSystemTest import InitSystemTest as Test1
from src.test.BlackBoxTests.AcceptanceTests.UcTests.LoginTest import LoginTest as Test7
from src.test.BlackBoxTests.AcceptanceTests.UcTests.LogoutTest import LogoutTest as Test8
from src.test.BlackBoxTests.AcceptanceTests.UcTests.ManageStockTest import ManageStockTest as Test10
from src.test.BlackBoxTests.AcceptanceTests.UcTests.ManageStoreTest import ManageStoreTest as Test9
from src.test.BlackBoxTests.AcceptanceTests.UcTests.OpenStoreTest import OpenStoreTest as Test11
from src.test.BlackBoxTests.AcceptanceTests.UcTests.PaymentSystemTest import PaymentSystemTest as Test12
from src.test.BlackBoxTests.AcceptanceTests.UcTests.PurchaseProductsTest import PurchaseProductsTest as Test13
from src.test.BlackBoxTests.AcceptanceTests.UcTests.RegisterTest import RegisterTest as Test14
from src.test.BlackBoxTests.AcceptanceTests.UcTests.RemoveStoreManagerTest import RemoveStoreManagerTest as Test15
from src.test.BlackBoxTests.AcceptanceTests.UcTests.SaveProductsTest import SaveProductsTest as Test16
from src.test.BlackBoxTests.AcceptanceTests.UcTests.SearchProductsTest import SearchProductsTest as Test17
from src.test.BlackBoxTests.AcceptanceTests.UcTests.UpdateCartTest import UpdateCartTest as Test18
from src.test.BlackBoxTests.AcceptanceTests.UcTests.ViewPersonalHistoryTest import ViewPersonalHistoryTest as Test19
from src.test.BlackBoxTests.AcceptanceTests.UcTests.ViewShopHistoryTest import ViewShopHistoryTest as Test20
from src.test.BlackBoxTests.AcceptanceTests.UcTests.ViewStoreInfoTest import ViewStoreInfoTest as Test21
from src.test.BlackBoxTests.AcceptanceTests.UcTests.ViewStoresAndUsersPurchaseHistoryTest import ViewStoresAndUsersPurchaseHistoryTest as Test22


class BlackBoxTestsRunner:
    # Build test suit
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()

    # add all tests in package UcTests (all acceptance tests) to test suite
    # suite.addTests(loader.loadTestsFromModule(UcTests))

    # add individual tests to the test suite
    suite.addTest(loader.loadTestsFromTestCase(Test1))
    suite.addTest(loader.loadTestsFromTestCase(Test2))
    suite.addTest(loader.loadTestsFromTestCase(Test3))
    suite.addTest(loader.loadTestsFromTestCase(Test4))
    suite.addTest(loader.loadTestsFromTestCase(Test5))
    suite.addTest(loader.loadTestsFromTestCase(Test6))
    suite.addTest(loader.loadTestsFromTestCase(Test7))
    suite.addTest(loader.loadTestsFromTestCase(Test8))
    suite.addTest(loader.loadTestsFromTestCase(Test9))
    suite.addTest(loader.loadTestsFromTestCase(Test10))
    suite.addTest(loader.loadTestsFromTestCase(Test11))
    suite.addTest(loader.loadTestsFromTestCase(Test12))
    suite.addTest(loader.loadTestsFromTestCase(Test13))
    suite.addTest(loader.loadTestsFromTestCase(Test14))
    suite.addTest(loader.loadTestsFromTestCase(Test15))
    suite.addTest(loader.loadTestsFromTestCase(Test16))
    suite.addTest(loader.loadTestsFromTestCase(Test17))
    suite.addTest(loader.loadTestsFromTestCase(Test18))
    suite.addTest(loader.loadTestsFromTestCase(Test19))
    suite.addTest(loader.loadTestsFromTestCase(Test20))
    suite.addTest(loader.loadTestsFromTestCase(Test21))
    suite.addTest(loader.loadTestsFromTestCase(Test22))

    # pass runner the suite and run it
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)


if __name__ == '__main__':
    unittest.main()


