from src.main.DomainLayer import Product


# class StoreInventory:
#
#     def __init__(self):
#         self._amountPerProduct = {}
#
#     def get_amount_of_product(self, p: Product):
#         if self.check_if_exists(p):
#             print(self._amountPerProduct.get (p))
#             return self._amountPerProduct.get (p)
#         else:
#             print("There is no such product as " + p.get_name())
#             return False
#
#     def add_to_amount(self, product: Product, addToAmount):
#         self._amountPerProduct[product] = self._amountPerProduct(product)+ addToAmount # TODO- check it overwrites the prev amount of product
#
#     def add_product (self, product, amount):
#         self._amountPerProduct[product] = amount # TODO- change the key to be the product name
class StoreInventory:

    def __init__(self):
        # list of the pairs (product, amount)
        self.__inv = []
        self.__fun_map = [lambda product_name: filter(lambda product: product.get_name() == product_name, [x[0] for x in self.__inv]),
                          lambda keyword: filter(lambda product: keyword in product.get_name(), [x[0] for x in self.__inv]),
                          lambda category: filter(lambda product: product.get_category() == category, [x[0] for x in self.__inv])]

    def getProductsBy(self, opt, string):
        return self.__fun_map[opt-1](string)

    def getProduct(self, product_name):
        for i in self.__inv:
            if i[0].get_name() == product_name:
                return i[0]
        return None

