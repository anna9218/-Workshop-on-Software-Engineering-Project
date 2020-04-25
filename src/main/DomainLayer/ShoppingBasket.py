class ShoppingBasket:
    def __init__(self):
        self.__products = []  # should be a list of (product, amount)

    def add_product(self, product_amount):
        self.__products.append(product_amount)  # add (product, quantity)
        return True

    def remove_product(self, product):
        self.__products.remove(product)
        return True

    def get_products(self):
        return self.__products
