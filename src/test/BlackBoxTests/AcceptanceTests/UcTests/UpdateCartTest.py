"""
    test class for use case 2.7 - view and update shopping cart
"""
from src.test.BlackBoxTests.AcceptanceTests.ProjectAT import ProjectAT


class UpdateCartTest(ProjectAT):

    def setUp(self) -> None:
        super().setUp()
        self.register_user(self._username, self._password)
        self.login(self._username, self._password)
        self.open_store(self._store_name)
        self.add_products_to_store(self._store_name,
                                   [{"name": "product", "price": 10, "category": "general", "amount": 5,
                                     "purchase_type": 0, "discount_type": 0}])
        self.add_products_to_cart("product", self._store_name, 1, 0, 0)

    def test_success(self):
        # view cart with valid details
        res = self.view_shopping_cart()
        self.assertTrue(res)
        # update with valid details
        res = self.update_shopping_cart("update",
                                        [{"product_name": "product", "store_name": self._store_name, "amount": 10}])
        self.assertTrue(res)
        # delete with valid details
        res = self.update_shopping_cart("remove",
                                        [{"product_name": "product", "store_name": self._store_name, "amount": 1}])
        self.assertTrue(res)

    def test_fail(self):
        # store doesn't exist
        res = self.update_shopping_cart("update",
                                        [{"product_name": "product", "store_name": "anotherStoreName", "amount": 10}])
        self.assertFalse(res['response'])
        res = self.update_shopping_cart("remove",
                                        [{"product_name": "product", "store_name": "anotherStoreName", "amount": 1}])
        self.assertFalse(res['response'])
        # product doesn't exist
        res = self.update_shopping_cart("update",
                                    [{"product_name": "anotherProduct", "store_name": self._store_name, "amount": 10}])
        self.assertFalse(res['response'])
        res = self.update_shopping_cart("remove",
                                    [{"product_name": "anotherProduct", "store_name": self._store_name, "amount": 1}])
        self.assertFalse(res['response'])
        # empty shopping cart
        self.update_shopping_cart("remove",
                                    [{"product_name": "product", "store_name": self._store_name, "amount": 1}])
        res = self.view_shopping_cart()
        self.assertFalse(res)

    def tearDown(self) -> None:
        self.update_shopping_cart("remove",
                                  [{"product_name": "product", "store_name": self._store_name, "amount": 1}])
        self.remove_products_from_store(self._store_name, ["product"])
        self.remove_store("store")
        self.delete_user(self._username)

    def __repr__(self):
        return repr("UpdateCartTest")