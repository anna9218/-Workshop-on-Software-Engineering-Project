"""
    test class for use case 6.4 - view purchase history of users and stores (by sys manager)
"""
from datetime import datetime

from src.Logger import logger
from src.test.BlackBoxTests.AcceptanceTests.ProjectTest import ProjectTest


class ViewStoresAndUsersPurchaseHistoryTest(ProjectTest):
    # @logger
    def setUp(self) -> None:
        super().setUp()
        self.__manager = "TradeManager"
        self.__manager_password = "123456789"
        self.init_sys()
        self.login("TradeManager", "123456789")
        self.open_store(self._store_name)
        self.add_products_to_store(self._store_name,
                                       [{"name": "product", "price": 10, "category": "general", "amount": 10}])
        self.add_products_to_cart("product", self._store_name, 5, 0, 0)
        self.__purchase_ls = self.purchase_products()
        self.confirm_purchase("my address 12", self.__purchase_ls)
        self.__date = datetime.now()

    # @logger
    def test_success(self):
        res = self.manager_view_user_purchases(self.__manager)
        self.assertTrue(res)
        res = self.manager_view_shop_purchase_history(self._store_name)
        self.assertTrue(res)

    # @logger
    def test_fail(self):
        # store doesn't exist
        res = self.manager_view_shop_purchase_history("anotherStoreName")
        self.assertFalse(res)
        # user doesn't exist
        res = self.manager_view_user_purchases("anotheUserName")
        self.assertFalse(res)

    # @logger
    def tearDown(self) -> None:
        self.remove_purchase(self._store_name, self.__date)
        self.update_shopping_cart("remove",
                                  [{"product_name": "product", "store_name": self._store_name, "amount": 10}])
        self.disconnect_payment_sys()
        self.disconnect_delivery_sys()
        self.remove_products_from_store(self._store_name, ["product"])
        self.remove_store("store")
        self.delete_user(self.__manager)

    def __repr__(self):
        return repr("ViewStoresAndUsersPurchaseHistoryTest")