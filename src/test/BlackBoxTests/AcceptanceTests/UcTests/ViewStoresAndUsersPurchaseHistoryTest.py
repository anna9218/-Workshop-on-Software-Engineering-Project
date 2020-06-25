"""
    test class for use case 6.4 - view purchase history of users and stores (by sys manager)
"""
from datetime import datetime

from src.test.BlackBoxTests.AcceptanceTests.ProjectAT import ProjectAT


class ViewStoresAndUsersPurchaseHistoryTest(ProjectAT):
    def setUp(self) -> None:
        super().setUp()
        self._username = "manager"
        self.__manager_password = "pass"
        self.add_system_manager(self._username, self.__manager_password)
        self.login(self._username, self.__manager_password)
        # self.init_sys()
        # self.login("A1", "pass")
        self.open_store(self._store_name)
        self.add_products_to_store(self._store_name,
                                       [{"name": "product", "price": 10, "category": "general", "amount": 10,
                                         "purchase_type": 0, "discount_type": 0}])
        self.add_products_to_cart("product", self._store_name, 5, 0, 0)
        self.__purchase_ls = self.purchase_products()
        self.__payment_details = {'card_number': "123", 'month': "march", 'year': "1991", 'holder': "s",
                                  'ccv': "111", 'id': "333"}
        self.__delivery_details = {'name': "nickname", 'address': "address 12", 'city': "ct", 'country': "i",
                                   'zip': "123"}
        self.confirm_purchase(self.__delivery_details, self.__payment_details, self.__purchase_ls)
        self.__date = datetime.now()

    def test_success(self):
        res = self.manager_view_user_purchases(self._username)
        self.assertTrue(res)
        res = self.manager_view_shop_purchase_history(self._store_name)
        self.assertTrue(res)

    def test_fail(self):
        # store doesn't exist
        res = self.manager_view_shop_purchase_history("anotherStoreName")
        self.assertFalse(res)
        # user doesn't exist
        res = self.manager_view_user_purchases("anotheUserName")
        self.assertFalse(res)

    def tearDown(self) -> None:
        self.remove_purchase(self._store_name, self.__date)
        self.update_shopping_cart("remove",
                                  [{"product_name": "product", "store_name": self._store_name, "amount": 10}])
        self.remove_products_from_store(self._store_name, ["product"])
        self.remove_store(self._store_name)
        self.remove_sys_manager(self._username)

    def __repr__(self):
        return repr("ViewStoresAndUsersPurchaseHistoryTest")