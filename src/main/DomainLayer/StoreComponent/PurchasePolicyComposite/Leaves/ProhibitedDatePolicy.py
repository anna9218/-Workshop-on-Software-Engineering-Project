from datetime import datetime

from src.main.DomainLayer.StoreComponent.PurchasePolicyComposite.PurchaseComponent import PurchaseComponent


class ProhibitedDatePolicy(PurchaseComponent):

    def __init__(self, dates: [datetime], products: [str]):
        super().__init__()
        self.__bad_dates = dates
        self.__products = products

    def operation(self):
        pass

    def add_leaf(self, component: PurchaseComponent):
        pass

    def remove_leaf(self):
        pass

    def is_composite(self):
        pass