"""
        purchase composite class - executes child operation for purchase component interface
"""
from datetime import datetime, timedelta
import unittest

from src.main.DomainLayer.StoreComponent.PurchasePolicyComposite.PurchasePolicy import PurchasePolicy


class PurchasePolicyTests(unittest.TestCase):

    def setUp(self):
        self.policy_composite = PurchasePolicy()
        self.curr_date = datetime.today()
        self.yesterday = timedelta(days=1)

    def test_can_purchase(self):
        self.policy_composite.add_purchase_policy({"name": "policy1", "products": ["product1", "product2"],
                                                   "min_amount": 3, "max_amount": 10})

        # valid purchase
        res = self.policy_composite.can_purchase([{"product_name": "product1", "amount": 8}], self.curr_date)
        self.assertTrue(res)

        # amount exceeding max
        res = self.policy_composite.can_purchase([{"product_name": "product1", "amount": 13}], self.curr_date)
        self.assertFalse(res)

        # amount lower than min
        res = self.policy_composite.can_purchase([{"product_name": "product1", "amount": 1}], self.curr_date)
        self.assertFalse(res)

    def test_add_purchase_policy(self):
        # valid details
        res = self.policy_composite.add_purchase_policy({"name": "policy1", "products": ["product1", "product2"],
                                                   "min_amount": 3, "max_amount": 10})
        self.assertTrue(res["response"])

        # min amount bigger than max
        res = self.policy_composite.add_purchase_policy({"name": "policy2", "products": ["product1", "product2"],
                                                   "min_amount": 13, "max_amount": 10})
        self.assertFalse(res["response"])

        # no policy rules
        res = self.policy_composite.add_purchase_policy({"name": "policy2", "products": ["product1", "product2"]})
        self.assertFalse(res["response"])

        # no products
        res = self.policy_composite.add_purchase_policy({"name": "policy2", "min_amount": 3, "max_amount": 10})
        self.assertFalse(res["response"])

        # no policy name set
        res = self.policy_composite.add_purchase_policy({"products": ["product1", "product2"], "min_amount": 3,
                                                         "max_amount": 10})
        self.assertFalse(res["response"])

    def test_equals(self):
        self.policy_composite.set_name("policy1")

        # equal
        res = self.policy_composite.equals({"name": "policy1"})
        self.assertTrue(res)

        # not equal
        res = self.policy_composite.equals({"name": "policy3"})
        self.assertFalse(res)

    def test_get_details(self):
        # no policies set
        res = self.policy_composite.get_details()
        self.assertTrue(len(res) == 0)

        # existing policy
        self.policy_composite.add_purchase_policy({"name": "policy1", "products": ["product1", "product2"],
                                                   "min_amount": 3, "max_amount": 10})
        res = self.policy_composite.get_details()
        self.assertTrue(len(res) > 0)

    def test_update(self):
        # valid update
        """ {"name": str, "products": [str], "min_amount": int or None, "max_amount": int or None,
                               "dates": [dict] or None, "bundle": bool or None} """
        res = self.policy_composite.update({"name": "policy1", "products": ["product1", "product2"], "min_amount": 5})
        self.assertTrue(res["response"])

        res = self.policy_composite.update({"name": "policy1", "products": ["product1", "product2"], "max_amount": 15})
        self.assertTrue(res["response"])

        # min amount bigger than max
        res = self.policy_composite.update({"name": "policy1", "products": ["product1", "product2"], "min_amount": 10,
                                            "max_amount": 5})
        self.assertFalse(res["response"])

    def __repr__(self):
        return repr("PurchasePolicyTests")
