"""
    Declares interface for composite pattern and implements default behaviour.
"""
from abc import ABC, abstractmethod


class DiscountComponent(ABC):
    @abstractmethod
    def operation(self):
        pass

    @abstractmethod
    def add_leaf(self, component):
        pass

    @abstractmethod
    def remove_leaf(self, component):
        pass

    @abstractmethod
    def is_composite(self):
        return False
