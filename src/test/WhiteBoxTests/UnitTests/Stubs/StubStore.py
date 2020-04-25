from src.main.DomainLayer.Store import Store
from src.main.DomainLayer.StoreInventory import StoreInventory
from src.main.DomainLayer.User import User


class StubStore(Store):

    def __init__(self):
        super().__init__("Eytan's best store")
#         self.__name = "Alcogel for all!"
#         self.__owners = []
#         self.__managers = []
#         self.__inventory = []

