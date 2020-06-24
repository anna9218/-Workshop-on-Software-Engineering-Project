"""
    test class for use case 7 - commit transaction via payment system
"""
from src.Logger import errorLogger
from src.test.BlackBoxTests.AcceptanceTests.ProjectAT import ProjectAT


class PaymentSystemTest(ProjectAT):
    def setUp(self) -> None:
        super().setUp()
        self.__payment_details = {'card_number': "123", 'month': "march", 'year': "1991", 'holder': "s",
                                               'ccv': "111", 'id': "333"}

    def test_success(self):
        # test payment system connection
        res = self.is_payment_sys_connected()
        self.assertTrue(res)
        # test successful payment
        res = self.commit_payment(self.__payment_details)
        self.assertTrue(res)
        # test successful payment cancellation
        tid = res.get("tid")
        self.assertTrue(tid is not None and self.cancel_payment_supply(tid))

    def test_fail(self):
        # test connection error with external system
        self.cause_payment_con_error()
        res = self.commit_payment(self.__payment_details)
        self.assertFalse(res["response"])
        self.set_connection_payment_back()
        # test communication error with the server (timeout error)
        self.cause_payment_timeout()
        res = self.commit_payment(self.__payment_details)
        self.assertFalse(res["response"])
        self.set_connection_payment_back()

    def tearDown(self) -> None:
        pass

    def __repr__(self):
        return repr("PaymentSystemTest")