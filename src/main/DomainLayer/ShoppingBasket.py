from src.Logger import logger


class ShoppingBasket:
    def __init__(self):
        self.__products = []  # should be a list of (product, amount)
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
    def add_product(self, product_amount) -> bool:
        self.__products.append(product_amount)  # add (product, quantity)
        return True

    @logger
    def remove_product(self, product) -> bool:
        for product_amount in self.__products:
            if product.get_name() == product_amount[0].get_name():
                self.__products.remove([product_amount[0], product_amount[1]])
                return True
        return False

    @logger
    def get_products(self):
        return self.__products

    @logger
    def get_product_by_name(self, product):
        for p in self.__products:
            if p.get_name() == product.get_name():
                return p
        return None

    @logger
    def is_in_basket(self, product) -> bool:
        for p in self.__products:
            if p[0].get_name() == product.get_name():
                return True
        return False

    def __repr__(self):
        return repr("ShoppingBasket")