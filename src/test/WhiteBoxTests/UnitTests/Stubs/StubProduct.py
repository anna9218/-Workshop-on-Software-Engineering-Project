from src.main.DomainLayer.Product import Product


class StubProduct(Product):
    def __init__(self):
        self.__name = "Alcogel"
        self.__price = 100
        # self.__category = category
