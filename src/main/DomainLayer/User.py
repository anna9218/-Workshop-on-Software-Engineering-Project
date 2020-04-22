from src.main.DomainLayer.Registration import Registration
from src.main.DomainLayer.Login import Login
from src.main.DomainLayer.Logout import Logout
from src.main.DomainLayer.TradeControl import TradeControl


class User:
    def __init__(self):
        self.registrationState = Registration()
        self.loginState = Login()
        self.logoutState = Logout()
        self.tradeControl = TradeControl()

    def register(self, username, password):
        ackMSG = self.registrationState.register(self, username, password)
        if ackMSG:
            print("registered successfully")
        else:
            print("something failed, please try again")
            
    def login(self, username, password):
        ackMSG = self.loginState.login(self, username, password)
        if ackMSG:
            print("logged in successfully")
        else:
            print("error while logging in")

    def logout(self):
        ackMSG = self.logoutState.logout(self)
        print("logged out successfully")

