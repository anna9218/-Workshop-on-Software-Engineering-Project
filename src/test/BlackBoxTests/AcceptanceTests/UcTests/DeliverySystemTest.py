"""
    test class for use case 8 - commit transaction via delivery system
"""
from src.Logger import errorLogger
from src.main.DomainLayer.DeliveryComponent.DeliveryProxy import DeliveryProxy
from src.test.BlackBoxTests.AcceptanceTests.ProjectAT import ProjectAT


class DeliverySystemTest(ProjectAT):

    def setUp(self) -> None:
        super().setUp()
        self.__delivery_details = {'name': "nickname", 'address': "address 12", 'city': "ct", 'country': "i", 'zip': "123"}

    def test_success(self):
        # test delivery system connection
        res = self.is_delivery_sys_connected()
        self.assertTrue(res)
        # test successful delivery
        res = self.deliver(self.__delivery_details)
        self.assertTrue(res["response"])
        # test successful delivery cancellation
        tid = res.get("tid")
        self.assertTrue(tid is not None and self.cancel_delivery_supply(tid))

    def test_fail(self):
        # test connection error with external system
        self.cause_delivery_con_error()
        res = self.deliver(self.__delivery_details)
        self.assertFalse(res["response"])
        self.set_connection_delivery_back()
        # test communication error with the server (timeout error)
        self.cause_delivery_timeout()
        res = self.deliver(self.__delivery_details)
        self.assertFalse(res["response"])
        self.set_connection_delivery_back()

    def tearDown(self) -> None:
        pass

    def __repr__(self):
        return repr("DeliverySystemTest")