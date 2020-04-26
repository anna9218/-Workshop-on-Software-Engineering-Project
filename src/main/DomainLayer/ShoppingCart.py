from src.Logger import logger
from src.main.DomainLayer.ShoppingBasket import ShoppingBasket


class ShoppingCart:
    def __init__(self):
        self.__shopping_baskets = []  # list of pairs (store, shopping basket) -> [ [store, shopping basket], ... ]

    @logger
    def remove_product(self, product):
        for store_basket in self.__shopping_baskets:  # __shopping_baskets contains pairs of (store, basket)
            for product_amount in store_basket[1]:  # each basket contains pairs of (products amount)
                if product.get_name == product_amount[0].get_name:  # compare
                    store_basket[1].remove_product(product)
                    if not store_basket[1]:  # if there are no other products in the basket
                        self.__shopping_baskets.remove(store_basket)
                    return True
        return False

    @logger
    def update_quantity(self, product, quantity):
        if self.is_product_in_cart(product):
            for store_basket in self.__shopping_baskets:
                for product_amount in store_basket[1]:
                    if product.get_name == product_amount[0].get_name:
                        product_amount[1] = quantity
                        return True
        return False

    @logger
    # Parameters: a list of products and their corresponding stores and quantities - [ [product, store, quantity], ... ]
    def add_products(self, products_stores_quantity_ls) -> bool:
        for product_store_quantity in products_stores_quantity_ls:
            if not self.__shopping_baskets:  # if cart is empty
                shopping_basket = ShoppingBasket()
                self.__shopping_baskets.append([product_store_quantity[1], shopping_basket])  # add [store, basket]
                shopping_basket.add_product([product_store_quantity[0], product_store_quantity[2]])
            else:
                for store_basket in self.__shopping_baskets:
                    if store_basket[0] == product_store_quantity[1]:  # basket already exists
                        store_basket[1].add_product([product_store_quantity[0], product_store_quantity[2]])
                    else:  # creating new basket to add
                        shopping_basket = ShoppingBasket()
                        self.__shopping_baskets.append([product_store_quantity[1], shopping_basket])  # add [store, basket]
                        shopping_basket.add_product([product_store_quantity[0], product_store_quantity[2]])
        return True

    def is_product_in_cart(self, product) -> bool:
        for store_basket in self.__shopping_baskets:
            if store_basket[1].is_in_basket(product):
                return True
        return False

    @logger
    def get_shopping_baskets(self):
        return self.__shopping_baskets

    # def is_basket_in_cart(self, store) -> bool:
    #     for store_basket in self.__shopping_baskets:
    #         if store_basket[0].get_name() == store.get_name():
    #             return True
    #     return False

    def __repr__(self):
        return repr("ShoppingCart")