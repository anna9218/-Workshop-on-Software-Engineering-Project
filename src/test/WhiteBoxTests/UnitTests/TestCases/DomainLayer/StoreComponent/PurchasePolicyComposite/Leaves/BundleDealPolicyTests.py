import unittest
from datetime import datetime

from src.main.DomainLayer.StoreComponent.PurchasePolicyComposite.Leaves.BundleDealPolicy import BundleDealPolicy


class BundleDealPolicyTests(unittest.TestCase):

    def setUp(self):
        self.product_ls = ["product1", "product2"]
        self.policy = BundleDealPolicy(self.product_ls)
        self.curr_date = datetime.today()

    def test_can_purchase(self):
        # valid purchase
        res = self.policy.can_purchase([{"product_name": "product1"}, {"product_name": "product2"}], self.curr_date)
        self.assertTrue(res)

        # invalid purchase
        res = self.policy.can_purchase([{"product_name": "product1"}], self.curr_date)
        self.assertFalse(res)

    def test_equals(self):
        # equal
        res = self.policy.equals({"products": self.product_ls, "bundle": True})
        self.assertTrue(res)

        # not equal
        res = self.policy.equals({"products": ["product1"], "bundle": True})
        self.assertFalse(res)

    def test_update(self):
        # valid update
        self.policy.update({"products": ["product1"], "bundle": True})
        res = self.policy.get_products()
        self.assertTrue(len(res) == 1 and res[0] == "product1")

        # invalid update
        self.policy.update({"products": []})
        res = self.policy.get_products()
        self.assertTrue(len(res) == 1)
