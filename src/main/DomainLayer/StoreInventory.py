from src.main.DomainLayer import Product


class StoreInventory:

    def __init__(self):
        # list of the pairs (product, amount)
        self.__inv = [] # short for inventory
        self.__fun_map = [lambda product_name: filter(lambda product: product.get_name() == product_name, [x[0] for x in self.__inv]),
                          lambda keyword: filter(lambda product: keyword in product.get_name(), [x[0] for x in self.__inv]),
                          lambda category: filter(lambda product: product.get_category() == category, [x[0] for x in self.__inv])]

    def get_products_by(self, opt, string):
        return self.__fun_map[opt-1](string)

    def get_product(self, product_name):
        for i in self.__inv:
            if i[0].get_name() == product_name:
                return i[0]
        return None

    def add_product(self, p, amount) -> bool:
        """
        :param p: product
        :param amount: amount of product
        :return: True if the inventory updated with the new product, else return false
        """
        if p in self.__inv:
            return False
        self.__inv.append((p, amount))
        return True

    def remove_product(self, product):
        """
        :param product: product to delete from inventory
        :return: True if the inventory updated without the product
        """
        for p in self.__inv:
            if product.get_name() == p[0].get_name():
                self.__inv.remove(p)
                return True
        return False

    def __repr__(self):
        return repr("There are " + str(len(self.__inv)) + " products on inventory")

    def change_amount(self, product: Product, new_amount) -> bool:
        """
        :param product: product to edit
        :param new_amount: number to replace with
        :return: True if the product updated with new amount on inventory
        """
        for i in self.__inv:
            if i[0].get_name() == product.get_name():
                self.__inv.remove(i)
                self.__inv.append((product, new_amount))
                return True
        return False

    def len (self):
        """
        :return: amount of products on inventory
        """
        return len(self.__inv)


    def get_amount_of_product (self, product_name):
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