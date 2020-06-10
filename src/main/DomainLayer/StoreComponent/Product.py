from src.Logger import logger


class Product:
    def __init__(self, name, price, category):
        if price < 0:
            raise ValueError("Price should be >=0")

        # self.__id = id
        self.__name = name
        self.__price = price
        self.__category = category
        # self.__rate = 0 TODO - for search 2.5

    def __repr__(self):
        return repr("Product")

    # @logger
    def get_price(self):
        return self.__price

    # @logger
    def get_name(self):
        return self.__name

    # @logger
    def get_category(self):
        return self.__category

    # @logger
    def set_price(self, new_price):
        self.__price = new_price

    @logger
    def set_name(self, new_name):
        self.__name = new_name

    @logger
    def __eq__(self, other):
        try:
            if self.__name == other.get_name() and self.__price == other.get_price() and \
                    self.__category == other.get_category():
                return True
            return False
        except Exception:
            return False
