import unittest
from datetime import datetime, timedelta
import jsonpickle
from src.main.DomainLayer.StoreComponent.PurchasePolicyComposite.Leaves.ProhibitedDatePolicy import ProhibitedDatePolicy


class ProhibitedDatePolicyTests(unittest.TestCase):

    def setUp(self):
        self.product_ls = ["product1", "product2"]
        self.curr_date = datetime.today()
        self.yesterday = jsonpickle.encode(timedelta(days=1))
        self.dates = [jsonpickle.encode(self.curr_date)]

    def test_can_purchase(self):
        # valid purchase
        policy = ProhibitedDatePolicy([], self.product_ls)
        res = policy.can_purchase([{"product_name": "product1"}], self.curr_date)
        self.assertTrue(res)

        # invalid purchase
        policy = ProhibitedDatePolicy(self.dates, self.product_ls)
        res = policy.can_purchase([{"product_name": "product1"}], self.curr_date)
        self.assertFalse(res)

    def test_equals(self):
        policy = ProhibitedDatePolicy(self.dates, self.product_ls)

        # equal
        res = policy.equals({"products": self.product_ls, "dates": self.dates})
        self.assertTrue(res)

        # not equal
        res = policy.equals({"products": self.product_ls, "dates": []})
        self.assertFalse(res)

    def test_update(self):
        policy = ProhibitedDatePolicy(self.dates, self.product_ls)

        # valid update
        policy.update({"products": self.product_ls, "dates": [self.yesterday]})
        res = policy.get_dates()
        self.assertTrue(res.__eq__([self.yesterday]))

        # invalid update
        policy.update({"products": self.product_ls, "dates": []})
        res = policy.get_dates()
        self.assertFalse(res.__eq__([]))

