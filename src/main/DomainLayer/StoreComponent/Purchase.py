from datetime import datetime as date_time

from src.Logger import logger


class Purchase:
    def __init__(self, purchase_id: int, amount_per_product: [], price: float, store_name: str, username: str = ""):
        self.__purchase_id: int = purchase_id
        self.__amount_per_product: [] = amount_per_product
        self.__price:  float = price
        self.__store_name: str = store_name
        self.__username: str = username
        self.__date: date_time = date_time.now()

    def __repr__(self):
        return repr("Purchase")

    @logger
    def get_price(self) -> float:
        return self.__price

    @logger
    def get_username(self) -> str:
        return self.__username

    @logger
    def get_store_name(self) -> str:
        return self.__store_name

    @logger
    def get_purchase_id(self) -> int:
        return self.__purchase_id


