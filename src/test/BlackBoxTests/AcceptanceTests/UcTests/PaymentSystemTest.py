"""
    test class for use case 7 - commit transaction via payment system
"""
from src.Logger import errorLogger
from src.test.BlackBoxTests.AcceptanceTests.ProjectAT import ProjectAT


class PaymentSystemTest(ProjectAT):
    def setUp(self) -> None:
        super().setUp()
        self.connect_payment_sys()

    def test_success(self):
        try:
            res = self.commit_payment({"total_price": 10, "purchases": ["product"]})
            self.assertTrue(res)
        except ResourceWarning:
            self.assertTrue(True, "System down warning")

    def test_fail(self):
        try:
            # price to purchase is 0
            res = self.commit_payment({"total_price": 0, "purchases": ["product"]})
            self.assertFalse(res['response'])
            # products list to purchase is empty
            res = self.commit_payment({"total_price": 0, "purchases": []})
            self.assertFalse(res['response'])
            # payment system is down test
            self.cause_connection_err_payment()
            self.assertFalse(True)
        except ResourceWarning:
            # errorLogger("System down warning")
            self.assertTrue(True, "System down warning")

    def tearDown(self) -> None:
        try:
            self.disconnect_payment_sys()
        except ResourceWarning:
            # errorLogger("System down warning")
            self.assertTrue(True, "System down warning")

    def __repr__(self):
        return repr("PaymentSystemTest")