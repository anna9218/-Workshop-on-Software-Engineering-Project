import datetime

from src.Logger import logger
from src.main.DomainLayer.StoreComponent.AppiontmentAgreement import AppointmentAgreement
from src.main.DomainLayer.StoreComponent.DiscountPolicyComposite.DiscountPolicy import DiscountPolicy
from src.main.DomainLayer.StoreComponent.ManagerPermission import ManagerPermission
from src.main.DomainLayer.StoreComponent.Product import Product
from src.main.DomainLayer.StoreComponent.Purchase import Purchase
from src.main.DomainLayer.StoreComponent.PurchasePolicyComposite.PurchasePolicy import PurchasePolicy
from src.main.DomainLayer.StoreComponent.StoreInventory import StoreInventory
from src.main.DomainLayer.StoreComponent.StoreAppointment import StoreAppointment
from src.main.DomainLayer.UserComponent.PurchaseType import PurchaseType
from src.main.DomainLayer.UserComponent.ShoppingBasket import ShoppingBasket
from src.main.DomainLayer.UserComponent.User import User


class Store:
    def __init__(self, store_name):
        # self.__id = id
        self.__name = store_name
        self.__StoreOwnerAppointments = []
        # list of StoreManagerAppointment (manager: User, permissions: ManagerPermissions[], appointer:User)
        self.__StoreManagerAppointments = []
        self.__inventory = StoreInventory()
        self.__discount_policies: [DiscountPolicy] = []
        self.__purchase_policies: [PurchasePolicy] = []
        self.__purchases: [Purchase] = []
        self.__purchases = []
        # default operator is 'and'
        self.__operator = "and"
        self.__StoreOwnerAppointmentAgreements: [AppointmentAgreement] = []

    @logger
    def add_products(self, user_nickname: str,
                     products_details: [{"name": str, "price": int, "category": str, "amount": int,
                                         "purchase_type": int}]) -> {'response': bool, 'msg': str}:
        """
        :param user_nickname: owner's/manager's nickname
        :param products_details: list of tuples (product_name, product_price, product_category, product_amount) / JSON
        :return: True if all products were added to the inventory
        """
        # check permission to add - EDIT_INV
        # if self.is_owner(user_nickname) or (self.is_manager(user_nickname) and
        #                                     self.has_permission(user_nickname, ManagerPermission.EDIT_INV)):
        if self.has_permission(user_nickname, ManagerPermission.EDIT_INV):

            for d in products_details:
                if d['name'].strip() == "":
                    return {'response': False, 'msg': "Error! invalid product name " + d['name']}
                if d['category'].strip() == "":
                    return {'response': False, 'msg': "Error! invalid category " + d['category']}
                if d["price"] < 0:
                    return {'response': False, 'msg': "Error! The price of product " + d['name'] +
                                                      " must be greater than 0"}
                if d["amount"] < 0:
                    return {'response': False, 'msg': "Error! The amount of product " + d['name'] +
                                                      " must be greater than 0"}

            results = list(map(lambda details: self.add_product(user_nickname, details["name"],
                                                                details["price"],
                                                                details["category"],
                                                                details["amount"],
                                                                details["purchase_type"]),
                               products_details))
            if False not in results:
                return {'response': True, 'msg': "Products were added successfully to the store"}
        return {'response': False, 'msg': "User has no permissions"}

    @logger
    def add_product(self, user_nickname: str, name: str, price: float, category: str, amount: int, purchase_type: int) \
            -> bool:
        """
        :param name: name of the new product
        :param price: price of the new product
        :param amount: amount of the new product
        :param category: category of the new product
        :return: True if product was added to the inventory
        """
        if name == "".strip() or price < 0.0 or category == "".strip() or amount < 0.0:
            return False
        if self.has_permission(user_nickname, ManagerPermission.EDIT_INV):
            product = Product(name, price, category)
            product.set_purchase_type(purchase_type)
            return self.__inventory.add_product(product, amount)

    @logger
    def remove_products(self, user_nickname: str, products_names: list) -> bool:
        """
        :param user_nickname: owner's/manager's nickname
        :param products_names: products to delete from inventory (assume they exists on inventory)
        :return: True if products were removed
        """
        # check permission to remove - EDIT_INV
        # if self.is_owner(user_nickname) or (self.is_manager(user_nickname) and
        #                                     self.has_permission(user_nickname, ManagerPermission.EDIT_INV)):
        if self.has_permission(user_nickname, ManagerPermission.EDIT_INV):
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
        # if self.is_owner(user_nickname) or (self.is_manager(user_nickname) and
        #                                     self.has_permission(user_nickname, ManagerPermission.EDIT_INV)):
        if self.has_permission(user_nickname, ManagerPermission.EDIT_INV):

            if op == "name":
                return self.change_name(product_name, new_value)
            elif op == "price":
                return self.change_price(product_name, float(new_value))
            elif op == "amount":
                return self.change_amount(product_name, int(new_value))
            elif op == "purchase_type":
                self.get_product(product_name).set_purchase_type(new_value)
                return True
            elif op == "category":
                self.get_product(product_name).set_category(new_value)
                return True
            else:
                return False
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

    def get_appointees(self, appointer_nickname: str, managers_or_owners: str) -> list:
        """
        :param appointer_nickname:
        :param managers_or_owners: "MANAGERS" or "OWNERS" to get a list of the managers or owners that appointer_nickname appointed
        :return: returns a list of nicknames, of all the managers appointer_nickname appointed
        """
        appointees_ls = []
        if managers_or_owners == "OWNERS":
            appointees_ls = self.__StoreOwnerAppointments
        if managers_or_owners == "MANAGERS":
            appointees_ls = self.__StoreManagerAppointments
        my_appointees = []
        for appointment in appointees_ls:
            if appointment.get_appointer() is not None and \
                    appointment.get_appointer().get_nickname() == appointer_nickname:
                my_appointees.append(appointment.get_appointee().get_nickname())
        return my_appointees

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
    def product_in_inventory(self, product_name: str):
        return self.__inventory.get_product(product_name) is not None

    # @logger
    def add_owner(self, appointer_nickname: str, appointee: User) -> bool:
        """
        appointee has to be registered.
        appointee can't be owner already.
        if appointee is already manager, we will remove him from being manager.

        :param appointer_nickname: owner's/manager's nickname.
        :param appointee: new manager from type User.
        :return: True if owner has been added
                 False else.
        """

        if not appointee.is_registered():
            return False

        if self.is_owner(appointee.get_nickname()):
            return False
        # if self.is_owner(appointer_nickname):
        #     return False

        managers = self.get_managers()

        if self.has_permission(appointer_nickname, ManagerPermission.APPOINT_OWNER):
            owners_and_managers = self.get_owners() + self.get_managers()
            appointer = list(filter(lambda user: user.get_nickname() == appointer_nickname, owners_and_managers))[0]
            self.__StoreOwnerAppointments.append(StoreAppointment(appointer, appointee, []))
            if appointee in managers:
                appointment = [manager_appointment for manager_appointment in self.__StoreManagerAppointments
                               if manager_appointment.get_appointee() == appointee]
                self.__StoreManagerAppointments.remove(appointment[0])
            return True
        return False

    @logger
    def is_owner(self, user_nickname: str):
        return user_nickname in [owner.get_nickname() for owner in self.get_owners()]

    @logger
    def is_manager(self, user_nickname: str):
        managers = [man.get_nickname() for man in self.get_managers()]
        return user_nickname in managers

    @logger
    def has_permission(self, user_nickname, permission):
        if self.is_owner(user_nickname):
            return True
        if self.is_manager(user_nickname):
            my_appointment = list(
                filter(lambda app: app.get_appointee().get_nickname() == user_nickname, self.__StoreManagerAppointments))
            if my_appointment:
                return my_appointment[0].has_permission(permission)
            return False
        return False

    @logger
    def get_products_by(self, opt, string):
        return self.__inventory.get_products_by(opt, string)

    @logger
    def get_product(self, product_name) -> Product:
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

        if appointee in self.get_owners() or appointee in self.get_managers():
            return False

        # if (self.is_owner(appointer.get_nickname()) or
        #         ((self.is_manager(appointer.get_nickname())) and
        #          self.has_permission(appointer.get_nickname(), ManagerPermission.APPOINT_MANAGER))):
        if self.has_permission(appointer.get_nickname(), ManagerPermission.APPOINT_MANAGER):

            self.__StoreManagerAppointments.append(StoreAppointment(appointer, appointee, permissions))
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
            return "Store owners: %s" % (str(self.__StoreOwnerAppointments.strip('[]')))
        else:
            if len(self.__StoreManagerAppointments) > 0:  # one manager exists
                return "Store owners: %s \n managers: $s" % (
                    str(self.__StoreOwnerAppointments.strip('[]')), self.__StoreManagerAppointments.strip('[]'))

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
    def empty_inventory(self):
        return self.__inventory.len() == 0

    @logger
    def get_inventory(self):
        return self.__inventory

    @logger
    def get_name(self):
        return self.__name

    @logger
    def get_owners_appointments(self):
        return self.__StoreOwnerAppointments

    @logger
    def get_owners(self):
        x = [owner_appointment.get_appointee() for owner_appointment in self.__StoreOwnerAppointments]
        return x
    @logger
    def get_managers(self):
        return [manager_appointment.get_appointee() for manager_appointment in self.__StoreManagerAppointments]

    @logger
    def edit_manager_permissions(self, appointer: User, appointee_nickname: str, permissions: list) -> bool:
        """
        :param appointer: store's owner/manager
        :param appointee_nickname: manager who's permissions will be edited
        :param permissions: ManagerPermission[] ->list of permissions (list of Enum)
        :return: True on success, else False
        """
        # check permission to add owner - EDIT_MANAGER_PER
        # if self.is_owner(appointer.get_nickname()) or (self.is_manager(appointer.get_nickname()) and
        #                                                self.has_permission(appointer.get_nickname(),
        #                                                                    ManagerPermission.EDIT_MANAGER_PER)):
        if self.has_permission(appointer.get_nickname(), ManagerPermission.EDIT_MANAGER_PER):
            for appointment in self.__StoreManagerAppointments:
                if appointment.get_appointee().get_nickname() == appointee_nickname and \
                        appointment.get_appointer().get_nickname() == appointer.get_nickname():
                    appointment.set_permissions(permissions)
                    return True
        return False

    @logger
    def remove_owner(self, appointer_nickname: str, appointee_nickname: str) -> {'response': [], 'msg': str}:
        """
        the function removes appointee_nickname as owner from the store, in addition to him it removes all the managers
        and owners appointee_nickname appointed.
        :param appointer_nickname: store's owner/manager
        :param appointee_nickname: owner to remove
        :return: dict =  {'response': [], 'msg': str}
                 response = nicknames list of all the removed appointees -> the appointee_nickname of the owner we want
                            to remove and all the appointees he appointed, we had to remove as well.
        """
        if self.has_permission(appointer_nickname, ManagerPermission.DEL_OWNER):
            for appointment in self.__StoreOwnerAppointments:
                if appointment.get_appointee().get_nickname() == appointee_nickname and \
                        appointment.get_appointer().get_nickname() == appointer_nickname:
                    # TODO: Yarin, send message for appointee_nickname that he was removed from the store as manager
                    self.__StoreOwnerAppointments.remove(appointment)
                    removed_appointees = self.remove_owner_appointees(appointee_nickname)
                    return {'response': [appointee_nickname + " removed as owner"] + removed_appointees,
                            'msg': "Store owner " + appointee_nickname + " and his appointees were removed successfully."}
        return {'response': [], 'msg': "Error! remove store owner failed."}

    @logger
    def remove_owner_appointees(self, appointer_nickname: str) -> list:
        """
        remove all the appointees of the store owner
        :param appointer_nickname: nickname of the store owner
        :return: list of nickname of the owner's appointees that were removed
        """


        result = []

        ls_to_remove = []
        for appointment in self.__StoreOwnerAppointments:
            if appointment.get_appointer() and appointment.get_appointer().get_nickname() == appointer_nickname:
                appointee = appointment.get_appointee()
                # TODO: Yarin, send message for appointee.get_nickname() that he was removed from the store as manager
                res = self.remove_owner_appointees(appointment.get_appointee().get_nickname())
                result.append(appointee.get_nickname() + " removed as owner")
                result += res
                ls_to_remove.append(appointment)

                # self.__StoreOwnerAppointments.remove(appointment)

        self.__StoreOwnerAppointments = [i for i in self.__StoreOwnerAppointments if i not in ls_to_remove]

        ls_to_remove = []
        for appointment in self.__StoreManagerAppointments:
            a = appointment
            if appointment.get_appointer().get_nickname() == appointer_nickname:
                appointee = appointment.get_appointee()
                # TODO: Yarin, send message for appointee.get_nickname() that he was removed from the store as manager
                result.append(appointee.get_nickname() + " removed as manager")
                # self.__StoreManagerAppointments.remove(appointment)
                ls_to_remove.append(appointment)

        self.__StoreManagerAppointments = [i for i in self.__StoreManagerAppointments if i not in ls_to_remove]

        return result



    @logger
    def remove_manager(self, appointer_nickname: str, appointee_nickname: str) -> bool:
        """
        :param appointer_nickname: store's owner/manager
        :param appointee_nickname: manager to remove
        :return: True on success, else False
        """
        # check permission to add owner - DEL_MANAGER
        # if self.is_owner(appointer_nickname) or (self.is_manager(appointer_nickname) and
        #                                          self.has_permission(appointer_nickname,
        #                                                              ManagerPermission.DEL_MANAGER)):
        if self.has_permission(appointer_nickname, ManagerPermission.DEL_MANAGER):
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
        # if self.is_owner(appointer_nickname) or (self.is_manager(appointer_nickname) and
        #                                          self.has_permission(appointer_nickname,
        #                                                              ManagerPermission.WATCH_PURCHASE_HISTORY)):
        if self.has_permission(appointer_nickname, ManagerPermission.WATCH_PURCHASE_HISTORY):

            return self.__purchases
        return []


    # def print_inventory(self):
    #     f"The products of store {self.__name}:"
    #     i = 0
    #     for name, p in self.__inventory:
    #         f"For {name} press {i}" #TODO- check if contains \n

    @logger
    def add_purchase(self, purchase: Purchase):
        self.__purchases.insert(0, purchase)

    @logger
    def purchase_basket(self, basket: ShoppingBasket) -> {'response': dict, 'msg': str}:
        """
        purchase user shopping basket
        :param basket:
        :return: dict
            {"store_name": str, "basket_price": float, "products":
                                                        [{"product_name": str, "product_price": float, "amount": int}]]}
        """
        products = []
        list(map(lambda curr_product:
                 products.append({"product_name": curr_product["product"].get_name(), "amount": curr_product["amount"]}),
                 basket.get_products()))

        if len(products) == 0:
            return {'response': None, 'msg': "No products added"}
        can_purchase = self.can_purchase(products, datetime.date.today())
        if not can_purchase["response"]:
            return {'response': None, 'msg': "Purchase failed: " + can_purchase["msg"]}

        products_purchases = []
        basket_price = 0
        for product in basket.get_products():
            if product["product"].get_purchase_type() == PurchaseType.DEFAULT:
                purchase = self.purchase_immediate(product["product"].get_name(),
                                               product["product"].get_price(), product["amount"])

            elif product["product"].get_purchase_type() == PurchaseType.AUCTION:
                purchase = self.purchase_auction(product["product"].get_name(),
                                             product["product"].get_price(), product["amount"])
            else:
                purchase = self.purchase_lottery(product["product"].get_name(),
                                             product["product"].get_price(), product["amount"])

            if purchase is not None:
                products_purchases.append(purchase)
                basket_price += purchase["product_price"]

        if len(products_purchases) == 0:
            return {'response': None, 'msg': " No purchases can be made"}
        else:
            return {'response': {"store_name": self.__name, "basket_price": basket_price, "products": products_purchases},
                    'msg': "Success"}

    # u.c 2.8.1
    @logger
    def purchase_immediate(self, product_name: str, product_price: int, amount: int):
        """
        :param product_name: product name
        :param product_price: product price
        :param amount: product amount
        :return: dictionary {"product_name": str, "product_price": float, "amount": int} or None
        """
   #     # if self.check_discount_policy(product_name):
   #     price = self.calculate_discount_price(product_name, product_price, amount)
   #     return {"product_name": product_name, "product_price": price, "amount": amount}
  #      # return None
        price = product_price
        for policy in self.__discount_policies:
            if policy.get_product_name() == product_name:
                if policy.is_worthy(amount, basket_price, prod_lst):
                    price = min(price, policy.get_price_after_discount(product_price))
        return {"product_name": product_name, "product_price": price*amount, "amount": amount}

    # u.c 2.8.2 - mostly temp initialization since we don't have purchase policy functionality yet
    @logger
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
    @logger
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

    @logger
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

    @logger
    def check_purchase_policy(self, details: [{"product_name": str, "amount": int}], curr_date: datetime) \
            -> {'response': bool, 'msg': str}:
        """
        :param curr_date:
        :param details: list [{"product_name": str, "amount": int}]
        :return: true if the user can purchase the product, otherwise false
        """
        xor_flag = False
        if self.__operator == "and":
            for policy in self.__purchase_policies:
                if not policy.can_purchase(details, curr_date):
                    return {'response': False, 'msg': "Policy: " + policy.get_name() + ", rule not met - for type 'all'"}
            return {'response': True, 'msg': "Great Success! Good Job!"}

        elif self.__operator == "or":
            for policy in self.__purchase_policies:
                if policy.can_purchase(details, curr_date):
                    return {'response': True, 'msg': "Great Success! Good Job!"}
            return {'response': False, 'msg': "All policies rule not met - for type: 'at least one'"}

        elif self.__operator == "xor":
            for policy in self.__purchase_policies:
                if policy.can_purchase(details, curr_date):
                    if not xor_flag:
                        xor_flag = True
                    else:
                        return {'response': False, 'msg': "More than one policy rules - for type: 'only one'"}
        return {'response': True, 'msg': "Great Success! Good Job!"}

    @logger
    def can_purchase(self, details: [{"product_name": str, "amount": int}], curr_date: datetime) \
            -> {'response': bool, 'msg': str}:
        for product in details:
            if self.__inventory.get_amount(product["product_name"]) < product["amount"]:
                return {'response': False, 'msg': "Requested amount for product: "
                                                  + product["product_name"] + ", exceeds amount in inventory"}
        return self.check_purchase_policy(details, curr_date)

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

    @staticmethod
    @logger
    def calculate_discount_price(product_name: str, price: int, amount: int):
        # once we have functionality for discounts, here we will calculate the discounted price according to the policy
        return price * amount

    @staticmethod
    @logger
    def check_purchase_end_time(store_name: str, product_name: str):
        # temp function since we don't have functionality for purchasing policy
        return False

    @staticmethod
    @logger
    def did_win_auction():
        # temp function till we have the policy
        return True

    @staticmethod
    @logger
    def does_price_exceed(price: int):
        # temp function till we have the policy
        return False

    # ------------- 4.2 --------------
    # ------------- purchase policy --------------
    def set_purchase_operator(self, operator: str):
        self.__operator = operator

    def get_purchase_operator(self):
        return self.__operator

    def purchase_policy_exists(self, details: {"name": str, "products": [str],
                                               "min_amount": int or None, "max_amount": int or None,
                                               "dates": [dict] or None, "bundle": bool or None}):
        """
            only used in trade control -> no need for returned msg
        :param details: {"name": str,                            -> policy name
                        "operator": str,                         -> and/or/xor
                        "products": [str],                       -> list of product names
                        "min_amount": int or None,               -> minimum amount of products required
                        "max_amount": int or None,               -> maximum amount of products required
                        "dates": [dict] or None,                 -> list of prohibited dated for the given products
                        "bundle": bool or None}                  -> true if the products are bundled together
        :return: true if policy exists, otherwise false
        """
        for policy in self.__purchase_policies:
            if policy.equals(details):
                return True
        return False

    @logger
    def define_purchase_policy(self, details: {"name": str, "products": [str],
                                               "min_amount": int or None, "max_amount": int or None,
                                               "dates": [datetime] or None, "bundle": bool or None})\
            -> {'response': bool, 'msg': str}:
        """
        :param details: {"name": str,                            -> policy name
                        "operator": str,                         -> and/or/xor
                        "products": [str],                       -> list of product names
                        "min_amount": int or None,               -> minimum amount of products required
                        "max_amount": int or None,               -> maximum amount of products required
                        "dates": [dict] or None,                 -> list of prohibited dated for the given products
                        "bundle": bool or None}                  -> true if the products are bundled together
        :return: true if successful, otherwise false
        """
        policy = PurchasePolicy()
        res = policy.add_purchase_policy(details)
        if res.get("response"):
            self.__purchase_policies.append(policy)
        return res

    @logger
    def update_purchase_policy(self, details: {"name": str, "products": [str],
                                               "min_amount": int or None, "max_amount": int or None,
                                               "dates": [dict] or None, "bundle": bool or None})\
            -> {'response': bool, 'msg': str}:
        policy = self.get_policy(details["name"])
        if policy:
            policy.update(details)
            return {'response': True, 'msg': "Great Success! Policy updated"}
        return {'response': False, 'msg': "Oops...no policy exist by the given name"}

    @logger
    def get_purchase_policies(self):
        ls = []
        for policy in self.__purchase_policies:
            details = policy.get_details()
            if len(details) > 0:
                ls.append(details)
        return ls

    @logger
    def get_policy(self, policy_name: str):
        for policy in self.__purchase_policies:
            if policy.get_name() == policy_name:
                return policy
        return None

    def set_purchase_policies(self, policy: PurchasePolicy):
        self.__purchase_policies.append(policy)

    # function for ut teardown
    def reset_policies(self):
        self.__purchase_policies = []
    # ------------- purchase policy end --------------
    # ------------- 4.2 --------------

    def __repr__(self):
        return repr("Store")

    def __eq__(self, other):
        # TODO: for v3 & catching, maybe improve this.
        if type(other) is not Store:
            return False

        if not self.__name == other.get_name():
            return False
        return True

