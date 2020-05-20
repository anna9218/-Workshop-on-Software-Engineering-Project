import unittest
from unittest.mock import MagicMock

from Backend.src.main.DomainLayer.DeliveryComponent.DeliveryProxy import DeliveryProxy
from src.main.DomainLayer.PaymentComponent.PaymentProxy import PaymentProxy
from Backend.src.main.DomainLayer.SecurityComponent.Security import Security
from Backend.src.main.DomainLayer.TradeComponent.TradeControl import TradeControl
from Backend.src.main.ServiceLayer.GuestRole import GuestRole


class GuestRoleTest(unittest.TestCase):
    # @logger
    def setUp(self) -> None:
        self.__guest_role = GuestRole()
        self.__trade_control_mock = TradeControl().get_instance()
        self.__security_mock = Security().get_instance()
        self.__payment_proxy_mock = PaymentProxy.get_instance()
        self.__delivery_proxy_mock = DeliveryProxy.get_instance()
        self.__nickname = "anna9218"
        self.__password = "password"
        self.__store_name = "Some Store"
        self.__product_name = "Some Product"
        self.__keyword = "Some Keyword"
        self.__category = "Some Category"

    # @logger
    # use case 2.2
    def test_register(self):
        self.__security_mock.get_instance().validated_password = MagicMock(return_value=True)
        self.__trade_control_mock.get_instance().register_guest = MagicMock(return_value=True)
        res = self.__guest_role.register(self.__nickname, self.__password)  # should succeed
        self.assertTrue(res)

        self.__security_mock.get_instance().validated_password = MagicMock(return_value=False)
        self.__trade_control_mock.get_instance().register_guest = MagicMock(return_value=True)
        res = self.__guest_role.register(self.__nickname, self.__password)
        self.assertFalse(res)

        self.__security_mock.get_instance().validated_password = MagicMock(return_value=False)
        self.__trade_control_mock.get_instance().register_guest = MagicMock(return_value=False)
        res = self.__guest_role.register(self.__nickname, self.__password)
        self.assertFalse(res)

        self.__security_mock.get_instance().validated_password = MagicMock(return_value=True)
        self.__trade_control_mock.get_instance().register_guest = MagicMock(return_value=False)
        res = self.__guest_role.register(self.__nickname, self.__password)
        self.assertFalse(res)

    # @logger
    # use case 2.3
    def test_login(self):
        self.__trade_control_mock.get_instance().login_subscriber = MagicMock(return_value=True)
        res = self.__guest_role.login(self.__nickname, self.__password)  # should succeed
        self.assertTrue(res)

        self.__trade_control_mock.get_instance().login_subscriber = MagicMock(return_value=False)
        res = self.__guest_role.login(self.__nickname, self.__password)
        self.assertFalse(res)

    # @logger
    # use case 2.4
    def test_display_stores_or_products_info(self):
        self.__trade_control_mock.get_instance().get_store_info = MagicMock(return_value=True)
        res = self.__guest_role.display_stores_or_products_info(self.__store_name, True, False)
        self.assertTrue(res)

        self.__trade_control_mock.get_instance().get_store_info = MagicMock(return_value=False)
        res = self.__guest_role.display_stores_or_products_info(self.__store_name, True, False)
        self.assertFalse(res)

        self.__trade_control_mock.get_instance().get_store_inventory = MagicMock(return_value=True)
        res = self.__guest_role.display_stores_or_products_info(self.__store_name, False, True)
        self.assertTrue(res)

        self.__trade_control_mock.get_instance().get_store_inventory = MagicMock(return_value=False)
        res = self.__guest_role.display_stores_or_products_info(self.__store_name, False, True)
        self.assertFalse(res)

    # @logger
    # use case 2.5.1
    def test_search_products_by(self):
        self.__trade_control_mock.get_instance().get_products_by = MagicMock(return_value=[])
        res = self.__guest_role.search_products_by(1, self.__product_name)
        self.assertEqual([], res)

        self.__trade_control_mock.get_instance().get_products_by = MagicMock(return_value=[])
        res = self.__guest_role.search_products_by(2, self.__keyword)
        self.assertEqual([], res)

        self.__trade_control_mock.get_instance().get_products_by = MagicMock(return_value=[])
        res = self.__guest_role.search_products_by(3, self.__category)
        self.assertEqual([], res)

    # @logger
    # use case 2.5.2
    def test_filter_products_by(self):
        self.__trade_control_mock.get_instance().filter_products_by = MagicMock(return_value=[])
        res = self.__guest_role.filter_products_by([], [])
        self.assertEqual([], res)

    # @logger
    # use case 2.6
    def test_save_products_to_basket(self):
        self.__trade_control_mock.get_instance().save_products_to_basket = MagicMock(return_value=[])
        res = self.__guest_role.save_products_to_basket([])
        self.assertEqual([], res)

    # @logger
    # use case 2.7
    def test_view_shopping_cart(self):
        self.__trade_control_mock.get_instance().view_shopping_cart = MagicMock(return_value=[])
        res = self.__guest_role.view_shopping_cart()
        self.assertEqual([], res)

    # @logger
    # use case 2.7
    def test_update_shopping_cart(self):
        self.__trade_control_mock.get_instance().remove_from_shopping_cart = MagicMock(return_value=True)
        res = self.__guest_role.update_shopping_cart("remove", [])
        self.assertTrue(res)

        self.__trade_control_mock.get_instance().remove_from_shopping_cart = MagicMock(return_value=False)
        res = self.__guest_role.update_shopping_cart("remove", [])
        self.assertFalse(res)

        self.__trade_control_mock.get_instance().update_quantity_in_shopping_cart = MagicMock(return_value=True)
        res = self.__guest_role.update_shopping_cart("update", [])
        self.assertTrue(res)

        self.__trade_control_mock.get_instance().update_quantity_in_shopping_cart = MagicMock(return_value=False)
        res = self.__guest_role.update_shopping_cart("update", [])
        self.assertFalse(res)

    # --------------------------------------------------------------------
    # use case 2.8
    # @logger
    def test_purchase_products(self):
        self.__trade_control_mock.get_instance().purchase_products = MagicMock(return_value=[])
        res = self.__guest_role.purchase_products()
        self.assertEqual([], res)

    # @logger
    def test_confirm_payment_test(self):
        # self.__trade_control_mock.get_instance().purchase_products = MagicMock(return_value=[])
        self.__payment_proxy_mock.get_instance().commit_payment = MagicMock(return_value=True)
        self.__delivery_proxy_mock.get_instance().deliver_products = MagicMock(return_value=True)
        self.__trade_control_mock.get_instance().accepted_purchase = MagicMock(return_value=True)
        res = self.__guest_role.confirm_payment("a", [])
        self.assertTrue(res)

        self.__delivery_proxy_mock.get_instance().deliver_products = MagicMock(return_value=False)
        self.__payment_proxy_mock.get_instance().cancel_payment = MagicMock(return_value=True)
        res = self.__guest_role.confirm_payment("a", [])
        self.assertFalse(res)

        self.__payment_proxy_mock.get_instance().commit_payment = MagicMock(return_value=False)
        res = self.__guest_role.confirm_payment("a", [])
        self.assertFalse(res)

    def tearDown(self):
        self.__trade_control_mock.__delete__()
        self.__security_mock.__delete__()

    def __repr__(self):
        return repr("GuestRoleTest")

    if __name__ == '__main__':
        unittest.main()
