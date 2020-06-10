import unittest

from src.main.DomainLayer.StoreComponent.DiscountPolicyComposite.Leaves.ConditionalDiscountPolicy import \
    ConditionalDiscountPolicy


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        dis_details = {'name': "p1", 'product': "Eytan"}
        pre_con__details = {'product': "Eytan", 'min_amount': 2, 'min_basket_price': None}
        self.__product_condition_policy = ConditionalDiscountPolicy(2.5, dis_details, pre_con__details)
        dis_details = {'name': "p2", 'product': "all"}
        pre_con__details = {'product': "all", 'min_amount': None, 'min_basket_price': 20}
        self.__basket_condition_policy = ConditionalDiscountPolicy(5, dis_details, pre_con__details)
        dis_details = {'name': "p3", 'product': "Eytan"}
        pre_con__details = {'product': "Eytan", 'min_amount': 2, 'min_basket_price': 20}
        self.__product_and_basket_condition_policy = ConditionalDiscountPolicy(50, dis_details, pre_con__details)

    def test_is_worthy_product_cond(self):
        # All valid
        self.assertTrue(self.__product_condition_policy.is_worthy(3, 0, ['Eytan']))
        self.assertTrue(self.__product_condition_policy.is_worthy(3, 21, ['Eytan']))
        self.assertTrue(self.__product_condition_policy.is_worthy(3, 21, ['Eytan', "Anna"]))

        # All valid - not worthy
        self.assertFalse(self.__product_condition_policy.is_worthy(1, 2, ['Eytan']))
        self.assertFalse(self.__product_condition_policy.is_worthy(3, 2, []))
        self.assertFalse(self.__product_condition_policy.is_worthy(1, 2, []))

        # All valid - edge case
        self.assertTrue(self.__product_condition_policy.is_worthy(2, 20, ['Eytan']))

    def test_get_price_after_discount_product_cond(self):
        result = self.__product_condition_policy.get_price_after_discount(12)
        self.assertEqual(result, 12-0.3)

    def test_is_worthy_basket_cond(self):
        # All valid
        self.assertTrue(self.__basket_condition_policy.is_worthy(0, 21, []))
        self.assertTrue(self.__basket_condition_policy.is_worthy(1, 21, []))
        self.assertTrue(self.__basket_condition_policy.is_worthy(0, 21, ['Eytan']))

        # All valid - not worthy
        self.assertFalse(self.__basket_condition_policy.is_worthy(0, 2, []))
        self.assertFalse(self.__basket_condition_policy.is_worthy(1, 2, []))
        self.assertFalse(self.__basket_condition_policy.is_worthy(0, 2, ['Eytan']))

        # All valid - edge case
        self.assertTrue(self.__basket_condition_policy.is_worthy(0, 20, []))
        self.assertTrue(self.__basket_condition_policy.is_worthy(1, 20, []))
        self.assertTrue(self.__basket_condition_policy.is_worthy(0, 20, ['Eytan']))

    def test_get_price_after_discount_basket_cond(self):
        result = self.__basket_condition_policy.get_price_after_discount(12)
        self.assertAlmostEqual(result, 12-0.6)

    def test_is_worthy__product_and_basket_cond(self):
        # All valid
        self.assertTrue(self.__product_and_basket_condition_policy.is_worthy(3, 21, ['Eytan']))
        self.assertTrue(self.__product_and_basket_condition_policy.is_worthy(3, 21, ['Eytan', "Anna"]))
        self.assertTrue(self.__product_and_basket_condition_policy.is_worthy(10, 21, ['Eytan']))

        # All valid - not worthy
        self.assertFalse(self.__product_and_basket_condition_policy.is_worthy(3, 2, ['Eytan']))
        self.assertFalse(self.__product_and_basket_condition_policy.is_worthy(1, 21, ['Eytan']))
        self.assertFalse(self.__product_and_basket_condition_policy.is_worthy(3, 21, ['Anna']))

        # All valid - edge case
        self.assertTrue(self.__product_and_basket_condition_policy.is_worthy(2, 20, ['Eytan']))

    def test_get_price_after_discount_product_and_basket_cond(self):
        result = self.__product_and_basket_condition_policy.get_price_after_discount(12)
        self.assertEqual(result, 6)

    def tearDown(self) -> None:
        pass


if __name__ == '__main__':
    unittest.main()
