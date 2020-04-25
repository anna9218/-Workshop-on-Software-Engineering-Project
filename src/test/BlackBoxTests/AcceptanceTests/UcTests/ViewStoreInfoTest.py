"""
    test class for use case 2.4 - view stores and stores' info
"""
from src.test.BlackBoxTests.AcceptanceTests.ProjectTest import ProjectTest


class ViewStoreInfoTest(ProjectTest):

    def setUp(self) -> None:
        pass

    def test_success(self):
        store_ls = self.view_stores()
        self.assertNotEqual(len(store_ls), 0)

        store = store_ls[0]
        store_inf = self.view_store_info(store, True, True)
        self.assertNotEqual(len(store_inf), 0)

    def test_fail(self):
        pass

    def tearDown(self) -> None:
        pass
