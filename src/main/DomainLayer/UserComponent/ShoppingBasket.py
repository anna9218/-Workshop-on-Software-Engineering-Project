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
    def add_product(self, product: Product, amount: int, discount_type: DiscountType, purchase_type: PurchaseType) -> \
            bool:
        """
        This function add a product to a basket, if the amount of the product is > 0 and the product not already in the
        basket.
        if the product is already in the basket, then the function ADD the new amount to the old one.

        :param product: the product to add
        :param amount: the amount of the product to add
        :param discount_type: the discount type, if exist.
        :param purchase_type: the purchase type. direct by default
        :return: True if added successfully,
                 False else
        """

        if amount <= 0:
            return False

        for product_amount in self.__products:
            if product.get_name() == product_amount["product"].get_name():
                product_amount["amount"] += amount
                return True
        self.__products.append({"product": product, "amount": amount, "discountType": discount_type,
                                "purchaseType": purchase_type})
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
    def remove_product(self, product_name: str) -> bool:
        """
        This function remove the product from the basket.

        :param product_name: the product to remove
        :return: True if the product were in the basket and remove successfully.
                 False else.
        """
        for p in self.__products:
            if product_name == p["product"].get_name():
                self.__products.remove(p)
                return True
        return False

    @logger
    # eden
    def update_amount(self, product_name: str, amount: int):
        """
         This function update the amount of the product in the basket, but only if the product exist anf the new amount
         is >= 0.

         :param product_name: the product to remove
         :param amount: the new amount
         :return: True if the product were in the basket and update successfully.
                  False else.
         """
        if amount < 0:
            return False

        for p in self.__products:
            if p["product"].get_name() == product_name:
                p["amount"] = amount
                return True
        return False

    @logger
    # eden
    def is_empty(self):
        return len(self.__products) == 0

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

    @logger
    def get_product(self, product_name: str):
        for p in self.__products:
            if p["product"].get_name() == product_name:
                return p
        return None

    @logger
    def complete_purchase(self, product_ls: [dict]):
        """
        Update shopping basket after successful purchase.

        :param product_ls: list of dict -> [{"product_name": str, "product_price": float, "amount": int}]
        :return: void
        """
        for product in product_ls:
            prod_name = product["product_name"]

            # TODO: Fixed this error(?)
            if self.get_product_amount(prod_name) - product["amount"] < 0:
                raise ValueError("You tried to buy more then you have in the cart.")

            # TODO: Fixed this error(?)
            if not self.update_amount(prod_name, self.get_product_amount(prod_name) - product["amount"]):
                raise ValueError("The product " + prod_name + " isn't in your cart.")

            if self.get_product_amount(prod_name) == 0:
                self.remove_product(prod_name)

    def __repr__(self):
        return repr("ShoppingBasket")

    def __eq__(self, other):
        try:
            if len(self.__products) != len(other.get_products()):
                return False
            for product in self.__products:
                if product not in other.get_products():
                    return False
            return True
        except Exception:
            return False
