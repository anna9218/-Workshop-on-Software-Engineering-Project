class Registration:
    def __init__(self):
        self.isRegistered = False
        self.username = None
        self.password = None

    @classmethod
    def register(cls, user, username, password):
        # check if username is valid
        isUsernameValid = cls.checkUsername(user, username)
        if isUsernameValid:
            isPasswordLegal = cls.checkPassword(password)
            # check if password legal
            if isPasswordLegal:
                cls.isRegistered = True
                cls.username = username
                cls.password = password
                user.tradeControl.subscribe(user)
                return True
            else:
                print("The password is not legal, please try again")
                return False
        else:
            print("The username is not legal, please try again")
            return False

    @classmethod
    def checkUsername(cls, user, username):
        isValid = True
        for user in user.tradeControl.users:
            if user.registrationState.get_username == username:
                isValid = False
        return isValid

    @classmethod
    def checkPassword(cls, password):
        return True

    @classmethod
    def get_username(cls):
        return cls.username

    @classmethod
    def get_password(cls):
        return cls.password
