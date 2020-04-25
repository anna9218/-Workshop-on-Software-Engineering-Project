
from src.main.DomainLayer import Purchase
from src.main.DomainLayer.Product import Product
from src.main.DomainLayer.StoreInventory import StoreInventory
from src.main.DomainLayer.User import User


class Store:
    def __init__(self, store_name):
        # self.__id = id
        self.__name = store_name
        self.__owners = []
        # list of pairs (manager: User, permissions: ManagerPermissions[])
        self.__managers_and_permissions = []
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
        return user_nickname in [manager.get_nickname() for manager in self.__managers_and_permissions]

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

    def add_manager(self, manager: User, permissions):
        """
        :param manager:
        :param permissions: type - ManagerPermission[]
        :return:
        """
        self.__managers_and_permissions.append((manager, permissions))
        return True



    def get_permissions(self, manager_nickname):
        for pair in self.__managers_and_permissions:
            if pair[0].get_nickname() == manager_nickname:
                return pair[1]
        return None

    def get_info(self):
        if not self.__managers_and_permissions:  # empty list
            return "Store owners: %s" % (str(self.__owners.strip('[]')))
        else:
            if len(self.__managers_and_permissions) > 0:  # one manager exists
                return "Store owners: %s \n managers: $s" % (str(self.__owners.strip('[]')), self.__managers_and_permissions.strip('[]'))

    def empty_inventory(self):
        return self.__inventory.len() == 0

    def get_inventory(self):
        return self.__inventory

    def get_name(self):
        return self.__name

    def get_owners(self):
        return self.__owners

    def get_managers(self):
        return self.__managers_and_permissions

    def get_purchases(self):
        return self.__purchases

    def print_inventory(self):
        f"The products of store {self.__name}:"
        i = 0
        for name, p in self.__inventory:
            f"For {name} press {i}" #TODO- check if contains \n

