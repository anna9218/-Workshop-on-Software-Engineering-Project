from src.main.DomainLayer.Appointment import Appointment
from src.main.DomainLayer.Registration import Registration
from src.main.DomainLayer.Login import Login
from src.main.DomainLayer.Logout import Logout


class User:
    def __init__(self, trade_control):
        self.__registrationState = Registration()
        self.__loginState = Login()
        self.__logoutState = Logout()
        self.__appointment = Appointment()
        self.__tradeControl = trade_control

    def register(self, username, password):
        ackMSG = self.__registrationState.register(self, username, password)
        if ackMSG:
            print("registered successfully")
        else:
            print("something failed, please try again")
            
    def login(self, username, password):
        ackMSG = self.__loginState.login(self, username, password)
        if ackMSG:
            print("logged in successfully")
        else:
            print("error while logging in")

    def logout(self):
        ackMSG = self.__logoutState.logout(self)
        print("logged out successfully")

    def open_store(self, store_name) -> bool:
        if self.__loginState.is_logged_in():
            new_store = self.__tradeControl.open_store(self, store_name)
            if new_store is None:
                return False
            else:
                return self.__appointment.appoint_owner(None, self, new_store)

    def get_trade_control(self):
        return self._tradeControl

    def get_login(self):
        return self.__loginState

    def get_logout(self):
        return self.__logoutState

    def get_registration(self):
        return self.__registrationState

    # def get_name(self):
    #     return self.__name
    #
    # def set_price(self, new_price):
    #     self.__price = new_price
    #
    # def set_name(self, new_name):
    #     self.__name = new_name