from Backend.src.Logger import logger
from Backend.src.main.DomainLayer.StoreComponent.Product import Product
from Backend.src.main.DomainLayer.StoreComponent.PurchasePolicyComposite.Leaves.MaxAmountPolicy import MaxAmountPolicy
from Backend.src.main.DomainLayer.StoreComponent.PurchasePolicyComposite.Leaves.MinAmountPolicy import MinAmountPolicy
from Backend.src.main.DomainLayer.StoreComponent.PurchasePolicyComposite.Leaves.ProhibitedDatePolicy import ProhibitedDatePolicy
from Backend.src.main.DomainLayer.StoreComponent.PurchasePolicyComposite.PurchaseComponent import PurchaseComponent
from Backend.src.main.DomainLayer.UserComponent.UserType import UserType


class PurchasePolicy:

    def __init__(self):
        self.__policies = [PurchaseComponent]

        """-> list of ([user_type: UserType, price: float, list of [product: Product, amount: int]] """
        self.policy_details = [{"type": str, "basic_rules": []}]
        self.__disallowed_purchases = list()
    # max_amount, min_amount -> if we need min products or max products allowed
    # products_together = [Product/product_name]

    def add_purchase_policy(self, details: [dict]):
        if not details["products"]:
            return False

        if details["min_amount"]:
            self.__policies.append(MinAmountPolicy(details["min-amount"], details["products"]))
            return True
        elif details["max_amount"]:
            self.__policies.append(MaxAmountPolicy(details["max_amount"], details["products"]))
            return True
        elif details["dates"]:
            self.__policies.append(ProhibitedDatePolicy(details["dates"], details["products"]))
            return True
        elif details["products"]:
            self.__policies.append(details["products"])
            return True
        else:
            return False

    def remove_purchase_policy(self, policy: PurchaseComponent):
        self.__policies.remove(policy)

    def update_purchase_policy(self, policy: PurchaseComponent, details: [str]):
        pass


    # @logger
    def add_disallowed_purchasing(self, disallowed_purchase: list):
        if type(disallowed_purchase) != [UserType, Product, list]:
            return
        for disallowed_purchase_term in disallowed_purchase:
            if type(disallowed_purchase_term[2]) != [Product, int]:
                return
        if disallowed_purchase in self.__disallowed_purchases:
            return
        self.__disallowed_purchases.insert(0, disallowed_purchase)

    # @logger
    def can_purchase(self, amount_per_product_per_user_type: []):
        if amount_per_product_per_user_type in self.__disallowed_purchases:
            return False
        return True

    def check_policy(self, store_name: str, product_name: str):
        return True

    def __repr__(self):
        return repr("PurchasePolicy")
