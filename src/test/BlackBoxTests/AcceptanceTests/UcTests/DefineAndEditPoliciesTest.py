"""
    uc 4.2 - define and update purchase and discount policies
"""
import jsonpickle
import datetime
from src.test.BlackBoxTests.AcceptanceTests.ProjectAT import ProjectAT


class DefineAndUpdatePoliciesTest(ProjectAT):
    def setUp(self) -> None:
        super().setUp()
        self.__dates: [dict] = [jsonpickle.encode(datetime.date.today())]
        self.register_user(self._username, self._password)
        self.login(self._username, self._password)
        self.open_store(self._store_name)
        self.add_products_to_store(self._store_name,
                                   [{"name": "product1", "price": 10, "category": "general", "amount": 10,
                                     "purchase_type": 0, "discount_type": 0},
                                    {"name": "product2", "price": 5, "category": "general", "amount": 10,
                                     "purchase_type": 0, "discount_type": 0}])

    def test_success(self):
        # ------------ purchase policy options -----------
        # .......... add policy + valid input ..........
        res = self.define_purchase_policy(self._store_name,
                                          {"name": "policy1", "products": ["product1"],
                                           "dates": self.__dates, "min_amount": 2, "max_amount": 3})
        self.assertTrue(res)
        # .......... update policy + valid input ..........
        res = self.update_purchase_policy(self._store_name,
                                          {"name": "policy1", "products": ["product1"], "min_amount": 1,
                                           "max_amount": 13})
        self.assertTrue(res)

        # ------------ simple discount policies ------------
        # .......... add policy + valid input ..........
        result = self.define_discount_policy(self._store_name, 10, {'name': "policy1", 'product': "product1"},
                                             {'product': 'product1', 'min_amount': 3, 'min_basket_price': None})
        self.assertTrue(result)

        result = self.define_discount_policy(self._store_name, 10, {'name': "policy2", 'product': "product1"},
                                             None)
        self.assertTrue(result)

        # .......... update policy + valid input ..........
        result = self.update_discount_policy(self._store_name, "policy1", 3)
        self.assertTrue(result)

        result = self.update_discount_policy(self._store_name, "policy2", 5)
        self.assertTrue(result)

        # ------------ composite discount policies ------------
        result = self.define_composite_policy(self._store_name, "policy1", "policy2", "xor", 2.5, "p1_xor_p2")
        self.assertTrue(result)

        # .......... add policy + valid input ..........
        result = self.update_discount_policy(self._store_name, "p1_xor_p2", 7.5)
        self.assertTrue(result)

    def test_fail(self):
        # ------------ purchase policy options ------------
        # .......... add policy ..........
        # store doesn't exist
        res = self.define_purchase_policy("anotherStoreName",
                                          {"name": "policy1", "products": ["product1"],
                                           "dates": self.__dates, "min_amount": 2, "max_amount": 3})

        self.assertFalse(res)
        # no products defined
        res = self.define_purchase_policy(self._store_name,
                                          {"name": "policy1", "dates": self.__dates,
                                           "min_amount": 2, "max_amount": 3})
        self.assertFalse(res)
        # no policy details given
        res = self.define_purchase_policy(self._store_name,
                                          {"name": "policy1", "products": ["product1"]})
        self.assertFalse(res)
        # policy name missing
        res = self.define_purchase_policy(self._store_name,
                                          {"products": ["product1"], "dates": self.__dates,
                                           "min_amount": 2, "max_amount": 3})
        self.assertFalse(res)
        # policy already exists with given name
        self.define_purchase_policy(self._store_name,
                                    {"name": "policy1", "products": ["product1"],
                                     "dates": self.__dates})
        res = self.define_purchase_policy(self._store_name,
                                          {"name": "policy1", "products": ["product1"], "max_amount": 3})
        self.assertFalse(res)

        # .......... update policy ..........
        # store doesn't exist
        res = self.update_purchase_policy("anotherStoreName",
                                          {"name": "policy1", "products": ["product1"], "min_amount": 1,
                                           "max_amount": 13})
        self.assertFalse(res)
        # policy doesn't exist
        res = self.update_purchase_policy(self._store_name,
                                          {"name": "policy9", "products": ["product1"], "min_amount": 1,
                                           "max_amount": 13})
        self.assertFalse(res)
        # no details given to update
        res = self.update_purchase_policy(self._store_name,
                                          {"name": "policy1"})
        self.assertFalse(res)

        # ------------ discount policy ------------
        # .......... add policy ..........

        # .......... update policy ..........
        pass

    def tearDown(self) -> None:
        self.remove_products_from_store(self._store_name, ["product1", "product2"])
        self.remove_store(self._store_name)
        self.delete_user(self._username)

    def __repr__(self):
        return repr("DefineAndUpdatePolicies")
