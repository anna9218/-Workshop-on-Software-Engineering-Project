from src.main.DomainLayer.Security import Security
from src.main.DomainLayer.TradeControl import TradeControl


class GuestRole:

    def __init__(self):
        self.__guest = TradeControl.getInstance().get_guest()

    # use case 2.2
    @staticmethod
    def register(self, nickname, password):
        if Security.get_instance().validated_password(password) and TradeControl.getInstance().validateNickName(nickname):
            self.__guest.register(nickname, password)
            TradeControl.getInstance().subscribe(self.__guest)
            return True
        return False

    # use case 2.3
    @staticmethod
    def login(self, nickname, password):
        # subscriber = TradeControl.getInstance().getSubscriber(nickname)
        # if subscriber is not None and subscriber.is_loggedOut() and subscriber.checkPassword(password):
        #     subscriber.login()
        #     return True
        # return False
        if self.__guest.is_registered() and self.__guest.is_loggedout():
            return self.__guest.login(nickname, password)
        return False

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
    # Parameters:
    #     search_option:  1 = search by_name, 2 = search by_keyword, 3 = search_by_category
    #     string:  product name/ keyword / category
    def search_products_by(self, search_option, string):
        product_and_amount_ls = TradeControl.getInstance().get_products_by(search_option, string)
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
            products = map(lambda pair: TradeControl.getInstance().get_store(pair[1]).get_product(pair[0]), products_ls)
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


