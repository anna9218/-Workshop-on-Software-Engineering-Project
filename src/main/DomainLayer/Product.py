# Creating a self._logger object with the relevant module name
import logging

# def logger():
#     logger = logging.getLogger(__name__)
#
#     # Setting the threshold of self._logger to DEBUG
#     logger.setLevel(logging.INFO)
#
#     formatter = logging.Formatter('%(asctime)s >> %(levelName)s: %(module)s %(funcName)s %(message)s')
#     file_handler = logging.FileHandler("WorkshopProject1.log")
#     file_handler.setFormatter(formatter)
#
#     # Creating a self._logger handler object
#     logger.addHandler(file_handler)

class Product:
    def __init__(self, name, price, category):
        # self.__id = id
        self.__name = name
        self.__price = price
        self.__category = category
        # self.__rate = 0 TODO - for search 2.5

    def __repr__(self):
        return repr("Product: " + self.__name)

    def get_price(self):
        return self.__price

    def get_name(self):
        return self.__name

    def get_category(self):
        return self.__category

    def set_price(self, new_price):
        self.__price = new_price

    # @logger
    def set_name(self, new_name):
        self.__name = new_name

    pass
