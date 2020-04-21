"""
    test example class - to be deleted once a real test is made
"""
from src.test.BlackBoxTests.AcceptanceTests import ProjectTest


class JunkTest(ProjectTest.ProjectTest):

    def setUp(self) -> None:
        super().setUp()
        self.x = int(1)
        self.y = int(2)
        self.expected = int(3)
        pass

    # example tests

    # def test_wrong_sum(self):
    #     true_sum = super().test_wrong_sum(self.x, self.y)
    #     self.assertNotEqual(true_sum, self.expected, "should be false")
    #     return
    #
    # def test_sum(self):
    #     true_sum = super().test_sum(self.x, self.y)
    #     self.assertEqual(true_sum, self.expected, "should be true")
    #     return

    def tearDown(self) -> None:
        pass
