from src.Logger import logger
from src.main.DomainLayer.StoreComponent.Product import Product
from src.main.DomainLayer.UserComponent.DiscountType import DiscountType
from src.main.DomainLayer.UserComponent.PurchaseType import PurchaseType
from src.main.DomainLayer.UserComponent.ShoppingBasket import ShoppingBasket


class ShoppingCart:
    def __init__(self):
        self.__shopping_baskets: [{"store_name": str, "basket": ShoppingBasket}] = []

    @logger
    def remove_products(self, products_details: [{"product_name": str, "store_name": str}]) -> {'response': bool, 'msg': str}:
        """
        :param products_details: [{"product_name": str,
                                       "store_name": str}, ...]
        :return: dict = {'response': bool, 'msg': str}
                 True on success, False when one of the products doesn't exist in the shopping cart
        """
        for curr in products_details:
            basket = self.get_store_basket(curr["store_name"])
            if basket:
                if not basket.remove_product(curr["product_name"]):
                    return {'response': False, 'msg': "Error! product " + curr["product_name"] +
                                                      " doesn't exist in the basket of store " + curr["store_name"]}
                if basket.is_empty():
                    self.remove_store_basket(curr["store_name"])
            else:
                return {'response': False, 'msg': "Error! basket of store " + curr["store_name"] +
                                                  " doesn't exist in your shopping cart"}
        return {'response': True, 'msg': "Products were removed from your shopping cart successfully"}

    @logger
    def update_quantity(self, products_details: [{"product_name": str, "store_name": str, "amount": int}]) -> \
            {'response': bool, 'msg': str}:
        """
        The function take a list of {"product_name": str, "store_name": str, "amount": int}.
        The function checks if the basket in the store exist, if the product exist in the basket and the amount isn't
                                                                                                               negative.
        If any one of the above is false, the function returns false and DOES NOT CHANGE ANY AMOUNT.
        Else, update the amount and return true.

        :param products_details: list of {"product_name": str, "store_name": str, "amount": int}
        :return: dict = {'response': bool, 'msg': str}
                 If any one of the above is false, the function returns false.
                 else, return true.
        """
        for curr in products_details:
            basket = self.get_store_basket(curr["store_name"])
            if not basket:
                return {'response': False, 'msg': "Error! basket of store " + curr["store_name"] +
                                                  " doesn't exist in your shopping cart"}
            if basket.get_product(curr['product_name']) is None:
                return {'response': False, 'msg': "Error! product " + curr["product_name"] +
                                                  " doesn't exist in the basket of store " + curr["store_name"]}
            if curr['amount'] < 0:
                return {'response': False, 'msg': "Error! Amount of product " + curr["product_name"] +
                                                  " must be greater than 0"}

        for curr in products_details:
            basket = self.get_store_basket(curr["store_name"])
            basket.update_amount(curr["product_name"], curr["amount"])
        return {'response': True, 'msg': "Shopping cart was updated successfully."}

    @logger
    def remove_store_basket(self, store_name: str):
        for s in self.__shopping_baskets:
            if s["store_name"] == store_name:
                self.__shopping_baskets.remove(s)
                return True
        return False

    @logger
    def add_products(self, products_stores_quantity_ls: [{"store_name": str,
                                                          "product": Product,
                                                          "amount": int}]) -> {'response': bool, 'msg': str}:
        """
        The function iterate over the list to see if all the arguments are valid.
        If all the arguments are valid, and the basket exist, the function add the products the corresponding basket.
        If all the arguments are valid, and the basket doesn't exist, the function create the basket and then
                                                                        add the products the corresponding basket.
        If not all the arguments are valid, the function do nothing and return false.

        :param products_stores_quantity_ls: list of products to add.
        :return:
                If all the arguments are valid, and the basket exist, the function add the products the corresponding
                                                                                                                basket.
                If all the arguments are valid, and the basket doesn't exist, the function create the basket and then
                                                                        add the products the corresponding basket.
                If not all the arguments are valid, the function do nothing and return false.
        """

        # Check if the arguments are valid.
        for curr in products_stores_quantity_ls:
            if curr is None:
                return {'response': False, 'msg': "Error! invalid input"}
            else:
                if curr['product'] is None:
                    return {'response': False, 'msg': "Error! invalid input"}
                if curr['amount'] <= 0:
                    return {'response': False, 'msg': "Error! the amount of product " + curr['product'].get_name() +
                                                      "is >= 0. A product amount must be bigger than 0"}

        # Rest of the function
        for curr in products_stores_quantity_ls:
            basket = self.get_store_basket(curr["store_name"])
            if basket:
                basket.add_product(curr["product"], curr["amount"])
            else:
                basket = ShoppingBasket()
                basket.add_product(curr["product"], curr["amount"])
                self.__shopping_baskets.append({"store_name": curr["store_name"], "basket": basket})

        return {'response': True, 'msg': "Products were added to shopping cart successfully"}

    @logger
    def get_store_basket(self, store_name: str) -> ShoppingBasket:
        for store_basket in self.__shopping_baskets:
            if store_basket["store_name"] == store_name:
                return store_basket["basket"]
        return None

    @logger
    def view_shopping_cart(self) -> {'response': list, 'msg': str}:
        """
        :return: dict: {'response': [{"store_name": str,
                                     "basket": [{"product_name": str
                                                 "amount": int}, ...]
                                    }, ...],
                        'msg': str}
        """
        ls = list(map(lambda x: {"store_name": x["store_name"],
                                   "basket": x["basket"].get_basket_info()}, self.__shopping_baskets))
        if len(ls) == 0:
            return {'response': [], 'msg': "Shopping cart is empty"}
        return {'response': ls, 'msg': "Shopping cart was retrieved successfully"}

    # def is_product_in_cart(self, product) -> bool:
    #     for store_basket in self.__shopping_baskets:
    #         if store_basket[1].is_in_basket(product):
    #             return True
    #     return False

    @logger
    def get_shopping_baskets(self):
        return self.__shopping_baskets

    def __repr__(self):
        return repr("ShoppingCart")
