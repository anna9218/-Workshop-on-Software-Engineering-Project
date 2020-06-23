from peewee import Expression, OP
from src.Logger import errorLogger
from src.main.DataAccessLayer.ConnectionProxy.Tables import ProductsInBasket
from src.main.DataAccessLayer.ConnectionProxy.DbProxy import DbProxy, and_exprs

"""
Represent the table of products in basket.
This class is the equivalence to both Domain.ShoppingBasket AND Domain.ShoppingCart.
"""


class ProductsInBasketData:
    __instance = None

    @staticmethod
    def get_instance():
        """ Static access method. """
        if ProductsInBasketData.__instance is None:
            ProductsInBasketData()
        return ProductsInBasketData.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if ProductsInBasketData.__instance is not None:
            errorLogger("This class is a singleton!")
            raise Exception("This class is a singleton!")
        else:
            self.__tbl = ProductsInBasket
            self.__attr_username = "username"
            self.__attr_product_ref = "product_ref"
            self.__attr_amount = "amount"
            self.__attributes_as_dictionary = {self.__attr_username: self.__tbl.username,
                                               self.__attr_product_ref: self.__tbl.product_ref,
                                               self.__attr_amount: self.__tbl.amount}
            ProductsInBasketData.__instance = self

    def read(self, attributes_to_read: [str], username: str = "", product_ref: int = None, amount: int = None):
        """
        Read products in baskets from db.
        Raise exception if an attribute in attributes_to_read is illegal.
        <attribute> will composite a constraint of where to read.
        example(if old_username != ""), it will composite the constraint-
                                               where(user.username == username).

        :param username: pk.
        :param product_ref: pk.
        :param amount:
        :param attributes_to_read: the list of attributes that will return from the db.
                                    type: [str]

        :return: list of dictionaries that contain attributes_to_read fields.
        """
        if len(attributes_to_read) > 0:
            for attribute in attributes_to_read:
                if attribute.lower() not in self.__attributes_as_dictionary.keys():
                    raise AttributeError("Attribute " + attribute + " doesn't exist in " + str(type(self.__tbl)) + ".")
        else:
            attributes_to_read = list(self.__attributes_as_dictionary.keys())

        const_lst = []
        if not (username == ""):
            const_lst.append(Expression(self.__tbl.username, OP.EQ, username))
        if not (product_ref is None):
            const_lst.append(Expression(self.__tbl.product_ref, OP.EQ, product_ref))
        if not (amount is None):
            const_lst.append(Expression(self.__tbl.amount, OP.EQ, amount))
        where_expr = and_exprs(const_lst)

        result = (DbProxy.get_instance()).read(self.__tbl, where_expr=where_expr)
        output_lst = []
        for data_obj in result:
            user_data_as_dictionary = {}
            if self.__attr_username in attributes_to_read:
                user_data_as_dictionary[self.__attr_username] = data_obj.username.username
            if self.__attr_product_ref in attributes_to_read:
                user_data_as_dictionary["store_name"] = data_obj.product_ref.store_name.store_name
                user_data_as_dictionary["product_name"] = data_obj.product_ref.product_name
            if self.__attr_amount in attributes_to_read:
                user_data_as_dictionary[self.__attr_amount] = data_obj.amount
            output_lst.append(user_data_as_dictionary)

        return output_lst

    def write(self, username: str, product_ref: int, amount: int):
        """
        Write a products in basket to db.

        :param username:
        :param product_ref:
        :param amount:
        :return: size of user tbl after inserting the new one.
        """
        attributes_as_dictionary = {self.__attributes_as_dictionary[self.__attr_username]: username,
                                    self.__attributes_as_dictionary[self.__attr_product_ref]: product_ref,
                                    self.__attributes_as_dictionary[self.__attr_amount]: amount}

        return (DbProxy.get_instance()).write(self.__tbl, attributes_as_dictionary)

    def update(self, old_username: str = "", old_product_ref: int = None, old_amount: int = None,
               new_username: str = "", new_product_ref: int = None, new_amount: int = None):
        """
        Update products in baskets in the db.
        old_<attribute> will composite a constraint of where to update.
        example(if old_username != ""), it will composite the constraint-
                                                where(user.username == old_username).
        new_<attribute> will update the <attribute> to the new value.
        example(if new_username != ""), it will update-
                                                update(user.username = new_username).

        :return: the number of updated rows.
        """
        const_lst = []
        if not (old_username == ""):
            const_lst.append(Expression(self.__tbl.username, OP.EQ, old_username))
        if not (old_product_ref is None):
            const_lst.append(Expression(self.__tbl.product_ref, OP.EQ, old_product_ref))
        if not (old_amount is None):
            const_lst.append(Expression(self.__tbl.amount, OP.EQ, old_amount))
        where_expr = and_exprs(const_lst)

        attributes_as_dictionary = {}
        if not (new_username == ""):
            attributes_as_dictionary[self.__attributes_as_dictionary[self.__attr_username]] = new_username
        if not (new_product_ref is None):
            attributes_as_dictionary[self.__attributes_as_dictionary[self.__attr_product_ref]] = new_product_ref
        if not (new_amount is None):
            attributes_as_dictionary[self.__attributes_as_dictionary[self.__attr_amount]] = new_amount

        if len(attributes_as_dictionary) == 0:
            raise AttributeError("Nothing to update")

        return DbProxy.get_instance().update(self.__tbl, attributes_as_dictionary, where_expr)

    def delete(self, username: str = "", product_ref: int = None, amount: int = None):
        """
        Delete products in baskets from the DB.
        <attribute> will composite a constraint of where to delete.
        example(if old_username != ""), it will composite the constraint-
                                               where(user.username == username).

        :return: the number of deleted rows.
        """
        const_lst = []
        if not (username == ""):
            const_lst.append(Expression(self.__tbl.username, OP.EQ, username))
        if not (product_ref is None):
            const_lst.append(Expression(self.__tbl.product_ref, OP.EQ, product_ref))
        if not (amount is None):
            const_lst.append(Expression(self.__tbl.amount, OP.EQ, amount))
        where_expr = and_exprs(const_lst)
        return (DbProxy.get_instance()).delete(self.__tbl, where_expr=where_expr)
