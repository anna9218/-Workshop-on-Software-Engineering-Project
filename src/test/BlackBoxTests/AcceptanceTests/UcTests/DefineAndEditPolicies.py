"""
    uc 4.2 - define and update purchase and discount policies
"""
import jsonpickle
import datetime
from src.test.BlackBoxTests.AcceptanceTests.ProjectTest import ProjectTest


class DefineAndUpdatePolicies(ProjectTest):
    def setUp(self) -> None:
        super().setUp()
        self.__dates: [dict] = [jsonpickle.encode(datetime.date.today())]
        self.register_user(self._username, self._password)
        self.login(self._username, self._password)
        self.open_store(self._store_name)
        self.add_products_to_store(self._store_name,
                                   [{"name": "product1", "price": 10, "category": "general", "amount": 10},
                                    {"name": "product2", "price": 5, "category": "general", "amount": 10}])

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

        # ------------ discount policy ------------
        # .......... add policy + valid input ..........

        # .......... update policy + valid input ..........
        pass

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
