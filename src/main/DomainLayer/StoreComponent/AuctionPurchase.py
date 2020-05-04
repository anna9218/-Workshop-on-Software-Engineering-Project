from datetime import datetime
from src.Logger import logger


class AuctionPurchase:

    def __init__(self, initial_price: float, end_date: datetime):
        self.__initial_price = initial_price
        self.__end_date: datetime = end_date
        self.__biddings = [] # [{user_name, bidding_price}]
        self.__max_bid = 0

    @logger
    def add_bid(self, nickname: str, bidding_price: float, curr_date: datetime):
        """
        add bid only if it's higher than all other bids and end_date wasn't reached
        :param curr_date: current date
        :param nickname: user nickname
        :param bidding_price: given bidding price for the auction
        :return: true if the bid was accepted, otherwise false
        """
        if curr_date.date() > self.__end_date.date() or bidding_price <= self.__max_bid:
            return False

        if self.get_bid(nickname) is not None:
            self.get_bid(nickname)["bidding_price"] += bidding_price
        else:
            self.__biddings.append({"nickname": nickname, "bidding_price": bidding_price})

        if self.get_bid(nickname)["bidding_price"] > self.__max_bid:
            self.__max_bid = bidding_price
        return True

    @logger
    def get_initial_price(self):
        return self.__initial_price

    @logger
    def get_end_date(self):
        return self.__end_date

    @logger
    def get_max_bid(self):
        return self.__max_bid

    @logger
    def get_biddings(self):
        return self.__biddings

    @logger
    def get_bid(self, nickname: str):
        for bid in self.__biddings:
            if bid["nickname"] == nickname:
                return bid
        return None

    @logger
    def has_biddings(self):
        return len(self.__biddings) != 0

