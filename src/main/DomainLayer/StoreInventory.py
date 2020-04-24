class StoreInventory:

    def __init__(self):
        """
        :field  __inv: list of the pairs (product, amount)
        """
        self.__inv: list = []
        self.__fun_map = [lambda product_name: filter(lambda product: product.get_name() == product_name, [x[0] for x in
                                                                                                           self.__inv]),
                          lambda keyword: filter(lambda product: keyword in product.get_name(), [x[0] for x in
                                                                                                 self.__inv]),
                          lambda category: filter(lambda product: product.get_category() == category, [x[0] for x in
                                                                                                       self.__inv])]

    def getProductsBy(self, opt, string):
        return self.__fun_map[opt-1](string)

    def getProduct(self, product_name):
        for i in self.__inv:
            if i[0].get_name() == product_name:
                return i[0]
        return None

    def is_in_stock(self, product_name, requested_amount):
        """

        :param product_name: the name of the product to search in inventory.
        :param requested_amount: the requested amount.
        :return: if is in stock true,
                 else false.
        """
        product = self.getProduct(product_name)
        if product:
            amount = product[1]
            if amount >= requested_amount:
                return True
        else:
            return False
