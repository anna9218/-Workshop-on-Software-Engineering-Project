"""
    test class for use case 2.5 - search and filter products
"""
from src.test.BlackBoxTests.AcceptanceTests.ProjectTest import ProjectTest


class SearchProductsTest(ProjectTest):

    def setUp(self) -> None:
        super().setUp()
        self.register_user("username", "password")
        self.login("username", "password")
        self.open_store("store")

    def test_success(self):
        self.add_products_to_store("username", "store", [("product", 10, "general", 5)])
        # search by name
        res = self.search_products_by(1, "product")
        self.assertEqual(True, res)
        # search by string
        res = self.search_products_by(2, "p")
        self.assertEqual(True, res)
        # search by category
        res = self.search_products_by(3, "general")
        self.assertEqual(True, res)
        # filter by category
        res = self.filter_products_by([2, "general"], [("product", "store")])
        self.assertEqual(True, res)
        self.remove_products_from_store("username", "store", ["product"])

    def test_fail(self):
        # search by name
        res = self.search_products_by(1, "product")
        self.assertEqual(False, res)
        # search by string
        res = self.search_products_by(2, "p")
        self.assertEqual(False, res)
        # search by category
        res = self.search_products_by(3, "general")
        self.assertEqual(False, res)

    def tearDown(self) -> None:
        self.remove_products_from_store("username", "store", ["product"])
        self.teardown_store("store")
        self.remove_user("username")

