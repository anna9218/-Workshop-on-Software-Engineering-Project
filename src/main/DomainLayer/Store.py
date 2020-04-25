from src.main.DomainLayer.Product import Product
from src.main.DomainLayer.StoreInventory import StoreInventory


class Store:
    def __init__(self, store_name):
        # self.__id = id
        self.__name = store_name
        self.__owners = []
        self.__managers = []
        self.__inventory = StoreInventory()
        # self.__rate = 0 TODO - for search 2.5
        self.__purchases = []

    def add_products(self, names, prices, amounts, categories) -> bool:
        """
        :param names: list of names of the new products
        :param prices: list of prices of the new products
        :param amounts: list of amounts of the new products
        :param categories: list of categories of the new products
        :return: true if all products was added to the inventory
        """
        for name in names:
            for price in prices:
                for amount in amounts:
                    for category in categories:
                        if not self.add_product (name, price, amount, category):
                            return False
        return True

    def add_product(self, name, price, amount, category) -> bool:
        """
        :param name: name of the new product
        :param price: price of the new product
        :param amount: amount of the new product
        :param category: category of the new product
        :return: True if succeed update the inventory with the new product
        """
        p = Product(name, price, category)
        if self.__inventory.get_product(p.get_name()):
            print ("The product is already existed")
            return False
            #TODO: here we should increase the amount in the inventory
        return self.__inventory.add_product(p, amount)

    def remove_products(self, products):
        """
        :param products: products to delete from inventory (assume they exists on inventory)
        :return: True if the inventory updated without the product
        """
        for p in products:
            if not self.remove_product(p):
                return False
        return True

    def remove_product(self, p: Product) -> bool:
        """
        :param p: product to delete from inventory
        :return: True if the inventory updated without the product
        """
        # assume the product exists on inventory
        return self.__inventory.remove_product(p)

    def change_price (self, product, new_price) -> bool:
        """
       :param product: product
       :param new_price: number to replace with
       :return: True if the product's price updated on inventory
       """
        if self.__inventory.get_product(product.get_name()) is not None:
            product.set_price(new_price)
            return True
        return False

    def change_name (self, product, new_name) -> bool:
        """
        :param product: product
        :param new_name: name to replace with
        :return: True if the product's name updated on inventory
        """
        if self.__inventory.get_product(product.get_name()) is not None:
            product.set_name(new_name)
            return True
        return False

    def change_amount (self, product, amount) -> bool:
        """
       :param product: product
       :param amount: number to replace with
       :return: True if the product's amount updated on inventory
       """
        if self.__inventory.get_product(product.get_name()) is not None and amount>0:
            return self.__inventory.change_amount(product, amount)
        return False

    def add_owner(self, owner):
        for o in self.__owners:
            if o.get_name() == owner.get_name:
                return False
        self.__owners.append(owner)
        return False

    def get_inventory(self): #for test
        return self.__inventory

    def get_name(self):
        return self.__name

    def get_owners(self):
        return self.__owners

    def get_managers(self):
        return self.__managers

    # eden added
    def get_products_by(self, opt, string):
        return self.__inventory.get_products_by(opt, string)

    # eden added
    def get_product(self, product_name):
        return self.__inventory.get_product(product_name)

    def empty_inventory(self):
        return self.__inventory.len() == 0

    def print_inventory(self):
        f"The products of store {self.__name}:"
        i = 0
        for name, p in self.__inventory:
            f"For {name} press {i}" #TODO- check if contains \n

    def get_info(self):
        if not self.__managers:  # empty list
            return "Store owners: %s" % (str(self.__owners.strip('[]')))
        else:
            if len(self.__managers) > 0:  # one manager exists
                return "Store owners: %s \n managers: $s" % (str(self.__owners.strip('[]')), self.__managers.strip('[]'))

    def get_purchases(self):
        return self.__purchases

    def get_purchase_info(self, purchase):
        for p in self.__purchases:
            if p == purchase:  # TODO - how do we compare purchases?
                return p

    def add_manager(self, manager):
        for o in self.__owners:
            if o.get_nickname() == manager.get_nickname():
                return False
        for m in self.__managers:
            if m.get_nickname() == manager.get_nickname():
                return False
        self.__managers.append(manager)
        return True