from src.main.DomainLayer.ShoppingBasket import ShoppingBasket


class ShoppingCart:
    def __init__(self):
        self.__shopping_baskets = []  # list of pairs (store, shopping basket) -> [ [store, shopping basket], ... ]

    def remove_product(self, product):
        for store_basket in self.__shopping_baskets:  # __shopping_baskets contains pairs of (store, basket)
            for product_amount in store_basket[1]:  # each basket contains pairs of (products amount)
                if product.get_name == product_amount[0].get_name:  # compare
                    store_basket[1].remove(product_amount)
                    if len(store_basket[1]) == 0:  # if there are no other products in the basket
                        self.__shopping_baskets.remove(store_basket)
                    return True
        return False

    def update_quantity(self, product, quantity):
        for store_basket in self.__shopping_baskets:
            for product_amount in store_basket[1]:
                if product.get_name == product_amount[0].get_name:
                    product_amount[1] = quantity
                    return True
        return False

    # Parameters: a list of products and their corresponding stores and quantities - [ [product, store, quantity], ... ]
    def add_products(self, products_stores_quantity_ls):
        for product_store_quantity in products_stores_quantity_ls[1]:
            for store_basket in self.__shopping_baskets:
                if store_basket[0] == product_store_quantity[1]:  # basket already exists
                    store_basket[1].add_product([product_store_quantity[0], product_store_quantity[2]])
                else:  # creating new basket to add
                    shopping_basket = ShoppingBasket()
                    self.__shopping_baskets.append([product_store_quantity[1], shopping_basket])  # add [store, basket]
                    shopping_basket.add_product([product_store_quantity[0], product_store_quantity[2]])
        return True
