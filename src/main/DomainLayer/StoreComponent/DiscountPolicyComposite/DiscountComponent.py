"""
    Declares interface for composite pattern and implements default behaviour.
"""
from abc import ABC, abstractmethod
from datetime import datetime


class DiscountComponent(ABC):

    def __init__(self):
        self._name = ""

    @abstractmethod
    def get_price_after_discount(self, price: float):
        pass

    @abstractmethod
    def is_worthy(self, amount: int, basket_price: float, prod_lst: [str]):
        pass

    @abstractmethod
    def update(self, percentage: float,
               valid_until: datetime,
               discount_details: {'name': str,
                                  'product': str},
               discount_precondition: {'product': str,
                                       'min_amount': int or None,
                                       'min_basket_price': str or None} or None
               ):
        pass

    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_product_name(self):
        pass

    @abstractmethod
    def get_percentage(self):
        pass

    @abstractmethod
    def get_discount_type(self):
        pass

    @abstractmethod
    def get_valid_until_date(self):
        pass

    @abstractmethod
    def set_valid_until_date(self, new_date: datetime):
        pass

    def __eq__(self, other):
        pass
