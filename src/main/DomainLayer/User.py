from src.main.DomainLayer.Appointment import Appointment
from src.main.DomainLayer.Registration import Registration
from src.main.DomainLayer.Login import Login
from src.main.DomainLayer.Logout import Logout
from src.main.DomainLayer.TradeControl import TradeControl


class User:
    def __init__(self):
        self.__registrationState = Registration()
        self.__loginState = Login()
        self.__logoutState = Logout()
        self.__appointment = Appointment()
        self.__tradeControl = TradeControl.getInstance()

    def register(self, username, password):
        self.__registrationState.register(username, password)
        # if ackMSG:
        #     print("registered successfully")
        # else:
        #     print("something failed, please try again")
            
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
        # if self.__loginState.is_logged_in():
        #     new_store = self.__tradeControl.open_store(self, store_name)
            if new_store is None:
                return False
            else:
                return self.__appointment.appoint_owner(None, self, new_store)

    def is_loggedIn(self):
        return self.__loginState.is_logged_in()

    def get_trade_control(self):
        return self._tradeControl

    def get_login(self):
        return self.__loginState

    def get_logout(self):
        return self.__logoutState

    def get_registration(self):
        return self.__registrationState.is_registered()

    def getName(self):
        return self.__registrationState.get_username()

    # def get_name(self):
    #     return self.__name
    #
    # def set_price(self, new_price):
    #     self.__price = new_price
    #
    # def set_name(self, new_name):
    #     self.__name = new_name