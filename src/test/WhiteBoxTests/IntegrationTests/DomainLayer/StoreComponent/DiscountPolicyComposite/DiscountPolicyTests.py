import unittest
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
        pre_con__details = {'product': "Eytan", 'min_amount': 2, 'min_basket_price': None}
        self.__leaf_pol1 = ConditionalDiscountPolicy(2.5, dis_details, pre_con__details)
        dis_details = {'name': "p2", 'product': "Eytan"}
        pre_con__details = {'product': "all", 'min_amount': None, 'min_basket_price': 1}
        self.__leaf_pol2 = ConditionalDiscountPolicy(5, dis_details, pre_con__details)
        self.__policy = DiscountPolicy(jsonpickle.encode(self.__leaf_pol1), jsonpickle.encode(self.__leaf_pol2),
                                       CompositeFlag.XOR, 10, "Comp_Pol")

    def test_is_worthy(self):
        # (amount, basket_price, prod_lst)
        result = self.__policy.is_worthy(1, 3, ["Eytan"])
        self.assertTrue(result)

        result = self.__policy.is_worthy(3, 0, ["Eytan"])
        self.assertTrue(result)

        result = self.__policy.is_worthy(2, 3, ["Eytan"])
        self.assertFalse(result)

    def tearDown(self) -> None:
        pass


if __name__ == '__main__':
    unittest.main()