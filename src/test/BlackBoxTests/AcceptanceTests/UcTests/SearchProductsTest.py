"""
    test class for use case 2.5 - search and filter products
"""
from src.test.BlackBoxTests.AcceptanceTests.ProjectTest import ProjectTest


class SearchProductsTest(ProjectTest):

    def setUp(self) -> None:
        super().setUp()

    def test_success(self):
        ls = self.search_products_by(1, "product") is not None
        self.assertEqual(True, ls)

    def test_fail(self):
        pass

    def tearDown(self) -> None:
        pass
