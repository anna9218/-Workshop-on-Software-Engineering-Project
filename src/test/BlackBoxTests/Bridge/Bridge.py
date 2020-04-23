"""
    abstract class representing the:
                                    - implementor in the Bridge pattern
                                    - target in the adapter pattern
                                    - subject in the proxy pattern  
"""
# from __future__ import annotations
from abc import ABC, abstractmethod


class Bridge(ABC):

    def __init__(self):
        super().__init__()

    # Register tests bridged functions
    @abstractmethod
    def register_user(self, username, password) -> bool:
        pass

    # Payment System tests bridged functions
    @abstractmethod
    def connect_payment_sys(self):
        pass

    @abstractmethod
    def commit_payment(self, username, amount, credit, date) -> bool:
        pass

    @abstractmethod
    def disconnect_payment_sys(self):
        pass

    # Payment System tests bridged functions
    @abstractmethod
    def connect_delivery_sys(self):
        pass

    @abstractmethod
    def deliver(self, username, address) -> bool:
        pass

    @abstractmethod
    def disconnect_delivery_sys(self):
        pass
