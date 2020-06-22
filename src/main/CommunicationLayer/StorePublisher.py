from jsonpickle import json


# from src.main.CommunicationLayer.WebSocketService import notifyPurchase
# from src.main.CommunicationLayer.WebSocketService import send_msg


class StorePublisher:

    def __init__(self, store_name, owner_nickname):
        # print ("in constructor")
        self.__name = store_name
        # list of all owners ( lastReadMsg: int, nickname: string, ws:websocket)
        # lastReadMsg = last msg id (from msgs) the owner have read
        self.__subscribers = [(owner_nickname, 0)]
        # list of all notifications (id: int, msg: string)
        self.__msgs = []
        # print(f"store name- {self.__name}, it's subscriber - {self.__subscribers}")

    def add_msg(self, msg):  # the setStatus function
        """

        :param msg:
        :return:
        """
        self.__msgs.append((len(self.__msgs), msg))  # maybe len-1
        self.notifyAll()

    def notifyAll(self):
        """
        check for each subscriber if there is a new msg- and send it if there is at least 1
        :return:
        """
        for (name, last_msg_id) in self.__subscribers:
            amount_of_msgs = len(self.__msgs)  # maybe len-1
            if last_msg_id < amount_of_msgs:
                self.notify(name)

    def notify(self, user_name):
        """
        if there is a new msg to send to the subscriber with user_name - send it
        :param user_name: of owner
        :return:
        """
        lastMsgID = self.get_last_read_msg_id(user_name)
        if lastMsgID > -1:
            # for (msg_id, msg) in self.__msgs:
            #     if msg_id > lastMsgID:
            #         send_msg(user_name, msg)
            unread_msgs = []
            for msg_id, msg in self.__msgs:
                if msg_id > lastMsgID:
                    unread_msgs += msg
                    self.inc_last_unread_msg(user_name)


    def get_last_read_msg_id(self, user_name):
        """
        returns the id of the last msg the subscriber with user_name has read
        :param user_name: subscriber nickname
        :return: msg id on queue. unique values: -1 if no msgs since the user subscribed, -2 as false
        """
        for (name, msg_id) in self.__subscribers:
            if name == user_name:
                return msg_id
        return -2

    def retrieve_msg_by_id(self, user_name, last_read_msg_id):  # maybe add store_name, or add store controller
        """
        sends unread msgs to the owner with user_name (if its a subscriber to this store)
        assumes validate input
        :param user_name: of owner
        :param last_read_msg_id: last read msg by the client-side
        :return:
        """
        last_read_msg_by_server = self.get_last_read_msg_id(user_name)
        if last_read_msg_by_server == last_read_msg_id:
            self.inc_last_msg_id(user_name)
            return self.__msgs[last_read_msg_id + 1]

    def subscribe_owner(self, nick_name):  # maybe add store_name, or add store controller
        """
        by receive new appointment of store owner, this func will subscribe the owner to the
        relevant store-topic-publisher, the owner will receive only msgs that have been sent after
        his appointment
        :param nick_name: owner-to-subscribe nickname
        """
        if (self.is_subscribed_to_store(nick_name)):
            return False
        self.__subscribers.append((nick_name, len(self.__msgs)))
        # print(f"subscribers: {self.__subscribers}")
        return True
        # return some validation?

    def unsubscribe_owner(self, nick_name):
        """
        delete owner from the store's subscribers list (probably will be called from remove owner)
        if the owner is not on subscribers list - the func will do nothing
        :param nick_name: of the removed owner
        """
        counter = 0
        for subscriber in self.__subscribers:
            if counter != 0:
                (owner_name, last_read_msg) = subscriber
                if owner_name == nick_name:
                    # print(f"owner {owner_name}, id {last_read_msg}, sub {subscriber}")
                    self.__subscribers.remove(subscriber)
                    # self.__subscribers.remove((owner_name, last_read_msg))
                    # print(f"is subscribe --> {self.is_subscribed_to_store(owner_name)}")
                    # print(f"subscribers: {self.__subscribers}")
                    return 0
            else:
                counter = counter+1
        return -1
        # return some validation?

    def store_name(self):
        return self.__name

    def subscribers(self):
        return self.__subscribers

    def amount_of_subscribers(self):
        return len(self.__subscribers)

    def amount_of_msgs(self):
        return len(self.__msgs)

    def is_subscribed_to_store(self, nickname):
        if self.__subscribers is None:
            # print ("is sub error")
            return False
        # print("is subscribe subscribers: " + str(self.__subscribers))
        for (owner_name, last_read_msg) in self.__subscribers: # [(owner_nickname, 0)]
            if owner_name == nickname:
                return True
            # print(f"nickname = {owner_name}, last id = {last_read_msg}")
        # print(f"cannot find owner {nickname}")
        return False

    def inc_last_unread_msg(self, user_name):
        for username, lastUnreadMsg in self.__subscribers:
            if user_name == username:
                lastUnreadMsg += 1

    def __repr__(self):
        return repr(f"{self.__name} Publisher Details --> Subscribers: {self.__subscribers}, Msgs: {self.__msgs}")
