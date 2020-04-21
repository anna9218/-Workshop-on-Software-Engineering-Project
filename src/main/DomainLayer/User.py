from src.main.DomainLayer.Logout import Logout
from src.main.DomainLayer.Registration import Registration


class User:
    def __init__(self):
        self.registrationState = Registration()
        self.logoutState = Logout()

    def logout(self):
        ackMSG = self.logoutState.logout(self)
        print("logged out successfully")

    def register(self, username, password):
        ackMSG = self.registrationState.register(self, username, password)
        if ackMSG:
            print("registered successfully")
        else:
            print("something failed, please try again")

