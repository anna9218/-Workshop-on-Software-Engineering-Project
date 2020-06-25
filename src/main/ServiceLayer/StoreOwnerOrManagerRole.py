from datetime import datetime

from src.Logger import logger
from src.main.DomainLayer.StoreComponent.AppointmentStatus import AppointmentStatus
from src.main.DomainLayer.TradeComponent.TradeControl import TradeControl


class StoreOwnerOrManagerRole:

    def __init__(self):
        pass

    # @logger
    # use case 4.1.1
    @staticmethod
    def add_products(curr_nickname: str, store_name: str, products_details: [{"name": str, "price": int, "category": str, "amount":
        float, "purchase_type": int}]) -> {'response': bool, 'msg': str}:
        """
        :param curr_nickname:
        :param store_name: store's name
        :param products_details: list of tuples (product_name, product_price, product_amounts, product_category)
        # param products_details: list products details: [{"name": str, "price": int, "amount": int, "category": str},...]
        :return: dict = {'response': bool, 'msg': str}
                    response = True if products were added, False otherwise
        """
        return TradeControl.get_instance().add_products(curr_nickname, store_name, products_details)

    @staticmethod
    @logger
    # use 4.1.2
    def remove_products(curr_nickname: str, store_name: str, products_names: list) -> bool:
        """
        :param curr_nickname:
        :param store_name: store's name
        :param products_names: list of products name to remove
        :return: True if all products were removed, else return False
        """
        return TradeControl.get_instance().remove_products(curr_nickname, store_name, products_names)

    @staticmethod
    @logger
    # use 4.1.3
    def edit_product(curr_nickname: str, store_name: str, product_name: str, op: str, new_value: str) -> {'response': bool, 'msg': str}:
        """
        :param curr_nickname:
        :param store_name: store's name
        :param product_name: product's name to edit
        :param op: edit options - name, price, amount
        :param new_value: new value to set to
        :return: dict =  {'response': bool, 'msg': str}
                 response = True if all products were removed, else return False
        """
        return TradeControl.get_instance().edit_product(curr_nickname, store_name, product_name, op, new_value)

    # use case 4.3
    @staticmethod
    @logger
    def appoint_additional_owner(curr_nickname: str, appointee_nickname: str, store_name: str) -> {'response': bool, 'msg': str}:
        """
        :param curr_nickname:
        :param appointee_nickname: nickname of the new owner that will be appointed
        :param store_name: store the owner will be added to
        :return: dict =  {'response': bool, 'msg': str}
                 response = True on success, else False
        """
        return TradeControl.get_instance().appoint_additional_owner(curr_nickname, appointee_nickname, store_name)

    @staticmethod
    @logger
    def update_agreement_participants(curr_nickname: str, appointee_nickname: str, store_name: str, owner_response: AppointmentStatus):
        """
        :param curr_nickname:
        :param appointee_nickname: nickname of the new owner that will be appointed
        :param store_name: store the owner will be added to
        :param owner_response: the owners response - declined/approved
        :return: dict =  {'response': bool, 'msg': str}
                 response = True on success, else False
        """
        return TradeControl.get_instance().update_agreement_participants(curr_nickname, appointee_nickname, store_name, owner_response)

    @staticmethod
    @logger
    def get_appointment_status(appointee_nickname: str, store_name: str):
        """
        :param appointee_nickname: nickname of the new owner that is being appointed
        :param store_name: store the owner should be added to
        :return: AppointmentStatus - DECLINED = 1,APPROVED = 2, PENDING = 3
        """
        return TradeControl.get_instance().get_appointment_status(appointee_nickname, store_name)

    # use case 4.4
    @staticmethod
    @logger
    def remove_owner(curr_nickname: str, appointee_nickname: str, store_name: str) -> {'response': [], 'msg': str}:
        """
        the function removes appointee_nickname as owner from the store, in addition to him it removes all the managers
        and owners appointee_nickname appointed.
        :param curr_nickname:
        :param appointee_nickname: nickname of the owner we want to remove as owner
        :param store_name: store the owner will be removed from as owner
        :return: dict =  {'response': [], 'msg': str}
                 response = nicknames list of all the removed appointees -> the appointee_nickname of the owner we want
                            to remove and all the appointees he appointed, we had to remove as well.
        """
        return TradeControl.get_instance().remove_owner(curr_nickname, appointee_nickname, store_name)

    # use case 4.5
    @staticmethod
    @logger
    def appoint_store_manager(curr_nickname: str, appointee_nickname: str, store_name: str, permissions: list) -> {'response': bool, 'msg': str}:
        """
        :param curr_nickname:
        :param appointee_nickname: new manager's nickname
        :param store_name: store's name
        :param permissions: ManagerPermission[] ->list of permissions (list of Enum)
        :return: dict = {'response': bool, 'msg': str}
                 response = True on success, else False
        """
        return TradeControl.get_instance().appoint_store_manager(curr_nickname, appointee_nickname, store_name, permissions)

    # use case 4.6
    @staticmethod
    @logger
    def edit_manager_permissions(curr_nickname: str, store_name: str, appointee_nickname: str, permissions: list) -> bool:
        """
        :param curr_nickname:
        :param store_name: store's name
        :param appointee_nickname: manager's nickname who's permissions will be edited
        :param permissions: ManagerPermission[] ->list of permissions (list of Enum)
        :return: True on success, else False
        """
        return TradeControl.get_instance().edit_manager_permissions(curr_nickname, store_name, appointee_nickname, permissions)

    @staticmethod
    @logger
    def get_manager_permissions(store_name) -> list:
        return TradeControl.get_instance().get_manager_permissions(store_name)

    # @logger
    @staticmethod
    def get_appointees(curr_nickname: str, store_name, managers_or_owners: str) -> list:
        """
        returns for the current manager/owner all the managers he appointed
        :param curr_nickname:
        :param store_name: name of the store
        :param managers_or_owners: "MANAGERS" or "OWNERS" to get a list of the managers or owners that appointer_nickname appointed
        :return: list of the managers nicknames
        """
        return TradeControl.get_instance().get_appointees(curr_nickname, store_name, managers_or_owners)

    # use case 4.7
    @staticmethod
    def remove_manager(curr_nickname: str, store_name: str, appointee_nickname: str) -> bool:
        """
        :param curr_nickname:
        :param store_name: store's name
        :param appointee_nickname: manager's nickname who's will be removed
        :return: True on success, else False
        """
        return TradeControl.get_instance().remove_manager(curr_nickname, store_name, appointee_nickname)

    # use case 4.10 - View store’s purchase history
    @staticmethod
    # @logger
    def display_store_purchases(curr_nickname: str, store_name: str) -> {'response': list, 'msg': str}:
        """
        :param curr_nickname:
        :param store_name: store's name
        :return: dict = {'response': list, 'msg': str}
                 response = purchases list
        """
        return TradeControl.get_instance().display_store_purchases(curr_nickname, store_name)

    @logger
    def close_store(self, store_name: str) -> bool:
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
    @staticmethod
    @logger
    def get_purchase_operator(store_name: str):
        return TradeControl.get_instance().get_store_purchase_operator(store_name)

    @staticmethod
    @logger
    def set_purchase_operator(store_name: str, operator: str):
        TradeControl.get_instance().define_store_purchase_operator(store_name, operator)

    # uc 4.2
    @staticmethod
    @logger
    def get_policies(curr_nickname: str, policy_type: str, store_name: str) -> {'response': [dict] or None, 'msg': str}:
        """
            according to the given type, displays a list of policies for the store
        :param policy_type:
        :param curr_nickname:
        :param purchase_type: can be "purchase" or "discount"
        :param store_name:
        :return: list of policies or empty list, returns None if user is not owner of the store or store doesn't exist
        """
        return TradeControl.get_instance().get_policies(curr_nickname, policy_type, store_name)

    # uc 4.2.1
    @staticmethod
    @logger
    def update_purchase_policy(curr_nickname: str, store_name: str, details: {"name": str, "products": [str] or None,
                                                                "min_amount": int or None, "max_amount": int or None,
                                                                "dates": [dict] or None, "bundle": bool or None})\
            -> {'response': bool, 'msg': str}:
        """
            update must have valid policy name of an existing policy and at least one more detail
        :param curr_nickname:
        :param store_name:
        :param details: {"name": str,                            -> policy name
                        "products": [str] or None,               -> list of product names
                        "min_amount": int or None,               -> minimum amount of products required
                        "max_amount": int or None,               -> maximum amount of products required
                        "dates": [dict] or None,                 -> list of prohibited dated for the given products
                        "bundle": bool or None}                  -> true if the products are bundled together
           i.e. details can be: {"products", "bundle"} / {"products", "min_amount"} etc.
        :return: true if successful, otherwise false with details for failure
        """
        return TradeControl.get_instance().update_purchase_policy(curr_nickname, store_name, details)

    # uc 4.2.2
    @staticmethod
    @logger
    def define_purchase_policy(curr_nickname: str, store_name: str, details: {"name": str, "products": [str],
                                                                "min_amount": int or None, "max_amount": int or None,
                                                                "dates": [datetime] or None, "bundle": bool or None})\
            -> {'response': bool, 'msg': str}:
        """
            define requires valid and unique policy name, none empty list of products and at least one more detail
        :param curr_nickname:
        :param store_name:
        :param details: {"name": str,                             -> policy name
                        "products": [str],                       -> list of product names
                        "min_amount": int or None,               -> minimum amount of products required
                        "max_amount": int or None,               -> maximum amount of products required
                        "dates": [dict] or None,                 -> list of prohibited dated for the given products
                        "bundle": bool or None}                  -> true if the products are bundled together
           i.e. details can be: {"products", "bundle"} / {"products", "min_amount"} etc.
        :return: true if successful, otherwise false with details for failure
        """
        return TradeControl.get_instance().define_purchase_policy(curr_nickname, store_name, details)

    # uc 4.2.3
    @staticmethod
    @logger
    def update_discount_policy(curr_nickname: str, store_name: str, policy_name: str,
                               percentage: float = -999,
                               valid_until: datetime = None,
                               discount_details: {'name': str,
                                                  'product': str} = None,
                               discount_precondition: {'product': str,
                                                       'min_amount': int or None,
                                                       'min_basket_price': str or None} or None = None) \
            -> {'response': bool, 'msg': str}:

        """
        Updating an existing policy, either visible, conditional or composite.
        The key word "all" will flag that the policy is on the entire basket.

        :param curr_nickname:
        :param valid_until: the last date the policy is valid.
        :param store_name.
        :param policy_name: the policy to update.
        :param percentage: for updating the percentage attribute.
        :param discount_details: for updating the name or product of the policy.
        :param discount_precondition: ONLY AVAILABLE FOR CONDITIONAL POLICY.
                for updating the precondition.
                DOES NOT AVAILABLE FOR COMPOSITE AND VISIBLE POLICIES.
        :return: true if successful, else false.
        """
        return TradeControl.get_instance().update_discount_policy(curr_nickname, store_name, policy_name, percentage, valid_until,
                                                                  discount_details, discount_precondition)

    # uc 4.2.4
    @staticmethod
    @logger
    def define_discount_policy(curr_nickname: str, store_name: str,
                               percentage: float,
                               valid_until: datetime,
                               discount_details: {'name': str,
                                                  'product': str},
                               discount_precondition: {'product': str,
                                                       'min_amount': int or None,
                                                       'min_basket_price': str or None} or None = None
                               ) \
            -> {'response': bool, 'msg': str}:
        """
        Define SIMPLE discount policy, either visible or conditional.
        The key word "all" will flag that the policy or constraint are on the entire basket.

        :param curr_nickname:
        :param valid_until: the last date the policy is valid.
        :param store_name.
        :param percentage: the percentage of the discount.
        :param discount_details:  the name and the product of the policy.
        :param discount_precondition: ONLY AVAILABLE FOR CONDITIONAL POLICY.
                        have a constraint either on the entire basket, or a specific product.
        :return: True if successful, else false.
        """
        return TradeControl.get_instance().define_discount_policy(curr_nickname, store_name, percentage, valid_until, discount_details,
                                                                  discount_precondition)

    @staticmethod
    @logger
    def define_composite_policy(curr_nickname: str, store_name: str, policy1_name: str, policy2_name: str, flag: str,
                                percentage: float, name: str, valid_until: datetime) -> {}:
        """
        Define a policy that composite from exactly 2 policies.
        Both policies should have the same product for success.
        The keyword "all" will flag that the policies are on the entire basket.

        :param curr_nickname:
        :param valid_until: the last date the policy is valid.
        :param store_name.
        :param policy1_name: the policy uid.
        :param policy2_name: the policy uid.
        :param flag: "and ,"or" or "xor"
        :param percentage.
        :param name: the policy name.
        :return: True if successful, else false.
        """
        return (TradeControl.get_instance()).define_composite_policy(curr_nickname, store_name, policy1_name, policy2_name, flag,
                                                                     percentage, name, valid_until)

    @staticmethod
    @logger
    def get_discount_policy(store_name: str, policy_name: str) -> {}:
        """
        return the policy.

        :param store_name.
        :param policy_name.
        :return: the policy if exist. None else.
        """
        return (TradeControl.get_instance()).get_discount_policy(store_name, policy_name)

    @staticmethod
    @logger
    def delete_policy(store_name: str, policy_name: str):
        """
        Delete discount policy with the name @policy_name, if exist.

        :param store_name.
        :param policy_name.
        :return: True if successful, else false.
        """
        return (TradeControl.get_instance()).delete_policy(store_name, policy_name)

    @staticmethod
    @logger
    def delete_purchase_policy(store_name: str, policy_name: str):
        """
        Delete purchase policy with the name @policy_name, if exist.

        :param store_name.
        :param policy_name.
        :return: True if successful, else false.
        """
        return (TradeControl.get_instance()).delete_purchase_policy(store_name, policy_name)

    # ------------------------------------

    # -------------------------------------------------------------
    @staticmethod
    # for managing inventory - uc 4.1
    def get_owned_stores(curr_nickname: str):
        return TradeControl.get_instance().get_owned_stores(curr_nickname)

    @staticmethod
    def get_managed_stores(curr_nickname: str):
        return TradeControl.get_instance().get_managed_stores(curr_nickname)
    # -------------------------------------------------------------

    def __repr__(self):
        return repr("StoreOwnerRole")

    @logger
    def username(self): # TODO - delete?
        return TradeControl.get_instance().get_curr_username()

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
