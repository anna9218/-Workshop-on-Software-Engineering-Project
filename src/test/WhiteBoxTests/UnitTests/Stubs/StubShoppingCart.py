from src.main.DomainLayer.UserComponent.ShoppingCart import ShoppingCart


class StubShoppingCart(ShoppingCart):
    def __init__(self):
        self.__shopping_baskets = []

    def add_products(self, products_stores_quantity_ls):
        self.__shopping_baskets.append([products_stores_quantity_ls[0][1],
                                        [products_stores_quantity_ls[0][0], products_stores_quantity_ls[0][2]]])
        return True

    def remove_product(self, product):
        return True

    def add_products(self, products_stores_quantity_ls: [{"product_name": str, "store_name": str,
                                                          "amount": int, "discount_type": DiscountType,
                                                          "purchase_type": PurchaseType}]) -> bool:

        return True
    def update_quantity(self, product, quantity):
        return True

    def update_quantity(self, product, quantity):
        return True
