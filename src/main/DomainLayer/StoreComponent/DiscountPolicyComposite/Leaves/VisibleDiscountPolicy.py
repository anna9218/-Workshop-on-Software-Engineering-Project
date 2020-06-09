from datetime import datetime

from src.Logger import logger
from src.main.DomainLayer.StoreComponent.DiscountPolicyComposite.DiscountComponent import DiscountComponent
from src.main.DomainLayer.UserComponent.DiscountType import DiscountType


class VisibleDiscountPolicy(DiscountComponent):

    def get_price_after_discount(self, price: float):
        return price*(100 - self.__percentage)

    def is_worthy(self, amount: int, basket_price: float, prod_lst: [str]):
        return True

    def get_discount_type(self):
        return DiscountType.VISIBLE

    def get_percentage(self):
        return self.__percentage

    def __init__(self, percentage: float, discount_details: {'name': str, 'product': str}):
        super().__init__()
        self.__name = discount_details['name']
        self.__percentage = percentage
        self.__product = discount_details['product']

    @logger
    def get_name(self):
        return self.__name

    @logger
    def get_product_name(self):
        return self.__product

    @logger
    def update(self, percentage: float = -999,
               discount_details: {'name': str,
                                  'product': str} = None,
               discount_precondition: {'product': str,
                                       'min_amount': int or None,
                                       'min_cart_price': str or None} or None = None
               ):

        if discount_precondition is not None:
            return {'response': False, 'msg': "Visible discount can't have precondition."}
        if percentage != -999:
            if 0 <= percentage <= 100:
                self.__percentage = percentage
        if discount_details is not None:
            self.__name = discount_details['name']
            self.__product = discount_details['product']
        return {'response': True, 'msg': "Policy updated successfully"}

    @logger
    def __eq__(self, other):
        pass
