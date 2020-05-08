from datetime import datetime
from src.Logger import logger


class LotteryPurchase:

    def __init__(self, product_price: float, end_date: datetime):
        self.__product_price = product_price
        self.__end_date: datetime = end_date
        self.__buyers = [] # [{user_name, buy_in_amount}]
        self.__total_price = 0 # total buy in price

    # @logger
    def purchase_tickets(self, nickname: str, buy_in_amount: float, curr_date: datetime):
        """
        purchase odds for lottery if end_date wasn't reached and total buy in amount doesn't reach
            the price of the product
        :param curr_date: current date
        :param nickname: user nickname
        :param buy_in_amount: given buy in price for the lottery
        :return: true if the purchase was accepted, otherwise false
        """
        if curr_date.date() > self.__end_date.date() or \
                (self.__total_price + buy_in_amount) >= self.__product_price:
            return False

        if self.get_buy(nickname) is not None:
            self.get_buy(nickname)["amount"] += buy_in_amount
        else:
            self.__buyers.append({"nickname": nickname, "amount": buy_in_amount})

        self.__total_price += buy_in_amount
        return True

    # @logger
    def get_product_price(self):
        return self.__product_price

    # @logger
    def get_end_date(self):
        return self.__end_date

    # @logger
    def get_total_price(self):
        return self.__total_price

    # @logger
    def get_buyers(self):
        return self.__buyers

    # @logger
    def get_buy(self, nickname: str):
        for buy in self.__buyers:
            if buy["nickname"] == nickname:
                return buy
        return None

    # @logger
    def has_buyers(self):
        return len(self.__buyers) != 0

