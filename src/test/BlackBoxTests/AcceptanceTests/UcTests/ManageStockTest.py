"""
    test class for use case 4.1 - manage stock (store)
"""
from src.Logger import logger
from src.test.BlackBoxTests.AcceptanceTests.ProjectTest import ProjectTest


class ManageStockTest(ProjectTest):
    # @logger
    def setUp(self) -> None:
        super().setUp()
        self.register_user(self._username, self._password)
        self.login(self._username, self._password)
        self.open_store(self._store_name)

    # @logger
    def test_success(self):
        # add product to store, valid details
        res = self.add_products_to_store(self._store_name, [{"name": "product", "price": 10, "category": "general", "amount": 5}])
        self.assertTrue(res)
        # edit products in store, valid details
        res = self.edit_products_in_store(self._store_name, "product", "price", 12)
        self.assertTrue(res)
        # remove product from store, valid details
        res = self.remove_products_from_store(self._store_name, ["product"])
        self.assertTrue(res)

    # @logger
    def test_fail(self):
        # store doesn't exist
        res = self.add_products_to_store("anotherStoreName",
                                         [{"name": "product", "price": 10, "category": "general", "amount": 5}])
        self.assertFalse(res)
        # store doesn't exist or product doesn't exist in store
        res = self.edit_products_in_store("anotherStoreName", "product", "price", 12)
        self.assertFalse(res)
        res = self.edit_products_in_store(self._store_name, "pizza", "price", 12)
        self.assertFalse(res)
        # store doesn't exist or product doesn't exist in store
        res = self.remove_products_from_store("anotherStoreName", ["product"])
        self.assertFalse(res)
        res = self.remove_products_from_store(self._store_name, ["pizza"])
        self.assertFalse(res)

    # @logger
    def tearDown(self) -> None:
        self.delete_user(self._username)
        self.remove_store(self._store_name)

    def __repr__(self):
        return repr("ManageStockTest")