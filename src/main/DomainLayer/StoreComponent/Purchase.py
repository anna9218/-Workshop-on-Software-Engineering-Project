from datetime import datetime as date_time

from src.Logger import logger


class Purchase(object):
    def __init__(self, products_list: [dict], total_price: float, store_name: str, username: str):
        # product_list -> [{"product_name": str, "product_price": float, "amount": int}]

        # self.__purchase_id: int = purchase_id
        self.__products = products_list
        self.__total_price:  float = total_price
        self.__store_name: str = store_name
        self.__username: str = username
        self.__curr_date: date_time = date_time.now()

    def __repr__(self):
        return repr("Purchase")

    @logger
    def get_total_price(self):
        return self.__total_price

    @logger
    def get_store_name(self):
        return self.__store_name

    @logger
    def get_nickname(self):
        return self.__username

    @logger
    def get_date(self):
        return self.__curr_date

    @logger
    def get_products(self):
        return self.__products
