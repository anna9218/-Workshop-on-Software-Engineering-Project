"""
        purchase composite class - executes child operation for purchase component interface
"""
from datetime import datetime

from src.Logger import logger
from src.main.DomainLayer.StoreComponent.PurchasePolicyComposite.Leaves.BundleDealPolicy import BundleDealPolicy
from src.main.DomainLayer.StoreComponent.PurchasePolicyComposite.Leaves.MaxAmountPolicy import MaxAmountPolicy
from src.main.DomainLayer.StoreComponent.PurchasePolicyComposite.Leaves.MinAmountPolicy import MinAmountPolicy
from src.main.DomainLayer.StoreComponent.PurchasePolicyComposite.Leaves.ProhibitedDatePolicy import ProhibitedDatePolicy
from src.main.DomainLayer.StoreComponent.PurchasePolicyComposite.PurchaseComponent import PurchaseComponent


class PurchasePolicy(PurchaseComponent):

    def __init__(self):
        super().__init__()
        self.__children: [PurchaseComponent] = []

    def can_purchase(self, details: [{"product_name": str, "amount": int}], curr_date: datetime):
        """
        :param curr_date:
        :param details: list [{"product_name": str, "amount": int}]
        :return: True if the user can purchase the products, else False
        """
        for policy in self.__children:
            if not policy.can_purchase(details, curr_date):
                return False
        return True

    def add_purchase_policy(self, details: {"name": str, "products": [str], "min_amount": int or None,
                                            "max_amount": int or None, "dates": [dict] or None,
                                            "bundle": bool or None}) -> {'response': bool, 'msg': str}:
        """
            add new purchase policy. current policies available are: grouped products, prohibited dates,
            min amount and max amount
        :param details: {"name": str,                             -> policy name
                        "products": [str],                       -> list of product names
                        "min_amount": int or None,               -> minimum amount of products required
                        "max_amount": int or None,               -> maximum amount of products required
                        "dates": [dict] or None,                 -> list of prohibited dated for the given products
                        "bundle": bool or None}                  -> true if the products are bundled together
                i.e. details can be: {"products", "bundle"} / {"products", "min_amount"} etc.
        :return: true if successful, otherwise false
        """
        if not details.get("name") or not details.get("products"):
            return {"response": False,
                    "msg": "Policy name must be set and at least one product should be added to policy"}

        policies = self.__get_policy_type(details)

        if len(policies["response"]) > 0:
            for policy in policies["response"]:
                self.__children.append(policy)
            self._name = details["name"]
            # self.__operator = details["operator"]
            return {'response': True, 'msg': "Great Success! Policy added"}
        return {'response': False, 'msg': "Oops...failed to add policy:\n" + policies["msg"]
                                          + "\n please check all details are correct and try again"}

    @staticmethod
    def __get_policy_type(
            details: {"name": str, "products": [str], "min_amount": int or None, "max_amount": int or None,
                      "dates": [dict] or None, "bundle": bool or None}) \
            -> {'response': [PurchaseComponent] or [], 'msg': str}:
        """
        :param details:{"name": str,                             -> policy name
                        "operator": str,                         -> and/or/xor
                        "products": [str],                       -> list of product names
                        "min_amount": int or None,               -> minimum amount of products required
                        "max_amount": int or None,               -> maximum amount of products required
                        "dates": [dict] or None,                 -> list of prohibited dated for the given products
                        "bundle": bool or None}                  -> true if the products are bundled together
        :return: list of leafs to be added
        """
        if details.get("min_amount") and details.get("max_amount") \
                and details.get("min_amount") >= details.get("max_amount"):
            return {'response': [], 'msg': "Minimum amount cannot exceed maximum amount"}

        policies = []
        if details.get("min_amount"):
            policies.append(MinAmountPolicy(details["min_amount"], details["products"]))
        if details.get("max_amount"):
            policies.append(MaxAmountPolicy(details["max_amount"], details["products"]))
        if details.get("dates"):
            policies.append(ProhibitedDatePolicy(details["dates"], details["products"]))
        if details.get("bundle") is True:
            policies.append(BundleDealPolicy(details["products"]))

        if len(policies) == 0:
            return {'response': [], 'msg': "No rules added to policy"}
        return {'response': policies, 'msg': "Success"}

    # @logger
    def equals(self, details: {"name": str, "products": [str], "min_amount": int or None, "max_amount": int or None,
                               "dates": [dict] or None, "bundle": bool or None}) -> bool:
        if details.get("name") and self._name == details["name"]:
            return True
        for rule in self.__children:
            if not rule.equals(details):
                return False
            return True
        return False

    @logger
    def get_details(self) -> dict:
        dictionary = {}
        if self._name != "":
            dictionary["name"] = self._name
        for policy in self.__children:
            dictionary = policy.get_details(dictionary)
        return dictionary

    @logger
    def get_name(self):
        return self._name

    @logger
    def update(self, details: {"name": str, "products": [str], "min_amount": int or None, "max_amount": int or None,
                               "dates": [dict] or None, "bundle": bool or None}) -> {'response': bool, 'msg': str}:
        if details.get("min_amount") and details.get("max_amount") \
                and details.get("min_amount") >= details.get("max_amount"):
            return {'response': False, 'msg': "Minimum amount cannot exceed maximum amount"}

        for policy in self.__children:
            policy.update(details)
        return {'response': True, 'msg': "Great Success! Policy updated"}

    def set_name(self, policy_name: str):
        self._name = policy_name

    def __repr__(self):
        return repr("PurchasePolicy")
