from src.main.DomainLayer import Product


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

    def get_products_by(self, opt, string):
        return self.__fun_map[opt-1](string)

    def get_product(self, product_name):
        for i in self.__inv:
            if i[0].get_name() == product_name:
                return i[0]
        return None

    def add_product(self, p, amount):
        if p in self.__inv:
            return False
        self.__inv.append((p, amount))

    def remove_product(self, product):
        for p in self.__inv:
            if product.get_name() == p[0].get_name():
                self.__inv.remove(p)

    def __repr__(self):
        return repr("There are " + str(len(self.__inv)) + " products on inventory")

    def add_to_amount(self, product: Product, new_amount):
        for i in self.__inv:
            if i[0].get_name() == product.get_name():
                self.__inv.remove(i)
                self.__inv.append((product, new_amount))

    def len(self):
        return len(self.__inv)

    def get_amount_of_product(self, product_name):
        for i in self.__inv:
            if i[0].get_name() == product_name:
                return i[1]
        return None

    def is_in_stock(self, product_name, requested_amount):
        """

        :param product_name: the name of the product to search in inventory.
        :param requested_amount: the requested amount.
        :return: if is in stock true,
                 else false.
        """
        product = self.get_product(product_name)
        if product:
            amount = product[1]
            if amount >= requested_amount:
                return True
        else:
            return False
