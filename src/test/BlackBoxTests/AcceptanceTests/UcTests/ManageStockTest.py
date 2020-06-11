"""
    test class for use case 4.1 - manage stock (store)
"""
from src.test.BlackBoxTests.AcceptanceTests.ProjectAT import ProjectAT


class ManageStockTest(ProjectAT):
    def setUp(self) -> None:
        super().setUp()
        self.register_user(self._username, self._password)
        self.login(self._username, self._password)
        self.open_store(self._store_name)

    def test_success(self):
        # add product to store, valid details
        res = self.add_products_to_store(self._store_name, [{"name": "product", "price": 10, "category": "general", "amount": 5,
                                                             "purchase_type": 0, "discount_type": 0}])
        self.assertTrue(res)
        # edit products in store, valid details
        res = self.edit_products_in_store(self._store_name, "product", "price", 12)
        self.assertTrue(res)
        # remove product from store, valid details
        res = self.remove_products_from_store(self._store_name, ["product"])
        self.assertTrue(res)

    def test_fail(self):
        # store doesn't exist
        res = self.add_products_to_store("anotherStoreName",
                                         [{"name": "product", "price": 10, "category": "general", "amount": 5,
                                           "purchase_type": 0, "discount_type": 0}])
        self.assertFalse(res['response'])
        # store doesn't exist or product doesn't exist in store
        res = self.edit_products_in_store("anotherStoreName", "product", "price", 12)
        self.assertFalse(res['response'])
        res = self.edit_products_in_store(self._store_name, "pizza", "price", 12)
        self.assertFalse(res['response'])
        # store doesn't exist or product doesn't exist in store
        res = self.remove_products_from_store("anotherStoreName", ["product"])
        self.assertFalse(res)
        res = self.remove_products_from_store(self._store_name, ["pizza"])
        self.assertFalse(res)

    def tearDown(self) -> None:
        self.remove_store(self._store_name)
        self.delete_user(self._username)

    def __repr__(self):
        return repr("ManageStockTest")