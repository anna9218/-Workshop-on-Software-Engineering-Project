from src.main.DomainLayer.Product import Product


class Store:
    def __init__(self, name, owner):
        # self.__id = id
        self.__name = name
        self.__owner = owner
        self.__managers = ()
        self.__inventory = {} # TODO - should it be an external class?
        # self.__rate = 0 TODO - for search 2.5

    #TODO - add check for manager? - maybe in ManagerPermission? (can be also for managers)
    def AddProducts (self, names_and_prices):
        for name, price in names_and_prices.items():
            self.AddProduct (name, price)

    def AddProduct (self, name, price):
        # TODO - add check if it was on inventory?
        self.__inventory[name] = Product (name, price)

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

    def empty_inventory (self):
        return len(self.__inventory) == 0

    def PrintInventory(self):
        f"The products of store {self.__name}:"
        i = 0
        for name, p in self.__inventory:
            f"For {name} press {i}" #TODO- check if contains \n

    pass


