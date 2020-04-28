"""
    test class for use case 2.4 - view stores and stores' info
"""
from src.Logger import logger
from src.test.BlackBoxTests.AcceptanceTests.ProjectTest import ProjectTest


class ViewStoreInfoTest(ProjectTest):
    @logger
    def setUp(self) -> None:
        super().setUp()
        self.register_user("username", "password")
        self.login("username", "password")

    @logger
    def test_success(self):
        self.open_store("store")
        self.add_products_to_store("username", "store", [("product", 10, 3, "general")])

        res = self.view_stores()
        self.assertEqual(True, res)
        self.remove_products_from_store("username", "store", ["product"])
        self.teardown_store("store")

    @logger
    def test_fail(self):
        res = self.view_stores()
        self.assertEqual(False, res)

    @logger
    def tearDown(self) -> None:
        self.remove_user("username")
