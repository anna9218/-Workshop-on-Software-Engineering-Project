from Backend.src.Logger import logger
from Backend.src.main.DomainLayer.StoreComponent import Product


class StoreInventory:

    def __init__(self):
        # list of the pairs (product, amount)
        self.__inventory: [{"product": Product, "amount": int}] = []
        # list of search functions: __fun_map[0] = searchProductsByName(product_name)
        #                           __fun_map[1] = searchProductByKeyword(keyword)
        #                           __fun_map[2] = searchProductByCategory(category)
        #  all the functions returns list of products
        self.__fun_map = [lambda product_name: list(filter(lambda p: p.get_name() == product_name, [x["product"] for x in self.__inventory])),
                          lambda keyword: list(filter(lambda p: keyword in p.get_name(), [x["product"] for x in self.__inventory])),
                          lambda category: list(filter(lambda p: category == p.get_category(), [x["product"] for x in self.__inventory]))]

    def __iter__(self):
        self.__i = 0
        return self

    def __next__(self):
        while self.__i < len(self.__inventory):
            x = self.__inventory[self.__i]
            self.__i += 1
            return x
        else:
            raise StopIteration

    # @logger
    def add_product(self, product: Product, amount: int) -> bool:
        """
        :param product: Product
        :param amount: amount of product
        :return: true,and the inventory updated with the new product or the products amount is increased
        """
        if amount < 0:
            return False

        products_ls = self.__fun_map[0](product.get_name())
        if len(products_ls):
            old_product_amount = self.get_amount(product.get_name())
            self.remove_product(product.get_name())
            self.__inventory.append({"product": product, "amount": amount + old_product_amount})
        else:
            self.__inventory.append({"product": product, "amount": amount})
        return True

    # @logger
    def get_product(self, product_name):
        products_list = self.__fun_map[0](product_name)
        if len(products_list):
            return products_list[0]
        return None

    # @logger
    def get_products_by(self, opt, string):
        """
        :param opt: search option = 1-byName, 2- byKeyword, 3- byCategory
        :param string: for opt: 1 -> productName, 2 -> string, 3 -> category
        :return: list of products according to the selected searching option
        """
        ls = self.__fun_map[opt-1](string)
        return ls

    # @logger
    def remove_product(self, product_name):
        """
        :param product_name: product to delete from inventory
        :return: True if the inventory updated without the product
        """
        for p in self.__inventory:
            if product_name == p["product"].get_name():
                self.__inventory.remove(p)
                return True
        return False

    # @logger
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
        if new_amount < 0:
            return False

        for i in self.__inventory:
            if i["product"].get_name() == product_name:
                i["amount"] = new_amount
                return True
        return False

    # @logger
    def len(self):
        """
        :return: amount of products on inventory
        """
        return len(self.__inventory)

    # @logger
    def get_amount(self, product_name: str) -> int:
        for i in self.__inventory:
            if i["product"].get_name() == product_name:
                return i["amount"]
        return 0

    # @logger
    def is_in_stock(self, product_name, requested_amount):
        """
        This function check if the product exist in the store inventory.
        If it does exist, check if the quantity of the product in the stock inventory is enough for making the purchase.

        :param product_name: the name of the product to search in inventory.
        :param requested_amount: the requested amount.
        :return: if is in stock true,
                 else false.
        """
        if requested_amount < 0:
            return False

        amount_in_stock = self.get_amount(product_name)
        if amount_in_stock:
            if int(amount_in_stock) >= requested_amount:
                return True
        return False

    # @logger
    def get_inventory(self):
        return self.__inventory

    # @logger
    def set_inventory(self, new_inventory):
        self.__inventory = new_inventory

    # @logger
    def is_empty(self):
        return len(self.__inventory) == 0

    def __repr__(self):
        return repr("StoreInventory")

    def __eq__(self, other):
        if type(other) is not StoreInventory:
            return False

        my_products_as_tuples = [(element['product'], element['amount']) for element in self.__inventory]
        other_products_as_tuples = [(element['product'], element['amount']) for element in other.get_inventory()]

        if len(my_products_as_tuples) != len(other_products_as_tuples):
            return False
        for product_as_tuple in other_products_as_tuples:
            if product_as_tuple not in my_products_as_tuples:
                return False

        return True
