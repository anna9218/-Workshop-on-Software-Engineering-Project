from Backend.src.Logger import logger
from Backend.src.main.DomainLayer.TradeComponent.TradeControl import TradeControl


class StoreOwnerOrManagerRole:

    def __init__(self):
        pass

    # @logger
    # use case 4.1.1
    def add_products(self, store_name: str, products_details: [{"name": str, "price": int, "category": str, "amount": int}]) -> bool:
        """
        :param store_name: store's name
        :param products_details: list of tuples (product_name, product_price, product_amounts, product_category)
        # param products_details: list products details: [{"name": str, "price": int, "amount": int, "category": str},...]
        :return: True if products were added, False otherwise
        """
        return TradeControl.get_instance().add_products(store_name, products_details)

    # @logger
    # use 4.1.2
    def remove_products(self, store_name: str, products_names: list) -> bool:
        """
        :param store_name: store's name
        :param products_names: list of products name to remove
        :return: True if all products were removed, else return False
        """
        return TradeControl.get_instance().remove_products(store_name, products_names)

    # @logger
    # use 4.1.3
    def edit_product(self, store_name: str, product_name: str, op: str, new_value: str) -> bool:
        """
        :param store_name: store's name
        :param product_name: product's name to edit
        :param op: edit options - name, price, amount
        :param new_value: new value to set to
        :return: True if all products were removed, else return False
        """
        return TradeControl.get_instance().edit_product(store_name, product_name, op, new_value)

    # @logger
    # use case 4.3
    def appoint_additional_owner(self, appointee_nickname: str, store_name: str) -> bool:
        """
        :param appointee_nickname: nickname of the new owner that will be appointed
        :param store_name: store the owner will be added to
        :return: True on success, else False
        """
        return TradeControl.get_instance().appoint_additional_owner(appointee_nickname, store_name)

    # @logger
    # use case 4.5
    def appoint_store_manager(self, appointee_nickname: str, store_name: str, permissions: list) -> bool:
        """
        :param appointee_nickname: new manager's nickname
        :param store_name: store's name
        :param permissions: ManagerPermission[] ->list of permissions (list of Enum)
        :return: True on success, else False
        """
        return TradeControl.get_instance().appoint_store_manager(appointee_nickname, store_name, permissions)

    # @logger
    # use case 4.6
    def edit_manager_permissions(self, store_name: str, appointee_nickname: str, permissions: list) -> bool:
        """
        :param store_name: store's name
        :param appointee_nickname: manager's nickname who's permissions will be edited
        :param permissions: ManagerPermission[] ->list of permissions (list of Enum)
        :return: True on success, else False
        """
        return TradeControl.get_instance().edit_manager_permissions(store_name, appointee_nickname, permissions)

    # @logger
    # use case 4.7
    def remove_manager(self, store_name: str, appointee_nickname: str) -> bool:
        """
        :param store_name: store's name
        :param appointee_nickname: manager's nickname who's will be removed
        :return: True on success, else False
        """
        return TradeControl.get_instance().remove_manager(store_name, appointee_nickname)

    # @logger
    # use case 4.10 - View store’s purchase history
    def display_store_purchases(self, store_name: str) -> list:
        """
        :param store_name: store's name
        :return: purchases list
        """
        return TradeControl.get_instance().display_store_purchases(store_name)

    def close_store(self, store_name: str):
        """
        This function check if the curr_user logged in and own the store with the name (:param store_name).
        If the above condition is true, the function delete the store.
        Else, return False

        :param store_name: the store name to delete. Curr_user Have to own the store.
        :return: True if deleted successfully
                 False else.
        """
        return TradeControl.get_instance().close_store(store_name)

    # -------- UC 4.2 -------------------
    # uc 4.2
    def define_and_update_policies(self, type: str, store_name: str) -> [dict] or None:
        """
            according to the given type, displays a list of policies for the store
        :param type: can be "purchase" or "discount"
        :param store_name:
        :return: list of policies or empty list, returns None if user is not owner of the store
        """
        return TradeControl.get_instance().define_and_update_policies(type, store_name)

    # uc 4.2.1
    def update_purchase_policy(self, store_name: str, details: {"name": str, "products": [str] or None,
                                                                "min_amount": int or None, "max_amount": int or None,
                                                                "dates": [dict] or None, "bundle": bool or None}):
        return TradeControl.get_instance().update_purchase_policy(store_name, details)

    # uc 4.2.2
    def define_purchase_policy(self, store_name: str, details: {"name": str, "products": [str],
                                                                "min_amount": int or None, "max_amount": int or None,
                                                                "dates": [dict] or None, "bundle": bool or None}):
        return TradeControl.get_instance().define_purchase_policy(store_name, details)

    # uc 4.2.3
    def update_discount_policy(self):
        return TradeControl.get_instance().update_discount_policy()

    # uc 4.2.4
    def define_discount_policy(self):
        return TradeControl.get_instance().define_discount_policy()
    # ------------------------------------

    def __repr__(self):
        return repr("StoreOwnerRole")

    # def check_if_owns_the_store(self, user_name, store_name) -> bool:
    #     user = TradeControl.get_instance().getUser(user_name)
    #     if user is None or not user.is_loggedIn():
    #         return False
    #     store = self.get_store(store_name)
    #     if user in store.get_owners():
    #         return True

    # @staticmethod
    # def validate_store_name(self, store_name):
    #     TradeFacade.getInstance().validate_store_name(store_name)

    # @staticmethod
    # def display_purchase_info(self, purchase, store):
    #     """
    #     :param self:
    #     :param purchase:
    #     :param store: name of the store - (string?)
    #     :return: returns a Purchase object
    #     """
    #     store = TradeControl.get_instance().get_store(store)
    #     store.get_purchase_info(purchase)
