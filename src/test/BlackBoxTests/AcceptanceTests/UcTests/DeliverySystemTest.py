"""
    test class for use case 8 - commit transaction via delivery system
"""
from src.Logger import errorLogger
from src.test.BlackBoxTests.AcceptanceTests.ProjectTest import ProjectTest


class DeliverySystemTest(ProjectTest):

    def setUp(self) -> None:
        super().setUp()
        self.connect_delivery_sys()
        self.__address = "some address 12"

    def test_success(self):
        try:
            # [{"product_name", "product_price", "amount"}]}]
            res = self.deliver(self.__address, [{"product_name": "product", "product_price": 10, "amount": 2}])
            self.assertTrue(res)
        except ResourceWarning:
            errorLogger("System down warning")
            self.assertTrue(True, "System down warning")

    def test_fail(self):
        try:
            # invalid address
            res = self.deliver("", [{"product_name": "product", "product_price": 10, "amount": 2}])
            self.assertFalse(res['response'])
            # empty product list
            res = self.deliver(self.__address, [])
            self.assertFalse(res['response'])
        except ResourceWarning:
            errorLogger("System down warning")
            self.assertTrue(True, "System down warning")

    def tearDown(self) -> None:
        try:
            self.disconnect_delivery_sys()
        except ResourceWarning:
            errorLogger("System down warning")
            self.assertTrue(True, "System down warning")

    def __repr__(self):
        return repr("DeliverySystemTest")