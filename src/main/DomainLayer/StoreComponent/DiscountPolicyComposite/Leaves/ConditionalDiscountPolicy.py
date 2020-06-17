from src.Logger import logger
from src.main.DomainLayer.StoreComponent.DiscountPolicyComposite.DiscountComponent import DiscountComponent
import src.main.ResponseFormat as Response
from src.main.DomainLayer.UserComponent.DiscountType import DiscountType


class ConditionalDiscountPolicy(DiscountComponent):

    def get_price_after_discount(self, price: float):
        return price*((100-self.__percentage)/100)

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

    def __init__(self, percentage: float,
                 discount_details: {'name': str,
                                    'product': str},
                 discount_precondition: {'product': str,
                                         'min_amount': int or None,
                                         'min_basket_price': str or None} or None
                 ):
        super().__init__()
        self.__name: str = discount_details['name']
        self.__percentage: float = percentage
        self.__product: str  = discount_details['product']
        self.__precondition : {} = discount_precondition

    @logger
    def get_name(self):
        return self.__name

    @logger
    def get_product_name(self):
        return self.__product

    @logger
    def update(self, percentage: float,
               discount_details: {'name': str,
                                  'product': str},
               discount_precondition: {'product': str,
                                       'min_amount': int or None,
                                       'min_cart_price': str or None} or None
               ):
        if discount_precondition is not None:
            if discount_precondition['min_amount'] < 0:
                return Response.ret(False, "Precondition minimum amount should be >= 0")

            if discount_precondition['min_basket_price'] < 0:
                return Response.ret(False, "Precondition minimum basket price should be >= 0")

            self.__precondition = discount_precondition
        if percentage != -999:
            if not 0 <= percentage <= 100:
                self.__percentage = percentage
        if discount_details is not None:
            self.__name = discount_details['name']
            self.__product = discount_details['product']
        return Response.ret(True, "Policy updated successfully.")

    @logger
    def __eq__(self, other):
        pass