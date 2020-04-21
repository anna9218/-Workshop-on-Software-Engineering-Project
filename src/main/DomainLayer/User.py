from src.main.DomainLayer.Logout import Logout


class User:
    def __init__(self):
        self.logoutState = Logout()

    def logout(self):
        ackMSG = self.logoutState.logout(self)
        print("logged out successfully")