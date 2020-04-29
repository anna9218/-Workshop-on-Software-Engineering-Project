"""
    test class for use case 3.7 - view personal shopping history
"""
from src.Logger import logger
from src.test.BlackBoxTests.AcceptanceTests.ProjectTest import ProjectTest


class ViewPersonalHistoryTest(ProjectTest):
    @logger
    def setUp(self) -> None:
        pass

    @logger
    def test_success(self):
        pass

    @logger
    def test_fail(self):
        pass

    @logger
    def tearDown(self) -> None:
        pass

    def __repr__(self):
        return repr("ViewPersonalHistoryTest")