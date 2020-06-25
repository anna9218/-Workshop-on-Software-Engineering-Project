import unittest
from unittest.mock import MagicMock

from src.main.DataAccessLayer.ConnectionProxy.Tables import rel_path
from src.main.DomainLayer.StoreComponent.AppointmentStatus import AppointmentStatus
from src.main.DomainLayer.StoreComponent.Store import Store
from src.main.ServiceLayer.StoreOwnerOrManagerRole import StoreOwnerOrManagerRole, TradeControl
from src.main.DomainLayer.StoreComponent.ManagerPermission import ManagerPermission


class StoreOwnerOrManagerTests(unittest.TestCase):
    def setUp(self) -> None:
        if not ("testing" in rel_path):
            raise ReferenceError("The Data Base is not the testing data base.\n"
                                 "\t\t\t\tPlease go to src.main.DataAccessLayer.ConnectionProxy.RealDb.rel_path\n"
                                 "\t\t\t\t and change rel_path to test_rel_path.\n"
                                 "\t\t\t\tThanks :D")
        self.__store_owner_or_manager_role: StoreOwnerOrManagerRole = StoreOwnerOrManagerRole()
        self.__trade_control_mock: TradeControl = TradeControl.get_instance()
        self.store_mock = Store("store1")
        self.name = "eden"

    def test_add_products(self):
        TradeControl.get_instance().add_products = MagicMock(return_value=True)
        self.assertTrue(self.__store_owner_or_manager_role.add_products(self.name, "Store", {}))

        TradeControl.get_instance().add_products = MagicMock(return_value=False)
        self.assertFalse(self.__store_owner_or_manager_role.add_products(self.name, "Store", {}))

    def test_remove_products(self):
        TradeControl.get_instance().remove_products = MagicMock(return_value=True)
        self.assertTrue(self.__store_owner_or_manager_role.remove_products(self.name, "Store", []))

        TradeControl.get_instance().remove_products = MagicMock(return_value=False)
        self.assertFalse(self.__store_owner_or_manager_role.remove_products(self.name, "Store", []))

    def test_edit_product(self):
        TradeControl.get_instance().edit_product = MagicMock(return_value=True)
        self.assertTrue(self.__store_owner_or_manager_role.edit_product(self.name, "Store", "product_name", "op", "new_value"))

        TradeControl.get_instance().edit_product = MagicMock(return_value=False)
        self.assertFalse(self.__store_owner_or_manager_role.edit_product(self.name, "Store", "product_name", "op", "new_value"))

    def test_appoint_additional_owner(self):
        TradeControl.get_instance().appoint_additional_owner = MagicMock(return_value=True)
        self.assertTrue(self.__store_owner_or_manager_role.appoint_additional_owner(self.name, "New Owner", "Store"))

        TradeControl.get_instance().appoint_additional_owner = MagicMock(return_value=False)
        self.assertFalse(self.__store_owner_or_manager_role.appoint_additional_owner(self.name, "New Owner", "Store"))

    def test_update_agreement_participants(self):
        TradeControl.get_instance().update_agreement_participants = MagicMock(return_value=True)
        self.assertTrue(self.__store_owner_or_manager_role.update_agreement_participants(self.name, "Appointee", "Store",
                                                                                         AppointmentStatus.APPROVED))

        TradeControl.get_instance().update_agreement_participants = MagicMock(return_value=False)
        self.assertFalse(self.__store_owner_or_manager_role.update_agreement_participants(self.name, "Appointee", "Store",
                                                                                         AppointmentStatus.APPROVED))

    def test_get_appointment_status(self):
        TradeControl.get_instance().get_appointment_status = MagicMock(return_value=True)
        self.assertTrue(self.__store_owner_or_manager_role.get_appointment_status("Appointee", "Store"))

        TradeControl.get_instance().get_appointment_status = MagicMock(return_value=False)
        self.assertFalse(self.__store_owner_or_manager_role.get_appointment_status("Appointee", "Store"))

    def test_appoint_store_manager(self):
        TradeControl.get_instance().appoint_store_manager = MagicMock(return_value=True)
        self.assertTrue(self.__store_owner_or_manager_role.appoint_store_manager(self.name, "New Manager", "Store", [ManagerPermission.WATCH_PURCHASE_HISTORY]))

        TradeControl.get_instance().appoint_store_manager = MagicMock(return_value=False)
        self.assertFalse(self.__store_owner_or_manager_role.appoint_store_manager(self.name, "New Manager", "Store", []))

    def test_edit_manager_permissions(self):
        TradeControl.get_instance().edit_manager_permissions = MagicMock(return_value=True)
        self.assertTrue(self.__store_owner_or_manager_role.edit_manager_permissions(self.name, "Store", "Appointee", [ManagerPermission.WATCH_PURCHASE_HISTORY]))

        TradeControl.get_instance().edit_manager_permissions = MagicMock(return_value=False)
        self.assertFalse(self.__store_owner_or_manager_role.edit_manager_permissions(self.name, "Store", "Appointee", []))

    def test_remove_manager(self):
        TradeControl.get_instance().remove_manager = MagicMock(return_value=True)
        self.assertTrue(self.__store_owner_or_manager_role.remove_manager(self.name, "Store", "Appointee"))

        TradeControl.get_instance().remove_manager = MagicMock(return_value=False)
        self.assertFalse(self.__store_owner_or_manager_role.remove_manager(self.name, "Store", "Appointee"))

    def test_remove_owner(self):
        TradeControl.get_instance().remove_owner = MagicMock(
            return_value={'response': ['owner was removed'], 'msg': "success"})

        res = self.__store_owner_or_manager_role.remove_owner(self.name, "owner", "myStore")
        self.assertEqual(res['response'], ['owner was removed'])
        self.assertEqual(res['msg'], "success")

    def test_display_store_purchases(self):
        TradeControl.get_instance().display_store_purchases = MagicMock(return_value=True)
        self.assertTrue(self.__store_owner_or_manager_role.display_store_purchases(self.name, "Store", True))

        TradeControl.get_instance().display_store_purchases = MagicMock(return_value=False)
        self.assertFalse(self.__store_owner_or_manager_role.display_store_purchases(self.name, "Store", True))

    def setup_for_policies(self):
        self.__trade_control_mock.get_store = MagicMock(return_value=self.store_mock)
        self.store_mock.get_name = MagicMock(return_value="store1")
        self.store_mock.is_owner = MagicMock(return_value=True)

    # TODO: add get tests for discount policies
    def test_get_policies(self):
        self.setup_for_policies()

        # ------------- purchase policies -------------
        # policies exist
        self.__trade_control_mock.get_policies = MagicMock(return_value={"response": ["policy1"], "msg": "ok"})

        res = self.__store_owner_or_manager_role.get_policies(self.name, "purchase", self.store_mock.get_name())["response"]
        self.assertTrue(len(res) > 0)

        # no policy exist
        self.__trade_control_mock.get_policies = MagicMock(return_value={"response": [], "msg": "ok"})

        res = self.__store_owner_or_manager_role.get_policies(self.name, "purchase", self.store_mock.get_name())["response"]
        self.assertTrue(len(res) == 0)
        # ------------- purchase policies -------------

    def test_update_purchase_policy(self):
        self.setup_for_policies()

        # valid update
        self.__trade_control_mock.update_purchase_policy = MagicMock(return_value={'response': True, 'msg': "updated"})
        res = self.__store_owner_or_manager_role.update_purchase_policy(self.name, self.store_mock.get_name(), {"name": "policy2",
                                                                                                        "products": [
                                                                                                         "product1",
                                                                                                         "product2"],
                                                                                                     "min_amount": 9})["response"]
        self.assertTrue(res)

        # invalid update
        self.__trade_control_mock.update_purchase_policy = MagicMock(return_value={'response': False,
                                                                                   'msg': "invalid update"})
        res = self.__store_owner_or_manager_role.update_purchase_policy(self.name, self.store_mock.get_name(), {"name": "policy2",
                                                                                                     "products": [
                                                                                                         "product1",
                                                                                                         "product2"],
                                                                                                     "min_amount": 9})[
            "response"]
        self.assertFalse(res)

    def test_define_purchase_policy(self):
        self.setup_for_policies()

        # valid define
        self.__trade_control_mock.define_purchase_policy = MagicMock(return_value={"response": True,
                                                                                   "msg": "policy added"})

        res = self.__store_owner_or_manager_role.define_purchase_policy(self.name, self.store_mock.get_name(), {"name": "policy2",
                                                                                    "products": ["product1",
                                                                                                 "product2"],
                                                                                    "min_amount": 9})["response"]
        self.assertTrue(res)

        # invalid define
        self.__trade_control_mock.define_purchase_policy = MagicMock(return_value={"response": False,
                                                                                   "msg": "policy not added"})

        res = self.__store_owner_or_manager_role.define_purchase_policy(self.name, self.store_mock.get_name(), {"name": "policy2",
                                                                                                     "products": [
                                                                                                         "product1",
                                                                                                         "product2"],
                                                                                                     "min_amount": 9})[
            "response"]
        self.assertFalse(res)

    def tearDown(self):
        self.__trade_control_mock.__delete__()

    def __repr__(self):
        return repr("StoreOwnerOrManagerRoleTests")


if __name__ == '__main__':
    unittest.main()
