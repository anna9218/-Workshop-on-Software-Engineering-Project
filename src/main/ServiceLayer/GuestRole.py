from src.Logger import logger, loggerStaticMethod
from src.main.DomainLayer.StoreComponent.Purchase import Purchase
from src.main.DomainLayer.SecurityComponent.Security import Security
from src.main.DomainLayer.TradeComponent.TradeControl import TradeControl
# from src.main.DomainLayer.TradeComponent.TradeFacade import TradeFacade
from src.main.DomainLayer.StoreComponent.Store import Store
from src.main.DomainLayer.UserComponent.DiscountType import DiscountType
from src.main.DomainLayer.UserComponent.PurchaseType import PurchaseType
from src.main.DomainLayer.UserComponent.User import User
from src.main.DomainLayer.DeliveryComponent.DeliveryProxy import DeliveryProxy
from src.main.DomainLayer.PaymentComponent.PaymentProxy import PaymentProxy


class GuestRole:

    def __init__(self):
        pass

    @logger
    # use case 2.2 - fixed
    def register(self, nickname, password):
        if Security.get_instance().validated_password(password):
            return TradeControl.get_instance().register_guest(nickname, password)

    @logger
    # use case 2.3 - fixed
    def login(self, nickname, password):
        return TradeControl.get_instance().login_subscriber(nickname, password)

    @staticmethod
    # def display_stores():
    #     loggerStaticMethod("GuestRole.display_stores", [])
    #     return TradeControl.get_instance().get_stores()


    # use case 2.4
    @staticmethod
    # store_info_flag = true if user wants to display store info
    # products_flag = true if user wants to display product info
    def display_stores_or_products_info(store_name, store_info_flag, products_info_flag):
        loggerStaticMethod("GuestRole.display_stores_info", [store_name, store_info_flag, products_info_flag])
        if store_info_flag:
            return TradeControl.get_instance().get_store_info(store_name)
        if products_info_flag:
            return TradeControl.get_instance().get_store_inventory(store_name)
        return []

    # use case 2.5.1
    @staticmethod
    def search_products_by(search_option: int, string: str):
        """
        :param search_option: = 1-byName/2-byKeyword/3-byCategoru
        :param string: for opt: 0 -> productName, 1 -> string, 2 -> category
        :return: list of products according to the selected searching option
        """
        loggerStaticMethod("GuestRole.search_products_by", [search_option, string])
        products_ls = TradeControl.get_instance().get_products_by(search_option, string)
        return products_ls

    # use case 2.5.2
    @staticmethod
    def filter_products_by(filter_details, products_ls):
        """
        :param filter_details: list of filter details = "byPriceRange" (1, min_num, max_num)
                                                        "byCategory" (2, category)
        :param products_ls: list of string: [(product_name, store_name), ...]
        :return: list of filtered products
        """
        loggerStaticMethod("GuestRole.filter_products_by", [filter_details, products_ls])
        return TradeControl.get_instance().filter_products_by(filter_details, products_ls)

    @logger
    # use case 2.6
    def save_products_to_basket(self, products_stores_quantity_ls: [{"product_name": str, "store_name": str,
                                                                     "amount": int, "discount_type": DiscountType,
                                                                     "purchase_type": PurchaseType}]):
        """
        :param products_stores_quantity_ls: [ {"product_name": str, "amount": int, "store_name": str}, .... ]
        :return: True on success, else False
        """
        return TradeControl.get_instance().save_products_to_basket(products_stores_quantity_ls)

    @logger
    # use case 2.7
    # Parameter is nickname of the subscriber. If its a guest - None
    def view_shopping_cart(self):
        """
        :return: list: [{"store_name": str,
                         "basket": [{"product_name": str
                                     "amount": int}, ...]
                        }, ...]
        """
        TradeControl.get_instance().view_shopping_cart()

    @logger
    def update_shopping_cart(self, flag: str, products_details: [{"product_name": str, "store_name": str, "amount": int}]):
        """
        :param flag: action option - "remove"/"update"
        :param products_details: [{"product_name": str,
                                       "store_name": str,
                                       "amount": int}, ...]
        :return: True on success, False when one of the products doesn't exist in the shopping cart
        """
        if flag == "remove":
            TradeControl.get_instance().remove_from_shopping_cart(products_details)
        elif flag == "update":
            TradeControl.get_instance().update_quantity_in_shopping_cart(products_details)
        return True

    # ---------------------------------------------------- U.C 2.8-----------------------------------------------------

    @staticmethod
    @logger
    def purchase_products():
        """
        purchase products in the guest shopping cart, according to purchase policy and discount policy
        :return: directory {"total_price": float, "baskets": [purchase json object]}
        """
        return TradeControl.get_instance().purchase_products()

    @logger
    def confirm_payment(self, purchase_ls: {"total_price": float, "baskets": [dict]}):
        """
        after guest confirms payment - finish purchase
        :param purchase_ls:
        :return: true if successful, otherwise false
        """
        pay_success = PaymentProxy.get_instance().commit_payment(purchase_ls)
        if pay_success:
            deliver_success = DeliveryProxy.get_instance().deliver_products(purchase_ls)
            if not deliver_success:
                PaymentProxy.get_instance().cancel_payment(purchase_ls)
                return False
            else:
                TradeControl.get_instance().accepted_purchase(purchase_ls)
                return True
        pass

    # ------------------------------------------------- END OF U.C 2.8 ----------------------------------------------

    def __repr__(self):
        return repr("GuestRole")
