class Appointment:
    def __init__(self):
        # pair of (appointer, store)
        self.__owned_stores = []

        # self.__appointer = appointer
        # self.__appointee = appointee
        # self.__store = store

    def appoint_owner(self, appointer, appointee, store) -> bool:
        # in case he is the one who opened the store
        if appointer is None:
            self.__owned_stores.append((None, store))
        # check if there isn't a circle
        else:
            if store.add_owner(appointee):
                self.__owned_stores.append((appointer, store))

    def is_owner(self, store_name):
        for (appointer, store) in self.__owned_stores:
            if store.get_name() == store_name:
                return True
        return False
