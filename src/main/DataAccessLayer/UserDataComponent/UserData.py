from peewee import Expression, OP
from src.Logger import errorLogger
from src.main.DataAccessLayer.ConnectionProxy.RealDb import RealDb
from src.main.DataAccessLayer.ConnectionProxy.DbProxy import DbProxy, and_exprs

"""
Represent the table of users.
NOT the domain users.
"""

class UserData:
    __instance = None

    @staticmethod
    def get_instance():
        """ Static access method. """
        if UserData.__instance is None:
            UserData()
        return UserData.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if UserData.__instance is not None:
            errorLogger("This class is a singleton!")
            raise Exception("This class is a singleton!")
        else:
            self.__tbl = RealDb.User
            self.__attr_username = "username"
            self.__attr_password = "password"
            self.__attr_is_system_manager = "is_system_manager"
            self.__attributes_as_dictionary = {self.__attr_username: self.__tbl.username,
                                               self.__attr_password: self.__tbl.password,
                                               self.__attr_is_system_manager: self.__tbl.is_system_manager}
            UserData.__instance = self

    def read(self, attributes_to_read: [str], username: str = "", password: str = "", is_system_manager: bool = None):
        """
        Read users from db.
        Raise exception if an attribute in attributes_to_read is illegal.
        <attribute> will composite a constraint of where to read.
        example(if old_username != ""), it will composite the constraint-
                                               where(user.username == username).

        :param attributes_to_read: the list of attributes that will return from the db.
                                    type: [str]
        :param username: pk
        :param password:
        :param is_system_manager:
        :return: list of dictionaries that contain attributes_to_read fields.
        """
        if len(attributes_to_read) > 0:
            for attribute in attributes_to_read:
                if attribute.lower() not in self.__attributes_as_dictionary.keys():
                    raise AttributeError("Attribute " + attribute + " doesn't exist in " + str(type(self.__tbl)) + ".")
        else:
            attributes_to_read = [self.__attr_username, self.__attr_password, self.__attr_is_system_manager]

        const_lst = []
        if not (username == ""):
            const_lst.append(Expression(self.__tbl.username, OP.EQ, username))
        if not (password == ""):
            const_lst.append(Expression(self.__tbl.password, OP.EQ, password))
        if is_system_manager is not None:
            const_lst.append(Expression(self.__tbl.is_system_manager, OP.EQ, is_system_manager))
        where_expr = and_exprs(const_lst)

        result = (DbProxy.get_instance()).read(self.__tbl, where_expr=where_expr)
        output_lst = []
        for data_obj in result:
            user_data_as_dictionary = {}
            if self.__attr_username in attributes_to_read:
                user_data_as_dictionary[self.__attr_username] = data_obj.username
            if self.__attr_password in attributes_to_read:
                user_data_as_dictionary[self.__attr_password] = data_obj.password
            if self.__attr_is_system_manager in attributes_to_read:
                user_data_as_dictionary[self.__attr_is_system_manager] = data_obj.is_system_manager
            output_lst.append(user_data_as_dictionary)

        return output_lst

    def write(self, username: str, password: str, is_system_manager: bool = False):
        """
        Write a user to db.

        :param username: pk
        :param password: user password.
        :param is_system_manager:
        :return: size of user tbl after inserting the new one.
        """
        attributes_as_dictionary = {self.__attributes_as_dictionary[self.__attr_username]: username,
                                    self.__attributes_as_dictionary[self.__attr_password]: password,
                                    self.__attributes_as_dictionary[self.__attr_is_system_manager]: is_system_manager}

        return (DbProxy.get_instance()).write(self.__tbl, attributes_as_dictionary)

    def update(self, old_username: str = "", old_password: str = "", old_is_system_manager: bool = None,
               new_username: str = "", new_password: str = "", new_is_system_manager: bool = None):
        """
        Update users in the db.
        old_<attribute> will composite a constraint of where to update.
        example(if old_username != ""), it will composite the constraint-
                                                where(user.username == old_username).
        new_<attribure> will update the <attribute> to the new value.
        example(if new_username != ""), it will update-
                                                update(user.username = new_username).


        :param old_username: pk. will composite a constraint on the username.
        :param old_password: will composite a constraint on the password.
        :param old_is_system_manager: will composite a constraint on the is_system_manager.
        :param new_username: pk. will update the username to the new value.
        :param new_password: will update the password to the new value.
        :param new_is_system_manager: will update the is_system_manager to the new value.
        :return: the number of updated rows.
        """
        const_lst = []
        if not (old_username == ""):
            const_lst.append(Expression(self.__tbl.username, OP.EQ, old_username))
        if not (old_password == ""):
            const_lst.append(Expression(self.__tbl.password, OP.EQ, old_password))
        if old_is_system_manager is not None:
            const_lst.append(Expression(self.__tbl.is_system_manager, OP.EQ, old_is_system_manager))
        where_expr = and_exprs(const_lst)

        attributes_as_dictionary = {}
        if not (new_username == ""):
            attributes_as_dictionary[self.__attributes_as_dictionary[self.__attr_username]] = new_username
        if not (new_password == ""):
            attributes_as_dictionary[self.__attributes_as_dictionary[self.__attr_password]] = new_password
        if new_is_system_manager is not None:
            attributes_as_dictionary[self.__attributes_as_dictionary[self.__attr_is_system_manager]] = \
                new_is_system_manager

        if len(attributes_as_dictionary) == 0:
            raise AttributeError("Nothing to update")

        return DbProxy.get_instance().update(self.__tbl, attributes_as_dictionary, where_expr)

    def delete(self, username: str = "", password: str = "", is_system_manager: bool = None):
        """
        Delete users from the DB.
        <attribute> will composite a constraint of where to delete.
        example(if old_username != ""), it will composite the constraint-
                                               where(user.username == username).

        :param username: pk. will composite a constraint of where to update.
        :param password: will composite a constraint of where to update.
        :param is_system_manager: will composite a constraint of where to update.
        :return: the number of deleted rows.
        """
        const_lst = []
        if not (username == ""):
            const_lst.append(Expression(self.__tbl.username, OP.EQ, username))
        if not (password == ""):
            const_lst.append(Expression(self.__tbl.password, OP.EQ, password))
        if is_system_manager is not None:
            const_lst.append(Expression(self.__tbl.is_system_manager, OP.EQ, is_system_manager))
        where_expr = and_exprs(const_lst)

        return (DbProxy.get_instance()).delete(self.__tbl, where_expr=where_expr)
