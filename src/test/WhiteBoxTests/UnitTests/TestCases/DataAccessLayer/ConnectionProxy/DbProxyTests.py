import unittest
from unittest.mock import MagicMock

from src.main.DataAccessLayer.ConnectionProxy.DbProxy import DbProxy


class DbProxyTests(unittest.TestCase):

    def setUp(self) -> None:
        self.__err_msg = "We having some tech problems, but we will rise again!"

    def test_System_down(self):
        (DbProxy.get_instance()).disconnect()

        # Read
        result = DbProxy.get_instance().read(None)
        self.assertFalse(result['response'])
        self.assertEqual(result['msg'], self.__err_msg)

        # Write
        result = DbProxy.get_instance().write(None, None)
        self.assertFalse(result['response'])
        self.assertEqual(result['msg'], self.__err_msg)

        # Update
        result = DbProxy.get_instance().update(None, None, None)
        self.assertFalse(result['response'])
        self.assertEqual(result['msg'], self.__err_msg)

        # Delete
        result = DbProxy.get_instance().delete(None, None)
        self.assertFalse(result['response'])
        self.assertEqual(result['msg'], self.__err_msg)

        # Execute
        result = DbProxy.get_instance().execute([])
        self.assertFalse(result['response'])
        self.assertEqual(result['msg'], self.__err_msg)

        (DbProxy.get_instance()).connect()
        (DbProxy.get_instance()).has_real_subject = MagicMock(return_value=False)

        # Read
        result = DbProxy.get_instance().read(None)
        self.assertFalse(result['response'])
        self.assertEqual(result['msg'], self.__err_msg)

        # Write
        result = DbProxy.get_instance().write(None, None)
        self.assertFalse(result['response'])
        self.assertEqual(result['msg'], self.__err_msg)

        # Update
        result = DbProxy.get_instance().update(None, None, None)
        self.assertFalse(result['response'])
        self.assertEqual(result['msg'], self.__err_msg)

        # Delete
        result = DbProxy.get_instance().delete(None, None)
        self.assertFalse(result['response'])
        self.assertEqual(result['msg'], self.__err_msg)

        # Execute
        result = DbProxy.get_instance().execute([])
        self.assertFalse(result['response'])
        self.assertEqual(result['msg'], self.__err_msg)

    def tearDown(self) -> None:
        pass

if __name__ == '__main__':
    unittest.main()
