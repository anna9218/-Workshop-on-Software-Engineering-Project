def check_valid_details(name, amount, credit, date) -> bool:
    if len(name) == 0 or len(credit) == 0 or len(date) == 0 or amount <= 0:
        return False
    else:
        return True


class FacadePayment:

    def __init__(self):
        self.isConnected = False

    def connect(self):
        if not self.isConnected:
            self.isConnected = True

    # need to check payment details with system once a system is set
    def commit_payment(self, username, amount, credit, date) -> bool:
        if not self.isConnected or not check_valid_details(username, amount, credit, date):
            return False
        else:
            return True

    def disconnect(self):
        if self.isConnected:
            self.isConnected = False
