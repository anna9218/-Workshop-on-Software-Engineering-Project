import unittest

from src.Logger import logger


class LoginTests(unittest.TestCase):
    @logger
    def setUp(self):
        # TODO
        pass

    @logger
    def test_login(self):
        # TODO
        pass

    @logger
    def test_logout(self):
        # TODO
        pass

    @logger
    def test_is_logged_in(self):
        # TODO
        pass

    @logger
    def tearDown(self):
        # maybe delete the registered user resulted from this test
        pass

    def __repr__(self):
        return repr("LoginTests")

    if __name__ == '__main__':
        unittest.main()
