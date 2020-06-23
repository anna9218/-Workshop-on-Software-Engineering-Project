from src.Logger import logger
from src.main.DomainLayer.StoreComponent.AppointmentStatus import AppointmentStatus
from src.main.DomainLayer.UserComponent.User import User


class AppointmentAgreement:
    def __init__(self, appointer: User, appointee: User, agreement_participants: list):
        self.__appointee = appointee
        self.__appointer = appointer
        self.__agreement_status = AppointmentStatus.PENDING
        self.__agreement_participants: [{"participant": User, "status": AppointmentStatus}] = []
        self.init_agreement_participants(agreement_participants)

    def init_agreement_participants(self, agreement_participants: list):
        for participant in agreement_participants:
            if participant.get_nickname() == self.__appointer.get_nickname():
                # set appointer's response as approved
                self.__agreement_participants.append({"participant": participant, "status": AppointmentStatus.APPROVED})
            else:
                # set any other owner's response as pending
                self.__agreement_participants.append({"participant": participant, "status": AppointmentStatus.PENDING})
        # if there's only one owner - set the appointments status as approved
        if len(agreement_participants) == 1:
            self.set_appointment_status(AppointmentStatus.APPROVED)
        return True

    def get_appointment_status(self) -> AppointmentStatus:
        return self.__agreement_status

    def set_appointment_status(self, status: AppointmentStatus):
        self.__agreement_status = status

    def get_appointer(self) -> User:
        return self.__appointer

    def get_appointee(self) -> User:
        return self.__appointee

    def get_agreement_participants(self) -> list:
        return self.__agreement_participants

    def update_agreement_participants(self, owner_nickname: str, owner_response: AppointmentStatus) -> bool:
        """
        Updates the response of a specific owner (received as an argument)
        Checks if it's possible to determine the status of the agreement already
        :param owner_nickname: nickname of an owner participating in the appointment agreement
        :param owner_response: owners response - can be DECLINED = 1, PENDING = 2, APPROVED = 3
        :return: True if the response was updated successfully, otherwise false
        """
        for participant in self.__agreement_participants:
            if participant["participant"].get_nickname() == owner_nickname:
                participant["status"] = owner_response
                self.check_appointment_status()
                return True
        return False

    def check_appointment_status(self) -> bool:
        """
        Check if some owner declined the appointment - sets the appointment status to DECLINED
        Checks if all owners approved the appointment - sets the appointment status to APPROVED
        :return: True upon successful update, otherwise False
        """
        is_approved = True
        for participant in self.__agreement_participants:
            if participant["status"] == AppointmentStatus.DECLINED:
                self.set_appointment_status(AppointmentStatus.DECLINED)
                is_approved = False
                break
            elif participant["status"] == AppointmentStatus.PENDING:
                is_approved = False
                break
        if is_approved:
            self.set_appointment_status(AppointmentStatus.APPROVED)
        return True

    def __repr__(self):
        return repr("AppointmentAgreement")

    def __iter__(self):
        self.__i = 0
        return self

    def __next__(self):
        while self.__i < len(self.__agreement_participants):
            x = self.__agreement_participants[self.__i]
            self.__i += 1
            return x
        else:
            raise StopIteration
