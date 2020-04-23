class ShoppingBasket:
    def __init__(self):
        self.__products = []

    def add_product(self, product):
        self.__products.append(product)

    def remove_product(self, product):
        self.__products.remove(product)

    def get_products(self):
        return self.__products
