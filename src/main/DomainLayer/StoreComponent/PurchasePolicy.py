from src.Logger import logger
from src.main.DomainLayer.StoreComponent.Product import Product
from src.main.DomainLayer.UserComponent.UserType import UserType


class PurchasePolicy:

    def __init__(self):
        """-> list of ([user_type: UserType, price: float, list of [product: Product, amount: int]] """
        self.__disallowed_purchases = list()

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
