from src.main.DomainLayer import Registration


class User:
    def __init__(self):
        self.registrationState = Registration()

    def register(self, username, password):
        ackMSG = self.registrationState.register(self, username, password)
        if ackMSG:
            print("registered successfully")
        else:
            print("something failed, please try again")

