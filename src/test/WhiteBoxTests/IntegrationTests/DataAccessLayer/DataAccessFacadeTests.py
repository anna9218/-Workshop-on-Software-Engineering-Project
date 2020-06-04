import unittest
from src.main.DataAccessLayer.DataAccessFacade import DataAccessFacade
from src.main.DataAccessLayer.ConnectionProxy.RealDb import rel_path
from peewee import IntegrityError


class DataAccessFacadeTests(unittest.TestCase):

    def setUp(self) -> None:
        if not ("testing" in rel_path):
            raise ReferenceError("The Data Base is not the testing data base.\n"
                                 "\t\t\t\tPlease go to src.main.DataAccessLayer.ConnectionProxy.RealDb.rel_path\n"
                                 "\t\t\t\t and change rel_path to test_rel_path.\n"
                                 "\t\t\t\tThanks :D")
        try:
            (DataAccessFacade.get_instance()).write_user("Eytan", "Eytan's password", False)
            (DataAccessFacade.get_instance()).write_user("System manager", "not Eytan's password", True)
        except IntegrityError:
            pass
        except Exception:
            raise ValueError("My error. check set up.")

    def test_read_users(self):
        # Select all
        result = (DataAccessFacade.get_instance()).read_users()
        self.assertListEqual(result,
                             [{'username': "Eytan", 'password': "Eytan's password", 'is_system_manager': False},
                              {'username': "System manager", 'password': "not Eytan's password",
                               'is_system_manager': True}])

        # Select specific columns
        result = (DataAccessFacade.get_instance()).read_users(["username", "password"])
        self.assertListEqual(result,
                             [{'username': "Eytan", 'password': "Eytan's password"},
                              {'username': "System manager", 'password': "not Eytan's password"}])

        # Select specific user
        result = (DataAccessFacade.get_instance()).read_users(username="Eytan")
        self.assertListEqual(result,
                             [{'username': "Eytan", 'password': "Eytan's password", 'is_system_manager': False}])

        # Select specific columns in specific user
        result = (DataAccessFacade.get_instance()).read_users(['username', 'password'], username="Eytan")
        self.assertListEqual(result,
                             [{'username': "Eytan", 'password': "Eytan's password"}])

        # Select with composite where constraint.
        result = (DataAccessFacade.get_instance()).read_users(username="Eytan", password="Eytan's password")
        self.assertListEqual(result,
                             [{'username': "Eytan", 'password': "Eytan's password", 'is_system_manager': False}])

        # Select result is empty.
        result = (DataAccessFacade.get_instance()).read_users(username="Yarin", password="Yarin's password")
        self.assertListEqual(result, [])

        # Invalid - attributes list contains not attribute key
        try:
            result = (DataAccessFacade.get_instance()).read_users(['username3', 'password'], username="Eytan")
            self.fail("My error. See Invalid - attributes list contains not attribute key")
        except AttributeError:
            pass
        except Exception:
            self.fail("My Error. See Invalid - attributes list contains not attribute key")

    def test_write_user(self):
        # Insert 1 with default is_sys_man
        result = (DataAccessFacade.get_instance()).write_user("Yarin", "Yarin's password")
        self.assertEqual(3, result)
        self.assertGreater(len((DataAccessFacade.get_instance()).read_users([], "Yarin", "Yarin's password")), 0)

        # Insert 1 with is_sys_man
        result = (DataAccessFacade.get_instance()).write_user("Yarin2", "Yarin's password", True)
        self.assertEqual(4, result)
        self.assertGreater(len((DataAccessFacade.get_instance()).read_users([], "Yarin2", "Yarin's password")), 0)

        # Invalid - pk already exist
        try:
            result = (DataAccessFacade.get_instance()).write_user("Yarin", "Eytan")
            self.fail("My error. See Invalid - attributes list contains not attribute key")
        except IntegrityError:
            pass
        except Exception:
            self.fail("My Error. See Invalid - attributes list contains not attribute key")

        # Delete the extra users:
        DataAccessFacade.get_instance().delete_users(username="Yarin")
        DataAccessFacade.get_instance().delete_users(username="Yarin2")

    def test_update_users(self):
        # update specific user password
        result = (DataAccessFacade.get_instance()).update_users(old_username="Eytan",
                                                                new_password="new password")
        self.assertEqual(1, result)
        self.assertGreater(len((DataAccessFacade.get_instance()).read_users([], username="Eytan",
                                                                            password="new password")), 0)

        # update all users password
        result = (DataAccessFacade.get_instance()).update_users(new_password="system password")
        self.assertEqual(2, result)
        self.assertGreater(len((DataAccessFacade.get_instance()).read_users([], password="system password")), 0)

        # not pk constraint
        result = (DataAccessFacade.get_instance()).update_users(old_is_system_manager=True, new_is_system_manager=False)
        self.assertEqual(1, result)
        self.assertGreaterEqual(len((DataAccessFacade.get_instance()).read_users([], is_system_manager=False)), 2)

        # composite constraint
        result = (DataAccessFacade.get_instance()).update_users(old_is_system_manager=False,
                                                                old_username="Eytan",
                                                                new_is_system_manager=True)
        self.assertEqual(1, result)
        self.assertGreaterEqual(len((DataAccessFacade.get_instance()).read_users([], is_system_manager=False)), 1)

        # Invalid: nothing to update
        try:
            result = (DataAccessFacade.get_instance()).update_users()
            self.fail()
        except AttributeError:
            pass
        except Exception:
            self.fail()

    def test_delete_users(self):
        # delete specific user
        result = (DataAccessFacade.get_instance()).delete_users(username="Eytan")
        self.assertEqual(result, 1)

        # insert new user
        (DataAccessFacade.get_instance()).write_user("Yarin2", "Yarin's password", True)

        # delete several users
        result = (DataAccessFacade.get_instance()).delete_users(is_system_manager=True)
        self.assertEqual(result, 2)

        # insert new users
        (DataAccessFacade.get_instance()).write_user("Yarin", "Yarin's password", True)
        (DataAccessFacade.get_instance()).write_user("Yarin2", "Yarin's password", False)

        # composite constraint
        result = (DataAccessFacade.get_instance()).delete_users(password="Yarin's password", is_system_manager=False)
        self.assertEqual(result, 1)

    def tearDown(self) -> None:
        (DataAccessFacade.get_instance()).delete_users()


if __name__ == '__main__':
    unittest.main()
