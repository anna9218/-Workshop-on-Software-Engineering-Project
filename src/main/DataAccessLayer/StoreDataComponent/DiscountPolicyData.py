from datetime import datetime
from peewee import Expression, OP
from src.Logger import errorLogger
from src.main.DataAccessLayer.ConnectionProxy.Tables import DiscountPolicy, CompositeDiscountPolicy, \
    ConditionalDiscountPolicy
from src.main.DataAccessLayer.ConnectionProxy.DbProxy import DbProxy, and_exprs
import jsonpickle

"""
Represent the table of stores.
NOT the domain stores.
"""


class DiscountPolicyData:
    __instance = None

    @staticmethod
    def get_instance():
        """ Static access method. """
        if DiscountPolicyData.__instance is None:
            DiscountPolicyData()
        return DiscountPolicyData.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if DiscountPolicyData.__instance is not None:
            errorLogger("This class is a singleton!")
            raise Exception("This class is a singleton!")
        else:
            self.__tbl = DiscountPolicy
            self.__attr_discount_policy_id = "discount_policy_id"
            self.__attr_policy_name = "policy_name"
            self.__attr_store_name = "store_name"
            self.__attr_product_name = "product_name"
            self.__attr_percentage = "percentage"
            self.__attr_valid_until = "valid_until"
            self.__attr_is_active = "is_active"
            self.__attributes_as_dictionary = {self.__attr_discount_policy_id: self.__tbl.discount_policy_id,
                                               self.__attr_policy_name: self.__tbl.policy_name,
                                               self.__attr_store_name: self.__tbl.store_name,
                                               self.__attr_product_name: self.__tbl.product_name,
                                               self.__attr_percentage: self.__tbl.percentage,
                                               self.__attr_valid_until: self.__tbl.valid_until,
                                               self.__attr_is_active: self.__tbl.is_active}
            DiscountPolicyData.__instance = self

    def read(self, attributes_to_read: [str], discount_policy_id: int = None, policy_name: str = "",
                               store_name="", product_name: str = "", percentage: float = None,
                               valid_until: datetime = None, is_active: bool = None,
                               precondition_product: str = "", precondition_min_amount: int = None,
                               precondition_min_basket_price: int = None,
                               policy1_ref: str = "", policy2_ref: str = "", flag: int = None):
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
            attributes_to_read.insert(len(attributes_to_read), 'precondition_product')
            attributes_to_read.insert(len(attributes_to_read), 'precondition_min_amount')
            attributes_to_read.insert(len(attributes_to_read), 'precondition_min_basket_price')
            attributes_to_read.insert(len(attributes_to_read), 'policy1_ref')
            attributes_to_read.insert(len(attributes_to_read), 'policy2_ref')
            attributes_to_read.insert(len(attributes_to_read), 'flag')
            # attributes_to_read.remove(self.__attr_discount_policy_id)

        const_lst = []
        if not (discount_policy_id is None):
            const_lst.append(Expression(self.__tbl.discount_policy_id, OP.EQ, discount_policy_id))
        if not (policy_name == ""):
            const_lst.append(Expression(self.__tbl.policy_name, OP.EQ, policy_name))
        if not (store_name == ""):
            const_lst.append(Expression(self.__tbl.store_name, OP.EQ, store_name))
        if not (product_name == ""):
            const_lst.append(Expression(self.__tbl.product_name, OP.EQ, product_name))
        if not (percentage is None):
            const_lst.append(Expression(self.__tbl.percentage, OP.EQ, percentage))
        if not (valid_until is None):
            const_lst.append(Expression(self.__tbl.valid_until, OP.EQ, valid_until))
        if not (is_active is None):
            const_lst.append(Expression(self.__tbl.is_active, OP.EQ, is_active))
        if not (policy1_ref is None):
            const_lst.append(Expression(CompositeDiscountPolicy.policy1_ref, OP.EQ, policy1_ref))
        if not (policy2_ref is None):
            const_lst.append(Expression(CompositeDiscountPolicy.policy2_ref, OP.EQ, policy2_ref))
        if not (flag is None):
            const_lst.append(Expression(CompositeDiscountPolicy.flag, OP.EQ, flag))
        if not (precondition_product == ""):
            const_lst.append(Expression(ConditionalDiscountPolicy.precondition_product, OP.EQ, precondition_product))
        if not (precondition_min_amount is None):
            const_lst.append(Expression(ConditionalDiscountPolicy.precondition_min_amount, OP.EQ, precondition_min_amount))
        if not (precondition_min_basket_price is None):
            const_lst.append(Expression(ConditionalDiscountPolicy.precondition_min_basket_price, OP.EQ, precondition_min_basket_price))
        where_expr = and_exprs(const_lst)

        result = (DbProxy.get_instance()).read_discount_policies(where_expr)
        output_lst = []
        for data_obj in result:
            data_as_dictionary = {}
            if self.__attr_discount_policy_id in attributes_to_read:
                data_as_dictionary[self.__attr_discount_policy_id] = data_obj.discount_policy_id
            if self.__attr_policy_name in attributes_to_read:
                data_as_dictionary[self.__attr_policy_name] = data_obj.policy_name
            if self.__attr_store_name in attributes_to_read:
                data_as_dictionary[self.__attr_store_name] = data_obj.store_name
            if self.__attr_product_name in attributes_to_read:
                data_as_dictionary[self.__attr_product_name] = data_obj.product_name
            if self.__attr_percentage in attributes_to_read:
                data_as_dictionary[self.__attr_percentage] = data_obj.percentage
            if self.__attr_valid_until in attributes_to_read:
                data_as_dictionary[self.__attr_valid_until] = data_obj.valid_until
            if self.__attr_is_active in attributes_to_read:
                data_as_dictionary[self.__attr_is_active] = data_obj.is_active
            if "precondition_product" in attributes_to_read:
                data_as_dictionary["precondition_product"] = data_obj.precondition_product
            if "precondition_min_amount" in attributes_to_read:
                data_as_dictionary["precondition_min_amount"] = data_obj.precondition_min_amount
            if "precondition_min_basket_price" in attributes_to_read:
                data_as_dictionary["precondition_min_basket_price"] = data_obj.precondition_min_basket_price
            if "policy1_ref" in attributes_to_read:
                data_as_dictionary["policy1_ref"] = (DbProxy.get_instance()).read_discount_policies(Expression(self.__tbl.discount_policy_id, OP.EQ, data_obj.policy1_ref.discount_policy_id))
            if "policy2_ref" in attributes_to_read:
                data_as_dictionary["policy2_ref"] = (DbProxy.get_instance()).read_discount_policies(Expression(self.__tbl.discount_policy_id, OP.EQ, data_obj.policy2_ref.discount_policy_id))
            if "flag" in attributes_to_read:
                data_as_dictionary["flag"] = data_obj.flag
            output_lst.append(data_as_dictionary)

        return output_lst

    def write(self, policy_name: str, store_name: str, product_name: str, percentage: float, valid_until: datetime,
              is_active: bool = True):
        """
        Write a store to db.

        :param store_name:
        :param founder_username:
        :return: size of user tbl after inserting the new one.
        """
        attributes_as_dictionary = {self.__attributes_as_dictionary[self.__attr_policy_name]: policy_name,
                                    self.__attributes_as_dictionary[self.__attr_store_name]: store_name,
                                    self.__attributes_as_dictionary[self.__attr_product_name]: product_name,
                                    self.__attributes_as_dictionary[self.__attr_percentage]: percentage,
                                    self.__attributes_as_dictionary[self.__attr_valid_until]: valid_until,
                                    self.__attributes_as_dictionary[self.__attr_is_active]: is_active}

        return (DbProxy.get_instance()).write(self.__tbl, attributes_as_dictionary)

    def update(self, old_discount_policy_id: int = None, old_policy_name: str = "",
               old_store_name: str = "", old_product_name: str = "", old_percentage: float = None,
               old_valid_until: datetime = None, old_is_active: bool = None,
               new_policy_name: str = "",
               new_store_name="", new_product_name: str = "", new_percentage: float = None,
               new_valid_until: datetime = None, new_is_active: bool = None):
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
        if not (old_discount_policy_id is None):
            const_lst.append(Expression(self.__tbl.discount_policy_id, OP.EQ, old_discount_policy_id))
        if not (old_policy_name == ""):
            const_lst.append(Expression(self.__tbl.policy_name, OP.EQ, old_policy_name))
        if not (old_store_name == ""):
            const_lst.append(Expression(self.__tbl.store_name, OP.EQ, old_store_name))
        if not (old_product_name == ""):
            const_lst.append(Expression(self.__tbl.product_name, OP.EQ, old_product_name))
        if not (old_percentage is None):
            const_lst.append(Expression(self.__tbl.percentage, OP.EQ, old_percentage))
        if not (old_valid_until is None):
            const_lst.append(Expression(self.__tbl.valid_until, OP.EQ, old_valid_until))
        if not (old_is_active is None):
            const_lst.append(Expression(self.__tbl.is_active, OP.EQ, old_is_active))
        where_expr = and_exprs(const_lst)

        attributes_as_dictionary = {}
        if not (new_policy_name == ""):
            attributes_as_dictionary[self.__attributes_as_dictionary[self.__attr_policy_name]] = new_policy_name
        if not (new_store_name == ""):
            attributes_as_dictionary[self.__attributes_as_dictionary[self.__attr_store_name]] = new_store_name
        if not (new_product_name == ""):
            attributes_as_dictionary[self.__attributes_as_dictionary[self.__attr_product_name]] = new_product_name
        if not (new_percentage is None):
            attributes_as_dictionary[self.__attributes_as_dictionary[self.__attr_percentage]] = new_percentage
        if not (new_valid_until is None):
            attributes_as_dictionary[self.__attributes_as_dictionary[self.__attr_valid_until]] = new_valid_until
        if not (new_is_active is None):
            attributes_as_dictionary[self.__attributes_as_dictionary[self.__attr_is_active]] = new_is_active

        if len(attributes_as_dictionary) == 0:
            raise AttributeError("Nothing to update")

        return DbProxy.get_instance().update(self.__tbl, attributes_as_dictionary, where_expr)

    def delete(self, discount_policy_id: int = None, policy_name: str = "",
               store_name="", product_name: str = "", percentage: float = None, valid_until: datetime = None,
               is_active: bool = None):
        """
        Delete users from the DB.
        <attribute> will composite a constraint of where to delete.
        example(if old_username != ""), it will composite the constraint-
                                               where(user.username == username).

        :return: the number of deleted rows.
        """
        const_lst = []
        if not (discount_policy_id is None):
            const_lst.append(Expression(self.__tbl.discount_policy_id, OP.EQ, discount_policy_id))
        if not (policy_name == ""):
            const_lst.append(Expression(self.__tbl.policy_name, OP.EQ, policy_name))
        if not (store_name == ""):
            const_lst.append(Expression(self.__tbl.store_name, OP.EQ, store_name))
        if not (product_name == ""):
            const_lst.append(Expression(self.__tbl.product_name, OP.EQ, product_name))
        if not (percentage is None):
            const_lst.append(Expression(self.__tbl.percentage, OP.EQ, percentage))
        if not (valid_until is None):
            const_lst.append(Expression(self.__tbl.valid_until, OP.EQ, valid_until))
        if not (is_active is None):
            const_lst.append(Expression(self.__tbl.is_active, OP.EQ, is_active))
        where_expr = and_exprs(const_lst)
        return (DbProxy.get_instance()).delete(self.__tbl, where_expr=where_expr)
