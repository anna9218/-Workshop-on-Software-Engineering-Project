# from src.main.DomainLayer.User import User


class Registration:
    def __init__(self):
        self.__isRegistered = False
        self.__username = None
        self.__password = None

    # @classmethod
    def register(self, user, username, password):
        # check if username is valid
        isUsernameValid = self.checkUsername(user, username)
        if isUsernameValid:
            isPasswordLegal = self.checkPassword(password)
            # check if password legal
            if isPasswordLegal:
                self.__isRegistered = True
                self.__username = username
                self.__password = password
                user.get_trade_control().subscribe(username, password)
                return True
            else:
                print("The password is not legal, please try again")
                return False
        else:
            print("The username is not legal, please try again")
            return False

    # @classmethod
    def checkUsername(self, user, username):
        isValid = True
        for u in user.get_trade_control().get_users():
            if u.registrationState.get_username() == username:
                isValid = False
        return isValid

    # @classmethod
    def checkPassword(self, password):
        return True

    # @classmethod
    def get_username(self):
        return cls.__username

    # @classmethod
    def get_password(self):
        return cls.__password

    def is_registered(self):
        return self.__isRegistered
