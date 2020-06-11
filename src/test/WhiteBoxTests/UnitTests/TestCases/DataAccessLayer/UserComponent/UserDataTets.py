import unittest
from unittest.mock import MagicMock

from src.main.DataAccessLayer.ConnectionProxy.DbProxy import DbProxy
from src.test.WhiteBoxTests.UnitTests.Stubs.StubUserData import StubUserData
from src.main.DataAccessLayer.UserDataComponent.UserData import UserData


class UserDataTests(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def test_read(self):
        try:
            (UserData.get_instance()).read(["not_attribute"])
            self.fail()
        except AttributeError:
            pass
        except Exception:
            self.fail()

        (DbProxy.get_instance()).read = MagicMock(return_value=[StubUserData("eytan", "password", False)])
        res = (UserData.get_instance()).read([], username="eytan")
        self.assertEqual((res[0]['username'], res[0]['password'], res[0]['is_system_manager']),
                         ("eytan", "password", False))

        res = (UserData.get_instance()).read([], password="password")
        self.assertEqual((res[0]['username'], res[0]['password'], res[0]['is_system_manager']),
                         ("eytan", "password", False))

        (DbProxy.get_instance()).read = MagicMock(return_value=[])
        res = (UserData.get_instance()).read([], is_system_manager=True)
        self.assertListEqual([], res)

    def test_write(self):
        (DbProxy.get_instance()).write = MagicMock(return_value=1)
        res = UserData.get_instance().write("eytan", "pswd")
        self.assertEqual(1, res)

        (DbProxy.get_instance()).write = MagicMock(return_value=0)
        res = UserData.get_instance().write("eytan", "pswd")
        self.assertEqual(0, res)

    def test_update(self):
        try:
            (UserData.get_instance()).update()
            self.fail()
        except AttributeError:
            pass
        except Exception:
            self.fail()

        DbProxy.get_instance().update = MagicMock(return_value=1)
        res = UserData.get_instance().update(new_is_system_manager=True)
        self.assertEqual(res, 1)

        DbProxy.get_instance().update = MagicMock(return_value=1)
        res = UserData.get_instance().update(old_password="password", old_is_system_manager=True, new_is_system_manager=False)
        self.assertEqual(res, 1)

    def test_delete(self):
        (DbProxy.get_instance()).delete = MagicMock(return_value=1)
        res = (UserData.get_instance()).delete(username="eytan")
        self.assertEqual(1, res)

        res = (UserData.get_instance()).delete(password="password")
        self.assertEqual(1, res)

        (DbProxy.get_instance()).delete = MagicMock(return_value=0)
        res = (UserData.get_instance()).delete(is_system_manager=True)
        self.assertEqual(0, res)

    def tearDown(self) -> None:
        pass


if __name__ == '__main__':
    unittest.main()
