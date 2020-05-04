import jsonpickle

from src.Logger import logger
from src.main.DomainLayer.StoreComponent.Purchase import Purchase
from src.main.DomainLayer.TradeComponent.TradeControl import TradeControl
from src.main.DomainLayer.UserComponent.DiscountType import DiscountType
from src.main.DomainLayer.UserComponent.PurchaseType import PurchaseType
from src.main.DomainLayer.UserComponent.ShoppingBasket import ShoppingBasket
from src.main.DomainLayer.UserComponent.User import User


class ShoppingCart:
    def __init__(self):
        self.__shopping_baskets: [{"store_name": str, "basket": ShoppingBasket}] = []

    @logger
    def remove_products(self, products_details: [{"product_name": str, "store_name": str}]):
        """
        :param products_details: [{"product_name": str,
                                       "store_name": str}, ...]
        :return: True on success, False when one of the products doesn't exist in the shopping cart
        """
        for curr in products_details:
            basket = self.get_store_basket(curr["store_name"])
            if basket:
                basket.remove_product(curr["product_name"])
                if basket.is_empty():
                    self.remove_store_basket(curr["store_name"])
            else:
                return False
        return True

    @logger
    def update_quantity(self, products_details: [{"product_name": str, "store_name": str, "amount": int}]):
        for curr in products_details:
            basket = self.get_store_basket(curr["store_name"])
            if basket:
                return basket.update_amount(curr["product_name"], curr["amount"])
            else:
                return False
        return True

    @logger
    def remove_store_basket(self, store_name: str):
        for s in self.__shopping_baskets:
            if s["store_name"] == store_name:
                self.__shopping_baskets.remove(s)
                return True
        return False

    @logger
    def add_products(self, products_stores_quantity_ls: [{"product_name": str, "store_name": str,
                                                          "amount": int, "discount_type": DiscountType,
                                                          "purchase_type": PurchaseType}]) -> bool:
        for curr in products_stores_quantity_ls:
            basket = self.get_store_basket(curr["store_name"])
            if basket:
                basket.add_product(curr["product"], curr["amount"], curr["discount_type"], curr["purchase_type"])
            else:
                basket = ShoppingBasket()
                basket.add_product(curr["product"], curr["amount"], curr["discount_type"], curr["purchase_type"])
                self.__shopping_baskets.append({"store_name": curr["store_name"], "basket": basket})
        return True

    @logger
    def get_store_basket(self, store_name: str) -> ShoppingBasket:
        for store_basket in self.__shopping_baskets:
            if store_basket["store_name"] == store_name:
                return store_basket["basket"]
        return None

    @logger
    def view_shopping_cart(self):
        """
        :return: list: [{"store_name": str,
                         "basket": [{"product_name": str
                                     "amount": int}, ...]
                        }, ...]
        """
        return list(map(lambda x: {"store_name": x["store_name"],
                                   "basket": x["basket"].get_basket_info()}, self.__shopping_baskets))

    # def is_product_in_cart(self, product) -> bool:
    #     for store_basket in self.__shopping_baskets:
    #         if store_basket[1].is_in_basket(product):
    #             return True
    #     return False

    @logger
    def get_shopping_baskets(self):
        return self.__shopping_baskets

    @logger
    def make_purchase(self):
        """
        :return: list of purchases according to baskets in the subscribers shopping cart
                    [{total_price, store_name, [{product_name, price, amount}]}]
        """
        purchase_details = []
        total_price = 0
        user = TradeControl.get_instance().get_curr_user()
        for basket in self.__shopping_baskets:
            res_i = basket["basket"].make_purchase(basket["store_name"])
            if res_i is not None:
                p = Purchase(res_i["dict"], res_i["basket_price"], basket["store_name"], user.get_nickname())
                user.add_unaccepted_purchase(jsonpickle.encode(p))
                purchase_details.append(p)
                total_price += res_i["basket_price"]
        return {"total_price": total_price, "baskets": jsonpickle.encode(purchase_details)}

    @logger
    def complete_purchase(self, purchase_ls: {"total_price": float, "baskets": [dict]}):
        for basket in purchase_ls["baskets"]:
            # remove products from basket (or update amount if needed)
            self.get_store_basket(basket["store_name"]).complete_purchase(basket["products_list"])

    def __repr__(self):
        return repr("ShoppingCart")
