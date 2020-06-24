from datetime import datetime

from src.main.DomainLayer.StoreComponent.PurchasePolicyComposite.PurchaseComponent import PurchaseComponent


class BundleDealPolicy(PurchaseComponent):

    def __init__(self, products: [str]):
        super().__init__()
        self._name = "bundle"
        self.__products = products

    def can_purchase(self, details: [{"product_name": str, "amount": int}], curr_date: datetime) -> bool:
        flag = [False]*len(self.__products)
        index = 0
        for product in details:
            if (product["product_name"] in self.__products) or ("all" in self.__products):
                flag[index] = True
            index += 1

        return False not in flag

    def equals(self, details: {"products": [str], "min_amount": int or None, "max_amount": int or None,
                               "dates": [dict] or None, "bundle": bool or None}) -> bool:
        if details.get("bundle") \
                and set(self.__products) == set(details["products"]):
            # for product in self.__products:
            #     if product not in details["products"]:
            #         return False
            return True
        return False

    def get_name(self):
        return self._name

    def get_details(self, dictionary: dict):
        dictionary[self._name] = True
        return dictionary

    def get_products(self):
        return self.__products

    def update(self, details: {"name": str, "products": [str], "min_amount": int or None, "max_amount": int or None,
                               "dates": [dict] or None, "bundle": bool or None}):
        if details.get("bundle"):
            self.__products = details["products"]
