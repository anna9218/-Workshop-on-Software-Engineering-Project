from src.main.DomainLayer.ShoppingBasket import ShoppingBasket


class ShoppingCart:
    def __init__(self):
        self.__shopping_baskets = []  # should be a pair of (store, shopping basket)

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
