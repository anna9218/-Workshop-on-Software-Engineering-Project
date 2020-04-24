"""
    test class for use case 1.1 - initialization
"""
from src.test.BlackBoxTests.AcceptanceTests.ProjectTest import ProjectTest


class InitSystemTest(ProjectTest):

    def setUp(self) -> None:
        super().setUp()

    def test_success(self):
        try:
            self.init_sys()
            res = self.is_payment_sys_connected() and self.is_delivery_sys_connected()
            self.assertEqual(True, res)
        except ResourceWarning:
            self.assertTrue(True, "System down warning")

    def test_fail(self):
        try:
            # need to cause communication error with systems
            self.init_sys()
            res = self.is_payment_sys_connected() and self.is_delivery_sys_connected()
            self.assertEqual(True, res)
        except ResourceWarning:
            self.assertTrue(True, "System down warning")

    def tearDown(self) -> None:
        pass
