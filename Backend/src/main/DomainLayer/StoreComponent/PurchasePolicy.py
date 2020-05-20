"""
        purchase composite class - executes child operation for purchase component interface
"""
from datetime import datetime

from Backend.src.Logger import logger
from Backend.src.main.DomainLayer.StoreComponent.PurchasePolicyComposite.Leaves.BundleDealPolicy import BundleDealPolicy
from Backend.src.main.DomainLayer.StoreComponent.PurchasePolicyComposite.Leaves.MaxAmountPolicy import MaxAmountPolicy
from Backend.src.main.DomainLayer.StoreComponent.PurchasePolicyComposite.Leaves.MinAmountPolicy import MinAmountPolicy
from Backend.src.main.DomainLayer.StoreComponent.PurchasePolicyComposite.Leaves.ProhibitedDatePolicy import ProhibitedDatePolicy
from Backend.src.main.DomainLayer.StoreComponent.PurchasePolicyComposite.PurchaseComponent import PurchaseComponent


class PurchasePolicy(PurchaseComponent):

    def __init__(self):
        super().__init__()
        self.__children: [PurchaseComponent] = []
        self.__operator = ""

    def can_purchase(self, details: [{"product_name": str, "amount": int}], curr_date: datetime):
        """
        :param curr_date:
        :param details: list [{"product_name": str, "amount": int}]
        :return: True if the user can purchase the products, else False
        """
        xor_flag = False
        for policy in self.__children:
            can_purchase = policy.can_purchase(details, curr_date)
            if self.__operator == "and" and not can_purchase:
                return False
            elif self.__operator == "xor":
                if can_purchase:
                    if not xor_flag:
                        xor_flag = True
                    else:
                        return False
            elif self.__operator == "or" and can_purchase:
                return True
            else:
                return False
        return True

    def add_purchase_policy(self, details: {"name": str, "operator": str, "products": [str], "min_amount": int or None,
                                            "max_amount": int or None, "dates": [dict] or None,
                                            "bundle": bool or None}) -> bool:
        """
            add new purchase policy. current policies available are: grouped products, prohibited dates,
            min amount and max amount
        :param details: {"name": str,                             -> policy name
                        "operator": str,                         -> and/or/xor
                        "products": [str],                       -> list of product names
                        "min_amount": int or None,               -> minimum amount of products required
                        "max_amount": int or None,               -> maximum amount of products required
                        "dates": [dict] or None,                 -> list of prohibited dated for the given products
                        "bundle": bool or None}                  -> true if the products are bundled together
                i.e. details can be: {"products", "bundle"} / {"products", "min_amount"} etc.
        :return: true if successful, otherwise false
        """
        if not details.get("products") or not details.get("name") or not details.get("operator"):
            return False

        policies = self.__get_policy_type(details)

        if len(policies) > 0:
            for policy in policies:
                self.__children.append(policy)
            self._name = details["name"]
            self.__operator = details["operator"]
            return True
        return False

    @staticmethod
    def __get_policy_type(details: {"name": str, "operator": str, "products": [str], "min_amount": int or None, "max_amount": int or None,
                                    "dates": [dict] or None, "bundle": bool or None}) -> [PurchaseComponent] or []:
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
        policies = []
        if details.get("min_amount"):
            policies.append(MinAmountPolicy(details["min_amount"], details["products"]))
        if details.get("max_amount"):
            policies.append(MaxAmountPolicy(details["max_amount"], details["products"]))
        if details.get("dates"):
            policies.append(ProhibitedDatePolicy(details["dates"], details["products"]))
        if details.get("bundle") is True:
            policies.append(BundleDealPolicy(details["products"]))
        return policies

    def equals(self, details: {"name": str, "operator": str or None, "products": [str], "min_amount": int or None, "max_amount": int or None,
                               "dates": [dict] or None, "bundle": bool or None}) -> bool:
        if details.get("name") and self._name == details["name"]:
            return True
        return False

    def get_details(self) -> dict:
        dictionary = {"name": self._name, "operator": self.__operator}
        for policy in self.__children:
            dictionary = policy.get_details(dictionary)
        return dictionary

    def get_name(self):
        return self._name

    def update(self, details: {"name": str, "operator": str or None, "products": [str], "min_amount": int or None, "max_amount": int or None,
                               "dates": [dict] or None, "bundle": bool or None}):
        for policy in self.__children:
            policy.update(details)
        return True

    def __repr__(self):
        return repr("PurchasePolicy")
