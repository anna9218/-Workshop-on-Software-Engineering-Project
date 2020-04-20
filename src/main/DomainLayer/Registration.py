# The system checks if the username and password are valid
# The system creates a new Subscriber in the system with the given username and password.
# The system returns an ACK message to the guest.

def register(username, password):
    isUsernameValid = True
    isPasswordLegal = True
    # TODO - check if username is valid. if not, change isUsernameLegal to F
    if isUsernameValid:
        # TODO - check if password legal. if not, change isPasswordLegal to F
        if isPasswordLegal:
        # TODO - create Subscriber - object? in DB? do we need to send to Security Component?
        else:
            print("The password is not legal, please try again")
    else:
        print("The username is not legal, please try again")
