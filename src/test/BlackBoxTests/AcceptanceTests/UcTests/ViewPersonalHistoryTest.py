"""
    test class for use case 3.7 - view personal shopping history
"""
from datetime import datetime

from src.test.BlackBoxTests.AcceptanceTests.ProjectAT import ProjectAT


class ViewPersonalHistoryTest(ProjectAT):
    def setUp(self) -> None:
        super().setUp()
        self.register_user(self._username, self._password)
        self.login(self._username, self._password)
        self.open_store(self._store_name)
        self.add_products_to_store(self._store_name,
                                   [{"name": "product", "price": 10, "category": "general", "amount": 10,
                                     "purchase_type": 0, "discount_type": 0}])
        self.connect_delivery_sys()
        self.connect_payment_sys()
        self.add_products_to_cart("product", self._store_name, 5, 0, 0)
        self.__purchase_ls = self.purchase_products()
        self.confirm_purchase("my address 12", self.__purchase_ls)
        self.__date = datetime.now()

    def test_success(self):
        # none empty shopping cart
        res = self.view_personal_purchase_history()
        self.assertTrue(res)

    def test_fail(self):
        # empty shopping cart
        self.remove_purchase(self._store_name, self.__date)
        res = self.view_personal_purchase_history()
        self.assertFalse(res)

    def tearDown(self) -> None:
        self.remove_purchase(self._store_name, self.__date)
        self.update_shopping_cart("remove",
                                  [{"product_name": "product", "store_name": self._store_name, "amount": 10}])
        self.disconnect_payment_sys()
        self.disconnect_delivery_sys()
        self.remove_products_from_store(self._store_name, ["product"])
        self.remove_store("store")
        self.delete_user(self._username)

    def __repr__(self):
        return repr("ViewPersonalHistoryTest")