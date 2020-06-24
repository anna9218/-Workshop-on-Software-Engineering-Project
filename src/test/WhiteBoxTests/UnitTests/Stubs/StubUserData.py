

class StubUserData:

    def __init__(self, username, password, is_system_manager):
        self.username = username
        self.password = password
        self.is_system_manager = is_system_manager

    def __eq__(self, other):
        if not (other is StubUserData):
            return False
        return (self.username == other.username and
                self.password == other.password and
                self.is_system_manager == other.is_system_manager)
