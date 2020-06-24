import unittest
from unittest.mock import MagicMock
from src.main.DomainLayer.PaymentComponent.PaymentProxy import PaymentProxy
from src.main.DomainLayer.PaymentComponent.RealPayment import RealPayment


class FacadePaymentTests(unittest.TestCase):

    def setUp(self) -> None:
        self.__payment_sys: PaymentProxy = PaymentProxy.get_instance()
        self.__real_payment_mock = RealPayment()
        self.__payment_sys.set_real(self.__real_payment_mock)
        self.__payment_details = {'card_number': "123", 'month': "march", 'year': "1991", 'holder': "s",
                                  'ccv': "111", 'id': "333"}

    def test_is_connected(self):
        # test that system is connected fine
        self.__real_payment_mock.is_connected = MagicMock(return_value=True)
        self.assertTrue(self.__payment_sys.is_connected())
        # test connection error
        self.__real_payment_mock.is_connected = MagicMock(return_value=False)
        self.assertFalse(self.__payment_sys.is_connected())

    def test_commit_payment(self):
        # test valid payment
        self.__real_payment_mock.commit_payment = MagicMock(return_value={"response": True, "msg": "ok"})
        self.assertTrue(self.__payment_sys.commit_payment(self.__payment_details)["response"])
        # test connection error
        self.__real_payment_mock.is_connected = MagicMock(return_value=False)
        self.assertFalse(self.__payment_sys.commit_payment(self.__payment_details)["response"])
        # test invalid payment details
        self.__real_payment_mock.commit_payment = MagicMock(return_value={"response": False, "msg": "ok"})
        self.assertFalse(self.__payment_sys.commit_payment({'card_number': "123", 'month': "march", 'year': "1991",
                                                            'holder': "s", 'ccv': "111"})["response"])
        self.assertFalse(self.__payment_sys.commit_payment({'card_number': "123", 'month': "march", 'year': "1991",
                                                            'holder': "s", 'id': "333"})["response"])
        self.assertFalse(self.__payment_sys.commit_payment({'card_number': "123", 'month': "march", 'year': "1991",
                                                            'ccv': "111", 'id': "333"})["response"])
        self.assertFalse(self.__payment_sys.commit_payment({'card_number': "123", 'month': "march",
                                                            'holder': "s", 'ccv': "111", 'id': "333"})["response"])
        self.assertFalse(self.__payment_sys.commit_payment({'card_number': "123", 'year': "1991",
                                                            'holder': "s", 'ccv': "111", 'id': "333"})["response"])
        self.assertFalse(self.__payment_sys.commit_payment({'month': "march", 'year': "1991",
                                                            'holder': "s", 'ccv': "111", 'id': "333"})["response"])
        self.assertFalse(self.__payment_sys.commit_payment({'card_number': "123", 'month': "march", 'year': "1991",
                                                            'holder': "s"})["response"])
        self.assertFalse(self.__payment_sys.commit_payment({'card_number': "123", 'month': "march",
                                                            'year': "1991", })["response"])
        self.assertFalse(self.__payment_sys.commit_payment({'card_number': "123", 'month': "march"})["response"])
        self.assertFalse(self.__payment_sys.commit_payment({'card_number': "123"})["response"])

    def test_cancel_supply(self):
        # test valid payment cancellation
        self.__real_payment_mock.cancel_pay = MagicMock(return_value={"response": True, "msg": "ok"})
        self.assertTrue(self.__payment_sys.cancel_pay("2020")["response"])
        # test connection error
        self.__real_payment_mock.is_connected = MagicMock(return_value=False)
        self.assertFalse(self.__payment_sys.cancel_pay("2020")["response"])
        # test invalid transaction number
        self.__real_payment_mock.cancel_pay = MagicMock(return_value={"response": False, "msg": "ok"})
        self.assertFalse(self.__payment_sys.cancel_pay("-1")["response"])
        self.assertFalse(self.__payment_sys.cancel_pay("")["response"])
        self.assertFalse(self.__payment_sys.cancel_pay("90")["response"])

    if __name__ == '__main__':
        unittest.main()

    def __repr__(self):
        return repr ("FacadePaymentTests")
