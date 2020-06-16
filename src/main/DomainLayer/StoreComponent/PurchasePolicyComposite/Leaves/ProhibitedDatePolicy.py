from datetime import datetime
import jsonpickle

from src.main.DomainLayer.StoreComponent.PurchasePolicyComposite.PurchaseComponent import PurchaseComponent


class ProhibitedDatePolicy(PurchaseComponent):

    def __init__(self, dates: [datetime], products: [str]):
        super().__init__()
        self._name = "dates"
        self.__bad_dates: [datetime] = dates
        # for d in dates:
            # self.__bad_dates.append(jsonpickle.decode(d))
        self.__products = products

    def can_purchase(self, details: [{"product_name": str, "amount": int}], curr_date: datetime) -> bool:
        flag = curr_date in self.__bad_dates
        if "all" in self.__products and flag:
            return False

        for product in details:
            if product["product_name"] in self.__products and flag:
                return False
        return True

    def equals(self, details: {"products": [str], "min_amount": int or None, "max_amount": int or None,
                               "dates": [dict] or None, "bundle": bool or None}) -> bool:
        if details.get("dates") and set(self.__products) == set(details["products"]):
            return True
        return False

    def update(self, details: {"name": str, "products": [str], "min_amount": int or None, "max_amount": int or None,
                               "dates": [dict] or None, "bundle": bool or None}):
        if details.get("dates"):
            self.__products = details["products"]
            self.__bad_dates = details["dates"]

    def get_dates(self):
        return self.__bad_dates

    def get_products(self):
        return self.__products

    def get_name(self):
        return self._name

    def get_details(self, dictionary: dict):
        dictionary[self._name] = self.__bad_dates
        return dictionary
