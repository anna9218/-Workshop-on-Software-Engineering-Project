from datetime import datetime

from src.Logger import logger
from src.main.DomainLayer.StoreComponent.DiscountPolicyComposite.DiscountComponent import DiscountComponent
import src.main.ResponseFormat as Response
from src.main.DomainLayer.UserComponent.DiscountType import DiscountType


class ConditionalDiscountPolicy(DiscountComponent):

    def __init__(self,
                 percentage: float,
                 valid_until: datetime,
                 discount_details: {'name': str,
                                    'product': str},
                 discount_precondition: {'product': str,
                                         'min_amount': int or None,
                                         'min_basket_price': str or None} or None
                 ):
        super().__init__()
        self.__name: str = discount_details['name']
        self.__percentage: float = percentage
        self.__product: str = discount_details['product']
        self.__precondition: {} = discount_precondition
        self.__valid_until = valid_until

    def get_as_dictionary(self):
        return {'name': self.__name,
                'percentage': self.__percentage,
                'product': self.__product,
                'valid_until': self.__valid_until,
                'precondition': self.__precondition}

    def get_valid_until_date(self):
        return self.__valid_until

    def set_valid_until_date(self, new_date: datetime):
        self.__valid_until = new_date

    def get_price_after_discount(self, price: float):
        return price * ((100 - self.__percentage) / 100)

    def is_worthy(self, amount: int, basket_price: float, prod_lst: [str]):
        if self.__precondition['product'].lower().strip() == "all":
            if basket_price >= self.__precondition['min_basket_price']:
                return True
        else:
            if amount >= self.__precondition['min_amount']:
                if self.__precondition['min_basket_price'] is not None:
                    if basket_price >= self.__precondition['min_basket_price']:
                        return True
                else:
                    return True
        return False

    def get_discount_type(self):
        return DiscountType.CONDITIONAL

    def get_percentage(self):
        return self.__percentage

    @logger
    def get_name(self):
        return self.__name

    @logger
    def get_product_name(self):
        return self.__product

    @logger
    def update(self, percentage: float = -999, valid_until: datetime = None,
               discount_details: {'name': str,
                                  'product': str} = None,
               discount_precondition: {'product': str,
                                       'min_amount': int or None,
                                       'min_cart_price': str or None} or None = None
               ):
        if discount_precondition is not None:
            if discount_precondition['min_amount'] is not None:
                if discount_precondition['min_amount'] >= 0:
                    self.__precondition['min_amount'] = discount_precondition['min_amount']

            if discount_precondition['min_basket_price'] is not None:
                if discount_precondition['min_basket_price'] >= 0:
                    self.__precondition['min_amount'] = discount_precondition['min_amount']

            if discount_details['product'] is not None:
                self.__precondition['product'] = discount_precondition['product']

        if percentage != -999:
            if 0 <= percentage <= 100:
                self.__percentage = percentage
            else:
                return {'response': False, 'msg': "Percentage should be between 0 and 100."}

        if discount_details is not None:
            if discount_details['name'] is not None:
                self.__name = discount_details['name']
            if discount_details['product'] is not None:
                self.__product = discount_details['product']
        return Response.ret(True, "Policy updated successfully.")

    @logger
    def __eq__(self, other):
        pass
