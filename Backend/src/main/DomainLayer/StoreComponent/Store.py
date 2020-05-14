from datetime import datetime

from Backend.src.Logger import logger
from Backend.src.main.DomainLayer.StoreComponent.DiscountPolicy import DiscountPolicy
from Backend.src.main.DomainLayer.StoreComponent.ManagerPermission import ManagerPermission
from Backend.src.main.DomainLayer.StoreComponent.Product import Product
from Backend.src.main.DomainLayer.StoreComponent.Purchase import Purchase
from Backend.src.main.DomainLayer.StoreComponent.PurchasePolicy import PurchasePolicy
from Backend.src.main.DomainLayer.StoreComponent.StoreInventory import StoreInventory
from Backend.src.main.DomainLayer.StoreComponent.StoreManagerAppointment import StoreManagerAppointment
from Backend.src.main.DomainLayer.UserComponent.DiscountType import DiscountType
from Backend.src.main.DomainLayer.UserComponent.PurchaseType import PurchaseType
from Backend.src.main.DomainLayer.UserComponent.ShoppingBasket import ShoppingBasket
from Backend.src.main.DomainLayer.UserComponent.User import User


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

    # @logger
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
            results = list(map(lambda details: self.add_product(details["name"],
                                                                details["price"],
                                                                details["category"],
                                                                details["amount"]),
                               products_details))
            return False not in results

    # @logger
    def add_product(self, name: str, price: int, category: str, amount: int) -> bool:
        """
        :param name: name of the new product
        :param price: price of the new product
        :param amount: amount of the new product
        :param category: category of the new product
        :return: True if product was added to the inventory
        """
        return self.__inventory.add_product(Product(name, price, category), amount)

    # @logger
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

    # @logger
    def remove_product(self, product_name: str) -> bool:
        """
        :param product_name: product's name to delete from inventory
        :return: True if product was removed
        """
        # assume the product exists in the inventory
        return self.__inventory.remove_product(product_name)

    # @logger
    def edit_product(self, user_nickname: str, product_name: str, op: str, new_value):  # new_value can be str or int
        """
        :param user_nickname: owner's/manager's nickname
        :param product_name:
        :param op:
        :param new_value:
        :return:
        """
        # check permission to remove - EDIT_INV
        if self.is_owner(user_nickname) or (self.is_manager(user_nickname) and
                                            self.has_permission(user_nickname, ManagerPermission.EDIT_INV)):
            if op == "name":
                self.change_name(product_name, new_value)
            elif op == "price":
                self.change_price(product_name, new_value)
            elif op == "amount":
                self.change_amount(product_name, new_value)
            else:
                return False
        return True

    # @logger
    def change_price(self, product_name: str, new_price: int) -> bool:
        """
       :param product_name: name of the product
       :param new_price: new price to replace with
       :return: True if price was updated
       """
        if new_price < 0:
            return False

        product = self.get_product(product_name)
        if product is not None:
            product.set_price(new_price)
            return True
        return False

    # @logger
    def change_name(self, product_name: str, new_name: str) -> bool:
        """
        :param product_name: name of the product
        :param new_name: name to replace with
        :return: True if name was updated
        """
        product = self.get_product(product_name)
        if product is not None:
            product.set_name(new_name)
            return True
        return False

    # @logger
    def change_amount(self, product_name: str, new_amount: int) -> bool:
        """
       :param product_name: product
       :param new_amount: new amount to replace with
       :return: True if amount was updated
       """
        if new_amount < 0:
            return False

        product = self.get_product(product_name)
        if product is not None and new_amount > 0:
            return self.__inventory.change_amount(product_name, new_amount)
        return False

    def product_in_inventory(self, product_name: str):
        return self.__inventory.get_product(product_name) is not None

    # @logger
    def add_owner(self, appointer: str, appointee: User) -> bool:
        """
        :param appointer: owner's/manager's nickname
        :param appointee: new manager's nickname
        :return: True if owner has been added
        """
        # first case: appointing first owner he when opens the
        # check permission to add owner - APPOINT_OWNER
        if self.is_owner(appointer) or (self.is_manager(appointer) and
                                        self.has_permission(appointer, ManagerPermission.APPOINT_MANAGER)):
            self.__owners.append(appointee)
            return True
        return False

    # @logger
    def is_owner(self, user_nickname):
        return user_nickname in [owner.get_nickname() for owner in self.__owners]

    # @logger
    def is_manager(self, user_nickname: str):
        return user_nickname in [appointment.get_appointee().get_nickname() for appointment in
                                 self.__StoreManagerAppointments]

    # @logger
    def has_permission(self, user_nickname, permission):
        my_appointment = list(
            filter(lambda app: app.get_appointee().get_nickname() == user_nickname, self.__StoreManagerAppointments))
        if my_appointment:
            return my_appointment[0].has_permission(permission)
        return False

    # @logger
    # eden added
    def get_products_by(self, opt, string):
        return self.__inventory.get_products_by(opt, string)

    # @logger
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

    # @logger
    def add_manager(self, appointer: User, appointee: User, permissions: list):
        """
        :param appointer: store's owner/manager
        :param appointee: manager to appoint
        :param permissions: type - ManagerPermission[]
        :return: True on success, else False
        """
        # check permission to add owner - APPOINT_MANAGER
        if self.is_owner(appointer.get_nickname()) or (self.is_manager(appointer) and
                                        self.has_permission(appointer, ManagerPermission.APPOINT_OWNER)):
            self.__StoreManagerAppointments.append(StoreManagerAppointment(appointer, appointee, permissions))
            return True
        return False

    # @logger
    def get_permissions(self, manager_nickname):
        for appointment in self.__StoreManagerAppointments:
            if appointment.get_appointee().get_nickname() == manager_nickname:
                return appointment.get_permissions()
        return None

    # @logger
    def get_info(self):
        if not self.__StoreManagerAppointments:  # empty list
            return "Store owners: %s" % (str(self.__owners.strip('[]')))
        else:
            if len(self.__StoreManagerAppointments) > 0:  # one manager exists
                return "Store owners: %s \n managers: $s" % (
                    str(self.__owners.strip('[]')), self.__StoreManagerAppointments.strip('[]'))

    # @logger
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



    # @logger
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

    # @logger
    def empty_inventory(self):
        return self.__inventory.len() == 0

    # @logger
    def get_inventory(self):
        return self.__inventory

    # @logger
    def get_name(self):
        return self.__name

    # @logger
    def get_owners(self):
        return self.__owners

    # @logger
    def get_managers(self):
        return [t[0] for t in self.__StoreManagerAppointments]

    # @logger
    def edit_manager_permissions(self, appointer: User, appointee_nickname: str, permissions: list) -> bool:
        """
        :param appointer: store's owner/manager
        :param appointee_nickname: manager who's permissions will be editted
        :param permissions: ManagerPermission[] ->list of permissions (list of Enum)
        :return: True on success, else False
        """
        # check permission to add owner - EDIT_MANAGER_PER
        if self.is_owner(appointer) or (self.is_manager(appointer) and
                                        self.has_permission(appointer, ManagerPermission.EDIT_MANAGER_PER)):
            for appointment in self.__StoreManagerAppointments:
                if appointment.get_appointee().get_nickname() == appointee_nickname and \
                        appointment.get_appointer().get_nickname() == appointer.get_nickname():
                    appointment.set_permissions(permissions)
                    return True
        return False

    # @logger
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

    # @logger
    def get_store_manager_appointments(self):
        return self.__StoreManagerAppointments

    # @logger
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
    def add_purchase(self, purchase: Purchase):
        self.__purchases.insert(0, purchase)

    def purchase_basket(self, basket: ShoppingBasket):
        """
        purchase user shopping basket
        :param basket:
        :return: dict
            {"store_name": str, "basket_price": float, "products":
                                                        [{"product_name": str, "product_price": float, "amount": int}]]}
        """
        products_purchases = []
        purchase = None
        basket_price = 0
        for product in basket.get_products():
            if self.can_purchase(product["product"].get_name(), product["amount"]):
                if product["purchaseType"] == PurchaseType.DEFAULT:
                    purchase = self.purchase_immediate(product["product"].get_name(),
                                                   product["product"].get_price(), product["amount"])

                elif product["purchaseType"] == PurchaseType.AUCTION:
                    purchase = self.purchase_auction(product["product"].get_name(),
                                                 product["product"].get_price(), product["amount"])
                else:
                    purchase = self.purchase_lottery(product["product"].get_name(),
                                                 product["product"].get_price(), product["amount"])
            # else:
            #     return None

            if purchase is not None:
                products_purchases.append(purchase)
                basket_price += purchase["product_price"]
        if len(products_purchases) == 0:
            return None
        else:
            return {"store_name": self.__name, "basket_price": basket_price, "products": products_purchases}

    # u.c 2.8.1
    # @logger
    def purchase_immediate(self, product_name: str, product_price: int, amount: int):
        """
        :param product_name: product name
        :param product_price: product price
        :param amount: product amount
        :return: dictionary {"product_name": str, "product_price": float, "amount": int} or None
        """
        if self.check_discount_policy(product_name):
            price = self.calculate_discount_price(product_name, product_price, amount)
            return {"product_name": product_name, "product_price": price, "amount": amount}
        return None

    # u.c 2.8.2 - mostly temp initialization since we don't have purchase policy functionality yet
    # @logger
    def purchase_auction(self, product_name: str, product_price: int, amount: int):
        """
        :param store_name: store name
        :param product_name: product name
        :param product_price: product price
        :param amount: product amount
        :return: dictionary {"product_name": str, "product_price": float, "amount": int} or None
        """
        if not self.check_purchase_end_time():
            if self.did_win_auction():
                return self.purchase_immediate(product_name, product_price, amount)
        else:
            # here ask guest for bidding amount
            # if it's higher than previous bids -> add new bid for the auction
            # since we don't have auction yet, we return None for now
            return None

    # u.c 2.8.3 - mostly temp initialization since we don't have purchase policy functionality yet
    # @logger
    def purchase_lottery(self, product_name: str, product_price: int, amount: int):
        """
        :param product_name: product name
        :param product_price: product price
        :param amount: product amount
        :return: dictionary {"product_name": str, "product_price": float, "amount": int} or None
        """
        if self.check_purchase_end_time():
            if not self.does_price_exceed(product_price):
                # buy tickets and return the amount bought with all other details
                # here we'll return to 2.8.1
                return self.purchase_immediate(product_name, product_price, amount)
        else:
            # here ask guest for bidding amount
            # if it's higher than previous bids -> add new bid for the auction
            # since we don't have auction yet, we return None for now
            return None

    # def complete_purchase(self, purchase: Purchase):

    def complete_purchase(self, purchase: Purchase):
        # add purchase to purchase history
        self.__purchases.append(purchase)
        # delete purchased products from inventory
        products = purchase.get_products()
        # products = [{"product_name": str, "product_price": float, "amount": int}]
        for product in products:
            amount = self.__inventory.get_amount(product["product_name"]) - product["amount"]
            if not self.__inventory.change_amount(product["product_name"], amount):
                self.__inventory.remove_product(product["product_name"])

    def remove_purchase(self, nickname: str, date: datetime):
        for p in self.__purchases:
            if p.get_nickname() == nickname and p.get_date() == date:
                self.__purchases.remove(p)

    def check_purchase_policy(self, product_name: str) -> bool:
        """
        :param product_name: product name
        :return: true if the user can purchase the product, otherwise false
        """
        for p in self.__purchase_policies:
            if not p.check_policy(self.__name, product_name):
                return False
        return True

    def check_discount_policy(self, product_name: str) -> bool:
        """
        :param product_name: product name
        :return: true if the user can purchase the product, otherwise false
        """
        for d in self.__discount_policies:
            if not d.check_discount(self.__name, product_name):
                return False
        return True

    def can_purchase(self, product_name: str, amount: int):
        if self.__inventory.get_amount(product_name) <= amount or \
                not self.check_purchase_policy(product_name):
            return False
        return True

    @staticmethod
    def calculate_discount_price(product_name: str, price: int, amount: int):
        # once we have functionality for discounts, here we will calculate the discounted price according to the policy
        return price * amount

    @staticmethod
    # @logger
    def check_purchase_end_time(store_name: str, product_name: str):
        # temp function since we don't have functionality for purchasing policy
        return False

    @staticmethod
    # @logger
    def did_win_auction():
        # temp function till we have the policy
        return True

    @staticmethod
    # @logger
    def does_price_exceed(price: int):
        # temp function till we have the policy
        return False

    def __repr__(self):
        return repr("Store")
