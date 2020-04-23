"""
    test class for use case 8 - commit transaction via delivery system
"""
from src.test.BlackBoxTests.AcceptanceTests.ProjectTest import ProjectTest


class DeliverySystemTest(ProjectTest):

    def setUp(self) -> None:
        super().setUp()
        super().connect_delivery_sys()
        self.__username = "username"
        self.__good_address = "some address 12"
        self.__bad_input = ""

    def test_success(self):
        try:
            result = super().deliver(self.__username, self.__good_address)
            self.assertEqual(True, result)
        except ResourceWarning:
            self.assertTrue(True, "System down warning")

    def test_fail(self):
        try:
            result = super().deliver(self.__bad_input, self.__good_address)
            self.assertEqual(False, result)
        except ResourceWarning:
            self.assertTrue(True, "System down warning")

    def tearDown(self) -> None:
        try:
            super().disconnect_delivery_sys()
        except ResourceWarning:
            self.assertTrue(True, "System down warning")
