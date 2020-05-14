# from __future__ import annotations
from abc import ABC, abstractmethod


class PaymentSubject(ABC):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    # need to check payment details with system once a system is set
    def commit_payment(self, products_ls: {"total_price": float, "products": [dict]}) -> bool:
        pass

    @abstractmethod
    def disconnect(self):
        pass

    @abstractmethod
    def is_connected(self) -> bool:
        pass

