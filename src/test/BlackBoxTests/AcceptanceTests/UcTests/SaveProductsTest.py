"""
    test class for use case 2.6 - save products to basket
"""
from src.test.BlackBoxTests.AcceptanceTests.ProjectAT import ProjectAT


class SaveProductsTest(ProjectAT):
    def setUp(self) -> None:
        super().setUp()
        self.register_user(self._username, self._password)
        self.login(self._username, self._password)
        self.open_store(self._store_name)
        self.add_products_to_store(self._store_name,
                                   [{"name": "product", "price": 10, "category": "general", "amount": 5}])

    def test_success(self):
        res = self.add_products_to_cart("product", self._store_name, 5, 0, 0)
        self.assertTrue(res)

    def test_fail(self):
        # store doesn't exist
        res = self.add_products_to_cart("product", "anotherStoreName", 5, 0, 0)
        self.assertFalse(res['response'])
        # product doesn't exist in the store
        res = self.add_products_to_cart("anotherProductName", self._store_name, 5, 0, 0)
        self.assertFalse(res['response'])

    def tearDown(self) -> None:
        self.update_shopping_cart("remove",
                                  [{"product_name": "product", "store_name": self._store_name, "amount": 5}])
        self.remove_products_from_store(self._store_name, ["product"])
        self.remove_store("store")
        self.delete_user(self._username)

    def __repr__(self):
        return repr("SaveProductsTest")
