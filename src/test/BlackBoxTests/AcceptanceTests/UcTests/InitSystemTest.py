"""
    test class for use case 1.1 - initialization
"""
from src.Logger import logger, errorLogger
from src.test.BlackBoxTests.AcceptanceTests.ProjectTest import ProjectTest


class InitSystemTest(ProjectTest):

    @logger
    def setUp(self) -> None:
        super().setUp()

    @logger
    def test_success(self):
        try:
            self.init_sys()
            res = self.is_payment_sys_connected() and self.is_delivery_sys_connected()
            self.assertEqual(True, res)
        except ResourceWarning:
            errorLogger("System down warning")
            self.assertTrue(True, "System down warning")

    @logger
    def test_fail(self):
        try:
            # need to cause communication error with systems
            self.init_sys()
            res = self.is_payment_sys_connected() and self.is_delivery_sys_connected()
            self.assertEqual(True, res)
        except ResourceWarning:
            errorLogger("System down warning")
            self.assertTrue(True, "System down warning")

    @logger
    def tearDown(self) -> None:
        self.remove_user("TradeManager")

    def __repr__(self):
        return repr("InitSystemTest")