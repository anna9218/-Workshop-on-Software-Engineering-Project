from src.Logger import logger
from src.main.DomainLayer.StoreComponent.Product import Product
from src.main.DomainLayer.UserComponent.DiscountType import DiscountType
from src.main.DomainLayer.UserComponent.PurchaseType import PurchaseType
from src.main.DomainLayer.TradeComponent.TradeControl import TradeControl


class ShoppingBasket:
    def __init__(self):
        self.__products: [{"product": Product, "amount": int, "discountType": DiscountType, "purchaseType": PurchaseType}] = []
        self.__i = 0

    # in order to make the object iterable
    def __iter__(self):
        self.__i = 0
        return self

    def __next__(self):
        while self.__i < len(self.__products):
            x = self.__products[self.__i]
            self.__i += 1
            return x
        else:
            raise StopIteration

    @logger
    def add_product(self, product: Product, amount: int, discount_type: DiscountType, purchase_type: PurchaseType) -> bool:
        for product_amount in self.__products:
            if product.get_name() == product_amount["product"].get_name():
                product_amount["amount"] += amount
                return True
        self.__products.append({"product": product, "amount": amount, "discountType": discount_type, "purchaseType": purchase_type})
        return True

    @logger
    def get_basket_info(self):
        """
        :return: list: [{"product_name": str
                         "amount": int}, ...]
        """
        return list(map(lambda x: {"product_name": x["product"].get_name(),
                                   "amount": x["amount"]}, self.__products))

    @logger
    # eden
    def remove_product(self, product_name: str) -> bool:
        for p in self.__products:
            if product_name == p["product"].get_name():
                self.__products.remove(p)
                return True
        return False

    @logger
    # eden
    def update_amount(self, product_name: str, amount: int):
        for p in self.__products:
            if p["product"].get_name() == product_name:
                p["amount"] = amount
                return True
        return False

    @logger
    # eden
    def is_empty(self):
        return self.__products == []

    # @logger
    # def get_product_by_name(self, product):
    #     for p in self.__products:
    #         if p.get_name() == product.get_name():
    #             return p
    #     return None
    #
    # @logger
    # def is_in_basket(self, product) -> bool:
    #     for p in self.__products:
    #         if p[0].get_name() == product.get_name():
    #             return True
    #     return False

    @logger
    def get_products(self):
        return self.__products

    @logger
    def get_product_amount(self, product_name: str):
        for p in self.__products:
            if p["product"].get_name() == product_name:
                return p["amount"]
        return 0

    @logger
    def make_purchase(self, store_name: str):
        """
        try to purchase all products in the shopping basket, provided the purchase policy and the discount
        policy allows for it
        :param store_name
        :return: json object representing purchase details
            {basket_price: float, dict: [{"product_name": product_name, "product_price": price, "amount": amount}]}
        """
        total_price = 0
        products_to_purchase = []
        store = TradeControl.get_instance().get_store(store_name)
        dictionary = {}
        for product in self.__products:
            if store.can_purchase(product["product"].get_name(), product["amount"]):
                if product["purchaseType"] == PurchaseType.DEFAULT:
                    dictionary = self.purchase_immediate(store_name, product["product"].get_name(),
                                                         product["product"].get_price(), product["amount"])

                elif product["purchaseType"] == PurchaseType.AUCTION:
                    dictionary = self.purchase_auction(store_name, product["product"].get_name(),
                                                         product["product"].get_price(), product["amount"])
                else:
                    dictionary = self.purchase_lottery(store_name, product["product"].get_name(),
                                                         product["product"].get_price(), product["amount"])

            if dictionary is not None and dictionary.keys().__contains__("product_price"):
                total_price += dictionary["product_price"]
                products_to_purchase.append(dictionary)
        return {"basket_price": total_price, "dict": products_to_purchase}

    # u.c 2.8.1
    @logger
    def purchase_immediate(self, store_name: str, product_name: str, product_price: int, amount: int):
        """
        :param store_name: store name
        :param product_name: product name
        :param product_price: product price
        :param amount: product amount
        :return: dictionary {"product_name": str, "product_price": float, "amount": int} or None
        """
        store = TradeControl.get_instance().get_store(store_name)
        if store.check_discount_policy(product_name):
            price = store.calculate_discount_price(product_name, product_price, amount)
            return {"product_name": product_name, "product_price": price, "amount": amount}
        return None

    # u.c 2.8.2 - mostly temp initialization since we don't have purchase policy functionality yet
    @logger
    def purchase_auction(self, store_name: str, product_name: str, product_price: int, amount: int):
        """
        :param store_name: store name
        :param product_name: product name
        :param product_price: product price
        :param amount: product amount
        :return: dictionary {"product_name": str, "product_price": float, "amount": int} or None
        """
        if not TradeControl.get_instance().check_end_time():
            if TradeControl.get_instance().did_win_auction():
                return self.purchase_immediate(store_name, product_name, product_price, amount)
        else:
            # here ask guest for bidding amount
            # if it's higher than previous bids -> add new bid for the auction
            # since we don't have auction yet, we return None for now
            return None

    # u.c 2.8.3 - mostly temp initialization since we don't have purchase policy functionality yet
    @logger
    def purchase_lottery(self, store_name: str, product_name: str, product_price: int, amount: int):
        """
        :param store_name: store name
        :param product_name: product name
        :param product_price: product price
        :param amount: product amount
        :return: dictionary {"product_name": str, "product_price": float, "amount": int} or None
        """
        if TradeControl.get_instance().check_end_time():
            if not TradeControl.get_instance().does_price_exceed(product_price):
                # buy tickets and return the amount bought with all other details
                # here we'll return to 2.8.1
                return self.purchase_immediate(store_name, product_name, product_price, amount)
        else:
            # here ask guest for bidding amount
            # if it's higher than previous bids -> add new bid for the auction
            # since we don't have auction yet, we return None for now
            return None

    def complete_purchase(self, product_ls):
        """
        update shopping basket after successful purchase
        :param product_ls:
        :return: Void
        """
        for product in product_ls:
            prod_name = product["product_name"]
            self.update_amount(prod_name, self.get_product_amount(prod_name) - product["amount"])
            if self.get_product_amount(prod_name) == 0:
                self.remove_product(prod_name)

    def __repr__(self):
        return repr("ShoppingBasket")
