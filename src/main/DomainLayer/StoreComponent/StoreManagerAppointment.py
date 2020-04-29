from src.Logger import logger
from src.main.DomainLayer.UserComponent.User import User


class StoreManagerAppointment:
    def __init__(self, appointer: User, appointee: User, permissions: list):
        self.__appointer = appointer
        self.__permissions = permissions
        self.__appointee = appointee

    @logger
    def set_permissions(self, permissions):
        self.__permissions = permissions

    @logger
    def get_permissions(self):
        return self.__permissions

    @logger
    def get_appointer(self):
        return self.__appointer

    @logger
    def get_appointee(self):
        return self.__appointee

    @logger
    def has_permission(self, permission):
        return permission in self.__permissions

    @logger
    def add_permission(self, permission):
        self.__permissions.append(permission)
        return True

    def __repr__(self):
        return repr("StoreManagerAppointment")

    # def appoint_owner(self, appointer, appointee, store) -> bool:
    #     # in case he is the one who opened the store
    #     if appointer is None:
    #         self.__owned_stores.append((None, store))
    #     # check if there isn't a circle
    #     else:
    #         if store.add_owner(appointee):
    #             self.__owned_stores.append((appointer, store))
    #
    # def appoint_manager (self, store):
    #     self.__manage_stores.append((store, []))
    #     # self.add_permission(store.get_name(), ManagerPermission.USERS_QUESTIONS) - in service layer
    #     # self.add_permission(store.get_name(), ManagerPermission.WATCH_PURCHASE_HISTORY)
    #
    # def is_owner(self, store_name):
    #     for (appointer, store) in self.__owned_stores:
    #         if store.get_name() == store_name:
    #             return True
    #     return False
    #
    # def is_manager (self, store_name):
    #     for (s, p) in self.__manage_stores:
    #         if store_name == s.get_name():
    #             return True
    #     return False
    #
    # def add_permission (self, store_name, permission):
    #     """
    #   :param store_name: name of the store
    #   :param permission: a ManagerPermission to add
    #   :return true if at the end of func the user have the permission on store
    #   """
    #     for (s, p) in self.__manage_stores:
    #         if s.get_name() == store_name:
    #             if permission not in p:
    #                 p.append(permission)
    #             return True
    #
    # def del_permission (self, store_name, permission):
    #     """
    #    :param store_name: name of the store
    #    :param permission: a ManagerPermission to delete
    #    """
    #     for (s, p) in self.__manage_stores:
    #         if s.get_name() == store_name:
    #             if permission in p:
    #                 p.remove(permission)
    #
    # def has_permission (self, store_name, permission) -> bool:
    #     """
    #     :param store_name: name of the store
    #     :param permission: a ManagerPermission
    #     :return: true if the manager's permissions include the given permission
    #     """
    #     for (s, p) in self.__manage_stores:
    #         if s.get_name() == store_name:
    #             if permission in p:
    #                 return True
    #             return False
    #     return False
    #
    # def get_permissions_of_store (self, store_name) :
    #     for (s, p) in self.__manage_stores:
    #         if s.get_name() == store_name:
    #             return p
    #     return []
