from datetime import datetime

from peewee import Expression, OP
from src.Logger import errorLogger
from src.main.DataAccessLayer.ConnectionProxy.Tables import Purchase
from src.main.DataAccessLayer.ConnectionProxy.DbProxy import DbProxy, and_exprs

"""
Represent the table of store owners appointments.
NOT the domain StoreOwnerAppointment.
"""


class PurchaseData:
    __instance = None

    @staticmethod
    def get_instance():
        """ Static access method. """
        if PurchaseData.__instance is None:
            PurchaseData()
        return PurchaseData.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if PurchaseData.__instance is not None:
            errorLogger("This class is a singleton!")
            raise Exception("This class is a singleton!")
        else:
            self.__tbl = Purchase
            self.__attr_purchase_id = "purchase_id"
            self.__attr_username = "username"
            self.__attr_store_name = "store_name"
            self.__attr_total_price = "total_price"
            self.__attr_date = "date"
            self.__attributes_as_dictionary = {self.__attr_purchase_id: self.__tbl.purchase_id,
                                               self.__attr_store_name: self.__tbl.store_name,
                                               self.__attr_username: self.__tbl.username,
                                               self.__attr_total_price: self.__tbl.total_price,
                                               self.__attr_date: self.__tbl.date}
            PurchaseData.__instance = self

    def read(self, attributes_to_read: [str], purchase_id: int = None, username: str = "", store_name: str = "",
             total_price: float = None, date: datetime = None):
        """
        Read store owner appointment from db.
        Raise exception if an attribute in attributes_to_read is illegal.
        <attribute> will composite a constraint of where to read.
        example(if old_username != ""), it will composite the constraint-
                                               where(user.username == username).

        :return: dict of the result data.
        """
        if len(attributes_to_read) > 0:
            for attribute in attributes_to_read:
                if attribute.lower() not in self.__attributes_as_dictionary.keys():
                    raise AttributeError("Attribute " + attribute + " doesn't exist in " + str(type(self.__tbl)) + ".")
        else:
            attributes_to_read: list = list(self.__attributes_as_dictionary.keys())
            attributes_to_read.remove(self.__attr_purchase_id)

        const_lst = []
        if not (purchase_id is None):
            const_lst.append((Expression(self.__tbl.purchase_id, OP.EQ, purchase_id)))
        if not (username == ""):
            const_lst.append((Expression(self.__tbl.username, OP.EQ, username)))
        if not (store_name == ""):
            const_lst.append(Expression(self.__tbl.store_name, OP.EQ, store_name))
        if not (total_price is None):
            const_lst.append((Expression(self.__tbl.total_price, OP.EQ, total_price)))
        if not (date is None):
            const_lst.append((Expression(self.__tbl.date, OP.EQ, date)))
        where_expr = and_exprs(const_lst)

        result = (DbProxy.get_instance()).read(self.__tbl, where_expr=where_expr)
        output_lst = []
        for data_obj in result:
            data_as_dictionary = {}
            if self.__attr_purchase_id in attributes_to_read:
                data_as_dictionary[self.__attr_purchase_id] = data_obj.purchase_id
            if self.__attr_username in attributes_to_read:
                data_as_dictionary[self.__attr_username] = data_obj.username.username
            if self.__attr_store_name in attributes_to_read:
                data_as_dictionary[self.__attr_store_name] = data_obj.store_name.store_name
            if self.__attr_total_price in attributes_to_read:
                data_as_dictionary[self.__attr_total_price] = data_obj.total_price
            if self.__attr_date in attributes_to_read:
                data_as_dictionary[self.__attr_date] = data_obj.date
            output_lst.append(data_as_dictionary)

        return output_lst

    def write(self, username: str = "", store_name: str = "", total_price: float = None, date: datetime = None):
        """
        write store owner appointment to db.

        :return:
        """
        attributes_as_dictionary = {self.__attributes_as_dictionary[self.__attr_username]: username,
                                    self.__attributes_as_dictionary[self.__attr_store_name]: store_name,
                                    self.__attributes_as_dictionary[self.__attr_total_price]: total_price,
                                    self.__attributes_as_dictionary[self.__attr_date]: date}

        return (DbProxy.get_instance()).write(self.__tbl, attributes_as_dictionary)

    def update(self, old_purchase_id: int = None, old_username: str = "", old_store_name: str = "",
               old_total_price: float = None, old_date: datetime = None, new_username: str = "", new_store_name: str = "",
               new_total_price: float = None, new_date: datetime = None):
        """
        Update store owner appointment in the db.
        old_<attribute> will composite a constraint of where to update.
        example(if old_username != ""), it will composite the constraint-
                                                where(user.username == old_username).
        new_<attribute> will update the <attribute> to the new value.
        example(if new_username != ""), it will update-
                                                update(user.username = new_username).

        :return: the number of updated rows.
        """
        const_lst = []
        if not (old_purchase_id is None):
            const_lst.append((Expression(self.__tbl.purchase_id, OP.EQ, old_purchase_id)))
        if not (old_username == ""):
            const_lst.append((Expression(self.__tbl.username, OP.EQ, old_username)))
        if not (old_store_name == ""):
            const_lst.append(Expression(self.__tbl.store_name, OP.EQ, old_store_name))
        if not (old_total_price is None):
            const_lst.append((Expression(self.__tbl.total_price, OP.EQ, old_total_price)))
        if not (old_date is None):
            const_lst.append((Expression(self.__tbl.date, OP.EQ, old_date)))
        where_expr = and_exprs(const_lst)

        attributes_as_dictionary = {}
        if not (new_username == ""):
            attributes_as_dictionary[self.__attributes_as_dictionary[self.__attr_username]] = \
                new_username
        if not (new_store_name == ""):
            attributes_as_dictionary[self.__attributes_as_dictionary[self.__attr_store_name]] = new_store_name
        if not (new_total_price is None):
            attributes_as_dictionary[self.__attributes_as_dictionary[self.__attr_total_price]] = \
                new_total_price
        if not (new_date is None):
            attributes_as_dictionary[self.__attributes_as_dictionary[self.__attr_date]] = \
                new_date
        if len(attributes_as_dictionary) == 0:
            raise AttributeError("Nothing to update")

        return DbProxy.get_instance().update(self.__tbl, attributes_as_dictionary, where_expr)

    def delete(self, purchase_id: int = None, username: str = "", store_name: str = "",
               total_price: float = None, date: datetime = None):
        """
        Delete store owner appointments from the DB.
        <attribute> will composite a constraint of where to delete.
        example(if old_username != ""), it will composite the constraint-
                                               where(user.username == username).

        :return: the number of deleted rows.
        """
        const_lst = []
        if not (purchase_id is None):
            const_lst.append((Expression(self.__tbl.purchase_id, OP.EQ, purchase_id)))
        if not (username == ""):
            const_lst.append((Expression(self.__tbl.username, OP.EQ, username)))
        if not (store_name == ""):
            const_lst.append(Expression(self.__tbl.store_name, OP.EQ, store_name))
        if not (total_price is None):
            const_lst.append((Expression(self.__tbl.total_price, OP.EQ, total_price)))
        if not (date is None):
            const_lst.append((Expression(self.__tbl.date, OP.EQ, date)))
        where_expr = and_exprs(const_lst)
        return (DbProxy.get_instance()).delete(self.__tbl, where_expr=where_expr)
