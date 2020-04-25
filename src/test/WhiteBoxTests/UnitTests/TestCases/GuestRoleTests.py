import unittest
# from src.main.DomainLayer.TradeControl import TradeControl as TC
from src.main.DomainLayer.User import User
from src.main.DomainLayer.TradeControl import TradeControl
from src.main.ServiceLayer.GuestRole import GuestRole
from src.test.WhiteBoxTests.UnitTests.Stubs.StubStore import StubStore
from datetime import datetime as date_time


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        eytan = User()
        eytan.register("eytan", "isTheBest")
        self.__user = eytan
        self.__store_name = "Eytan's best store"
        stub_store = StubStore()
        (TradeControl.get_instance()).get_stores().insert(0, stub_store)
        self.__amount_per_product = list([{'product': "A", 'amount': 10}])
        self.__amount_per_product_per_store = list([{'product': "A", 'amount': 10, 'store': "Eytan's best store"}])

    def test_calculate_purchase_price_direct_approach(self):
        # All valid
        result = GuestRole.calculate_purchase_price_direct_approach(self.__store_name, self.__amount_per_product,
                                                                    self.__user.get_nickname())
        self.assertNotEqual(result, 0)

        # store name not valid
        result = GuestRole.calculate_purchase_price_direct_approach("1", self.__amount_per_product,
                                                                    self.__user.get_nickname())
        self.assertEqual(result, -1)

        # amount_per_product name not valid
        result = GuestRole.calculate_purchase_price_direct_approach(self.__store_name, [],
                                                                    self.__user.get_nickname())
        self.assertEqual(result, -1)

    def test_calculate_purchase_price_walkaround_approach(self):
        # All valid
        result = GuestRole.calculate_purchase_price_walkaround_approach(self.__amount_per_product_per_store,
                                                                        self.__user.get_nickname())
        self.assertNotEqual(result, 0)

        # store name not valid
        result = GuestRole.calculate_purchase_price_walkaround_approach([],
                                                                        self.__user.get_nickname())
        self.assertEqual(result, -1)

    def test_make_purchase(self):
        # All valid
        result = GuestRole.make_purchase(StubStore(), self.__amount_per_product,
                                         self.__user.get_nickname())
        self.assertNotEqual(result, 0)

        # store not valid
        result = GuestRole.make_purchase(StubStore(), self.__amount_per_product,
                                         self.__user.get_nickname())
        self.assertEqual(result, -1)

        # amount_per_product name not valid
        result = GuestRole.make_purchase(StubStore(), [],
                                         self.__user.get_nickname())
        self.assertEqual(result, -1)

    def test_accepted_price_purchase(self):
        # All valid
        date = date_time(2021, 4, 19)
        result = GuestRole.accepted_price_purchase(self.__user.get_nickname(), 12.0, {"4230014", date})

        self.assertTrue(result)

        # username not valid
        result = GuestRole.accepted_price_purchase("Trilala",12.0,
                                                   {"4230014", date})
        self.assertFalse(result)

        # price not valid
        result = GuestRole.accepted_price_purchase(self.__user.get_nickname(), -99.0,
                                                   {"4230014", date})
        self.assertFalse(result)

        # card not valid
        result = GuestRole.accepted_price_purchase("self.__user.get_nickname()", 12.0,
                                                   {12, date})
        self.assertFalse(result)

        # date not valid
        result = GuestRole.accepted_price_purchase(self.__user.get_nickname(), 12.0,
                                                   {"4230014", date_time(2012, 12, 12)})
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
