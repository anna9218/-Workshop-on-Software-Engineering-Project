import unittest
from unittest.mock import MagicMock

from src.main.DomainLayer.StoreComponent.Purchase import Purchase
from src.main.DomainLayer.UserComponent.Login import Login
from src.main.DomainLayer.UserComponent.Registration import Registration
from src.main.DomainLayer.UserComponent.ShoppingBasket import ShoppingBasket
from src.main.DomainLayer.UserComponent.ShoppingCart import ShoppingCart
from src.main.DomainLayer.UserComponent.User import User
from src.test.WhiteBoxTests.UnitTests.Stubs.StubProduct import StubProduct
from src.test.WhiteBoxTests.UnitTests.Stubs.StubRegistration import StubRegistration
from src.test.WhiteBoxTests.UnitTests.Stubs.StubShoppingCart import StubShoppingCart
from src.test.WhiteBoxTests.UnitTests.Stubs.StubStore import StubStore


class UserTests(unittest.TestCase):
    def setUp(self):
        # self.user.logoutState = StubLogout()
        # self.__valid_name = "anna9218"
        # self.__valid_pass = "password"
        # self.__invalid_input = ""
        # self.__product = StubProduct()
        # self.__store = StubStore()
        # self.__product_ls_to_add = [[self.__product, self.__store, 1]]  # products_stores_quantity_ls

        self.__user = User()
        self.__registration_state_mock = Registration()
        self.__login_state_mock = Login()
        self.__shopping_cart_mock = ShoppingCart()
        self.__purchase_history_mock = []
        self.__purchase_mock = Purchase([], 10.0, "store_name", "username")
        self.__shopping_basket_mock = ShoppingBasket()

        # self.__user.__registration = self.__user.set_registration_state(StubRegistration())
        # # self.__user.__loginState = self.__user.set_login_state(StubLogin())
        # self.__user.__shoppingCart = self.__user.set_shopping_cart(StubShoppingCart())

    def test_register(self):
        # self.assertTrue(self.__user.register(self.__valid_name, self.__valid_pass)['response'])
        # self.assertFalse(self.__user.register(self.__valid_name, self.__valid_pass)['response'])
        self.__user.is_registered = MagicMock(return_value=True)
        res = self.__user.register("nickname", "password")
        self.assertFalse(res['response'])

        self.__user.is_registered = MagicMock(return_value=False)
        self.__user.set_registration_state(self.__registration_state_mock)
        res = self.__user.register("nickname", "password")
        self.assertTrue(res['response'])

    def test_login(self):
        # self.__user.register(self.__valid_name, self.__valid_pass)
        # self.assertTrue(self.__user.login(self.__valid_name, self.__valid_pass)['response'])
        # self.assertFalse(self.__user.login(self.__invalid_input, self.__invalid_input)['response'])
        self.__user.check_password = MagicMock(return_value=False)
        res = self.__user.login("nickname", "password")
        self.assertFalse(res['response'])

        self.__user.check_password = MagicMock(return_value=True)
        self.__user.is_logged_in = MagicMock(return_value=True)
        res = self.__user.login("nickname", "password")
        self.assertFalse(res['response'])

        self.__user.is_logged_in = MagicMock(return_value=False)
        self.__user.check_nickname = MagicMock(return_value=True)
        self.__login_state_mock.login = MagicMock(return_value=True)
        self.__user.set_login_state(self.__login_state_mock)
        self.__user.get_nickname = MagicMock(return_value="TradeManager")
        self.__user.set_registration_state(self.__registration_state_mock)
        res = self.__user.login("nickname", "password")
        self.assertTrue(res['response'])

        self.__user.get_nickname = MagicMock(return_value="nickname")
        self.__user.set_registration_state(self.__registration_state_mock)
        res = self.__user.login("nickname", "password")
        self.assertTrue(res['response'])

    def test_logout(self):
        # self.__user.register(self.__valid_name, self.__valid_pass)
        # self.__user.login(self.__valid_name, self.__valid_pass)
        # self.assertTrue(self.__user.logout())
        self.__user.is_logged_in = MagicMock(return_value=True)
        self.__user.set_login_state(self.__login_state_mock)
        res = self.__user.logout()
        self.assertTrue(res)

        self.__user.is_logged_in = MagicMock(return_value=False)
        self.__user.set_login_state(self.__login_state_mock)
        res = self.__user.logout()
        self.assertFalse(res)

    def test_check_password(self):
        # self.__user.register(self.__valid_name, self.__valid_pass)
        # self.assertTrue(self.__user.check_password(self.__valid_pass))
        # self.assertFalse(self.__user.check_password(self.__invalid_input))

        # hashed value of 'password'
        self.__registration_state_mock.get_password = MagicMock(return_value='fcf0a27361d035a079499e86d461e787d8fb328cc3de44df3a96f1d8d00798774cd4375f08353275c2d46a730834e75f3003cf98555b7f19b267b8aaaa5c5b3ae052890976839ca40cc00d16a5c5515093ade62e6d46a550c4cce095c65bb789')
        self.__user.set_registration_state(self.__registration_state_mock)
        self.assertTrue(self.__user.check_password("password"))
        self.assertFalse(self.__user.check_password("wrong password"))


    def test_check_nickname(self):
        # self.__user.register(self.__valid_name, self.__valid_pass)
        # self.assertTrue(self.__user.check_nickname(self.__valid_name))
        # self.assertFalse(self.__user.check_nickname(self.__invalid_input))
        self.__registration_state_mock.get_nickname = MagicMock(return_value="nickname")
        self.__user.set_registration_state(self.__registration_state_mock)
        self.assertTrue(self.__user.check_nickname("nickname"))
        self.assertFalse(self.__user.check_nickname("wrong nickname"))

    def test_is_logged_in(self):
        # self.__user.register(self.__valid_name, self.__valid_pass)
        # self.assertFalse(self.__user.is_logged_in())
        # self.__user.login(self.__valid_name, self.__valid_pass)
        # self.assertTrue(self.__user.is_logged_in())
        self.__login_state_mock.is_logged_in = MagicMock(return_value=True)
        self.__user.set_login_state(self.__login_state_mock)
        self.assertTrue(self.__user.is_logged_in())

        self.__login_state_mock.is_logged_in = MagicMock(return_value=False)
        self.__user.set_login_state(self.__login_state_mock)
        self.assertFalse(self.__user.is_logged_in())

    def test_is_logged_out(self):
        # self.__user.register(self.__valid_name, self.__valid_pass)
        # self.assertTrue(self.__user.is_logged_out())
        # self.__user.login(self.__valid_name, self.__valid_pass)
        # self.assertFalse(self.__user.is_logged_out())
        self.__login_state_mock.is_logged_in = MagicMock(return_value=False)
        self.__user.set_login_state(self.__login_state_mock)
        self.assertTrue(self.__user.is_logged_out())

        self.__login_state_mock.is_logged_in = MagicMock(return_value=True)
        self.__user.set_login_state(self.__login_state_mock)
        self.assertFalse(self.__user.is_logged_out())

    def test_is_registered(self):
        # self.assertFalse(self.__user.is_registered())
        # self.__user.register(self.__valid_name, self.__valid_pass)
        # self.assertTrue(self.__user.is_registered())
        self.__registration_state_mock.is_registered = MagicMock(return_value=True)
        self.__user.set_registration_state(self.__registration_state_mock)
        self.assertTrue(self.__user.is_registered())

        self.__registration_state_mock.is_registered = MagicMock(return_value=False)
        self.__user.set_registration_state(self.__registration_state_mock)
        self.assertFalse(self.__user.is_registered())

    def test_get_nickname(self):
        # self.__user.register(self.__valid_name, self.__valid_pass)
        # self.assertEqual(self.__user.get_nickname(), self.__valid_name, "")
        # self.assertNotEqual(self.__user.get_nickname(), self.__invalid_input, "")
        self.__registration_state_mock.get_nickname = MagicMock(return_value="nickname")
        self.__user.set_registration_state(self.__registration_state_mock)
        self.assertEqual(self.__user.get_nickname(), "nickname")
        self.assertNotEqual(self.__user.get_nickname(), "wrong nickname")

    def test_save_products_to_basket(self):
        # # test for guest
        # self.assertTrue(self.__user.save_products_to_basket(self.__product_ls_to_add))
        # # test for subscriber
        # self.__user.register(self.__valid_name, self.__valid_pass)
        # self.assertTrue(self.__user.save_products_to_basket(self.__product_ls_to_add))
        self.__shopping_cart_mock.add_products = MagicMock(
            return_value={'response': True, 'msg': "Products were added to shopping cart successfully"})

        self.__user.set_shopping_cart(self.__shopping_cart_mock)
        res = self.__user.save_products_to_basket([])
        self.assertTrue(res['response'])

        self.__shopping_cart_mock.add_products = MagicMock(
            return_value={'response': False, 'msg': "Error! invalid input"})

        self.__user.set_shopping_cart(self.__shopping_cart_mock)
        res = self.__user.save_products_to_basket([])
        self.assertFalse(res['response'])

    def test_view_shopping_cart(self):
        self.__shopping_cart_mock.view_shopping_cart = MagicMock(
            return_value={'response': [], 'msg': "Shopping cart was retrieved successfully"})

        self.__user.set_shopping_cart(self.__shopping_cart_mock)
        res = self.__user.view_shopping_cart()
        self.assertEqual(res['msg'], "Shopping cart was retrieved successfully")

    def test_remove_from_shopping_cart(self):
        self.__shopping_cart_mock.remove_from_shopping_cart = MagicMock(
            return_value={'response': True, 'msg': "Products were removed from your shopping cart successfully"})

        self.__user.set_shopping_cart(self.__shopping_cart_mock)
        res = self.__user.remove_from_shopping_cart([])
        self.assertTrue(res['response'])

    def test_update_quantity_in_shopping_cart(self):
        self.__shopping_cart_mock.update_quantity = MagicMock(
            return_value={'response': True, 'msg': "Shopping cart was updated successfully."})

        self.__user.set_shopping_cart(self.__shopping_cart_mock)
        res = self.__user.update_quantity_in_shopping_cart([])
        self.assertTrue(res['response'])

    def test_complete_purchase(self):
        self.__shopping_cart_mock.get_store_basket = MagicMock(return_value=self.__shopping_basket_mock)
        self.__user.set_shopping_cart(self.__shopping_cart_mock)
        self.__purchase_mock.get_store_name = MagicMock(return_value="store_name")
        self.__shopping_basket_mock.complete_purchase = MagicMock(return_value=True)
        res = self.__user.complete_purchase(self.__purchase_mock)
        self.assertTrue(res)

    # def test_remove_purchase(self):
    #     res = self.__user.remove_purchase(self.__purchase_mock)
    #     self.assertTrue(res)

    def test_get_password(self):
        self.__registration_state_mock.get_password = MagicMock(return_value="password")
        self.__user.set_registration_state(self.__registration_state_mock)
        self.assertEqual(self.__user.get_password(), "password")
        self.assertNotEqual(self.__user.get_password(), "wrong password")

    def tearDown(self):
        # maybe delete the registered user resulted from this test
        pass

    def __repr__(self):
        return repr("UserTests")

    if __name__ == '__main__':
        unittest.main()

