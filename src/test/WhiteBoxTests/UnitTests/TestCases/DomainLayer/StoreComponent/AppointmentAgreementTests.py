import unittest
from unittest.mock import MagicMock

from src.main.DomainLayer.StoreComponent.AppiontmentAgreement import AppointmentAgreement
from src.main.DomainLayer.StoreComponent.AppointmentStatus import AppointmentStatus
from src.main.DomainLayer.TradeComponent.TradeControl import TradeControl
from src.main.DomainLayer.UserComponent.User import User


class AppointmentAgreementTests(unittest.TestCase):
    def setUp(self):
        self.__appointer_mock = User()
        self.__appointee_mock = User()
        self.__participant_owner = User()
        self.__participants = [self.__appointer_mock, self.__participant_owner]
        self.__appointer_mock.get_nickname = MagicMock(return_value="appointer-nickname")
        self.__appointee_mock.get_nickname = MagicMock(return_value="appointee-nickname")
        self.__participant_owner.get_nickname = MagicMock(return_value="participant-nickname")
        self.__trade_control_mock = TradeControl.get_instance()

        self.__appointment_agreement_1 = AppointmentAgreement(self.__appointer_mock, self.__appointee_mock,
                                                            self.__participants)
        self.__appointment_agreement_2 = AppointmentAgreement(self.__appointer_mock, self.__appointee_mock,
                                                            [self.__appointer_mock])

    def test_init_agreement_participants(self):
        self.assertEqual(AppointmentStatus.PENDING,  self.__appointment_agreement_1.get_appointment_status())
        self.assertEqual(self.__appointment_agreement_1.get_appointer(), self.__appointer_mock)

        self.assertEqual(AppointmentStatus.APPROVED, self.__appointment_agreement_2.get_appointment_status())
        self.assertEqual(self.__appointment_agreement_2.get_appointer(), self.__appointer_mock)

    def test_update_agreement_participants(self):
        res = self.__appointment_agreement_1.update_agreement_participants("participant-nickname",
                                                                           AppointmentStatus.APPROVED)
        self.assertTrue(res)
        participants = self.__appointment_agreement_1.get_agreement_participants()
        for participant in participants:
            if participant["participant"].get_nickname() == "participant-nickname":
                self.assertEqual(participant["status"], AppointmentStatus.APPROVED)

    def test_check_appointment_status(self):
        res = self.__appointment_agreement_1.check_appointment_status()
        self.assertTrue(res)
        self.assertEqual(self.__appointment_agreement_1.get_appointment_status(), AppointmentStatus.PENDING)

        res = self.__appointment_agreement_2.check_appointment_status()
        self.assertTrue(res)
        self.assertEqual(self.__appointment_agreement_2.get_appointment_status(), AppointmentStatus.APPROVED)

    def tearDown(self) -> None:
        self.__appointment_agreement_1 = None
        self.__appointment_agreement_2 = None

    def __repr__(self):
        return repr("AppointmentAgreementTests")
