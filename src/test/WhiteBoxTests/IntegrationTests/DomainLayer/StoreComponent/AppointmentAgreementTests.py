import unittest

from src.main.DomainLayer.StoreComponent.AppiontmentAgreement import AppointmentAgreement
from src.main.DomainLayer.StoreComponent.AppointmentStatus import AppointmentStatus
from src.main.DomainLayer.StoreComponent.Store import Store
from src.main.DomainLayer.StoreComponent.StoreAppointment import StoreAppointment
from src.main.DomainLayer.TradeComponent.TradeControl import TradeControl
from src.main.DomainLayer.UserComponent.User import User


class AppointmentAgreementTests(unittest.TestCase):
    # @logger
    def setUp(self):
        self.__store = Store("store")
        self.__appointer = User()
        self.__appointer.register("appointer", "password")
        self.__store.get_owners_appointments().append(StoreAppointment(None, self.__appointer, []))

        self.__appointee = User()
        self.__appointee.register("appointee", "password")

        self.__participant = User()
        self.__participant.register("participant", "password")
        self.__store.get_owners_appointments().append(StoreAppointment(self.__appointer, self.__appointee, []))

        self.__participants = [self.__appointer, self.__participant]

        # agreement with another participant who need to approve the appointment
        self.__appointment_agreement_1 = AppointmentAgreement(self.__appointer, self.__appointee, self.__participants)

        # agreement with just the original owner, no need for anyone to approve
        self.__appointment_agreement_2 = AppointmentAgreement(self.__appointer, self.__appointee, [self.__appointer])

    def test_init_agreement_participants(self):
        self.assertEqual(AppointmentStatus.PENDING, self.__appointment_agreement_1.get_appointment_status())
        self.assertEqual(self.__appointment_agreement_1.get_appointer(), self.__appointer)

        self.assertEqual(AppointmentStatus.APPROVED, self.__appointment_agreement_2.get_appointment_status())
        self.assertEqual(self.__appointment_agreement_2.get_appointer(), self.__appointer)

    def test_update_agreement_participants(self):
        res = self.__appointment_agreement_1.update_agreement_participants("participant", AppointmentStatus.APPROVED)
        self.assertTrue(res)
        participants = self.__appointment_agreement_1.get_agreement_participants()
        for participant in participants:
            if participant["participant"].get_nickname() == "participant":
                self.assertEqual(participant["status"], AppointmentStatus.APPROVED)

    def test_check_appointment_status(self):
        res = self.__appointment_agreement_1.check_appointment_status()
        self.assertTrue(res)
        self.assertEqual(self.__appointment_agreement_1.get_appointment_status(), AppointmentStatus.PENDING)

        res = self.__appointment_agreement_2.check_appointment_status()
        self.assertTrue(res)
        self.assertEqual(self.__appointment_agreement_2.get_appointment_status(), AppointmentStatus.APPROVED)

    def test_circularity(self):
        self.store = Store("storename")
        self.owner_1 = User()
        self.owner_1.register("owner_1", "password")
        self.store.get_owners_appointments().append(StoreAppointment(None, self.owner_1, []))

        self.owner_2 = User()
        self.owner_2.register("owner_2", "password")
        self.store.get_owners_appointments().append(StoreAppointment(self.owner_1, self.owner_2, []))

        self.owner_3 = User()
        self.owner_3.register("owner_3", "password")
        self.store.get_owners_appointments().append(StoreAppointment(self.owner_2, self.owner_3, []))

        # (TradeControl.get_instance()).set_curr_user(self.owner_3)
        # (TradeControl.get_instance()).register_guest("owner_3", "password")
        # (TradeControl.get_instance()).login_subscriber("owner_3", "password")
        # (TradeControl.get_instance()).open_store("storename")

        res = (TradeControl.get_instance()).appoint_additional_owner("owner_1", "storename")
        self.assertFalse(res['response'])

    def tearDown(self) -> None:
        self.__appointment_agreement_1 = None
        self.__appointment_agreement_2 = None

    def __repr__(self):
        return repr("AppointmentAgreementTests")
