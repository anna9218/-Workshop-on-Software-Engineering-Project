"""
    test suite class - used to test V1 Features.
"""
import unittest
# from src.test.WhiteBoxTests.RegressionTests.Version1.SystemManagerRoleTests import SystemManagerRoleTests as \
#     SystemManagerRoleTests_V1
# from src.test.WhiteBoxTests.RegressionTests.Version1.SubscriberRoleTests import SubscriberRoleTests as \
#     SubscriberRoleTests_V1
# from src.test.WhiteBoxTests.RegressionTests.Version1.StoreOwnerOrManagerTests import StoreOwnerOrManagerTests \
#     as StoreOwnerOrManagerTests_V1
# from src.test.WhiteBoxTests.RegressionTests.Version1.GuestRoleTests import GuestRoleTest as \
#     GuestRoleTests_V1
from src.main.DataAccessLayer.ConnectionProxy.Tables import rel_path
from src.main.DataAccessLayer.DataAccessFacade import DataAccessFacade


class RegressionTestsRunner:
    # Build test suit
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()

    # add individual tests to the test suite for version 1
    # suite.addTest(loader.loadTestsFromTestCase(SystemManagerRoleTests_V1))
    # suite.addTest(loader.loadTestsFromTestCase(SubscriberRoleTests_V1))
    # suite.addTest(loader.loadTestsFromTestCase(StoreOwnerOrManagerTests_V1))
    # suite.addTest(loader.loadTestsFromTestCase(GuestRoleTests_V1))

    if not ("testing" in rel_path):
        raise ReferenceError("The Data Base is not the testing data base.\n"
                             "\t\t\t\tPlease go to src.main.DataAccessLayer.ConnectionProxy.RealDb.rel_path\n"
                             "\t\t\t\t and change rel_path to test_rel_path.\n"
                             "\t\t\t\tThanks :D")

    # pass runner the suite and run it
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

    (DataAccessFacade.get_instance()).delete_purchases()
    # (DataAccessFacade.get_instance()).delete_discount_policies()
    (DataAccessFacade.get_instance()).delete_statistics()
    (DataAccessFacade.get_instance()).delete_store_owner_appointments()
    (DataAccessFacade.get_instance()).delete_products_in_baskets()
    (DataAccessFacade.get_instance()).delete_products()
    (DataAccessFacade.get_instance()).delete_store_manager_appointments()
    (DataAccessFacade.get_instance()).delete_stores()
    (DataAccessFacade.get_instance()).delete_users()


if __name__ == '__main__':
    unittest.main()


