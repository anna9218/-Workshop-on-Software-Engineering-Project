"""
    test class for use case 1.1 - initialization
"""
from src.Logger import errorLogger
from src.test.BlackBoxTests.AcceptanceTests.ProjectAT import ProjectAT


class InitSystemTest(ProjectAT):

    def setUp(self) -> None:
        super().setUp()

    def test_success(self):
        res = self.init_sys()
        self.assertTrue(res)

    def test_fail(self):
        self.test_communication_error_payment()
        self.test_communication_error_delivery()

    def test_communication_error_payment(self):
        # test connection error with external system
        self.cause_payment_con_error()
        res = self.init_sys()
        self.assertFalse(res)
        self.set_connection_payment_back()
        # test communication error with the server (timeout error)
        self.cause_payment_timeout()
        res = self.init_sys()
        self.assertFalse(res)
        self.set_connection_payment_back()

    def test_communication_error_delivery(self):
        # test connection error with external system
        self.cause_delivery_con_error()
        res = self.init_sys()
        self.assertFalse(res)
        self.set_connection_delivery_back()
        # test communication error with the server (timeout error)
        self.cause_delivery_timeout()
        res = self.init_sys()
        self.assertFalse(res)
        self.set_connection_delivery_back()

    def tearDown(self) -> None:
        self.delete_user("A1")

    def __repr__(self):
        return repr("InitSystemTest")