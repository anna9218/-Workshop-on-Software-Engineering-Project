class StubRegistration:
    def __init__(self):
        self.isRegistered = False
        self.count = 0

    def register(self, user, username, password):
        if username == "anna9218" and self.count == 0:
            self.isRegistered = True
            self.count = 1
        else:
            self.isRegistered = False
