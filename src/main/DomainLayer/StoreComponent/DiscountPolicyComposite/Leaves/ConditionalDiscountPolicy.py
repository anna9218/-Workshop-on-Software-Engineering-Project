from datetime import datetime
from src.main.DomainLayer.StoreComponent.DiscountPolicyComposite.DiscountComponent import DiscountComponent


class ConditionalDiscountPolicy(DiscountComponent):

    def __init__(self, details: {"name": str, "operator": str, "products": [{"name": str, "price": float}],
                                            "end_time": datetime, "percentage": float, "conditions": [str] or None}):
        """
        :param products: products with discount on them
        :param percentage: discount
        :param end_time: discount end time
        :param condition: products needed in order to get the discount
        """
        super().__init__()
        self.__products = details["products"]
        self.__percentage = details["percentage"]
        self.__end_time = details["end_time"]
        self.__conditions = details["conditions"]

    def get_discount(self, details):
        pass

    def equals(self, details):
        pass

    def update(self, details):
        pass



