from src.main.DomainLayer.StoreComponent.PurchasePolicyComposite.PurchaseComponent import PurchaseComponent


class MinAmountPolicy(PurchaseComponent):

    def __init__(self, min_amount: int, products: [str]):
        super().__init__()
        self.__amount = min_amount
        self.__products = products

    def operation(self):
        pass

    def add_leaf(self, component: PurchaseComponent):
        pass

    def remove_leaf(self):
        pass

    def is_composite(self):
        pass