from src.Logger import logger
from src.main.DomainLayer.StoreComponent.Product import Product
from src.main.DomainLayer.UserComponent.UserType import UserType


class DiscountPolicy:

    def __init__(self):
        """-> list of ([user_type: UserType, price: float, list of [product: Product, amount: int]] """
        self.__discounts = list()

    # @logger
    def add_disallowed_purchasing(self, discounts: list):
        if type(discounts) != [UserType, Product, list]:
            return
        for disallowed_purchase_term in discounts:
            if type(disallowed_purchase_term[2]) != [Product, int]:
                return
        if discounts in self.__discounts:
            return
        self.__discounts.insert(0, discounts)

    # @logger
    def is_deserve_to_discount(self, amount_per_product_per_user_type: []):
        if amount_per_product_per_user_type in self.__discounts:
            return False
        return True

    def check_discount(self, store_name: str, product_name: str):
        return True

    def __repr__(self):
        return repr ("DiscountPolicy")