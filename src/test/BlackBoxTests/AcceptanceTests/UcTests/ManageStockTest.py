"""
    test class for use case 4.1 - manage stock (store)
"""
from src.Logger import logger
from src.test.BlackBoxTests.AcceptanceTests.ProjectTest import ProjectTest


class ManageStockTest(ProjectTest):
    @logger
    def setUp(self) -> None:
        super().setUp()
        self.__username = "username"
        self.__pass = "password"
        self.__store = "store"

    @logger
    def test_success(self):
        # add product to store
        self.register_user(self.__username, self.__pass)
        self.login(self.__username, self.__pass)
        self.open_store(self.__store)
        res = self.add_products_to_store(self.__username, self.__store, [("product", 10, 3, "general")])
        self.assertEqual(True, res)
        # edit products in store
        res = self.edit_products_in_store(self.__username, self.__store, "product", "price", 12)
        self.assertEqual(True, res)
        # remove product from store
        res = self.remove_products_from_store(self.__username, self.__store, ["product"])
        self.assertEqual(True, res)

    @logger
    def test_fail(self):
        pass

    @logger
    def test_add(self):
        pass

    @logger
    def test_edit(self):
        pass

    @logger
    def test_remove(self):
        pass

    @logger
    def tearDown(self) -> None:
        pass

    def __repr__(self):
        return repr("ManageStockTest")