"""
    test class for use case 7 - commit transaction via payment system
"""
from src.Logger import logger, errorLogger
from src.test.BlackBoxTests.AcceptanceTests.ProjectTest import ProjectTest
from datetime import datetime as date_time


class PaymentSystemTest(ProjectTest):
    # @logger
    def setUp(self) -> None:
        super().setUp()
        self.connect_payment_sys()

    # @logger
    def test_success(self):
        try:
            res = self.commit_payment({"total_price": 10, "purchases": ["product"]})
            self.assertTrue(res)
        except ResourceWarning:
            errorLogger("System down warning")
            self.assertTrue(True, "System down warning")

    # @logger
    def test_fail(self):
        try:
            # price to purchase is 0
            res = self.commit_payment({"total_price": 0, "purchases": ["product"]})
            self.assertFalse(res)
            # products list to purchase is empty
            res = self.commit_payment({"total_price": 0, "purchases": []})
            self.assertFalse(res)
            # payment system is down test
            self.cause_connection_err_payment()
            self.assertFalse(True)
        except ResourceWarning:
            errorLogger("System down warning")
            self.assertTrue(True, "System down warning")

    # @logger
    def tearDown(self) -> None:
        try:
            self.disconnect_payment_sys()
        except ResourceWarning:
            errorLogger("System down warning")
            self.assertTrue(True, "System down warning")

    def __repr__(self):
        return repr("PaymentSystemTest")