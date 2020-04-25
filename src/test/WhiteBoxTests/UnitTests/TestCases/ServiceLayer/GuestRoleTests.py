import unittest
# from src.main.DomainLayer.TradeControl import TradeControl as TC
from src.main.DomainLayer.Store import Store
from src.main.DomainLayer.User import User
from src.main.DomainLayer.TradeControl import TradeControl
from src.main.ServiceLayer.GuestRole import GuestRole
from datetime import datetime as date_time

from src.test.WhiteBoxTests.UnitTests.Stubs.StubTradeControl import StubTradeControl


class GuestRoleTest(unittest.TestCase):

    def setUp(self) -> None:
        eytan = User()
        eytan.register("eytan", "isTheBest")
        self.__user = eytan
        #self.__tc = StubTradeControl()
        self.__store_name = "Eytan's best store"
        self.__store = Store(self.__store_name)
        self.__store.add_product("Eytan's Product", 100, "Eytan Category", 5)
        self.__store.add_product("not Eytan's Product", 10, "Eytan Category", 2)
        (TradeControl.get_instance()).get_stores().insert(0, self.__store)

    def test_calculate_purchase_price_direct_approach(self):
        # All valid
        amount_per_product = [["Eytan's Product", 4], ["not Eytan's Product", 1]]
        result = GuestRole.calculate_purchase_price_direct_approach(self.__store_name, amount_per_product,
                                                                    self.__user.get_nickname())
        self.assertEqual(result, 410)

        # store name not valid
        result = GuestRole.calculate_purchase_price_direct_approach("Eytan's worst store", amount_per_product,
                                                                    self.__user.get_nickname())
        self.assertEqual(result, -1)

        # amount_per_product name not valid
        result = GuestRole.calculate_purchase_price_direct_approach(self.__store_name, [],
                                                                    self.__user.get_nickname())
        self.assertEqual(result, -1)

    def test_calculate_purchase_price_walkaround_approach(self):
        amount_per_product_per_store = [[self.__store_name, "Eytan's Product", 4], [self.__store_name,
                                                                                    "not Eytan's Product", 1]]
        # All valid
        result = GuestRole.calculate_purchase_price_walkaround_approach(amount_per_product_per_store,
                                                                        self.__user.get_nickname())
        self.assertEqual(result, 410)

        # Only first store valid valid
        result = GuestRole.calculate_purchase_price_walkaround_approach([[self.__store_name, "Eytan's Product", 4],
                                                                        [self.__store_name, "not Eytan's Product", 20]],
                                                                        self.__user.get_nickname())
        self.assertEqual(result, 400)

        # store name not valid
        result = GuestRole.calculate_purchase_price_walkaround_approach([["Eytan's worst store", "Eytan's Product", 4]],
                                                                        self.__user.get_nickname())
        self.assertEqual(result, -1)

    def test_make_purchase(self):
        amount_per_product = [["Eytan's Product", 4], ["not Eytan's Product", 1]]
        # All valid
        result = GuestRole.make_purchase(self.__store, amount_per_product,
                                         self.__user.get_nickname())
        self.assertNotEqual(result, 0)

        # amount_per_product name not valid
        result = GuestRole.make_purchase(self.__store, [],
                                         self.__user.get_nickname())
        self.assertEqual(result, -1)

    def test_accepted_price_purchase(self):
        # All valid
        date = date_time(2021, 4, 19)
        result = GuestRole.accepted_price_purchase(self.__user.get_nickname(), 12.0, ["4230014", date])

        # self.assertTrue(result)

        # username not valid
        result = GuestRole.accepted_price_purchase("Trilala",12.0,
                                                   ["4230014", date])
        self.assertFalse(result)

        # price not valid
        result = GuestRole.accepted_price_purchase(self.__user.get_nickname(), -99.0,
                                                   ["4230014", date])
        self.assertFalse(result)

        # card not valid
        result = GuestRole.accepted_price_purchase("self.__user.get_nickname()", 12.0,
                                                   ["4230014", date])
        self.assertFalse(result)

        # date not valid
        result = GuestRole.accepted_price_purchase(self.__user.get_nickname(), 12.0,
                                                   ["4230014", date_time(1999, 4, 19)])
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
