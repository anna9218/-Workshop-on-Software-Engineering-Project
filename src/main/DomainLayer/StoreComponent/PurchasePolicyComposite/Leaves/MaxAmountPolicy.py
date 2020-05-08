from src.main.DomainLayer.StoreComponent.PurchasePolicyComposite.PurchaseComponent import PurchaseComponent


class MaxAmountPolicy(PurchaseComponent):

    def __init__(self, max_amount: int, products: [str]):
        super().__init__()
        self.__amount = max_amount
        self.__products = products

    def operation(self):
        pass

    def add_leaf(self, component: PurchaseComponent):
        pass

    def remove_leaf(self):
        pass

    def is_composite(self):
        pass