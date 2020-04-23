class Product:
    def __init__(self, name, price):
        # self.__id = id
        self.__name = name
        self.__price = price
        # self._amount = amount
        # self.__rate = 0 TODO - for search 2.5
        # TODO - add category here or on Store? (for search - use case 2.5)
        # TODO - add more details? for each new detail need to open set_detail for use case 4.1 - owner can edit product's details

    def __eq__(self, p):
        if self.__name == p.get_name() and self.__price == p.get_price():
            return True
        else:
            return False

    def __repr__(self):
       # stri = "Product: " + self.__name + " - " + str(self.get_price) + "$"
        return self.__name

    def __hash__(self):
        return hash(repr(self))

    def get_price(self):
        return self.__price

    def get_name(self):
        return self.__name

    def set_price(self, new_price):
        self.__price = new_price

    def set_name(self, new_name):
        self.__name = new_name

    pass
