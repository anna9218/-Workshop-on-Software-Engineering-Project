# from __future__ import annotations
from abc import ABC, abstractmethod


class DeliverySubject(ABC):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def is_connected(self) -> bool:
        pass

    @abstractmethod
    # need to check address details with system once a system is set
    def deliver_products(self, delivery_details: {'name': str, 'address': str, 'city': str, 'country': str,
                                                  'zip': str}) -> {'response': bool, 'msg': str}:
        pass

    @abstractmethod
    def cancel_supply(self, transaction_id: str) -> {'response': bool, 'msg': str}:
        pass
