import unittest

from src.Logger import logger


class DiscountPolicyTests(unittest.TestCase):
    @logger
    def setUp(self):
        # TODO
        pass

    @logger
    def test_add_disallowed_purchasing(self):
        # TODO
        pass

    @logger
    def test_is_deserve_to_discount(self):
        # TODO
        pass

    @logger
    def tearDown(self):
        pass

    def __repr__(self):
        return repr ("DiscountPolicyTests")

    if __name__ == '__main__':
        unittest.main()
