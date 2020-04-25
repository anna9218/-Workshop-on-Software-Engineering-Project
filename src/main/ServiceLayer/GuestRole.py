from src.main.DomainLayer.Security import Security
from src.main.DomainLayer.TradeControl import TradeControl


class GuestRole:

    def __init__(self):
        self.__guest = TradeControl.get_instance().get_guest()

    # use case 2.2
    @staticmethod
    def register(self, nickname, password):
        if Security.get_instance().validated_password(password) and TradeControl.get_instance().validate_nickname(nickname):
            self.__guest.register(nickname, password)
            TradeControl.get_instance().subscribe(self.__guest)
            return TradeControl.get_instance().get_subscriber(nickname)
        return None

    # use case 2.3
    @staticmethod
    def login(self, nickname, password):
        # subscriber = TradeControl.getInstance().getSubscriber(nickname)
        # if subscriber is not None and subscriber.is_loggedOut() and subscriber.checkPassword(password):
        #     subscriber.login()
        #     return True
        # return False
        if self.__guest.is_registered() and self.__guest.is_logged_out():
            return self.__guest.login(nickname, password)
        return False

    def logout(self):
        if self.__guest.is_registered() and self.__guest.is_logged_in():
            return self.__guest.logout()
        return False

    # use case 2.4
    @staticmethod
    def display_stores(self):
        return TradeControl.get_instance().get_stores()

    @staticmethod
    # store_info_flag = true if user wants to display store info
    # products_flag = true if user wants to display product info
    def display_stores_info(self, store_name, store_info_flag, products_flag):
        if store_info_flag:
            return TradeControl.get_instance().get_store(store_name).get_info()
        else:
            if products_flag:
                return TradeControl.get_instance().get_store(store_name).get_inventory()

    # use case 2.5
    @staticmethod
    def search_products_by(self, search_option, string):
        """
        :param search_option: = 0-byName, 1- byKeyword, 2- byCategoru
        :param string: for opt: 0 -> productName, 1 -> string, 2 -> category
        :return: list of products according to the selected searching option
        """
        product_and_amount_ls = TradeControl.get_instance().get_products_by(search_option, string)
        return [product[0] for product in product_and_amount_ls]

    # use case 2.5
    @staticmethod
    def filter_products_by(self, filter_details, products_ls):
        """
        :param filter_details: list of filter details = "byPriceRange" (1, min_num, max_num)
                                                        "byCategory" (2, category)
        :param products_ls: list of pairs: [(product_name, store_name)]
        :return: list of filtered products
        """
        if products_ls is []:
            return False
        else:
            products = map(lambda pair: TradeControl.get_instance().get_store(pair[1]).get_product(pair[0]), products_ls)
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

