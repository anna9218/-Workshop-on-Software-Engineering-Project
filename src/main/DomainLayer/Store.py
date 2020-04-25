
from src.main.DomainLayer import Purchase
from src.main.DomainLayer.Product import Product
from src.main.DomainLayer.StoreInventory import StoreInventory
from src.main.DomainLayer.User import User


class Store:
    def __init__(self, store_name):
        # self.__id = id
        self.__name = store_name
        self.__owners = []
        # list of pairs (manager: User, permissions: ManagerPermissions[], appointer:User)
        self.__managers_permissions_and_appointer = []
        self.__inventory = StoreInventory()
        # self.__rate = 0 TODO - for search 2.5
        self.__purchases = []

    def add_products(self, products_details) -> bool:
        """
        :param products_details: list of tuples (product_name, product_price, product_amount, product_category)
        :return: true if all products was added to the inventory
        """
        results = list(map(lambda details: self.add_product(details[0], details[1], details[2], details[3]), products_details))
        return False not in results

    def add_product(self, name, price, category, amount) -> bool:
        """
        :param name: name of the new product
        :param price: price of the new product
        :param amount: amount of the new product
        :param category: category of the new product
        :return: True if succeed update the inventory with the new product
        """
        return self.__inventory.add_product(Product(name, price, category), amount)

    def remove_products(self, products_names):
        """
        :param products_names: products to delete from inventory (assume they exists on inventory)
        :return: True if the inventory updated without the product
        """
        results = list(map(lambda p_name: self.remove_product(p_name), products_names))
        return False not in results

    def remove_product(self, product_name) -> bool:
        """
        :param product_name: product's name to delete from inventory
        :return: True if the inventory updated without the product
        """
        # assume the product exists on inventory
        return self.__inventory.remove_product(product_name)

    def change_price(self, product_name, new_price) -> bool:
        """
       :param product_name: product
       :param new_price: number to replace with
       :return: True if the product's price updated on inventory
       """
        product = self.get_product(product_name)
        if product is not None:
            product.set_price(new_price)
            return True
        return False

    def change_name(self, product_name, new_name) -> bool:
        """
        :param product_name: product
        :param new_name: name to replace with
        :return: True if the product's name updated on inventory
        """
        product = self.get_product(product_name)
        if product is not None:
            product.set_name(new_name)
            return True
        return False

    def change_amount(self, product_name, amount: int) -> bool:
        """
       :param product_name: product
       :param amount: number to replace with
       :return: True if the product's amount updated on inventory
       """
        product = self.get_product(product_name)
        if product is not None and amount > 0:
            return self.__inventory.change_amount(product_name, amount)
        return False

    def add_owner(self, owner: User):
        for o in self.__owners:
            if o.get_name() == owner.get_name:
                return False
        self.__owners.append(owner)
        return True

    def is_owner(self, user_nickname):
        return user_nickname in [owner.get_nickname() for owner in self.__owners]

    def is_manager(self, user_nickname):
        return user_nickname in [tuple[0].get_nickname() for tuple in self.__managers_permissions_and_appointer]

    # eden added
    def get_products_by(self, opt, string):
        return self.__inventory.get_products_by(opt, string)

    # eden added
    def get_product(self, product_name):
        return self.__inventory.get_product(product_name)

    def get_purchase_info(self, purchase: Purchase):
        for p in self.__purchases:
            if p == purchase:  # TODO - how do we compare purchases?
                return p

    def print_inventory(self):
        f"The products of store {self.__name}:"
        i = 0
        for name, p in self.__inventory:
            f"For {name} press {i}" #TODO- check if contains \n

    def add_manager(self, future_manager: User, permissions, appointer: User):
        """
        :param future_manager: subscriber to appoint as manager
        :param permissions: type - ManagerPermission[]
        :param appointer: store's owner that appoints the subscriber as manager
        :return:
        """
        self.__managers_permissions_and_appointer.append((future_manager, permissions, appointer))
        return True

    def get_permissions(self, manager_nickname):
        for tuple in self.__managers_permissions_and_appointer:
            if tuple[0].get_nickname() == manager_nickname:
                return tuple[1]
        return None

    def get_info(self):
        if not self.__managers_permissions_and_appointer:  # empty list
            return "Store owners: %s" % (str(self.__owners.strip('[]')))
        else:
            if len(self.__managers_permissions_and_appointer) > 0:  # one manager exists
                return "Store owners: %s \n managers: $s" % (str(self.__owners.strip('[]')), self.__managers_permissions_and_appointer.strip('[]'))

    def is_in_store_inventory(self, amount_per_product):
        for product_and_amount in amount_per_product:
            if not self.get_inventory().is_in_stock(product_and_amount['product'], product_and_amount['amount']):
                return False
        return True

    def check_purchase_policy(self, amount_per_product: [], username: str):
        """
        This function should check if the user can/can't complete the purchase.
        Due to the fact that we does'nt have the purchase policies requirements, this func is currently a stab.

        :param amount_per_product: param to check policy.
        :param price: param to check policy.
        :param username: param to check policy.
        :return: the price if possible.
                 -1 else.
        """
        return (self.get_inventory().get_product(amount_per_product[0])).get_price()

    @staticmethod
    def calc_discount(amount_per_product: [], price: float, username: str):
        """
        This function should check if the user can/can't complete the purchase.
        Due to the fact that we does'nt have the purchase policies requirements, this func is currently a stab.

        :param amount_per_product: param to check policy.
        :param price: param to check policy.
        :param username: param to check policy.
        :return: the price after discount. if no discount is available, return the price.
        """
        return price

    def empty_inventory(self):
        return self.__inventory.len() == 0

    def get_inventory(self):
        return self.__inventory

    def get_name(self):
        return self.__name

    def get_owners(self):
        return self.__owners

    def get_managers(self):
        return [t[0] for t in self.__managers_permissions_and_appointer]

    def edit_manager_permissions(self, manager: User, permissions, appointer: User):
        for t in self.__managers_permissions_and_appointer:
            if t[0].get_nickname() == manager.get_nickname() and t[2].get_nickname() == appointer.get_nickname():
                self.__managers_permissions_and_appointer.remove(t)
                self.__managers_permissions_and_appointer.append((manager, permissions,appointer))
                return True
        return False

    def get_managers_tuple(self):
        return self.__managers_permissions_and_appointer

    get_managers_tuple
    def get_purchases(self):
        return self.__purchases

    def print_inventory(self):
        f"The products of store {self.__name}:"
        i = 0
        for name, p in self.__inventory:
            f"For {name} press {i}" #TODO- check if contains \n

