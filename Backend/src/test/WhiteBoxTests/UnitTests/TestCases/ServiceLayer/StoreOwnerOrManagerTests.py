import unittest
from unittest.mock import MagicMock

from Backend.src.Logger import logger
from Backend.src.main.ServiceLayer.StoreOwnerOrManagerRole import StoreOwnerOrManagerRole, TradeControl
from Backend.src.main.DomainLayer.StoreComponent.ManagerPermission import ManagerPermission


class StoreOwnerOrManagerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.__store_owner_or_manager_role: StoreOwnerOrManagerRole = StoreOwnerOrManagerRole()
        self.__trade_control_mock: TradeControl = TradeControl.get_instance()

    # @logger
    def test_add_products(self):
        TradeControl.get_instance().add_products = MagicMock(return_value=True)
        self.assertTrue(self.__store_owner_or_manager_role.add_products("Eytan", {}))

        TradeControl.get_instance().add_products = MagicMock(return_value=False)
        self.assertFalse(self.__store_owner_or_manager_role.add_products("Eytan", {}))

    # @logger
    def test_remove_products(self):
        TradeControl.get_instance().remove_products = MagicMock(return_value=True)
        self.assertTrue(self.__store_owner_or_manager_role.remove_products("Eytan", []))

        TradeControl.get_instance().remove_products = MagicMock(return_value=False)
        self.assertFalse(self.__store_owner_or_manager_role.remove_products("Eytan", []))

    # @logger
    def test_edit_product(self):
        TradeControl.get_instance().edit_product = MagicMock(return_value=True)
        self.assertTrue(self.__store_owner_or_manager_role.edit_product("Eytan", "is", "the", "best"))

        TradeControl.get_instance().edit_product = MagicMock(return_value=False)
        self.assertFalse(self.__store_owner_or_manager_role.edit_product("Eytan", "is", "the", "best"))

    # @logger
    def test_appoint_additional_owner(self):
        TradeControl.get_instance().appoint_additional_owner = MagicMock(return_value=True)
        self.assertTrue(self.__store_owner_or_manager_role.appoint_additional_owner("Eytan is", "the best"))

        TradeControl.get_instance().appoint_additional_owner = MagicMock(return_value=False)
        self.assertFalse(self.__store_owner_or_manager_role.appoint_additional_owner("Eytan is", "the best"))

    # @logger
    def test_appoint_store_manager(self):
        TradeControl.get_instance().appoint_store_manager = MagicMock(return_value=True)
        self.assertTrue(self.__store_owner_or_manager_role.appoint_store_manager("Eytan is", "the best",
                                                                            [ManagerPermission.WATCH_PURCHASE_HISTORY])
                        )

        TradeControl.get_instance().appoint_store_manager = MagicMock(return_value=False)
        self.assertFalse(self.__store_owner_or_manager_role.appoint_store_manager("Eytan is", "the best", []))

    # @logger
    def test_edit_manager_permissions(self):
        TradeControl.get_instance().edit_manager_permissions = MagicMock(return_value=True)
        self.assertTrue(self.__store_owner_or_manager_role.edit_manager_permissions("Eytan is", "the best",
                                                                            [ManagerPermission.WATCH_PURCHASE_HISTORY])
                        )

        TradeControl.get_instance().edit_manager_permissions = MagicMock(return_value=False)
        self.assertFalse(self.__store_owner_or_manager_role.edit_manager_permissions("Eytan is", "the best", []))

    # @logger
    def test_remove_manager(self):
        TradeControl.get_instance().remove_manager = MagicMock(return_value=True)
        self.assertTrue(self.__store_owner_or_manager_role.remove_manager("Eytan is", "the best"))

        TradeControl.get_instance().remove_manager = MagicMock(return_value=False)
        self.assertFalse(self.__store_owner_or_manager_role.remove_manager("Eytan is", "the best"))

    # @logger
    def test_display_store_purchases(self):
        TradeControl.get_instance().display_store_purchases = MagicMock(return_value=True)
        self.assertTrue(self.__store_owner_or_manager_role.display_store_purchases("Eytan is the best"))

        TradeControl.get_instance().display_store_purchases = MagicMock(return_value=False)
        self.assertFalse(self.__store_owner_or_manager_role.display_store_purchases("Eytan is the best"))

    # @logger
    def tearDown(self):
        self.__trade_control_mock.__delete__()

    def __repr__(self):
        return repr("StoreOwnerOrManagerRoleTests")


if __name__ == '__main__':
    unittest.main()
