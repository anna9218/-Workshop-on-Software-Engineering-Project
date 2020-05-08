"""
    executes child operation for component interface
"""
from src.main.DomainLayer.StoreComponent.PurchasePolicyComposite.PurchaseComponent import PurchaseComponent


class DiscountComposite(PurchaseComponent):

    def __init__(self):
        self.__children = []

    def operation(self):
        pass

    def add_leaf(self, component: PurchaseComponent):
        self.__children.append(component)

    def remove_leaf(self,  component: PurchaseComponent):
        self.__children.remove(component)

    def is_composite(self):
        return True
