"""
    Declares interface for composite pattern and implements default behaviour.
"""
from abc import ABC, abstractmethod


class DiscountComponent(ABC):

    def __init__(self):
        self._name = ""

    @abstractmethod
    def get_discount(self, details):
        pass

    @abstractmethod
    def equals(self, details):
        pass

    @abstractmethod
    def update(self, details):
        pass
