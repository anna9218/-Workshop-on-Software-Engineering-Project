class StubLogout:
    def __init__(self):
        self.isLoggedOut = False

    def logout(self, user):
        self.isLoggedOut = True
