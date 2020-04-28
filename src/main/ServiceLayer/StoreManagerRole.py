from src.main.DomainLayer.ManagerPermission import ManagerPermission
from src.main.DomainLayer.TradeControl import TradeControl
from src.main.DomainLayer.User import User
from src.main.ServiceLayer.StoreOwnerRole import StoreOwnerRole


class StoreManagerRole(StoreOwnerRole):
    def __init__(self, user, store_name):
        self.__manager = user
        self.store_name = store_name
        self.owner_role = StoreOwnerRole(self.__manager)

    # use case 4.1.1
    def add_products(self, store_name) -> bool:
        if self.has_permission(ManagerPermission.EDIT_INV, self.__manager.get_nickname()):
            return self.owner_role.add_products(products_details, )
        return False

    # use 4.1.2
    def remove_products(self, store_name, products_names) -> bool:
        if self.has_permission(ManagerPermission.EDIT_INV, self.__manager.get_nickname()):
            return self.owner_role.remove_products(store_name, products_names)
        return False

    # use 4.1.3
    def edit_product(self, store_name, product_name, op, new_value) -> bool:
        if self.has_permission(ManagerPermission.EDIT_INV, self.__manager.get_nickname()):
            return self.owner_role.edit_product(nickcname, store_name, product_name, op)
        return False

    # use case 4.2
    def edit_purchase_and_discount_policies(self):
        if self.has_permission(ManagerPermission.EDIT_POLICIES, self.__manager.get_nickname()):
            return self.owner_role.edit_purchase_and_discount_policies()
        return False

    # use case 4.3
    def appoint_additional_owner(self, appointee_nickname):
        if self.has_permission(ManagerPermission.APPOINT_OWNER, self.__manager.get_nickname()):
            return self.owner_role.appoint_additional_owner(store_name, )
        return False

    # use case 4.5
    def appoint_store_manager(self, appointee_nickname, store_name):
        if self.has_permission(ManagerPermission.APPOINT_MAMAGER, self.__manager.get_nickname()):
            return self.owner_role.appoint_store_manager(store_name, permissions, )
        return False

    # use case 4.6
    def edit_manager_permissions(self, store_name, manager_nickname):
        if self.has_permission(ManagerPermission.EDIT_MANAGER_PER, self.__manager.get_nickname()):
            return self.owner_role.edit_manager_permissions(manager_nickname, permissions, )
        return False

    # use case 4.7
    def remove_manager(self, store_name, appointee_nickname):
        if self.has_permission(ManagerPermission.DEL_MANAGER, self.__manager.get_nickname()):
            return self.owner_role.remove_manager(str, str)
        return False

    # use case 4.10 - View store’s purchase history
    def display_store_purchases(self, store_name):
        return self.owner_role.display_store_purchases(store_name)


