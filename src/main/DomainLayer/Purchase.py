
from src.main.DomainLayer.Store import Store
from src.main.DomainLayer.User import User


class Purchase:
    def __init__(self, purchase_id: int, amount_per_product: [], store: Store):
        """

        :param amount_per_product: a list of  [product, amount]
        """
        self.__Purchase_id: int = purchase_id
        self.__amount_per_product = amount_per_product
        self.__store: Store = store

    def get_product(self, product_name):
        for amount_per_product in self.__inv:
            if amount_per_product[0].get_name() == product_name:
                return amount_per_product
        return None

    def get_product_name(self, product_name):
        for amount_per_product in self.__inv:
            if amount_per_product[0].get_name() == product_name:
                return amount_per_product[0]
        return None

    def get_product_amount(self, product_name):
        product = self.get_product(product_name)
        if product:
            return product[1]
        return None
