import unittest
# from src.main.DomainLayer.TradeControl import TradeControl as TC
from src.Logger import logger
from src.main.DomainLayer.Purchase import Purchase
from src.main.DomainLayer.Store import Store
from src.main.DomainLayer.User import User
from src.main.DomainLayer.TradeControl import TradeControl
from src.main.ServiceLayer.GuestRole import GuestRole
from datetime import datetime as date_time


class GuestRoleTest(unittest.TestCase):

    @logger
    def setUp(self) -> None:
        eytan = User()
        eytan.register("eytan", "isTheBest")
        self.__user = eytan
        self.__store_name = "Eytan's best store"
        self.__store = Store(self.__store_name)
        self.__store.add_product("Eytan's Product", 100, "Eytan Category", 5)
        self.__store.add_product("not Eytan's Product", 10, "Eytan Category", 2)
        (TradeControl.get_instance()).get_stores().insert(0, self.__store)
        self.__guest_role = GuestRole()

    @logger
    def test_calculate_purchase_price_direct_approach(self):
        # All valid
        amount_per_product = [["Eytan's Product", 4], ["not Eytan's Product", 1]]
        result = self.__guest_role.calculate_purchase_price_direct_approach(self.__store_name, amount_per_product,
                                                                            self.__user.get_nickname())
        self.assertEqual(result, 410)

        # store name not valid
        result = self.__guest_role.calculate_purchase_price_direct_approach("Eytan's worst store", amount_per_product,
                                                                            self.__user.get_nickname())
        self.assertEqual(result, -1)

        # amount_per_product name not valid
        result = self.__guest_role.calculate_purchase_price_direct_approach(self.__store_name, [],
                                                                            self.__user.get_nickname())
        self.assertEqual(result, -1)

    @logger
    def test_calculate_purchase_price_walkaround_approach(self):
        amount_per_product_per_store = [[self.__store_name, [["Eytan's Product", 4], ["not Eytan's Product", 1]]]]
        # All valid
        result = self.__guest_role.calculate_purchase_price_walkaround_approach(amount_per_product_per_store,
                                                                                self.__user.get_nickname())
        self.assertEqual(result, 410)

        # Only first store valid valid
        result = self.__guest_role.calculate_purchase_price_walkaround_approach(
            [[self.__store_name, [["Eytan's Product", 4],
             ["not Eytan's Product", 20]]]],
            self.__user.get_nickname())

        self.assertEqual(result, -1)

        # store name not valid
        result = self.__guest_role.calculate_purchase_price_walkaround_approach([["Eytan's worst store",
                                                                                 [["Eytan's Product", 4]]]],
                                                                                self.__user.get_nickname())
        self.assertEqual(result, -1)

    @logger
    def test_make_purchase(self):
        amount_per_product = [["Eytan's Product", 4], ["not Eytan's Product", 1]]
        # All valid
        result: Purchase = self.__guest_role.make_purchase(self.__store, amount_per_product,
                                                           self.__user.get_nickname())
        self.assertEqual(result.get_price(), 410)

        # amount_per_product name not valid
        result = self.__guest_role.make_purchase(self.__store, [],
                                                 self.__user.get_nickname())
        self.assertIsNone(result)

    @logger
    def test_accepted_price_purchase(self):
        purchase: Purchase = Purchase((TradeControl.get_instance()).get_next_purchase_id(),
                                      [["Eytan's Product", 4], ["not Eytan's Product", 1]],
                                      410, self.__store_name, self.__user.get_nickname())
        self.__user.add_unaccepted_purchase(purchase)
        # All valid
        date = date_time(2021, 4, 19)
        result = self.__guest_role.accepted_price_purchase(purchase, ["4230014", date])

        # self.assertTrue(result)

        # card not valid
        result = self.__guest_role.accepted_price_purchase(purchase, ["4230014", date])
        self.assertFalse(result)

        # date not valid
        result = self.__guest_role.accepted_price_purchase(purchase, ["4230014", date_time(1999, 4, 19)])
        self.assertFalse(result)

    def __repr__(self):
        return repr ("GuestRoleTest")

if __name__ == '__main__':
    unittest.main()
