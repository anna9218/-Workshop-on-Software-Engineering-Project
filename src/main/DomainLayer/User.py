from src.main.DomainLayer.Login import Login


class User:
    def __init__(self):
        self.loginState = Login()

    def login(self, username, password):
        ackMSG = self.loginState.login(self, username, password)
        if ackMSG:
            print("logged in successfully")
        else:
            print("error while logging in")
