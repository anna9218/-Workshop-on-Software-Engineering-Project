from src.main.DomainLayer.ShoppingBasket import ShoppingBasket


class ShoppingCart:
    def __init__(self):
        self.__shopping_baskets = []  # should be a pair of (store, shopping basket)

    # Parameters: a list of products and their corresponding stores - (product, store)
    def add_products(self, products_stores_ls):
        for product_store in products_stores_ls[1]:
            for store_basket in self.__shopping_baskets:
                if store_basket[0] == product_store[1]:  # basket already exists
                    store_basket[1].add_product(product_store[0])
                else:  # creating new basket to add
                    shopping_basket = ShoppingBasket()
                    self.__shopping_baskets.append(product_store[1], shopping_basket)
                    shopping_basket.add_product(product_store[0])
        return True

    def remove_products(self, products_ls):
        pass
