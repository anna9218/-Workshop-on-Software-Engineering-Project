from src.main.DomainLayer import Product


class StoreInventory:

    def __init__(self):
        self._amountPerProduct = {}

    def get_amount_of_product(self, p: Product):
        if self.check_if_exists(p):
            print(self._amountPerProduct.get (p))
            return self._amountPerProduct.get (p)
        else:
            print("There is no such product as " + p.get_name())
            return False

    def add_to_amount(self, product: Product, addToAmount):
        self._amountPerProduct[product] = self._amountPerProduct(product)+ addToAmount # TODO- check it overwrites the prev amount of product

    def add_product (self, product, amount):
        self._amountPerProduct[product] = amount # TODO- change the key to be the product name

    def check_if_exists (self, product: Product):
        # TODO- maybe check by product name? (is it possible to have 2 products with the same name and different prices?)- check if __eq__ is enough
        if not self.empty_inventory():
            if product in self._amountPerProduct:
                return True #TODO- maybe add check if amount>0?
        return False

    def empty_inventory (self):
        return len(self._amountPerProduct) == 0

    def PrintInventory(self):
        i = 0
        for name, p in self.__inventory:
            f"For {name} press {i}" #TODO- check if contains \n
            i += 1

    def RemoveFromList(self, p):
        del self._amountPerProduct[p]

    pass