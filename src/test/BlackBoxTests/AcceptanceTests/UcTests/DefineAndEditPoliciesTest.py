"""
    uc 4.2 - define and update purchase and discount policies
"""
import jsonpickle
from datetime import datetime, date
from src.test.BlackBoxTests.AcceptanceTests.ProjectAT import ProjectAT


class DefineAndUpdatePoliciesTest(ProjectAT):
    def setUp(self) -> None:
        super().setUp()
        self.__dates: [dict] = [jsonpickle.encode(date.today())]
        self.register_user(self._username, self._password)
        self.login(self._username, self._password)
        self.open_store(self._store_name)
        self.add_products_to_store(self._store_name,
                                   [{"name": "product1", "price": 10, "category": "general", "amount": 10,
                                     "purchase_type": 0, "discount_type": 0},
                                    {"name": "product2", "price": 5, "category": "general", "amount": 10,
                                     "purchase_type": 0, "discount_type": 0}])
        self.__later_date = datetime(2021, 8, 21)

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
        result = self.define_discount_policy(self._store_name, 10, self.__later_date,
                                             {'name': "policy1", 'product': "product1"},
                                             {'product': 'product1', 'min_amount': 3, 'min_basket_price': None})
        self.assertTrue(result)

        result = self.define_discount_policy(self._store_name, 10, self.__later_date,
                                             {'name': "policy2", 'product': "product1"}, None)
        self.assertTrue(result)

        # .......... update policy + valid input ..........
        result = self.update_discount_policy(self._store_name, "policy1", 3)
        self.assertTrue(result)

        result = self.update_discount_policy(self._store_name, "policy1", discount_precondition={'product': "product2",
                                                                                                 'min_amount': None,
                                                                                                 'min_basket_price':
                                                                                                     None})
        self.assertTrue(result)

        result = self.update_discount_policy(self._store_name, "policy2", 5)
        self.assertTrue(result)

        # ------------ composite discount policies ------------
        result = self.define_composite_policy(self._store_name, "policy1", "policy2", "xor", 2.5, "p1_xor_p2",
                                              self.__later_date)
        self.assertTrue(result)

        # .......... update composite policy + valid input ..........
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

        # ------------ discount policy ---------------------------------------------------------------------------------
        # add two good simple policies.
        self.define_discount_policy(self._store_name, 10, self.__later_date, {'name': "policy1", 'product': "product1"},
                                    {'product': 'product1', 'min_amount': 3, 'min_basket_price': None})
        self.define_discount_policy(self._store_name, 10, self.__later_date, {'name': "policy2", 'product': "product1"},
                                    None)
        # .......... add policy ..........
        # already existing policy
        result = self.define_discount_policy(self._store_name, 10, self.__later_date,
                                             {'name': "policy1", 'product': "product1"},
                                             {'product': 'product1', 'min_amount': 3, 'min_basket_price': None})
        self.assertFalse(result)

        result = self.define_discount_policy(self._store_name, 10, self.__later_date,
                                             {'name': "policy2", 'product': "product1"},
                                             None)
        self.assertFalse(result)

        # Illegal product
        result = self.define_discount_policy(self._store_name, 10, self.__later_date,
                                             {'name': "pol1", 'product': "product11"},
                                             {'product': 'product1', 'min_amount': 3, 'min_basket_price': None})
        self.assertFalse(result)

        result = self.define_discount_policy(self._store_name, 10, self.__later_date,
                                             {'name': "pol2", 'product': "product11"},
                                             None)
        self.assertFalse(result)

        # Illegal percentage
        result = self.define_discount_policy(self._store_name, -10, self.__later_date,
                                             {'name': "pol1", 'product': "product1"},
                                             {'product': 'product1', 'min_amount': 3, 'min_basket_price': None})
        self.assertFalse(result)

        result = self.define_discount_policy(self._store_name, 1090, self.__later_date,
                                             {'name': "pol2", 'product': "product1"},
                                             None)
        self.assertFalse(result)

        # Illegal pre condition
        result = self.define_discount_policy(self._store_name, 10, self.__later_date,
                                             {'name': "pol1", 'product': "product1"},
                                             {'product': 'product11', 'min_amount': 3, 'min_basket_price': None})
        self.assertFalse(result)

        result = self.define_discount_policy(self._store_name, 10, self.__later_date,
                                             {'name': "pol1", 'product': "product1"},
                                             {'product': 'product1', 'min_amount': -9, 'min_basket_price': None})
        self.assertFalse(result)

        result = self.define_discount_policy(self._store_name, 10, self.__later_date,
                                             {'name': "pol1", 'product': "product1"},
                                             {'product': 'product1', 'min_amount': 3, 'min_basket_price': -10.7})
        self.assertFalse(result)

        # illegal valid date
        result = self.define_discount_policy(self._store_name, 10, datetime(202, 2, 20),
                                             {'name': "pol1", 'product': "product1"},
                                             {'product': 'product1', 'min_amount': 3, 'min_basket_price': -10.7})
        self.assertFalse(result)

        # .......... update policy ..........
        # illegal percentage
        result = self.update_discount_policy(self._store_name, "policy1", -3.3)
        self.assertFalse(result)

        result = self.update_discount_policy(self._store_name, "policy2", -5.7)
        self.assertFalse(result)

        # illegal policy name
        result = self.update_discount_policy(self._store_name, "policy11", 3.3)
        self.assertFalse(result)

        result = self.update_discount_policy(self._store_name, "", 5.7)
        self.assertFalse(result)

        # illegal percentage
        result = self.update_discount_policy("self._store_name", "policy1", 3.3)
        self.assertFalse(result)

        result = self.update_discount_policy("self._store_name", "policy2", 5.7)
        self.assertFalse(result)

        # illegal new_name
        result = self.update_discount_policy(self._store_name, "policy1", discount_details={'name': "policy2",
                                                                                            'product': None})
        self.assertFalse(result)

        result = self.update_discount_policy(self._store_name, "policy2", discount_details={'name': "",
                                                                                            'product': None})
        self.assertFalse(result)

        # illegal new product
        result = self.update_discount_policy(self._store_name, "policy1", discount_details={'name': None,
                                                                                            'product': "all2"})
        self.assertFalse(result)

        result = self.update_discount_policy(self._store_name, "policy2", discount_details={'name': None,
                                                                                            'product': "None"})
        self.assertFalse(result)

        # illegal precondition
        result = self.update_discount_policy(self._store_name, "policy1", discount_precondition={'product': "",
                                                                                                 'min_amount': None,
                                                                                                 'min_basket_price':
                                                                                                     None})
        self.assertFalse(result)

        result = self.update_discount_policy(self._store_name, "policy1", discount_precondition={'product': "product1",
                                                                                                 'min_amount': -1,
                                                                                                 'min_basket_price':
                                                                                                     None})
        self.assertFalse(result)

        result = self.update_discount_policy(self._store_name, "policy1", discount_precondition={'product': "product1",
                                                                                                 'min_amount': None,
                                                                                                 'min_basket_price':
                                                                                                     -1})
        self.assertFalse(result)

        # illegal valid date
        result = self.update_discount_policy(self._store_name, "policy1", valid_util=datetime(2020, 2, 20))
        self.assertFalse(result)

        # Composite policy

        # add policies
        # illegal sub-policies.
        result = self.define_composite_policy(self._store_name, "policy11", "policy2", "xor", 2.5, "p1_xor_p2",
                                              self.__later_date)
        self.assertFalse(result)

        # illegal flag.
        result = self.define_composite_policy(self._store_name, "policy1", "policy2", "xand", 2.5, "p1_xor_p2",
                                              self.__later_date)
        self.assertFalse(result)

        # illegal percentage.
        result = self.define_composite_policy(self._store_name, "policy1", "policy2", "xor", -2.5, "p1_xor_p2",
                                              self.__later_date)
        self.assertFalse(result)

        # illegal flag.
        result = self.define_composite_policy(self._store_name, "policy1", "policy2", "xor", 2.5, "policy1",
                                              self.__later_date)
        self.assertFalse(result)

        # creating good composite policy
        self.define_composite_policy(self._store_name, "policy1", "policy2", "xor", 2.5, "p1_xor_p2",
                                     self.__later_date)

        # update policy
        # illegal percentage
        result = self.update_discount_policy(self._store_name, "p1_xor_p2", -4)
        self.assertFalse(result)

        # illegal store
        result = self.update_discount_policy("self._store_name", "p1_xor_p2", 4)
        self.assertFalse(result)

        # illegal policy
        result = self.update_discount_policy(self._store_name, "p1xor_p2", 4)
        self.assertFalse(result)

        # illegal new name
        result = self.update_discount_policy(self._store_name, "p1xor_p2", 4,
                                             discount_details={'name': "", 'product': 'all'})
        self.assertFalse(result)

        # illegal new product
        result = self.update_discount_policy(self._store_name, "p1xor_p2", 4,
                                             discount_details={'name': "new_policy", 'product': 'all2'})
        self.assertFalse(result)

        # illegal valid date
        result = self.update_discount_policy(self._store_name, "p1xor_p2", 4,
                                             valid_util=datetime(2020, 2, 2))
        self.assertFalse(result)

    def tearDown(self) -> None:
        self.remove_products_from_store(self._store_name, ["product1", "product2"])
        self.remove_store(self._store_name)
        self.delete_user(self._username)

    def __repr__(self):
        return repr("DefineAndUpdatePolicies")
