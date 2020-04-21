# The system checks if the username and password are valid
# The system creates a new Subscriber in the system with the given username and password.
# The system returns an ACK message to the guest.


class Registration:
    def __init__(self):
        self.isRegistered = False
        self.username = None
        self.password = None

    @classmethod
    def register(cls, user, username, password):
        # need to check if registered and act accordingly
        isUsernameValid = True
        isPasswordLegal = True
        # TODO - check if username is valid. if not, change isUsernameLegal to F
        if isUsernameValid:
            # TODO - check if password legal. if not, change isPasswordLegal to F
            if isPasswordLegal:
                cls.isRegistered = True
                cls.username = username
                cls.password = password
                # TODO - create Subscriber - object? in DB? do we need to send to Security Component?
            else:
                print("The password is not legal, please try again")
        else:
            print("The username is not legal, please try again")

    @classmethod
    def get_username(cls):
        return cls.username

    @classmethod
    def get_password(cls):
        return cls.password
