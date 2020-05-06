# from src.main.DomainLayer import Purchase
from src.Logger import logger
from src.main.DomainLayer.StoreComponent.DiscountPolicy import DiscountPolicy
from src.main.DomainLayer.StoreComponent.ManagerPermission import ManagerPermission
from src.main.DomainLayer.StoreComponent.Purchase import Purchase
from src.main.DomainLayer.StoreComponent.PurchasePolicy import PurchasePolicy
from src.main.DomainLayer.StoreComponent.StoreInventory import StoreInventory
from src.main.DomainLayer.StoreComponent.Product import Product
from src.main.DomainLayer.StoreComponent.StoreManagerAppointment import StoreManagerAppointment, User
# from src.main.DomainLayer.UserComponent.DiscountType import DiscountType
# from src.main.DomainLayer.UserComponent.PurchaseType import PurchaseType


class Store:
    def __init__(self, store_name):
        # self.__id = id
        self.__name = store_name
        self.__owners = []
        # list of StoreManagerAppointment (manager: User, permissions: ManagerPermissions[], appointer:User)
        self.__StoreManagerAppointments = []
        self.__inventory = StoreInventory()
        self.__discount_policies: [DiscountPolicy] = [DiscountPolicy()]
        self.__purchase_policies: [PurchasePolicy] = [PurchasePolicy()]
        self.__purchases = []

    @logger
    def add_products(self, user_nickname: str, products_details: [{"name": str, "price": int, "category": str, "amount": int}]) -> bool:
        """
        :param user_nickname: owner's/manager's nickname
        :param products_details: list of tuples (product_name, product_price, product_category, product_amount) / JSON
        :return: True if all products were added to the inventory
        """

        # check permission to add - EDIT_INV
        if self.is_owner(user_nickname) or (self.is_manager(user_nickname) and
                                            self.has_permission(user_nickname, ManagerPermission.EDIT_INV)):
            for d in products_details:
                if d["price"] < 0:
                    return False
                if d["amount"] < 0:
                    return False
                if d['name'].strip() == "":
                    return False
                if d['category'].strip() == "":
                    return False
            results = list(map(lambda details: self.add_product(details["name"],
                                                                details["price"],
                                                                details["category"],
                                                                details["amount"]),
                               products_details))
            return False not in results

    @logger
    def add_product(self, name: str, price: float, category: str, amount: int) -> bool:
        """
        :param name: name of the new product
        :param price: price of the new product
        :param amount: amount of the new product
        :param category: category of the new product
        :return: True if product was added to the inventory
        """
        if name == "".strip() or price < 0.0 or category == "".strip() or amount < 0.0:
            return False
        return self.__inventory.add_product(Product(name, price, category), amount)

    @logger
    def remove_products(self, user_nickname: str, products_names: list) -> bool:
        """
        :param user_nickname: owner's/manager's nickname
        :param products_names: products to delete from inventory (assume they exists on inventory)
        :return: True if products were removed
        """
        # check permission to remove - EDIT_INV
        if self.is_owner(user_nickname) or (self.is_manager(user_nickname) and
                                            self.has_permission(user_nickname, ManagerPermission.EDIT_INV)):
            results = list(map(lambda p_name: self.remove_product(p_name), products_names))
            return False not in results

    @logger
    def remove_product(self, product_name: str) -> bool:
        """
        :param product_name: product's name to delete from inventory
        :return: True if product was removed
        """
        # assume the product exists in the inventory
        return self.__inventory.remove_product(product_name)

    @logger
    def edit_product(self, user_nickname: str, product_name: str, op: str, new_value):  # new_value can be str or int
        """
        :param user_nickname: owner's/manager's nickname
        :param product_name: the name of the product to change
        :param op: "name" -> change name, "price" -> change price, "amount" -> change amount
        :param new_value: the new value of the product in the attribute that corresponded with the op.
        :return: True if successful,
                 False else.
        """
        # check permission to remove - EDIT_INV
        if self.is_owner(user_nickname) or (self.is_manager(user_nickname) and
                                            self.has_permission(user_nickname, ManagerPermission.EDIT_INV)):
            if op == "name":
                return self.change_name(product_name, new_value)
            elif op == "price":
                return self.change_price(product_name, new_value)
            elif op == "amount":
                return self.change_amount(product_name, new_value)
            else:
                return False

    @logger
    def change_price(self, product_name: str, new_price: float) -> bool:
        """
       :param product_name: name of the product
       :param new_price: new price to replace with
       :return: True if price was updated
       """
        if new_price < 0.0:
            return False

        product = self.get_product(product_name)
        if product is not None:
            product.set_price(new_price)
            return True
        return False

    @logger
    def change_name(self, product_name: str, new_name: str) -> bool:
        """
        :param product_name: name of the product
        :param new_name: name to replace with
        :return: True if name was updated
        """
        if new_name.strip() == "":
            return False

        product = self.get_product(product_name)
        if product is not None:
            product.set_name(new_name)
            return True
        return False

    @logger
    def change_amount(self, product_name: str, new_amount: int) -> bool:
        """
       :param product_name: product
       :param new_amount: new amount to replace with
       :return: True if amount was updated
       """
        if new_amount < 0:
            return False

        product = self.get_product(product_name)
        if product is not None:
            return self.__inventory.change_amount(product_name, new_amount)
        return False

    @logger
    def add_owner(self, appointer: str, appointee: User) -> bool:
        """
        appointee has to be registered.
        appointee can't be owner already.
        if appointee is already manager, we will remove him from being manager.

        :param appointer: owner's/manager's nickname.
        :param appointee: new manager from type User.
        :return: True if owner has been added
                 False else.
        """

        if not appointee.is_registered():
            return False

        if appointee in self.__owners:
            return False

        managers = [manager_appointment.get_appointee() for manager_appointment in self.__StoreManagerAppointments]
        if self.is_owner(appointer):
            self.__owners.append(appointee)
            if appointee in managers:
                appointment = [manager_appointment for manager_appointment in self.__StoreManagerAppointments
                               if manager_appointment.get_appointee() == appointee]
                self.__StoreManagerAppointments.remove(appointment[0])
            return True
        return False


    @logger
    def is_owner(self, user_nickname: str):
        return user_nickname in [owner.get_nickname() for owner in self.__owners]

    @logger
    def is_manager(self, user_nickname: str):
        managers = [man.get_nickname() for man in self.get_managers()]
        return user_nickname in managers

    @logger
    def has_permission(self, user_nickname, permission):
        my_appointment = list(
            filter(lambda app: app.get_appointee().get_nickname() == user_nickname, self.__StoreManagerAppointments))
        if my_appointment:
            return my_appointment[0].has_permission(permission)
        return False

    @logger
    # eden added
    def get_products_by(self, opt, string):
        return self.__inventory.get_products_by(opt, string)

    @logger
    # eden added
    def get_product(self, product_name):
        return self.__inventory.get_product(product_name)

    # def get_purchase_info(self, purchase: Purchase):
    #     for p in self.__purchases:
    #         if p == purchase:  # TODO - how do we compare purchases?
    #             return p

    # def print_inventory(self):
    #     f"The products of store {self.__name}:"
    #     i = 0
    #     for name, p in self.__inventory:
    #         f"For {name} press {i}" #TODO- check if contains \n

    @logger
    def add_manager(self, appointer: User, appointee: User, permissions: list):
        """
        :param appointer: store's owner/manager
        :param appointee: manager to appoint
        :param permissions: type - ManagerPermission[]
        :return: True on success, else False
        """
        # check permission to add owner - APPOINT_MANAGER
        if not appointee.is_registered():
            return False

        if appointee in self.__owners or appointee in self.get_managers():
            return False

        if (self.is_owner(appointer.get_nickname()) or
                ((self.is_manager(appointer.get_nickname())) and
                 self.has_permission(appointer.get_nickname(), ManagerPermission.APPOINT_MANAGER))):
            self.__StoreManagerAppointments.append(StoreManagerAppointment(appointer, appointee, permissions))
            return True
        return False

    @logger
    def get_permissions(self, manager_nickname):
        for appointment in self.__StoreManagerAppointments:
            if appointment.get_appointee().get_nickname() == manager_nickname:
                return appointment.get_permissions()
        return None

    @logger
    def get_info(self):
        if not self.__StoreManagerAppointments:  # empty list
            return "Store owners: %s" % (str(self.__owners.strip('[]')))
        else:
            if len(self.__StoreManagerAppointments) > 0:  # one manager exists
                return "Store owners: %s \n managers: $s" % (
                    str(self.__owners.strip('[]')), self.__StoreManagerAppointments.strip('[]'))

    @logger
    def is_in_store_inventory(self, amount_per_product):
        """
        :param amount_per_product: [product name : str, amount:int]
                                    product name is the *id* of the product.
                                    amount is the requested quantity.
        :return: True if product is in store inventory in a quantity >= amount.
                 False else.
        """
        for product_and_amount in amount_per_product:
            if not self.get_inventory().is_in_stock(product_and_amount[0], product_and_amount[1]):
                return False
        return True


    @logger
    def calc_discount(self, amount_per_product: [], price: float, username: str):
        """
        This function should check if the user can/can't complete the purchase.
        Due to the fact that we does'nt have the purchase policies requirements, this func is currently a stab.

        :param amount_per_product: param to check policy.
        :param price: param to check policy.
        :param username: param to check policy.
        :return: the price after discount. if no discount is available, return the price.
        """
        return price

    @logger
    def empty_inventory(self):
        return self.__inventory.len() == 0

    @logger
    def get_inventory(self):
        return self.__inventory

    @logger
    def get_name(self):
        return self.__name

    @logger
    def get_owners(self):
        return self.__owners

    @logger
    def get_managers(self):
        return [manager_appointment.get_appointee() for manager_appointment in self.__StoreManagerAppointments]

    @logger
    def edit_manager_permissions(self, appointer: User, appointee_nickname: str, permissions: list) -> bool:
        """
        :param appointer: store's owner/manager
        :param appointee_nickname: manager who's permissions will be editted
        :param permissions: ManagerPermission[] ->list of permissions (list of Enum)
        :return: True on success, else False
        """
        # check permission to add owner - EDIT_MANAGER_PER
        if self.is_owner(appointer.get_nickname()) or (self.is_manager(appointer.get_nickname()) and
                                        self.has_permission(appointer.get_nickname(), ManagerPermission.EDIT_MANAGER_PER)):
            for appointment in self.__StoreManagerAppointments:
                if appointment.get_appointee().get_nickname() == appointee_nickname and \
                        appointment.get_appointer().get_nickname() == appointer.get_nickname():
                    appointment.set_permissions(permissions)
                    return True
        return False

    @logger
    def remove_manager(self, appointer_nickname: str, appointee_nickname: str) -> bool:
        """
        :param appointer_nickname: store's owner/manager
        :param appointee_nickname: manager to remove
        :return: True on success, else False
        """
        # check permission to add owner - DEL_MANAGER
        if self.is_owner(appointer_nickname) or (self.is_manager(appointer_nickname) and
                                                 self.has_permission(appointer_nickname,
                                                                     ManagerPermission.DEL_MANAGER)):
            for appointment in self.__StoreManagerAppointments:
                if appointment.get_appointee().get_nickname() == appointee_nickname and \
                        appointment.get_appointer().get_nickname() == appointer_nickname:
                    self.__StoreManagerAppointments.remove(appointment)
                    return True
        return False

    @logger
    def get_store_manager_appointments(self):
        return self.__StoreManagerAppointments

    @logger
    def get_purchases(self, appointer_nickname: str):
        # check permission to add owner - WATCH_PURCHASE_HISTORY
        if self.is_owner(appointer_nickname) or (self.is_manager(appointer_nickname) and
                                                 self.has_permission(appointer_nickname,
                                                                     ManagerPermission.WATCH_PURCHASE_HISTORY)):
            return self.__purchases
        return []


    # def print_inventory(self):
    #     f"The products of store {self.__name}:"
    #     i = 0
    #     for name, p in self.__inventory:
    #         f"For {name} press {i}" #TODO- check if contains \n

    # @logger
    # def check_purchase_policy(self, amount_per_product: [], username: str) -> float:
    #     """
    #     This function should check if the user can/can't complete the purchase.
    #     Due to the fact that we does'nt have the purchase policies requirements, this func is currently a stab.
    #
    #     If the user can complete the purchase, the function calculate its price without discount.
    #
    #     :param amount_per_product: param to check policy.
    #     :param username: param to check policy.
    #     :return: the price if possible.
    #              -1 else.
    #     """
    #     total_price: float = 0
    #     for product_and_amount in amount_per_product:
    #         try:
    #             product: Product = self.__inventory.get_product(product_and_amount[0])
    #             product_price = float(product.get_price())
    #         except AttributeError:
    #             product_price = -1
    #         if product_price >= 0:
    #             total_price = total_price + (product_price * product_and_amount[1])
    #             total_price = total_price + (product_price * product_and_amount[1])
    #
    #     return total_price
    @logger
    def add_purchase(self, purchase: Purchase):
        self.__purchases.insert(0, purchase)

    @logger
    def check_purchase_policy(self, product_name: str) -> bool:
        """
        :param product_name: product name
        :return: true if the user can purchase the product, otherwise false
        """
        for p in self.__purchase_policies:
            if not p.check_policy(self.__name, product_name):
                return False
        return True

    @logger
    def check_discount_policy(self, product_name: str) -> bool:
        """
        :param product_name: product name
        :return: true if the user can purchase the product, otherwise false
        """
        for d in self.__discount_policies:
            if not d.check_discount(self.__name, product_name):
                return False
        return True

    @logger
    def can_purchase(self, product_name: str, amount: int):
        if self.__inventory.get_amount(product_name) <= amount or \
                not self.check_purchase_policy(product_name):
            return False
        return True

    @staticmethod
    def calculate_discount_price(product_name: str, price: int, amount: int):
        # once we have functionality for discounts, here we will calculate the discounted price according to the policy
        return price * amount

    @logger
    def complete_purchase(self, purchase_ls: [dict]):
        for p in purchase_ls:
            amount = self.__inventory.get_amount(p["product_name"]) - p["amount"]
            if not self.__inventory.change_amount(p["product_name"], amount):
                self.__inventory.remove_product(p["product_name"])
        pass

    def __repr__(self):
        return repr("Store")
