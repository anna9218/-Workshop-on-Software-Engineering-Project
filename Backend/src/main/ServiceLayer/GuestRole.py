from Backend.src.Logger import logger, loggerStaticMethod
from Backend.src.main.DomainLayer.StoreComponent.Purchase import Purchase
from Backend.src.main.DomainLayer.SecurityComponent.Security import Security
from Backend.src.main.DomainLayer.TradeComponent.TradeControl import TradeControl
from Backend.src.main.DomainLayer.StoreComponent.Store import Store
from Backend.src.main.DomainLayer.UserComponent.DiscountType import DiscountType
from Backend.src.main.DomainLayer.UserComponent.PurchaseType import PurchaseType
from Backend.src.main.DomainLayer.UserComponent.User import User
from Backend.src.main.DomainLayer.DeliveryComponent.DeliveryProxy import DeliveryProxy
from Backend.src.main.DomainLayer.PaymentComponent.PaymentProxy import PaymentProxy


class GuestRole:

    def __init__(self):
        pass

    @staticmethod
    # use case 2.2 - fixed
    def register(nickname, password):
        if Security.get_instance().validated_password(password):
            return TradeControl.get_instance().register_guest(nickname, password)
        return False

    @staticmethod
    # use case 2.3 - fixed
    def login(nickname, password):
        return TradeControl.get_instance().login_subscriber(nickname, password)

    # use case 2.4
    @staticmethod
    def display_stores():
        # loggerStaticMethod("GuestRole.display_stores", [])
        return TradeControl.get_instance().get_stores_names()

    @staticmethod
    def display_stores_or_products_info(store_name, store_info_flag=False, products_info_flag=False):
        # store_info_flag = true if user wants to display store info
        # products_flag = true if user wants to display product info
        # TODO: fix flags - make it 1-flag, that get either store or product. and fix the test after.
        # loggerStaticMethod("GuestRole.display_stores_info", [store_name, store_info_flag, products_info_flag])
        if store_info_flag:
            return TradeControl.get_instance().get_store_info(store_name)
        if products_info_flag:
            return TradeControl.get_instance().get_store_inventory(store_name)
        return None

    # use case 2.5.1
    @staticmethod
    def search_products_by(search_option: int, string: str):
        """
        :param search_option: = 1-byName/2-byKeyword/3-byCategoru
        :param string: for opt: 0 -> productName, 1 -> string, 2 -> category
        :return: list of products according to the selected searching option
        """
        # loggerStaticMethod("GuestRole.search_products_by", [search_option, string])
        products_ls = TradeControl.get_instance().get_products_by(search_option, string)
        return products_ls

    # use case 2.5.2
    @staticmethod
    def filter_products_by(products_ls: [{"store_name": str, "product_name": str, "price": float, "category": str}],
                           filter_by_option: int, min_price: (float or None) = None,
                           max_price: (float or None) = None, category: (str or None) = None):
        """
        This function have two options:
            Either filter_by_option == 1, and then the function should get min price and max price.
            Or filter_by_option == 2, and then the function should get category.

        The other parameters should be None, but this isn't a constraint. If they are not none, the program will ignore
                                                                                                                   them.

        Any other option should return an empty list(A.K.A Error).

        :param products_ls: list of product to filter. the user should get them by searching products.
                            Each element in the list should be a dictionary:
                                {"store_name": str, "product_name": str, "price": float, "category": str}
                                :key store_name: the name( A.K.A Unique id) of the store that sells the product.
                                :key product_name: the name( A.K.A Unique id) of the product.
                                :key price: the price of the product with the id @product_name
                                                        in the store with the id @ store_name.
                                :key category: the category of the product with the id @product_name
                                                        in the store with the id @ store_name.

        :param filter_by_option: which filter to apply. either 1: by price or
                                                               2: by category
        :param min_price: only used with option 1. this is the minimum price to filter by.
        :param max_price: only used with option 1. this is the maximum price to filter by.
        :param category: only used with option 2. this is the category to filter by.
        :return: a list of the filtered product.
                 an empty list if an error occurs.
        """
        # loggerStaticMethod("GuestRole.filter_products_by", [products_ls, filter_by_option, min_price, max_price,
        #                                                     category])
        return TradeControl.get_instance().filter_products_by(products_ls=products_ls,
                                                              filter_by_option=filter_by_option,
                                                              min_price=min_price,
                                                              max_price=max_price,
                                                              category=category)

    # @logger
    # use case 2.6
    def save_products_to_basket(self, products_stores_quantity_ls: [{"product_name": str, "store_name": str,
                                                                     "amount": int, "discount_type": DiscountType,
                                                                     "purchase_type": PurchaseType}]):
        """
        :param products_stores_quantity_ls: [ {"product_name": str, "amount": int, "store_name": str}, .... ]
        :return: True on success, else False
        """
        return TradeControl.get_instance().save_products_to_basket(products_stores_quantity_ls)

    # @logger
    # use case 2.7
    def view_shopping_cart(self):
        """
        :return: list: [{"store_name": str,
                         "basket": [{"product_name": str
                                     "amount": int}, ...]
                        }, ...]
        """
        return TradeControl.get_instance().view_shopping_cart()

    # @logger
    def update_shopping_cart(self, flag: str, products_details: [{"product_name": str, "store_name": str, "amount": int}]):
        """
        :param flag: action option - "remove"/"update"
        :param products_details: [{"product_name": str,
                                       "store_name": str,
                                       "amount": int}, ...]
        :return: True on success, False when one of the products doesn't exist in the shopping cart
        """
        if flag == "remove":
            lst = [{'product_name': element['product_name'], 'store_name': element['store_name']} for element in
                   products_details]
            return TradeControl.get_instance().remove_from_shopping_cart(lst)
        elif flag == "update":
            return TradeControl.get_instance().update_quantity_in_shopping_cart(products_details)
        else:
            return False

    # ---------------------------------------------------- U.C 2.8-----------------------------------------------------

    @staticmethod
    # @logger
    def purchase_products():
        """
            purchase all products in the guest shopping cart, according to purchase policy and discount policy
        :return: None if purchases failed, else dict
            {"total_price": float, "baskets": [{"store_name": str, "basket_price": float, "products":
                                                                        [{"product_name", "product_price", "amount"}]
                                              }]
            }
        """
        return TradeControl.get_instance().purchase_products()

    @staticmethod
    def purchase_basket(store_name: str):
        """
            single basket purchase by given store name, according to purchase policy and discount policy
        :param store_name:
        :return: None if purchase failed, else dict
            {"total_price": float, "baskets": [{"store_name": str, "basket_price": float, "products":
                                                                        [{"product_name", "product_price", "amount"}]
                                              }]
            }
        """
        return TradeControl.get_instance().purchase_basket(store_name)

    # @logger
    def confirm_payment(self, address: str, purchase_ls: dict):
        """
            purchase confirmation and addition to user & store purchases
        :param purchase_ls: dict
                [{"store_name": str, "basket_price": float, "products": [{"product_name", "product_price", "amount"}]}]
        :return: true if successful, otherwise false
        """
        pay_success = PaymentProxy.get_instance().commit_payment(purchase_ls)
        if pay_success:
            # username: str, address: str, products: [])
            deliver_success = DeliveryProxy.get_instance().deliver_products(address, purchase_ls)
            if not deliver_success:
                PaymentProxy.get_instance().cancel_payment(purchase_ls)
                return False
            else:
                TradeControl.get_instance().accept_purchases(purchase_ls)
                return True
    # ------------------------------------------------- END OF U.C 2.8 ----------------------------------------------

    def __repr__(self):
        return repr("GuestRole")