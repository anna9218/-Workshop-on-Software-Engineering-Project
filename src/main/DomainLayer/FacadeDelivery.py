def check_valid_details(name, address) -> bool:
    if len(name) == 0 or len(address) == 0:
        return False
    else:
        return True


class FacadeDelivery:

    def __init__(self):
        self.isConnected = False

    def connect(self):
        if not self.isConnected:
            self.isConnected = True

    # need to check payment details with system once a system is set
    def deliver_products(self, username, address) -> bool:
        if not self.isConnected or not check_valid_details(username, address):
            return False
        else:
            return True

    def disconnect(self):
        if self.isConnected:
            self.isConnected = False
