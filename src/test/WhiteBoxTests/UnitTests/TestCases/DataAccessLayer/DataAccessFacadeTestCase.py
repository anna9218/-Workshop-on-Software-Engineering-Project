import unittest
from unittest.mock import MagicMock
from src.main.DataAccessLayer.DataAccessFacade import DataAccessFacade
from src.main.DataAccessLayer.UserDataComponent.UserData import UserData


class DataAccessFacadeTests(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def test_read_users(self):
        UserData.get_instance().read = MagicMock(return_value=[])
        self.assertListEqual([], DataAccessFacade.get_instance().read_users())

        UserData.get_instance().read = MagicMock(return_value=[{"username": "eytan", "password": "password",
                                                                "is_system_manager": False}])
        self.assertListEqual([{"username": "eytan", "password": "password",
                               "is_system_manager": False}], DataAccessFacade.get_instance().read_users())

    def test_write_user(self):
        UserData.get_instance().write = MagicMock(return_value=0)
        self.assertEqual(0, DataAccessFacade.get_instance().write_user("eytan", "password"))

        UserData.get_instance().write = MagicMock(return_value=1)
        self.assertEqual(1, DataAccessFacade.get_instance().write_user("eytan", "password"))

    def test_update_users(self):
        UserData.get_instance().update = MagicMock(return_value=0)
        self.assertEqual(0, DataAccessFacade.get_instance().update_users(new_username="not eytan"))

        UserData.get_instance().update = MagicMock(return_value=1)
        self.assertEqual(1, DataAccessFacade.get_instance().update_users())

        UserData.get_instance().update = MagicMock(return_value=2)
        self.assertEqual(2, DataAccessFacade.get_instance().update_users())

    def test_delete_users(self):
        UserData.get_instance().delete = MagicMock(return_value=0)
        self.assertEqual(0, DataAccessFacade.get_instance().delete_users())

        UserData.get_instance().delete = MagicMock(return_value=1)
        self.assertEqual(1, DataAccessFacade.get_instance().delete_users())

        UserData.get_instance().delete = MagicMock(return_value=2)
        self.assertEqual(2, DataAccessFacade.get_instance().delete_users())

    def tearDown(self) -> None:
        pass


if __name__ == '__main__':
    unittest.main()
