"""
    test class for use case 1.1 - initialization
"""
from src.test.BlackBoxTests.AcceptanceTests.ProjectTest import ProjectTest


class InitSystemTest(ProjectTest):

    def setUp(self) -> None:
        super().setUp()

    def test_success(self):
        try:
            res = self.init_sys()
            self.assertTrue(res)
        except ResourceWarning:
            self.assertTrue(True, "System down warning")

    def test_fail(self):
        self.test_communication_error_payment()
        self.test_communication_error_delivery()

    def test_communication_error_payment(self):
        try:
            # communication error with payment
            res = self.init_sys()
            self.cause_connection_err_payment()
            self.assertTrue(False)
        except ResourceWarning:
            self.assertTrue(True, "System down warning")

    def test_communication_error_delivery(self):
        try:
            # communication error with delivery
            res = self.init_sys()
            self.cause_connection_err_delivery()
            self.assertTrue(False)
        except ResourceWarning:
            self.assertTrue(True, "System down warning")

    # @logger
    def tearDown(self) -> None:
        self.delete_user("TradeManager")

    def __repr__(self):
        return repr("InitSystemTest")