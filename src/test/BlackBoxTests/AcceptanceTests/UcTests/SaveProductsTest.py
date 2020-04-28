"""
    test class for use case 2.6 - save products to basket
"""
from src.Logger import logger
from src.test.BlackBoxTests.AcceptanceTests.ProjectTest import ProjectTest


class SaveProductsTest(ProjectTest):
    @logger
    def setUp(self) -> None:
        super().setUp()
        self.register_user("username", "password")
        self.login("username", "password")
        self.open_store("store")
        self.add_products_to_store("username", "store", [("product", 10, "general", 5)])

    @logger
    def test_success(self):
        # [ [product, quantity, store], .... ]
        res = self.add_products_to_cart("username", [("product", 1, "store")])
        self.assertEqual(True, res)

    @logger
    def test_fail(self):
        res = self.add_products_to_cart("username", [("products", 1, "store")])
        self.assertEqual(False, res)

    @logger
    def tearDown(self) -> None:
        self.remove_products_from_store("username", "store", ["product"])
        self.teardown_store("store")
        self.remove_user("username")