"""
    Declares interface for composite pattern and implements default behaviour.
"""
from abc import ABC, abstractmethod
from datetime import datetime


class PurchaseComponent(ABC):

    def __init__(self):
        self._name = ""

    @abstractmethod
    def can_purchase(self, details: [{"product_name": str, "amount": int}], curr_date: datetime) -> bool:
        pass

    @abstractmethod
    def equals(self, details: {"products": [str], "min_amount": int or None, "max_amount": int or None,
                               "dates": [dict] or None, "bundle": bool or None}) -> bool:
        pass

    @abstractmethod
    def update(self, details: {"name": str, "products": [str], "min_amount": int or None, "max_amount": int or None,
                               "dates": [dict] or None, "bundle": bool or None}):
        pass

    @abstractmethod
    def get_details(self) -> dict:
        pass
