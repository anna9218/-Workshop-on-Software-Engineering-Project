from src.main.DomainLayer.Purchase import Purchase
from src.main.DomainLayer.Security import Security
from src.main.DomainLayer.TradeControl import TradeControl
from src.main.DomainLayer.Store import Store
from src.main.DomainLayer.User import User
from src.main.ServiceLayer.SubscriberRole import SubscriberRole


class GuestRole:

    def __init__(self):
        self.__guest: User = TradeControl.get_instance().get_guest()

    # use case 2.2
    def register(self, nickname, password):
        if Security.get_instance().validated_password(password) and \
                TradeControl.get_instance().validate_nickname(nickname) and not self.__guest.is_registered():
            self.__guest.register(nickname, password)
            TradeControl.get_instance().subscribe(self.__guest)
            return TradeControl.get_instance().get_subscriber(nickname)
        return None

    # use case 2.3
    def login(self, nickname, password):
        # subscriber = TradeControl.getInstance().getSubscriber(nickname)
        # if subscriber is not None and subscriber.is_loggedOut() and subscriber.checkPassword(password):
        #     subscriber.login()
        #     return True
        # return False
        if self.__guest.is_registered() and self.__guest.is_logged_out():
            self.__guest.login(nickname, password)
            return SubscriberRole(self.__guest)
        return None

    # use case 2.4
    @staticmethod
    def display_stores():
        return TradeControl.get_instance().get_stores()

    @staticmethod
    # store_info_flag = true if user wants to display store info
    # products_flag = true if user wants to display product info
    def display_stores_info(store_name, store_info_flag, products_flag):
        if store_info_flag:
            return TradeControl.get_instance().get_store(store_name).get_info()
        else:
            if products_flag:
                return TradeControl.get_instance().get_store(store_name).get_inventory()

    # use case 2.5.1
    @staticmethod
    def search_products_by(search_option, string):
        """
        :param self:
        :param search_option: = 0-byName, 1- byKeyword, 2- byCategoru
        :param string: for opt: 0 -> productName, 1 -> string, 2 -> category
        :return: list of products according to the selected searching option
        """
        products_ls = TradeControl.get_instance().get_products_by(search_option, string)
        return products_ls

    # use case 2.5.2
    @staticmethod
    def filter_products_by(filter_details, products_ls):
        """
        :param filter_details: list of filter details = "byPriceRange" (1, min_num, max_num)
                                                        "byCategory" (2, category)
        :param products_ls: list of pairs: [(product_name, store_name)]
        :return: list of filtered products
        """
        if products_ls is []:
            return None
        else:
            products = list(map(lambda pair: TradeControl.get_instance().get_store(pair[1]).get_product(pair[0]), products_ls))
            # products = map(lambda store: store.getProduct(pair[0]), stores)
            if filter_details[0] == 1:
                return list(filter(lambda p: filter_details[1] <= p.get_price() <= filter_details[2], products))
            else:
                if filter_details[0] == 2:
                    return list(filter(lambda p: filter_details[1] == p.get_category(), products))

    # use case 2.6
    # Parameters: nickname of the user,
    #             products_stores_quantity_ls is list of lists: [ [product, quantity, store], .... ]
    def save_products_to_basket(self, nickname, products_stores_quantity_ls):
        subscriber = TradeControl.get_instance().get_subscriber(nickname)
        if subscriber is None:  # if it's a guest, who isn't subscribed
            self.__guest.save_products_to_basket(products_stores_quantity_ls)
        else:  # subscriber exists
            subscriber.save_products_to_basket(products_stores_quantity_ls)
        return True

    # use case 2.7
    # Parameter is nickname of the subscriber. If its a guest - None
    def view_shopping_cart(self, nickname):
        if nickname is None:
            self.__guest.view_shopping_cart()
        else:
            subscriber = TradeControl.get_instance().getSubscriber(nickname)
            subscriber.view_shopping_cart()

    # Parameters: nickname of the subscriber. If its a guest - None
    #             flag=0 update quantity, flag=1 remove product
    #             product can be a single product or a pair of (product quantity)
    def update_shopping_cart(self, nickname, flag, product):
        if flag == 1:  # remove product
            if nickname is None:
                self.__guest.remove_from_shopping_cart(product)
            else:
                subscriber = TradeControl.get_instance().getSubscriber(nickname)
                subscriber.remove_from_shopping_cart(product)
        else:
            if flag == 0:  # update quantity -> product is a list of (product, quantity)
                if nickname is None:
                    self.__guest.update_quantity_in_shopping_cart(product[0], product[1])
                else:
                    subscriber = TradeControl.get_instance().getSubscriber(nickname)
                    subscriber.update_quantity_in_shopping_cart(product[0], product[1])
        return True
        # ---------------------------------------------------- U.C 2.8----------------------------------------------------------

    # U.C 2.8.1 - purchase product direct approach
    def calculate_purchase_price_direct_approach(self, store_name: str, amount_per_product: list,
                                                 username: str) -> float:
        """
        Purchasing some products from one store only.

        :param username: the username of the user which uses this system
        :param store_name: The store from which we want to purchase.
        :param amount_per_product: list of dictionary {product, amount}
        :return: if succeed true,
                  else false.
        """
        store: Store = TradeControl.get_instance().get_store(store_name)
        if store:
            if store.is_in_store_inventory(amount_per_product):
                purchase: Purchase = self.make_purchase(store, amount_per_product, username)
                if purchase:
                    return purchase.get_price()
        return -1

    # U.C 2.8.2 - purchase product in walkaround approach
    def calculate_purchase_price_walkaround_approach(self, amount_per_product_per_store: [], username: str) -> float:
        """
        Assumption: all purchases cost money.

        for each basket(i.e, each store) calculate price and sum all the prices.

        IF the purchasing failed in ALL THE STORES, then total_price = 0, and the purchasing fails.

        :param username: the username of the user which uses this system
        :param amount_per_product_per_store: list of  [store, [product, amount]]
        :return: if succeed true,
                  else false.
        """
        total_price: float = 0
        for store_and_product_and_amount in amount_per_product_per_store:
            basket_price: float = self.calculate_purchase_price_direct_approach(store_and_product_and_amount[0],
                                                                                store_and_product_and_amount[1],
                                                                                username)
            if basket_price:
                if basket_price > 0:
                    total_price = total_price + basket_price

        if total_price <= 0:
            return -1
        return total_price

    # U.C 2.8.3 & U.C 2.8.4
    def make_purchase(self, store: Store, amount_per_product: [], username: str = "") -> Purchase or None:
        """
        This function check if purchases policies allow this purchase.
        if so, check if the purchase deserves discounts and save it for further use.

        :param store: purchase policy and discount policy param.
        :param amount_per_product: purchase policy and discount policy param.
        :param username: purchase policy and discount policy param.
        :return: the purchase details.
        """
        total_price = store.check_purchase_policy(amount_per_product, username)
        if total_price > 0:
            final_price = store.calc_discount(amount_per_product, total_price, username)
            purchase = Purchase((TradeControl.get_instance()).get_next_purchase_id(), amount_per_product, final_price,
                                store.get_name(), username)
            user = (TradeControl.get_instance()).get_subscriber(username)
            if user:
                user.add_unaccepted_purchase(purchase)
                store.add
            else:
                self.__guest.add_unaccepted_purchase(purchase)
            return purchase
        return None

    # U.C 2.8.5 - purchase_product
    def accepted_price_purchase(self, purchase: Purchase, payment_details: []) -> bool:
        """
        This function take a *confirmed* purchase and sent it + payment details to the external system for payment.

        :param purchase:
        :param payment_details: [credit number-type str, the expiration date-type date_time]..
        :return: if purchase succeeded -> true.
                 else                  -> false.
        """
        user: User = (TradeControl.get_instance()).get_subscriber(purchase.get_username())
        if not user:
            if purchase in self.__guest.get_unaccepted_purchases():
                self.__guest.remove_unaccepted_purchase(purchase)
                self.__guest.add_accepted_purchase(purchase)
                store: Store = (TradeControl.get_instance()).get_store(purchase.get_store_name())
                store.add_purchase(purchase)
            else:
                return False
        else:
            if purchase in user.get_unaccepted_purchases():
                user.remove_unaccepted_purchase(purchase)
                user.add_accepted_purchase(purchase)
                store: Store = (TradeControl.get_instance()).get_store(purchase.get_store_name())
                store.add_purchase(purchase)
            else:
                return False
        return (TradeControl.get_instance()).make_payment(purchase.get_username(), purchase.get_price(),
                                                          payment_details[0], payment_details[1])

    # ------------------------------------------------- END OF U.C 2.8 -----------------------------------------------------

