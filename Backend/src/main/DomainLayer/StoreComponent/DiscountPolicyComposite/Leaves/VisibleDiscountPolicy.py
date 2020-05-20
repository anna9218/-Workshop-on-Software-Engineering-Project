from datetime import datetime

from Backend.src.main.DomainLayer.StoreComponent.DiscountPolicyComposite.DiscountComponent import DiscountComponent


class VisibleDiscountPolicy(DiscountComponent):

    def __init__(self, details: {"products": [{"name": str, "price": float}],
                                            "end_time": datetime, "percentage": float}):
        super().__init__()
        self.__products = details["products"]
        self.__percentage = details["percentage"]
        self.end_time = details["end_time"]

    def get_discount(self, details):
        pass

    def equals(self, details):
        pass

    def update(self, details):
        pass
