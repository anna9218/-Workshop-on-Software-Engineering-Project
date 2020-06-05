"""
    test suite class - used to organize the tests and run them together
"""
import unittest
from src.test.WhiteBoxTests.UnitTests import TestCases
# ---------------------------------- unit tests -----------------------------------------------------------------------
from src.test.WhiteBoxTests.UnitTests.TestCases.DomainLayer.DeliveryComponent.FacadeDeliveryTests \
    import FacadeDeliveryTests as Uc1
from src.test.WhiteBoxTests.UnitTests.TestCases.DomainLayer.PaymentComponent.FacadePaymentTests \
    import FacadePaymentTests as Uc2
from src.test.WhiteBoxTests.UnitTests.TestCases.DomainLayer.StoreComponent.PurchasePolicyComposite.Leaves.\
    BundleDealPolicyTests import BundleDealPolicyTests as Uc3
from src.test.WhiteBoxTests.UnitTests.TestCases.DomainLayer.StoreComponent.PurchasePolicyComposite.Leaves.\
    MaxAmountPolicyTests import MaxAmountPolicyTests as Uc4
from src.test.WhiteBoxTests.UnitTests.TestCases.DomainLayer.StoreComponent.PurchasePolicyComposite.Leaves.\
    MinAmountPolicyTests import MinAmountPolicyTests as Uc5
from src.test.WhiteBoxTests.UnitTests.TestCases.DomainLayer.StoreComponent.PurchasePolicyComposite.Leaves.\
    ProhibitedDatePolicyTests import ProhibitedDatePolicyTests as Uc6
from src.test.WhiteBoxTests.UnitTests.TestCases.DomainLayer.StoreComponent.PurchasePolicyComposite.PurchasePolicyTests\
    import PurchasePolicyTests as Uc7
from src.test.WhiteBoxTests.UnitTests.TestCases.DomainLayer.StoreComponent.StoreInventoryTests \
    import StoreInventoryTests as Uc8
from src.test.WhiteBoxTests.UnitTests.TestCases.DomainLayer.StoreComponent.StoreTests \
    import StoreTests as Uc9
from src.test.WhiteBoxTests.UnitTests.TestCases.DomainLayer.TradeComponent.TradeControlTestCase \
    import TradeControlTestCase as Uc10
from src.test.WhiteBoxTests.UnitTests.TestCases.DomainLayer.UserComponent.ShoppingBasketTests \
    import ShoppingBasketTests as Uc11
from src.test.WhiteBoxTests.UnitTests.TestCases.DomainLayer.UserComponent.ShoppingCartTests \
    import ShoppingCartTests as Uc12
from src.test.WhiteBoxTests.UnitTests.TestCases.DomainLayer.UserComponent.UserTests \
    import UserTests as Uc13
from src.test.WhiteBoxTests.UnitTests.TestCases.ServiceLayer.StoreOwnerOrManagerTests \
    import StoreOwnerOrManagerTests as Uc14
from src.test.WhiteBoxTests.UnitTests.TestCases.ServiceLayer.SubscriberRoleTests \
    import SubscriberRoleTests as Uc15
from src.test.WhiteBoxTests.UnitTests.TestCases.ServiceLayer.SystemManagerRoleTests \
    import SystemManagerRoleTests as Uc16
from src.test.WhiteBoxTests.UnitTests.TestCases.ServiceLayer.TradeControlServiceTests \
    import TradeControlServiceTests as Uc17
from src.test.WhiteBoxTests.UnitTests.TestCases.ServiceLayer.GuestRoleTests \
    import GuestRoleTest as Uc18
# ---------------------------------- unit tests end --------------------------------------------------------------------


class WhiteBoxTestsRunner:
    # Build test suit
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()

    # add all tests to test suite
    suite.addTests(loader.loadTestsFromModule(TestCases))

    # add individual tests to the test suite
# ---------------------------------- add unit tests --------------------------------------------------------------------
    suite.addTest(loader.loadTestsFromTestCase(Uc1))
    suite.addTest(loader.loadTestsFromTestCase(Uc2))
    suite.addTest(loader.loadTestsFromTestCase(Uc3))
    suite.addTest(loader.loadTestsFromTestCase(Uc4))
    suite.addTest(loader.loadTestsFromTestCase(Uc5))
    suite.addTest(loader.loadTestsFromTestCase(Uc6))
    suite.addTest(loader.loadTestsFromTestCase(Uc7))
    suite.addTest(loader.loadTestsFromTestCase(Uc8))
    suite.addTest(loader.loadTestsFromTestCase(Uc9))
    suite.addTest(loader.loadTestsFromTestCase(Uc10))
    suite.addTest(loader.loadTestsFromTestCase(Uc11))
    suite.addTest(loader.loadTestsFromTestCase(Uc12))
    suite.addTest(loader.loadTestsFromTestCase(Uc13))
    suite.addTest(loader.loadTestsFromTestCase(Uc14))
    suite.addTest(loader.loadTestsFromTestCase(Uc15))
    suite.addTest(loader.loadTestsFromTestCase(Uc16))
    suite.addTest(loader.loadTestsFromTestCase(Uc17))
    suite.addTest(loader.loadTestsFromTestCase(Uc18))
# ---------------------------------- add unit tests end ----------------------------------------------------------------

    # pass runner the suite and run it
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

    if __name__ == '__main__':
        unittest.main()


