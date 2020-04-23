from src.main.DomainLayer.Product import Product
from src.main.DomainLayer.StoreInventory import StoreInventory


class Store:
    def __init__(self, name, owner):
        # self.__id = id
        self.__name = name
        self.__owner = owner
        self.__managers = ()
        self.__inventory = StoreInventory()
        # self.__rate = 0 TODO - for search 2.5

    def AddProducts (self, names, prices, amounts):
        for name in names:
            for price in prices:
                for amount in amounts:
                    self.AddProduct (name, price, amount)

    def AddProduct (self, name, price, amount):
        p = Product (name, price)
        if not self.__inventory.empty_inventory():
            if self.__inventory.check_if_exists(p):
                print ("The product is already existed")
                return False
        self.__inventory.add_product(p, amount)
        return True

    def RemoveProducts (self, products):
        for p in products:
            self.RemoveProduct (p)

    def RemoveProduct(self, p):
        # TODO- check something?
        del self.__inventory[p.get_name()]

    def ChangePrice (self, product, new_price):
        if product in self.__inventory:
            product.set_price (new_price)

    def get_inventory(self): #for test
        return self.__inventory

    def get_name (self):
        return self.__name


    pass


