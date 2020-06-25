import concurrent
import threading
import unittest
from datetime import datetime

from src.main.DataAccessLayer.DataAccessFacade import DataAccessFacade
from src.main.DomainLayer.StoreComponent.Store import Store
from src.main.DomainLayer.TradeComponent.TradeControl import TradeControl
from src.main.DomainLayer.UserComponent.User import User
from src.main.ServiceLayer.GuestRole import GuestRole
from src.main.ServiceLayer.StoreOwnerOrManagerRole import StoreOwnerOrManagerRole
from src.main.ServiceLayer.SubscriberRole import SubscriberRole


class ParallelTests(unittest.TestCase):
    def setUp(self):
        super().setUp()
        # variables deceleration
        self.trad: TradeControl = TradeControl.get_instance()
        self.owner_name = 'owner'
        self.user_name = 'user'
        self.password = 'pass'
        self.store = Store('store1')
        self.GuestRole: GuestRole = GuestRole()
        self.SubscriberRole: SubscriberRole = SubscriberRole()
        self.OwnerManagerRole: StoreOwnerOrManagerRole = StoreOwnerOrManagerRole()
        self.products_ls = [{"name": "product", "price": 10, "category": "general", "amount": 11, "purchase_type": 0}]
        self.basket_ls = [{"product_name": self.products_ls[0]['name'], "store_name": self.store.get_name(),
                                                                        "amount": 10}]
        self.date = datetime.now()
        self.payment_details = {'card_number': "123", 'month': "march", 'year': "1991", 'holder': "s",
                                  'ccv': "111", 'id': "333"}
        self.delivery_details = {'name': "nickname", 'address': "address 12", 'city': "ct", 'country': "i",
                                   'zip': "123"}

        # register owner & user
        self.GuestRole.register(self.owner_name, self.password)
        self.GuestRole.register(self.user_name, self.password)

        # owner opens store and adds products
        self.GuestRole.login(self.owner_name, self.password)
        self.SubscriberRole.open_store(self.owner_name, self.store.get_name())
        self.OwnerManagerRole.add_products(self.owner_name, self.store.get_name(), self.products_ls)
        self.SubscriberRole.logout(self.owner_name)

    def purchase(self, name: str):
        products_ls = self.GuestRole.purchase_products(name)
        result = self.GuestRole.confirm_payment(name, self.delivery_details, self.payment_details, products_ls)
        return result

    def test_parallel_purchase(self):
        self.GuestRole.login(self.owner_name, self.password)
        self.GuestRole.save_products_to_basket(self.owner_name, self.basket_ls)

        self.GuestRole.login(self.user_name, self.password)
        self.GuestRole.save_products_to_basket(self.user_name, self.basket_ls)

        users_nickname = [self.owner_name, self.user_name]

        # success for owner and fail for user, both try to purchase the exact amount in the store inventory
        with concurrent.futures.ThreadPoolExecutor() as executor:
            threads = [executor.submit(self.purchase, user_nickname) for user_nickname in users_nickname]
            return_value_ls = [thread.result() for thread in threads]
            print(return_value_ls)

        self.SubscriberRole.logout(self.owner_name)
        self.SubscriberRole.logout(self.user_name)

        self.assertEqual(return_value_ls[0]['msg'], "Great Success! Purchase complete")
        self.assertTrue(return_value_ls[0]['response'])
        self.assertEqual(return_value_ls[1]['msg'], "Can't complete purchase. Requested amount for product product" +
                                                    " exceeds amount in store inventory")
        self.assertFalse(return_value_ls[1]['response'])

    def test_parallel_registration(self):
        users_nickname = ["name1", "name1"]

        with concurrent.futures.ThreadPoolExecutor() as executor:
            threads = [executor.submit(self.GuestRole.register, user_nickname, 'pass') for user_nickname in users_nickname]
            return_value_ls = [thread.result() for thread in threads]
            print(return_value_ls)

        self.assertEqual(return_value_ls[0]['msg'], "Guest registered successfully")
        self.assertTrue(return_value_ls[0]['response'])
        self.assertEqual(return_value_ls[1]['msg'], "Invalid nickname, nickname already exist")
        self.assertFalse(return_value_ls[1]['response'])

    def test_parallel_update_inventory(self):
        users_nickname = ["name1", "name1"]

        with concurrent.futures.ThreadPoolExecutor() as executor:
            threads = [executor.submit(self.GuestRole.register, user_nickname, 'pass') for user_nickname in users_nickname]
            return_value_ls = [thread.result() for thread in threads]
            print(return_value_ls)

        self.assertEqual(return_value_ls[0]['msg'], "Guest registered successfully")
        self.assertTrue(return_value_ls[0]['response'])
        self.assertEqual(return_value_ls[1]['msg'], "Invalid nickname, nickname already exist")
        self.assertFalse(return_value_ls[1]['response'])

    def tearDown(self):
        (DataAccessFacade.get_instance()).delete_purchases()
        # (DataAccessFacade.get_instance()).delete_discount_policies()
        (DataAccessFacade.get_instance()).delete_statistics()
        (DataAccessFacade.get_instance()).delete_store_owner_appointments()
        (DataAccessFacade.get_instance()).delete_products_in_baskets()
        (DataAccessFacade.get_instance()).delete_products()
        (DataAccessFacade.get_instance()).delete_store_manager_appointments()
        (DataAccessFacade.get_instance()).delete_stores()
        (DataAccessFacade.get_instance()).delete_users()
        (TradeControl.get_instance()).__delete__()

if __name__ == '__main__':
    unittest.main()
