from src.main.DomainLayer import Product


class StoreInventory:

    def __init__(self):
        # list of the pairs (product, amount)
        self.__inventory = []
        # list of search functions: __fun_map[0] = searchProductsByName(product_name)
        #                           __fun_map[1] = searchProductByKeyword(keyword)
        #                           __fun_map[2] = searchProductByCategory(category)
        #  all the functions returns list of products
        self.__fun_map = [lambda product_name: list(filter(lambda product: product.get_name() == product_name, [x[0] for x in self.__inventory])),
                          lambda keyword: list(filter(lambda product: keyword in product.get_name(), [x[0] for x in self.__inventory])),
                          lambda category: list(filter(lambda product: product.get_category() == category, [x[0] for x in self.__inventory]))]

    def add_product(self, product: Product, amount) -> bool:
        """
        :param product: Product
        :param amount: amount of product
        :return: true,and the inventory updated with the new product or the products amount is increased
        """
        products_ls = self.__fun_map[0](product.get_name())
        if len(products_ls):
            old_product_amount = self.get_amount_of_product(product.get_name())
            self.remove_product(product.get_name())
            self.__inventory.append((product, amount + old_product_amount))
        else:
            self.__inventory.append((product, amount))
        return True

    def get_product(self, product_name):
        products_list = self.__fun_map[0](product_name)
        if len(products_list):
            return products_list[0]
        return None

    def get_products_by(self, opt, string):
        """
        :param opt: search option = 1-byName, 2- byKeyword, 3- byCategoru
        :param string: for opt: 1 -> productName, 2 -> string, 3 -> category
        :return: list of products according to the selected searching option
        """
        ls = self.__fun_map[opt-1](string)
        return ls

    def remove_product(self, product_name):
        """
        :param product_name: product to delete from inventory
        :return: True if the inventory updated without the product
        """
        for p in self.__inventory:
            if product_name == p[0].get_name():
                self.__inventory.remove(p)
                return True
        return False

    def change_amount(self, product_name, new_amount) -> bool:
        """
        :param product_name: product name to edit
        :param new_amount: number to replace with
        :return: True if the product updated with new amount on inventory
        """
        # product = self.get_product(product_name)
        # if product is not None:
        #     product.set_amount(new_amount)
        #     return True
        for i in self.__inventory:
            if i[0].get_name() == product_name:
                self.__inventory.remove(i)
                self.__inventory.append((i[0], new_amount))
                return True
        return False

    def len(self):
        """
        :return: amount of products on inventory
        """
        return len(self.__inventory)

    def get_amount_of_product(self, product_name):
        for i in self.__inventory:
            if i[0].get_name() == product_name:
                return i[1]
        return None

    def __repr__(self):
        return repr("There are " + str(len(self.__inventory)) + " products in inventory")