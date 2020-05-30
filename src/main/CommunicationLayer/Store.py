from src.main.CommunicationLayer.WebSocketService import notifyPurchase


class Store:

    def __init__(self, store_name, owner_nickname):
        self.__name = store_name
        # list of all owners (nickname: string, lastReadMsg: int)
        # lastReadMsg = last msg id (from msgs) the owner have read
        self.__subscribers = [(0, owner_nickname)]
        # list of all notifications (id: int, msg: string)
        self.__msgs = []

    def add_msg(self, msg): # the setStatus function
        """

        :param msg:
        :return:
        """
        self.__msgs.append((self.__msgs.len(), msg)) # maybe len-1
        self.notifyAll()

    def notifyAll(self):
        """
        check for each subscriber if there is a new msg- and send it if there is at least 1
        :return:
        """
        for (name, last_msg_id) in self.__subscribers:
            amount_of_msgs = len(self.__msgs) # maybe len-1
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
            for (msg_id, msg) in self.__msgs:
                if msg_id > lastMsgID:
                    notifyPurchase(user_name, msg)

    def get_last_read_msg_id (self, user_name):
        for (name, msg_id) in self.__subscribers:
            if name == user_name:
                return msg_id
        return -2

    def retrieve_msg_by_id(self, user_name, last_read_msg_id): # maybe add store_name, or add store controller
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
            return self.__msgs[last_read_msg_id+1]

    def subscribe_owner (self, nick_name): # maybe add store_name, or add store controller
        """
        by receive new appointment of store owner, this func will subscribe the owner to the
        relevant store-topic-publisher, the owner will receive only msgs that have been sent after
        his appointment
        :param nick_name: owner-to-subscribe nickname
        """
        self.__subscribers.append((len(self.__msgs), nick_name)) # maybe len-1
        # return some validation?

    def unsubscribe_owner (self, nick_name): # maybe add store_name, or add store controller
        """
        delete owner from the store's subscribers list (probably will be called from remove owner)
        if the owner is not on subscribers list - the func will do nothing
        :param nick_name: of the removed owner
        """
        for (owner_name, last_read_msg) in self.__subscribers:
            if owner_name == nick_name:
                self.__subscribers.remove((owner_name, last_read_msg))
        # return some validation?

    def store_name(self):
        return self.__name

    def subscribers(self):
        return self.__subscribers

    def amount_of_msgs (self):
        return len(self.__msgs)

