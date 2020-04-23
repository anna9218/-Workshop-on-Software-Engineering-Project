from src.main.DomainLayer.ShoppingBasket import ShoppingBasket


class ShoppingCart:
    def __init__(self):
        self.__shopping_baskets = []  # should be a pair of (store, shopping basket)

    # Parameters: a list of products and their corresponding stores and quantities - (product, store, quantity)
    def add_products(self, products_stores_quantity_ls):
        for product_store_quantity in products_stores_quantity_ls[1]:
            for store_basket in self.__shopping_baskets:
                if store_basket[0] == product_store_quantity[1]:  # basket already exists
                    store_basket[1].add_product([product_store_quantity[0], product_store_quantity[2]])
                else:  # creating new basket to add
                    shopping_basket = ShoppingBasket()
                    self.__shopping_baskets.append(product_store_quantity[1], shopping_basket)  # add (store, basket)
                    shopping_basket.add_product([product_store_quantity[0], product_store_quantity[2]])
        return True

