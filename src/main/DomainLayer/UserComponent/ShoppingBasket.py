from src.Logger import logger
from src.main.DomainLayer.StoreComponent.Product import Product
from src.main.DomainLayer.UserComponent.DiscountType import DiscountType
from src.main.DomainLayer.UserComponent.PurchaseType import PurchaseType


class ShoppingBasket:
    def __init__(self):
        self.__products: [{"product": Product, "amount": int, "discountType": DiscountType, "purchaseType": PurchaseType}] = []
        self.__i = 0

    # in order to make the object iterable
    def __iter__(self):
        self.__i = 0
        return self

    def __next__(self):
        while self.__i < len(self.__products):
            x = self.__products[self.__i]
            self.__i += 1
            return x
        else:
            raise StopIteration

    @logger
    def add_product(self, product: Product, amount: int, discount_type: DiscountType, purchase_type: PurchaseType) -> bool:
        for product_amount in self.__products:
            if product.get_name() == product_amount["product"].get_name():
                product_amount["amount"] += amount
                return True
        self.__products.append({"product": product, "amount": amount, "discountType": discount_type, "purchaseType": purchase_type})
        return True

    @logger
    def get_basket_info(self):
        """
        :return: list: [{"product_name": str
                         "amount": int}, ...]
        """
        return list(map(lambda x: {"product_name": x["product"].get_name(),
                                   "amount": x["amount"]}, self.__products))

    @logger
    # eden
    def remove_product(self, product_name: str) -> bool:
        for p in self.__products:
            if product_name == p["product"].get_name():
                self.__products.remove(p)
                return True
        return False

    @logger
    # eden
    def update_amount(self, product_name: str, amount: int):
        for p in self.__products:
            if p["product"].get_name() == product_name:
                p["amount"] = amount
                return True
        return False

    @logger
    # eden
    def is_empty(self):
        return self.__products == []

    # @logger
    # def get_product_by_name(self, product):
    #     for p in self.__products:
    #         if p.get_name() == product.get_name():
    #             return p
    #     return None
    #
    # @logger
    # def is_in_basket(self, product) -> bool:
    #     for p in self.__products:
    #         if p[0].get_name() == product.get_name():
    #             return True
    #     return False

    @logger
    def get_products(self):
        return self.__products

    @logger
    def get_product_amount(self, product_name: str):
        for p in self.__products:
            if p["product"].get_name() == product_name:
                return p["amount"]
        return 0

    def __repr__(self):
        return repr("ShoppingBasket")
