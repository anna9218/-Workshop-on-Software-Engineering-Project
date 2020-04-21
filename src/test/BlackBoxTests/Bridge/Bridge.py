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

    @abstractmethod
    def register_user(self, username, password) -> str:
        pass
