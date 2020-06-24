# from __future__ import annotations
from abc import ABC, abstractmethod


class PaymentSubject(ABC):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def is_connected(self) -> bool:
        pass

    @abstractmethod
    def commit_payment(self, payment_details: {'card_number': str, 'month': str, 'year': str, 'holder': str,
                                               'ccv': str, 'id': str}) -> {'response': bool, 'msg': str}:
        pass

    @abstractmethod
    def cancel_pay(self, transaction_id: str) -> {'response': bool, 'msg': str}:
        pass
