import unittest
from datetime import datetime

from src.main.DomainLayer.StoreComponent.PurchasePolicyComposite.Leaves.MaxAmountPolicy import MaxAmountPolicy


class MaxAmountPolicyTests(unittest.TestCase):

    def setUp(self):
        self.product_ls = ["product1", "product2"]
        self.curr_date = datetime.today()
        self.policy = MaxAmountPolicy(10, self.product_ls)

    def test_can_purchase(self):
        # valid purchase
        res = self.policy.can_purchase([{"product_name": "product1", "amount": 5}], self.curr_date)
        self.assertTrue(res)

        # invalid purchase
        res = self.policy.can_purchase([{"product_name": "product1", "amount": 20}], self.curr_date)
        self.assertFalse(res)

    def test_equals(self):
        # equal
        res = self.policy.equals({"products": self.product_ls, "max_amount": 10})
        self.assertTrue(res)

        # not equal
        res = self.policy.equals({"products": self.product_ls, "max_amount": 4})
        self.assertFalse(res)

        res = self.policy.equals({"products": ["product3"], "max_amount": 10})
        self.assertFalse(res)

    def test_update(self):
        # valid update
        self.policy.update({"max_amount": 20, "products": self.product_ls})
        self.assertTrue(self.policy.get_max_amount() == 20)

        # invalid update
        self.policy.update({"products": ["product1"]})
        self.assertTrue(len(self.policy.get_products()) == 2)
