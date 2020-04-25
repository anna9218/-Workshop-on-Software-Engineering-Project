class StubLogout:
    def __init__(self):
        self.isLoggedOut = False

    def logout(self):
        self.isLoggedOut = True
