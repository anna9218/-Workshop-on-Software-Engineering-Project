"""
    test class for use case 2.5 - search and filter products
"""
from datetime import datetime
from src.test.BlackBoxTests.AcceptanceTests.ProjectTest import ProjectTest


class SearchProductsTest(ProjectTest):
    def setUp(self) -> None:
        super().setUp()
        self.register_user(self._username, self._password)
        self.login(self._username, self._password)
        self.open_store(self._store_name)
        self.add_products_to_store(self._store_name,
                                   [{"name": "product", "price": 10, "category": "general", "amount": 10}])
        self.add_products_to_cart("product", self._store_name, 5, 0, 0)
        self.__date = datetime.now()

    def test_success(self):
        # search by name
        res = self.search_products_by(1, "product")
        self.assertTrue(res)
        # search by string
        res = self.search_products_by(2, "p")
        self.assertTrue(res)
        # search by category
        res = self.search_products_by(3, "general")
        self.assertTrue(res)
        # filter by category
        res = self.filter_products_by([2, "general"], [("product", "store")])
        self.assertTrue(res)

    def test_fail(self):
        self.remove_products_from_store(self._store_name, ["product"])
        # search by name
        res = self.search_products_by(1, "product")
        self.assertFalse(res)
        # search by string
        res = self.search_products_by(2, "p")
        self.assertFalse(res)
        # search by category
        res = self.search_products_by(3, "general")
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
        return repr("SearchProductsTest")