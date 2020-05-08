from src.main.DomainLayer.StoreComponent.PurchasePolicyComposite.PurchaseComponent import PurchaseComponent


class BundleDealPolicy(PurchaseComponent):

    def __init__(self):
        self.__products = []

    def operation(self):
        pass

    def add_leaf(self, component: PurchaseComponent):
        pass

    def remove_leaf(self):
        pass

    def is_composite(self):
        pass