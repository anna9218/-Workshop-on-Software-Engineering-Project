import unittest

from src.Logger import logger


class PurchasePolicyTests(unittest.TestCase):
    @logger
    def setUp(self):
        # TODO
        pass

    @logger
    def test_add_disallowed_purchasing(self):
        # TODO
        pass

    @logger
    def test_can_purchase(self):
        # TODO
        pass

    @logger
    def tearDown(self):
        # maybe delete the registered user resulted from this test
        pass

    def __repr__(self):
        return repr("PurchasePolicyTests")

    if __name__ == '__main__':
        unittest.main()
