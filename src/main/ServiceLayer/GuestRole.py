from src.main.DomainLayer.Security import Security
from src.main.DomainLayer.TradeControl import TradeControl


class GuestRole:

    def __init__(self):
        self.__guest = TradeControl.getInstance().get_guest()

    # use case 2.2
    @staticmethod
    def register(self, nickname, password):
        if Security.getInstance().validatedPassword(password) and TradeControl.getInstance().validateNickName(nickname):
            subscriber = TradeControl.getInstance().subscribe()
            subscriber.register(nickname, password)
            return True
        return False

    # use case 2.3
    @staticmethod
    def login(self, nickname, password):
        subscriber = TradeControl.getInstance().getSubscriber(nickname)
        if subscriber is not None and subscriber.is_loggedOut() and subscriber.checkPassword(password):
            subscriber.login()
            return True
        return False

        # if user.registrationState.is_registered() and
        #    user.registrationState.get_name() == username and
        #    user.registrationState.get_password() == password:
        #
        #     cls.set_state(True)
        #     user.logoutState.set_state(False)
        #     return True
        # else:
        #     print("login failed")
        #     return False

    # use case 2.4
    @staticmethod
    def display_stores(self):
        return TradeControl.getInstance().get_stores()

    @staticmethod
    def display_stores_info(self, store, store_info_flag, products_flag):
        if store_info_flag:
            return TradeControl.getInstance().get_store(store.get_name()).get_info()
        else:
            if products_flag:
                return TradeControl.getInstance().get_store(store.get_name()).get_inventory()

    # use case 2.5
    @staticmethod
    # option: 1 = by name, 2 = by keyword, 3 = by category
    def search_products_by(self, search_option, string):
        product_and_amount_ls = TradeControl.getInstance().getProductsBy(search_option, string)
        return [product[0] for product in product_and_amount_ls]

    # use case 2.5
    @staticmethod
    # Parameters:
    #    filter_details: list of filter details = "byPriceRange" (1, min_num, max_num)
    #                                             "byCategory" (2, category)
    #    products_ls: list of pairs: [(product_name, store_name)]
    # Returns:
    #    reverse(str1):The string which gets reversed.
    def filter_products_by(self, filter_details, products_ls):
        if products_ls is []:
            return False
        else:
            products = map(lambda pair: TradeControl.getInstance().get_store(pair[1]).getProduct(pair[0]), products_ls)
            # products = map(lambda store: store.getProduct(pair[0]), stores)
            if filter_details[0] == 1:
                return filter(lambda p: filter_details[1] <= p.get_price() <= filter_details[2], products)
            else:
                if filter_details[0] == 2:
                    return filter(lambda p: filter_details[1] == p.get_category(), products)
                  
    # use case 2.6
    @staticmethod
    # Parameters: nickname of the user,
    #             products_stores_quantity_ls is list of lists: [ [product, quantity, store], .... ]
    def save_products_to_basket(self, nickname, products_stores_quantity_ls):
        subscriber = TradeControl.getInstance().getSubscriber(nickname)
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
            subscriber = TradeControl.getInstance().getSubscriber(nickname)
            subscriber.view_shopping_cart()

    # Parameters: nickname of the subscriber. If its a guest - None
    #             flag=0 update quantity, flag=1 remove product
    #             product can be a single product or a pair of (product quantity)
    def update_shopping_cart(self, nickname, flag, product):
        if flag == 1:  # remove product
            if nickname is None:
                self.__guest.remove_from_shopping_cart(product)
            else:
                subscriber = TradeControl.getInstance().getSubscriber(nickname)
                subscriber.remove_from_shopping_cart(product)
        else:
            if flag == 0:  # update quantity -> product is a list of (product, quantity)
                if nickname is None:
                    self.__guest.update_quantity_in_shopping_cart(product[0], product[1])
                else:
                    subscriber = TradeControl.getInstance().getSubscriber(nickname)
                    subscriber.update_quantity_in_shopping_cart(product[0], product[1])
        return True

