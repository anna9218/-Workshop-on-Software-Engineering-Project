import unittest
from src.main.DomainLayer.FacadePayment import FacadePayment
from datetime import datetime as date_time


class FacadePaymentTests(unittest.TestCase):

    def setUp(self) -> None:
        self.__payment_sys = FacadePayment.get_instance()
        self.__payment_sys.connect()
        self.__valid_username = "username"
        self.__valid_date = date_time(2021, 12, 21)
        self.__valid_credit = "123456789"
        self.__wrong_input = ""
        self.__passed_date = date_time(2012, 12, 21)

    def test_connection(self):
        # test that system is connected fine
        self.assertEqual(True, self.__payment_sys.is_connected())

        # test that the system disconnect fine
        self.__payment_sys.disconnect()
        self.assertEqual(False, self.__payment_sys.is_connected())

    def test_wrong_input(self):
        # valid user, amount, credit + invalid date
        res = self.__payment_sys.commit_payment(self.__valid_username, 10, self.__valid_credit, self.__wrong_input)
        self.assertEqual(False, res)
        # valid user, amount, credit + invalid date
        res = self.__payment_sys.commit_payment(self.__valid_username, 10, self.__valid_credit, self.__passed_date)
        self.assertEqual(False, res)
        # valid user, amount, date + invalid credit
        res = self.__payment_sys.commit_payment(self.__valid_username, 10, self.__wrong_input, self.__valid_date)
        self.assertEqual(False, res)
        # valid user, credit, date + invalid amount
        res = self.__payment_sys.commit_payment(self.__valid_username, -10, self.__valid_credit, self.__valid_date)
        self.assertEqual(False, res)
        # valid amount, credit, date + invalid user
        res = self.__payment_sys.commit_payment(self.__wrong_input, 10, self.__valid_credit, self.__valid_date)
        self.assertEqual(False, res)
        # all data invalid
        res = self.__payment_sys.commit_payment(self.__wrong_input, -10, self.__wrong_input, self.__wrong_input)
        self.assertEqual(False, res)
        # all data is valid + system is disconnected
        self.__payment_sys.disconnect()
        res = self.__payment_sys.commit_payment(self.__valid_username, 10, self.__valid_credit, self.__valid_date)
        self.assertEqual(False, res)

    def test_correct_input(self):
        # all valid input
        res = self.__payment_sys.commit_payment(self.__valid_username, 10, self.__valid_credit, self.__valid_date)
        self.assertEqual(True, res)

    def tearDown(self) -> None:
        self.__payment_sys.disconnect()

    if __name__ == '__main__':
        unittest.main()
