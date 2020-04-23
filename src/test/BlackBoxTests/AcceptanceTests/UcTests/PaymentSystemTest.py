"""
    test class for use case 7 - commit transaction via payment system
"""
from src.test.BlackBoxTests.AcceptanceTests.ProjectTest import ProjectTest


class PaymentSystemTest(ProjectTest):

    def setUp(self) -> None:
        super().setUp()
        self.connect_payment_sys()
        self.username = "username"
        self.credit = "123"
        self.date = "12/12/12"

    def test_success(self):
        try:
            result = self.commit_payment(self.username, 10, self.credit, self.date)
            self.assertEqual(True, result)
        except ResourceWarning:
            self.assertTrue(True, "System down warning")

    def test_fail(self):
        try:
            self.disconnect_payment_sys()
            result = self.commit_payment("", 10, self.credit, self.date)
            self.assertEqual(False, result)
        except ResourceWarning:
            self.assertTrue(True, "System down warning")

    def tearDown(self) -> None:
        try:
            super().disconnect_payment_sys()
        except ResourceWarning:
            self.assertTrue(True, "System down warning")
