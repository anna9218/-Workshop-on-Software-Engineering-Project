from src.main.DomainLayer.ManagerPermission import ManagerPermission


class Appointment:
    def __init__(self):
        # pairs of (appointer, store)
        self.__owned_stores = []
        # pairs of (store, permissions)
        self.__manage_stores = []

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

    def appoint_manager (self, store):
        self.__manage_stores.append((store, []))
        # self.add_permission(store.get_name(), ManagerPermission.USERS_QUESTIONS) - in service layer
        # self.add_permission(store.get_name(), ManagerPermission.WATCH_PURCHASE_HISTORY)

    def is_owner(self, store_name):
        for (appointer, store) in self.__owned_stores:
            if store.get_name() == store_name:
                return True
        return False

    def is_manager (self, store_name):
        for (s, p) in self.__manage_stores:
            if store_name == s.get_name():
                return True
        return False

    def add_permission (self, store_name, permission):
        """
      :param store_name: name of the store
      :param permission: a ManagerPermission to add
      """
        for (s, p) in self.__manage_stores:
            if s.get_name() == store_name:
                if not permission in p:
                    p.append(permission)

    def del_permission (self, store_name, permission):
        """
       :param store_name: name of the store
       :param permission: a ManagerPermission to delete
       """
        for (s, p) in self.__manage_stores:
            if s.get_name() == store_name:
                if permission in p:
                    p.remove(permission)

    def has_permission (self, store_name, permission) -> bool:
        """
        :param store_name: name of the store
        :param permission: a ManagerPermission
        :return: true if the manager's permissions include the given permission
        """
        for (s, p) in self.__manage_stores:
            if s.get_name() == store_name:
                if permission in p:
                    return True
                return False
        return False

    def get_permissions_of_store (self, store_name) :
        permissions = []
        for (s, p) in self.__manage_stores:
            if s.get_name() == store_name:
                return p