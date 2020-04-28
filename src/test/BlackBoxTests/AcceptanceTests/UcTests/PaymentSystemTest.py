"""
    test class for use case 7 - commit transaction via payment system
"""
from src.Logger import logger, errorLogger
from src.test.BlackBoxTests.AcceptanceTests.ProjectTest import ProjectTest
from datetime import datetime as date_time


class PaymentSystemTest(ProjectTest):
    @logger
    def setUp(self) -> None:
        super().setUp()
        self.connect_payment_sys()
        self.username = "username"
        self.credit = "123"
        self.date = date_time(2021, 6, 1)

    @logger
    def test_success(self):
        try:
            result = self.commit_payment(self.username, 10, self.credit, self.date)
            self.assertEqual(True, result)
        except ResourceWarning:
            errorLogger("System down warning")
            self.assertTrue(True, "System down warning")

    @logger
    def test_fail(self):
        try:
            self.disconnect_payment_sys()
            result = self.commit_payment("", 10, self.credit, self.date)
            self.assertEqual(False, result)
        except ResourceWarning:
            errorLogger("System down warning")
            self.assertTrue(True, "System down warning")

    @logger
    def tearDown(self) -> None:
        try:
            super().disconnect_payment_sys()
        except ResourceWarning:
            errorLogger("System down warning")
            self.assertTrue(True, "System down warning")
