from src.main.DomainLayer.StoreComponent.PurchasePolicyComposite.PurchaseComponent import PurchaseComponent


class MaxAmountPolicy(PurchaseComponent):

    def __init__(self):
        self.__conditional = []
        self.__conditioned = []

    def operation(self):
        pass

    def add_leaf(self, component: PurchaseComponent):
        pass

    def remove_leaf(self):
        pass

    def is_composite(self):
        pass