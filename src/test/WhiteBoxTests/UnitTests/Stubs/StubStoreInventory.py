from src.main.DomainLayer.Product import Product
from src.main.DomainLayer.StoreInventory import StoreInventory


class StubStoreInventory(StoreInventory):

    def __init__(self):
        super().__init__()
        self.__inventory = [(Product("Chair", 100, "Furniture"), 5),
                            (Product("Sofa", 100, "Furniture"), 5),
                            (Product("Guitar", 100, "Musical Instruments"), 5)]

    def get_inventory(self):
        return self.__inventory


