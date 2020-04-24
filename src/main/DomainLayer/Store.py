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

    def add_products (self, names, prices, amounts, categories):
        for name in names:
            for price in prices:
                for amount in amounts:
                    for category in categories:
                        self.add_product (name, price, amount, category)

    def add_product (self, name, price, amount, category):
        p = Product (name, price, category)
        if self.__inventory.get_product(p.get_name()):
            print ("The product is already existed")
            return False
        self.__inventory.add_product(p, amount)
        return True

    def remove_products (self, products):
        for p in products:
            self.remove_product (p)

    def remove_product(self, p):
        # assume the product exists on inventory
        self.__inventory.remove_product(p)

    def change_price (self, product, new_price):
        if product in self.__inventory:
            product.set_price(new_price)

    def change_name (self, product, new_name):
        if product in self.__inventory:
            product.set_name(new_name)

    def change_amount (self, product, amount):
        if self.__inventory.get_product(product.get_name()):
            self.__inventory.add_to_amount(product, amount)


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
