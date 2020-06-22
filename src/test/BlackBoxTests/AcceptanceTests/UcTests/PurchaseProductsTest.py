"""
    test class for use case 2.8 - purchase products
"""
from datetime import datetime

from src.test.BlackBoxTests.AcceptanceTests.ProjectAT import ProjectAT


class PurchaseProductsTest(ProjectAT):
    def setUp(self) -> None:
        super().setUp()
        self.register_user(self._username, self._password)
        self.login(self._username, self._password)
        self.open_store(self._store_name)
        self.add_products_to_store(self._store_name,
                                   [{"name": "product", "price": 10, "category": "general", "amount": 10,
                                     "purchase_type": 0, "discount_type": 0}])
        self.add_products_to_cart("product", self._store_name, 5, 0, 0)
        self.__date = datetime.now()
        self.__payment_details = {'card_number': "123", 'month': "march", 'year': "1991", 'holder': "s",
                                  'ccv': "111", 'id': "333"}
        self.__delivery_details = {'name': "nickname", 'address': "address 12", 'city': "ct", 'country': "i",
                                   'zip': "123"}

    def test_success(self):
        # valid none empty cart purchase
        purchase_ls = self.purchase_products()
        self.assertTrue(len(purchase_ls) != 0)
        # confirmation
        res = self.confirm_purchase(self.__delivery_details, self.__payment_details, purchase_ls)
        self.assertTrue(res)

    def test_fail(self):
        # one or more invalid detail in delivery details
        purchase_ls = self.purchase_products()
        res = self.confirm_purchase({'name': "nickname", 'address': "address 12", 'city': "ct", 'country': "i"},
                                    self.__payment_details, purchase_ls) # missing zip
        self.assertFalse(res['response'])
        purchase_ls = self.purchase_products()
        res = self.confirm_purchase({'name': "nickname", 'address': "address 12", 'city': "ct"},
                                    self.__payment_details, purchase_ls)  # missing zip and country
        self.assertFalse(res['response'])
        # one or more invalid detail in payment details
        purchase_ls = self.purchase_products()
        res = self.confirm_purchase(self.__delivery_details, {'card_number': "123", 'month': "march", 'year': "1991",
                                                              'holder': "s", 'ccv': "111"}, purchase_ls) # missing id
        self.assertFalse(res['response'])
        purchase_ls = self.purchase_products()
        res = self.confirm_purchase(self.__delivery_details, {'card_number': "123", 'month': "march", 'year': "1991",
                                                              'holder': "s"}, purchase_ls)  # missing id and ccv
        self.assertFalse(res['response'])
        # empty cart
        self.update_shopping_cart("remove",
                                  [{"product_name": "product", "store_name": self._store_name, "amount": 10}])
        purchase_ls = self.purchase_products()
        self.assertEqual(purchase_ls , [])

    def tearDown(self) -> None:
        self.remove_purchase(self._store_name, self.__date)
        self.update_shopping_cart("remove",
                                  [{"product_name": "product", "store_name": self._store_name, "amount": 10}])
        self.remove_products_from_store(self._store_name, ["product"])
        self.remove_store("store")
        self.delete_user(self._username)

    def __repr__(self):
        return repr("PurchaseProductsTest")