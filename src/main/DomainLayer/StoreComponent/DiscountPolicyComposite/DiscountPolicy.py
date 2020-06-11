from datetime import datetime

from src.Logger import logger
from src.main.DomainLayer.StoreComponent.DiscountPolicyComposite.DiscountComponent import DiscountComponent
from src.main.DomainLayer.StoreComponent.DiscountPolicyComposite.Leaves.ConditionalDiscountPolicy import \
    ConditionalDiscountPolicy
from src.main.DomainLayer.StoreComponent.DiscountPolicyComposite.Leaves.VisibleDiscountPolicy import \
    VisibleDiscountPolicy


class DiscountPolicy(DiscountComponent):

    def __init__(self):
        super().__init__()
        self.__children: [DiscountComponent] = []

    @logger
 #   def get_discount(self, details):
 #       pass
    def update(self, percentage: float = -999,
               discount_details: {'name': str,
                                  'product': str} = None,
               discount_precondition: {'product': str,
                                       'min_amount': int or None,
                                       'min_basket_price': str or None} or None = None):

        if discount_precondition is not None:
            return {'response': False, 'msg': "Composite discount can't have not-policy precondition."}

        if percentage != -999:
            if 0 <= percentage <= 100:
                self.__percentage = percentage
            else:
                return {'response': False, 'msg': "Composite discount can't have not-policy precondition."}
        if discount_details is not None:
            self.__name = discount_details['name']
            self.__product = discount_details['product']
        return {'response': True, 'msg': "Policy updated successfully."}

    @logger
    def add_discount_policy(self, details: {"name": str, "operator": str, "products": [{"name": str, "price": float}],
                                            "end_time": datetime, "percentage": float, "conditions": [str] or None}):
        """
        :param details: {"name": str,                   -> policy name
                         "operator": str,               -> or/and/xor
                         "products": [str],             -> list of products names that have discount on them
                         "end_time": datetime,          -> time the discount ends
                         "percentage": float,           -> discount
                         "conditions": [str] or None}   -> products that are needed in order to get the discount
        :return: true if successful, otherwise false
        """
        if not details.get("products") or not details.get("name") \
                or not details.get("operator") or not details.get("end_time") or not details.get("percentage"):
            return False

        self._name = details["name"]
        if details.get("conditions"):
            self.__children.append(ConditionalDiscountPolicy(details))
        else:
            self.__children.append(VisibleDiscountPolicy(details))
        return True

    @logger
    def update_discount_policy(self, details):
        pass

    @logger
    def equals(self, details):
        pass

    @logger
    def update(self, details):
        pass

    def __repr__(self):
        return repr ("DiscountPolicy")