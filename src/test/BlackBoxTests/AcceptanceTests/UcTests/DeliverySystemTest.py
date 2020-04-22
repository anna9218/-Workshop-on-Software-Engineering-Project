"""
    test class for use case 8 - commit transaction via delivery system
"""
from src.test.BlackBoxTests.AcceptanceTests.ProjectTest import ProjectTest


class DeliverySystemTest(ProjectTest):

    def setUp(self) -> None:
        self.connect_delivery_sys()
        self.username = "username"
        self.good_address = "some address 12"
        self.bad_input = ""

    def test_success(self):
        result = self.deliver(self.username, self.good_address)
        self.assertEqual(True, result)

    def test_fail(self):
        result = self.deliver(self.bad_input, self.good_address)
        self.assertEqual(False, result)

    def test_fatal_error(self):
        self.reusableTests.test_server_error()

    def tearDown(self) -> None:
        self.disconnect_delivery_sys()
