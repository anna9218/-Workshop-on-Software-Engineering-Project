from datetime import datetime
from peewee import Expression, OP
from src.Logger import errorLogger
from src.main.DataAccessLayer.ConnectionProxy.Tables import CompositeDiscountPolicy
from src.main.DataAccessLayer.ConnectionProxy.DbProxy import DbProxy, and_exprs
import jsonpickle

"""
Represent the table of stores.
NOT the domain stores.
"""


class CompositeDiscountPolicyData:
    __instance = None

    @staticmethod
    def get_instance():
        """ Static access method. """
        if CompositeDiscountPolicyData.__instance is None:
            CompositeDiscountPolicyData()
        return CompositeDiscountPolicyData.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if CompositeDiscountPolicyData.__instance is not None:
            errorLogger("This class is a singleton!")
            raise Exception("This class is a singleton!")
        else:
            self.__tbl = CompositeDiscountPolicy
            self.__attr_policy_ref = "policy_ref"
            self.__attr_policy1_ref = "policy1_ref"
            self.__attr_policy2_ref = "policy2_ref"
            self.__attr_flag = "flag"
            self.__attributes_as_dictionary = {self.__attr_policy_ref: self.__tbl.policy_ref,
                                               self.__attr_policy1_ref: self.__tbl.policy1_ref,
                                               self.__attr_policy2_ref: self.__tbl.policy2_ref,
                                               self.__attr_flag: self.__tbl.flag}
            CompositeDiscountPolicyData.__instance = self

    def read(self, attributes_to_read: [str], policy_ref: int = None, policy1_ref: int = None, policy2_ref: int = None,
             flag: int = None):
        """
        Read discount policy from db.
        Raise exception if an attribute in attributes_to_read is illegal.
        <attribute> will composite a constraint of where to read.
        example(if old_username != ""), it will composite the constraint-
                                               where(user.username == username).

        :param founder_username:
        :param store_name:
        :param attributes_to_read: the list of attributes that will return from the db.
                                    type: [str]

        :return: list of dictionaries that contain attributes_to_read fields.
        """
        if len(attributes_to_read) > 0:
            for attribute in attributes_to_read:
                if attribute.lower() not in self.__attributes_as_dictionary.keys():
                    raise AttributeError("Attribute " + attribute + " doesn't exist in " + str(type(self.__tbl)) + ".")
        else:
            attributes_to_read: list = list(self.__attributes_as_dictionary.keys())
            attributes_to_read.remove(self.__attr_policy_ref)

        const_lst = []
        if not (policy_ref is None):
            const_lst.append(Expression(self.__tbl.policy_ref, OP.EQ, policy_ref))
        if not (policy1_ref is None):
            const_lst.append(Expression(self.__tbl.policy1_ref, OP.EQ, policy1_ref))
        if not (policy2_ref is None):
            const_lst.append(Expression(self.__tbl.policy2_ref, OP.EQ, policy2_ref))
        if not (flag is None):
            const_lst.append(Expression(self.__tbl.flag, OP.EQ, flag))
        where_expr = and_exprs(const_lst)

        result = (DbProxy.get_instance()).read(self.__tbl, where_expr=where_expr)
        output_lst = []
        for data_obj in result:
            data_as_dictionary = {}
            if self.__attr_policy_ref in attributes_to_read:
                data_as_dictionary[self.__attr_policy_ref] = data_obj.discount_policy_id
            if self.__attr_policy1_ref in attributes_to_read:
                data_as_dictionary[self.__attr_policy1_ref] = data_obj.policy1_ref.policy_name
            if self.__attr_policy2_ref in attributes_to_read:
                data_as_dictionary[self.__attr_policy2_ref] = data_obj.policy2_ref.policy_name
            if self.__attr_flag in attributes_to_read:
                data_as_dictionary[self.__attr_flag] = data_obj.flag
            output_lst.append(data_as_dictionary)

        return output_lst

    def write(self, policy_ref: int = None, policy1_ref: int = None, policy2_ref: int = None,
              flag: int = None):
        """
        Write a store to db.

        :param store_name:
        :param founder_username:
        :return: size of user tbl after inserting the new one.
        """
        attributes_as_dictionary = {self.__attributes_as_dictionary[self.__attr_policy_ref]: policy_ref,
                                    self.__attributes_as_dictionary[self.__attr_policy1_ref]:
                                        policy1_ref,
                                    self.__attributes_as_dictionary[self.__attr_policy2_ref]:
                                        policy2_ref,
                                    self.__attributes_as_dictionary[self.__attr_flag]:
                                        flag}

        return (DbProxy.get_instance()).write(self.__tbl, attributes_as_dictionary)

    def update(self, old_policy_ref: int = None, old_policy1_ref: int = None, old_policy2_ref: int = None,
               old_flag: int = None, new_policy1_ref: int = None, new_policy2_ref: int = None,
               new_flag: int = None):
        """
        Update users in the db.
        old_<attribute> will composite a constraint of where to update.
        example(if old_username != ""), it will composite the constraint-
                                                where(user.username == old_username).
        new_<attribute> will update the <attribute> to the new value.
        example(if new_username != ""), it will update-
                                                update(user.username = new_username).

        :return: the number of updated rows.
        """
        const_lst = []
        if not (old_policy_ref is None):
            const_lst.append(Expression(self.__tbl.policy_ref, OP.EQ, old_policy_ref))
        if not (old_policy1_ref is None):
            const_lst.append(Expression(self.__tbl.policy1_ref, OP.EQ, old_policy1_ref))
        if not (old_policy2_ref is None):
            const_lst.append(Expression(self.__tbl.policy2_ref, OP.EQ, old_policy2_ref))
        if not (old_flag is None):
            const_lst.append(Expression(self.__tbl.flag, OP.EQ,
                                        old_flag))
        where_expr = and_exprs(const_lst)

        attributes_as_dictionary = {}
        if not (new_policy1_ref == ""):
            attributes_as_dictionary[self.__attributes_as_dictionary[self.__attr_policy1_ref]] = \
                new_policy1_ref
        if not (new_policy2_ref is None):
            attributes_as_dictionary[self.__attributes_as_dictionary[self.__attr_policy2_ref]] = \
                new_policy2_ref
        if not (new_flag is None):
            attributes_as_dictionary[self.__attributes_as_dictionary[self.__attr_flag]] = \
                old_flag

        if len(attributes_as_dictionary) == 0:
            raise AttributeError("Nothing to update")

        return DbProxy.get_instance().update(self.__tbl, attributes_as_dictionary, where_expr)

    def delete(self, policy_ref: int = None, policy1_ref: int = None, policy2_ref: int = None,
               flag: int = None):
        """
        Delete users from the DB.
        <attribute> will composite a constraint of where to delete.
        example(if old_username != ""), it will composite the constraint-
                                               where(user.username == username).

        :return: the number of deleted rows.
        """
        const_lst = []
        if not (policy_ref is None):
            const_lst.append(Expression(self.__tbl.policy_ref, OP.EQ, policy_ref))
        if not (policy1_ref is None):
            const_lst.append(Expression(self.__tbl.policy1_ref, OP.EQ, policy1_ref))
        if not (policy2_ref is None):
            const_lst.append(Expression(self.__tbl.policy2_ref, OP.EQ, policy2_ref))
        if not (flag is None):
            const_lst.append(Expression(self.__tbl.flag, OP.EQ, flag))
        where_expr = and_exprs(const_lst)

        return (DbProxy.get_instance()).delete(self.__tbl, where_expr=where_expr)
