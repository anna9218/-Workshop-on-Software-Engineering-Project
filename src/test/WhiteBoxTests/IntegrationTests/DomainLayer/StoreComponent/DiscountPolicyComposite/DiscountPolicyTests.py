import unittest
from datetime import datetime

import jsonpickle
from src.main.DomainLayer.StoreComponent.DiscountPolicyComposite.DiscountPolicy import DiscountPolicy, DiscountType, \
    DiscountComponent, CompositeFlag
from src.main.DomainLayer.StoreComponent.DiscountPolicyComposite.Leaves.ConditionalDiscountPolicy import \
    ConditionalDiscountPolicy
from src.main.DomainLayer.StoreComponent.DiscountPolicyComposite.Leaves.VisibleDiscountPolicy import \
    VisibleDiscountPolicy


class DiscountPolicyTests(unittest.TestCase):

    def setUp(self) -> None:
        dis_details = {'name': "p1", 'product': "Eytan"}
        later_date = datetime(2021, 8, 21)
        pre_con__details = {'product': "Eytan", 'min_amount': 2, 'min_basket_price': None}
        self.__leaf_pol1 = ConditionalDiscountPolicy(2.5, later_date, dis_details, pre_con__details)
        dis_details = {'name': "p2", 'product': "Eytan"}
        pre_con__details = {'product': "all", 'min_amount': None, 'min_basket_price': 1}
        self.__leaf_pol2 = ConditionalDiscountPolicy(5, later_date, dis_details, pre_con__details)
        self.__xor_policy = DiscountPolicy(jsonpickle.encode(self.__leaf_pol1), jsonpickle.encode(self.__leaf_pol2),
                                           CompositeFlag.XOR, 10, "Comp__Xor_Pol", later_date)
        self.__or_policy = DiscountPolicy(jsonpickle.encode(self.__leaf_pol1), jsonpickle.encode(self.__leaf_pol2),
                                          CompositeFlag.OR, 9, "Comp__Or_Pol", later_date)
        self.__and_policy = DiscountPolicy(jsonpickle.encode(self.__leaf_pol1), jsonpickle.encode(self.__leaf_pol2),
                                           CompositeFlag.AND, 8, "Comp_And_Pol", later_date)

    def test_is_worthy(self):
        # Xor tests
        result = self.__xor_policy.is_worthy(1, 3, ["Eytan"])
        self.assertTrue(result)

        result = self.__xor_policy.is_worthy(3, 0, ["Eytan"])
        self.assertTrue(result)

        result = self.__xor_policy.is_worthy(2, 3, ["Eytan"])
        self.assertFalse(result)

        result = self.__xor_policy.is_worthy(1, 0, ["Eytan"])
        self.assertFalse(result)

        # Or tests
        result = self.__or_policy.is_worthy(1, 3, ["Eytan"])
        self.assertTrue(result)

        result = self.__or_policy.is_worthy(3, 0, ["Eytan"])
        self.assertTrue(result)

        result = self.__or_policy.is_worthy(2, 3, ["Eytan"])
        self.assertTrue(result)

        result = self.__or_policy.is_worthy(1, 0, ["Eytan"])
        self.assertFalse(result)

        # And tests
        result = self.__and_policy.is_worthy(1, 3, ["Eytan"])
        self.assertFalse(result)

        result = self.__and_policy.is_worthy(3, 0, ["Eytan"])
        self.assertFalse(result)

        result = self.__and_policy.is_worthy(2, 3, ["Eytan"])
        self.assertTrue(result)

        result = self.__and_policy.is_worthy(1, 0, ["Eytan"])
        self.assertFalse(result)

    def tearDown(self) -> None:
        pass


if __name__ == '__main__':
    unittest.main()
