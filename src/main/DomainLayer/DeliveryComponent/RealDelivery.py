from src.Logger import logger
from src.main.DomainLayer.DeliveryComponent.DeliverySubject import DeliverySubject
from requests.exceptions import HTTPError, ConnectionError, ProxyError, SSLError, Timeout
import requests


class RealDelivery(DeliverySubject):

    def __init__(self):
        super().__init__()
        self.__url = 'https://cs-bgu-wsep.herokuapp.com/'
        self.__isConnected = False
        self.__max_timeout = 10

    @logger
    def is_connected(self) -> bool:
        try:
            res = requests.post(self.__url, data={'action_type': 'handshake'}, timeout=self.__max_timeout)

            if res is not None and res.text == "OK":
                return True
            else:
                # if response from the server is not "OK" or if the server didn't reply
                return  False
        except Exception:
            # if there is a connection error or the server timed out
            return False

    @logger
    def deliver_products(self, delivery_details: {'name': str, 'address': str, 'city': str, 'country': str,
                                                  'zip': str}) -> {'response': bool, 'msg': str}:
        """
            deliver through the external delivery system
        :param delivery_details:
        :return: dict = {'response': bool, 'msg': str}:
                 response = true if successful, otherwise false
        """
        try:
            res = requests.post(self.__url,
                                data={'action_type': 'supply', 'name': delivery_details['name'],
                                      'address': delivery_details.get('address'), 'city': delivery_details.get('city'),
                                      'country': delivery_details.get('country'), 'zip': delivery_details.get('zip')},
                                timeout=self.__max_timeout)
            if res is None:
                return {'response': False, 'msg': "Delivery failed. Server didn't reply"}

            transaction_id = int(res.text)

            if res is not None and 10000 <= transaction_id <= 100000:
                return {'response': True, 'msg': res.text}
            else:
                return {'response': False, 'msg': "Delivery failed. Transaction has failed."}
        except (HTTPError, ConnectionError, ProxyError, SSLError, ValueError):
            return {'response': False, 'msg': "Delivery failed. An error occurred during connection to the server."}
        except Timeout:
            return {'response': False, 'msg': "Delivery failed. The request timed out."}

    @logger
    def cancel_supply(self, transaction_id: str) -> {'response': bool, 'msg': str}:
        """

        :param transaction_id:
        :return:
        """
        try:
            res = requests.post(self.__url,
                                data={'action_type': 'cancel_supply', ' transaction_id': transaction_id},
                                timeout=self.__max_timeout)
            if res is None:
                return {'response': False, 'msg': "Delivery cancellation failed. Server didn't reply"}

            cancellation = int(res.text)

            if res is not None and cancellation == 1:
                return {'response': True, 'msg': "Delivery was cancelled successfully."}
            else:
                return {'response': False, 'msg': "Delivery cancellation failed."}
        except (HTTPError, ConnectionError, ProxyError, SSLError, ValueError):
            return {'response': False, 'msg': "Delivery cancellation failed. An error occurred during connection to "
                                              "the server."}
        except Timeout:
            return {'response': False, 'msg': "Delivery cancellation failed. The request timed out."}

    def cause_connection_error(self):
        self.__url = 'https://errorUrl/'

    def cause_timeout_error(self):
        self.__max_timeout = 0.001

    def set_connection_back(self):
        self.__url = 'https://cs-bgu-wsep.herokuapp.com/'
        self.__max_timeout = 10
