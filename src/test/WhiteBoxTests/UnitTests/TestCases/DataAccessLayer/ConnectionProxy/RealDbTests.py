import unittest
from unittest.mock import MagicMock, Mock
from peewee import Expression, OP

from src.main.DataAccessLayer.ConnectionProxy.RealDb import RealDb, database
from src.test.WhiteBoxTests.UnitTests.Stubs.StubUserData import StubUserData


class RealDbTests(unittest.TestCase):
    def setUp(self) -> None:
        self.real_db = RealDb()

    def test_connect(self):
        database.connect = MagicMock(return_value=True)
        self.assertTrue(self.real_db.connect())

        database.connect = MagicMock(return_value=False)
        self.assertFalse(self.real_db.connect())

        database.connect = MagicMock(return_value=AttributeError())
        try:
            self.real_db.connect()
            self.fail()
        except Exception:
            pass

    def test_disconnect(self):
        database.close = MagicMock(return_value=True)
        self.assertTrue(self.real_db.disconnect())

        database.close = MagicMock(return_value=False)
        self.assertFalse(self.real_db.disconnect())

        database.close = MagicMock(return_value=AttributeError())
        try:
            self.real_db.disconnect()
            self.fail()
        except Exception:
            pass

    def test_is_connected(self):
        database.is_closed = MagicMock(return_value=True)
        self.assertFalse(self.real_db.is_connected())

        database.is_closed = MagicMock(return_value=False)
        self.assertTrue(self.real_db.is_connected())

        database.is_closed = MagicMock(return_value=AttributeError())
        try:
            self.real_db.is_connected()
            self.fail()
        except Exception:
            pass

    # TODO: Can't create mock of the DB
    def test_read(self):
        # self.real_db.User.select().execute = MagicMock(return_value=[StubUserData("eytan", "pass word", False)])
        # self.assertListEqual([StubUserData("eytan", "pass word", False)], self.real_db.read(self.real_db.User))
        #
        # self.assertListEqual([StubUserData("eytan", "pass word", False)],
        #                      self.real_db.read(self.real_db.User, attributes_lst=[self.real_db.User.username]))
        #
        # self.real_db.User.select().where().execute = MagicMock(return_value=[StubUserData("eytan",
        #                                                                                   "pass word",
        #                                                                                   False)])
        # self.assertListEqual([StubUserData("eytan", "pass word", False)],
        #                      self.real_db.read(self.real_db.User, where_expr=Expression(self.real_db.User.username,
        #                                                                                 OP.EQ, "eytan")))
        #
        # self.assertListEqual([StubUserData("eytan", "pass word", False)],
        #                      self.real_db.read(self.real_db.User,
        #                                        attributes_lst=[self.real_db.User.username],
        #                                        where_expr=Expression(self.real_db.User.username, OP.EQ, "eytan")))
        pass

    def test_write(self):
        pass

    def test_update(self):
        pass

    def test_delete(self):
        pass

    def tearDown(self) -> None:
        pass


if __name__ == '__main__':
    unittest.main()
