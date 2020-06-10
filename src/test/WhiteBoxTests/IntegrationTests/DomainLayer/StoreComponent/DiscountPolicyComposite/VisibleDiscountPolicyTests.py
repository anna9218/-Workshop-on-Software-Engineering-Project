import unittest

from src.main.DomainLayer.StoreComponent.DiscountPolicyComposite.Leaves.VisibleDiscountPolicy import \
    VisibleDiscountPolicy


class VisibleDiscountPolicyTests(unittest.TestCase):

    def setUp(self) -> None:
        dis_details = {'name': "p1", 'product': "Eytan"}
        self.__policy = VisibleDiscountPolicy(2.5, dis_details)

    def test_is_worthy(self):
        self.assertTrue(self.__policy.is_worthy(12, 12, []))

    def test_get_price_after_discount(self):
        result = self.__policy.get_price_after_discount(12)
        self.assertEqual(result, 12-0.3)

    def tearDown(self) -> None:
        pass


if __name__ == '__main__':
    unittest.main()
