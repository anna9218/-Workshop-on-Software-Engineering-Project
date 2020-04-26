from src.Logger import logger
from src.main.DomainLayer.ManagerPermission import ManagerPermission
from src.main.DomainLayer.TradeControl import TradeControl
from src.main.DomainLayer.User import User
from src.main.ServiceLayer.StoreOwnerRole import StoreOwnerRole


class StoreManagerRole(StoreOwnerRole):
    ##### changed this  from _init_ (one underscore line instead of two) is it on purpose?
    def __init__(self, user, store_name):
        # super(StoreManagerRole, self)
        self.__manager = user
        self.store_name = store_name
        self.owner_role = StoreOwnerRole(self.__manager)

    @logger
    # use case 4.1.1
    def add_products(self, store_name, products_details):
        if self.has_permission(ManagerPermission.EDIT_INV, store_name, self.__manager.get_nickname()):
            return self.owner_role.add_products(self.__manager.get_nickname(), store_name, products_details)
        return False

    @logger
    # use 4.1.2
    def remove_products(self, user_nickname, store_name, products_names) -> bool:
        if self.has_permission(ManagerPermission.EDIT_INV, store_name, self.__manager.get_nickname()):
            return self.owner_role.remove_products(user_nickname, store_name, products_names)
        return False

    @logger
    # use 4.1.3
    def edit_product(self, nickcame, store_name, product_name, op, new_value) -> bool:
        if self.has_permission(ManagerPermission.EDIT_INV, store_name, self.__manager.get_nickname()):
            return self.owner_role.edit_product(self, nickcame, store_name, product_name, op, new_value)
        return False

    @logger
    # use case 4.2
    def edit_purchase_and_discount_policies(self, store_name):
        if self.has_permission(ManagerPermission.EDIT_POLICIES, store_name, self.__manager.get_nickname()):
            return self.owner_role.edit_purchase_and_discount_policies()
        return False

    @logger
    # use case 4.3
    def appoint_additional_owner(self, nickname_to_add, store_name):
        if self.has_permission(ManagerPermission.APPOINT_OWNER, store_name, self.__manager.get_nickname()):
            return self.owner_role.appoint_additional_owner(nickname_to_add, store_name)
        return False

    @logger
    # use case 4.5
    def appoint_store_manager(self, manager_nickname, store_name, permissions):
        if self.has_permission(ManagerPermission.APPOINT_MANAGER, store_name, self.__manager.get_nickname()):
            return self.owner_role.appoint_store_manager(manager_nickname, store_name, permissions)
        return False

    @logger
    # use case 4.6
    def edit_manager_permissions(self, store_name, manager_nickname, permissions):
        if self.has_permission(ManagerPermission.EDIT_MANAGER_PER, store_name, self.__manager.get_nickname()):
            return self.owner_role.edit_manager_permissions(store_name, manager_nickname, permissions)
        return False

    @logger
    # use case 4.7
    def remove_manager(self, store_name, manager_nickname):
        if self.has_permission(ManagerPermission.DEL_MANAGER, store_name, self.__manager.get_nickname()):
            return self.owner_role.remove_manager(store_name, manager_nickname)
        return False

    @logger
    # use case 4.10 - View store’s purchase history
    def display_store_purchases(self, nickname, store_name):
        return self.owner_role.display_store_purchases(nickname, store_name)

    def has_permission(self, permission, store_name, manager_nickname):
        for p in TradeControl.get_instance().get_store(store_name).get_permissions(manager_nickname):
            if ManagerPermission(p).value == permission.value:
                return True
            return False


    # def has_permission(self, permission, store_name, manager_nickname):
    #     result = False
    #     store_manager_appointments = TradeControl.get_instance().get_store(store_name).get_store_manager_appointments()
    #     for appointment in store_manager_appointments:
    #         if appointment.get_appointee().get_nickname() == manager_nickname:
    #             for tmp_permission in appointment.get_permissions():
    #                 if permission == tmp_permission:  # NEED TO COMPARE 2 ENUMS, HOW? PLEASE CHECK
    #                     result = True
    #     return result

    def __repr__(self):
        return repr("StoreManagerRole")
