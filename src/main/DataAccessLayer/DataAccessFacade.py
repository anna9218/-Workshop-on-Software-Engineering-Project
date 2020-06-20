from src.Logger import errorLogger, logger, loggerStaticMethod
from src.main.DataAccessLayer.ConnectionProxy.DbProxy import DbProxy
from src.main.DataAccessLayer.UserDataComponent.UserData import UserData

"""
This class is the facade class for the DA layer.

It should contain 4 function for each persistent domain object: read, write, update and delete.
read = select query.
write = insert query.
update = update query.
delete = delete query.

Our persistent domain objects:
    store component:
        Purchase policy
        Discount policy
        Product
        Purchase
        Store
        Store inventory
        Store manager appointment
    user component:
        Shopping cart
        Shopping basket
        User(only subscribers).
"""


class DataAccessFacade:
    # TODO: maybe add try-catch for each function.
    __instance = None

    @staticmethod
    def get_instance():
        """ Static access method. """
        loggerStaticMethod("DataAccessFacade.get_instance", [])
        if DataAccessFacade.__instance is None:
            DataAccessFacade()
        return DataAccessFacade.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if DataAccessFacade.__instance is not None:
            errorLogger("This class is a singleton!")
            raise Exception("This class is a singleton!")
        else:
            self.__proxy = DbProxy()
            self.__proxy.connect()
            DataAccessFacade.__instance = self

    @logger
    def get_proxy(self):
        return self.__proxy

    @logger
    def write_user(self, username: str, password: str, is_system_manager: bool = False):
        """
        Write a user to db.

        :param username: pk
        :param password: user password.
        :param is_system_manager:
        :return: size of user tbl after inserting the new one.
        """
        return UserData.get_instance().write(username, password, is_system_manager)

    @logger
    def read_users(self, attributes_to_read=None, username: str = "", password: str = "",
                   is_system_manager: bool = None):
        """
        Read users from db.
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
        if attributes_to_read is None:
            attributes_to_read = []
        return UserData.get_instance().read(attributes_to_read, username, password, is_system_manager)

    @logger
    def update_users(self, old_username: str = "", old_password: str = "", old_is_system_manager: bool = None,
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
        return UserData.get_instance().update(old_username,
                                              old_password,
                                              old_is_system_manager,
                                              new_username,
                                              new_password,
                                              new_is_system_manager)

    @logger
    def delete_users(self, username: str = "", password: str = "", is_system_manager: bool = None):
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
        return UserData.get_instance().delete(username, password, is_system_manager)

    def __repr__(self):
        return repr("DataAccessFacade")