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
    def somefunction(self) -> str:
        pass

    @abstractmethod
    def test_sum(self, x, y) -> int:
        pass

    @abstractmethod
    def test_wrong_sum(self, x, y) -> int:
        pass
