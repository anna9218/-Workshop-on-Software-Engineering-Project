# from __future__ import annotations
from abc import ABC, abstractmethod


class DeliverySubject(ABC):

    def __init__(self):
        super().__init__()

    # Register tests bridged functions
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    # need to check address details with system once a system is set
    def deliver_products(self, address: str, products_ls: []) -> bool:
        pass

    @abstractmethod
    def disconnect(self):
        pass

    @abstractmethod
    def is_connected(self) -> bool:
        pass
