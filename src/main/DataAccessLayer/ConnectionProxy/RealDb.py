import os
from peewee import Expression, ModelObjectCursorWrapper
from src.Logger import logger
from src.main.ResponseFormat import ret
from src.main.DataAccessLayer.ConnectionProxy.DbSubject import DbSubject
from peewee import *

# abs_path = os.path.dirname(os.path.abspath(__file__))
# test_rel_path = os.path.join(abs_path, 'testing.db')
# project_rel_path = os.path.join(abs_path, 'project.db')
#
# # Use test_rel_path while testing only.
# rel_path = test_rel_path
# database = SqliteDatabase(rel_path, pragmas={'journal_mode': 'wal'})
from src.main.DataAccessLayer.ConnectionProxy.Tables import database, create_tables,  User, Store, Product


class RealDb(DbSubject):

    def __init__(self):
        super().__init__()

    def create_tables(self):
        """
        Should happen once, only when the DB is empty.
        """
        return database.create_tables([User, Store, Product])

    # class BaseModel(Model):
    #     class Meta:
    #         database = database
    #
    # class User(BaseModel):
    #     """
    #     table: user
    #     """
    #     username = CharField(primary_key=True)
    #     password = CharField(null=False)
    #     is_system_manager = BooleanField(null=False, default=False)
    #
    # class Store(BaseModel):
    #     """
    #     table: store
    #     """
    #     store_name = CharField(primary_key=True)
    #     founder_username = ForeignKeyField(User, backref="username", on_delete="Cascade", on_update="Cascade")
    #
    # class Product(BaseModel):
    #     """
    #     table: product
    #     """
    #     product_name = CharField(primary_key=True)
    #     store_name = ForeignKeyField(Store, backref="store_name", primary_key=True,  on_delete="Cascade",
    #                                  on_update="Cascade")
    #     founder_username = ForeignKeyField(User, backref="username", on_delete="Cascade", on_update="Cascade")

    @logger
    def connect(self):
        try:
            return database.connect(reuse_if_open=True)
        except Exception:
            raise DatabaseError("Can't open connection to db.")

    @logger
    def disconnect(self):
        try:
            return database.close()
        except Exception:
            raise DatabaseError("Can't close connection to db.")

    @logger
    def is_connected(self) -> bool:
        try:
            return not database.is_closed()
        except Exception:
            return False

    def read(self, tbl, where_expr: Expression = None):
        """

        :param tbl: read from tbl table.
        :param where_expr: where to read.
        :return: list of RealDb.tbl
        """
        return tbl.select().where(where_expr).execute()

    def write(self, tbl, attributes_as_dictionary: {}):
        """

        :param tbl: write to tbl table
        :param attributes_as_dictionary: a dictionary of attribute(not type str!) as key, and <value> as value.
        :return: size of RealDb.tbl(I think)
        """
        return tbl.insert(attributes_as_dictionary)

    def update(self, tbl, attributes_as_dictionary: {}, where_expr: Expression):
        """
        TODO: Can update pk. Maybe block this option.

        :param tbl: update tbl table
        :param attributes_as_dictionary: a dictionary of attribute(not type str!) as key, and <value> as value.
        :param where_expr: where to update.
        :return: number of updated rows.
        """
        return tbl.update(attributes_as_dictionary).where(where_expr)

    def delete(self, tbl, where_expr: Expression):
        """

        :param tbl: delete from tbl table
        :param where_expr: where to delete.
        :return: number of updated rows.
        """
        return tbl.delete().where(where_expr)

    def execute(self, queries: []):
        with database.atomic() as transaction:  # Opens new transaction.
            try:
                for query in queries:
                    query.execute()
                return ret(True, "Successful.")
            except Exception as e:
                transaction.rollback()
                print(e)
                return ret(False, "Failed.")
