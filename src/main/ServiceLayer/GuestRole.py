from src.main.DomainLayer.Security import Security
from src.main.DomainLayer.TradeControl import TradeControl


class GuestRole:

    def __init__(self):
        pass

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
    def display_stores_info(self):
        pass

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




