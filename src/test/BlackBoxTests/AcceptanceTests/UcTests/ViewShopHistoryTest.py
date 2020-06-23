"""
    test class for use case 4.10 - view shop shopping history
"""
from datetime import datetime

from src.test.BlackBoxTests.AcceptanceTests.ProjectAT import ProjectAT


class ViewShopHistoryTest(ProjectAT):
    def setUp(self) -> None:
        super().setUp()
        self.register_user(self._username, self._password)
        self.login(self._username, self._password)
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
        # existing purchases and existing store
        res = self.view_store_purchase_history(self._store_name)
        self.assertTrue(res)

    def test_fail(self):
        # store doesn't exist
        res = self.view_store_purchase_history("anotherStoreName")
        self.assertFalse(res)
        # no purchased for store
        self.remove_purchase(self._store_name, self.__date)
        res = self.view_store_purchase_history(self._store_name)
        self.assertFalse(res)

    def tearDown(self) -> None:
        self.remove_purchase(self._store_name, self.__date)
        self.update_shopping_cart("remove",
                                  [{"product_name": "product", "store_name": self._store_name, "amount": 10}])
        self.remove_products_from_store(self._store_name, ["product"])
        self.remove_store("store")
        self.delete_user(self._username)

    def __repr__(self):
        return repr("ViewShopHistoryTest")