from src.main.DomainLayer import Product


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

    def add_product(self, p, amount):
        # TODO - add check if exist before?
        self.__inv.append((p, amount))

    def __repr__(self):
        return repr("There are " + str(len(self.__inv)) + " products on inventory")

    def add_to_amount(self, product: Product, addToAmount):
        self._amountPerProduct[product] = self._amountPerProduct(product)+ addToAmount # TODO- check it overittes the prev amount of product


    def get_amount_of_product (self, product_name):
        for i in self.__inv:
            if i[0].get_name() == product_name:
                return i[1]
        return None

