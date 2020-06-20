import os

from peewee import *

abs_path = os.path.dirname(os.path.abspath(__file__))
test_rel_path = os.path.join(abs_path, 'testing.db')
project_rel_path = os.path.join(abs_path, 'project.db')

# Use test_rel_path while testing only.
rel_path = test_rel_path
database = SqliteDatabase(rel_path, pragmas={'journal_mode': 'wal', 'foreign_keys': 1})


def create_tables():
    """
    Should happen once, only when the DB is empty.
    """
    return database.create_tables([User, Store, Product, StoreManagerAppointment])


class BaseModel(Model):
    class Meta:
        database = database


class User(BaseModel):
    """
    table: user
    """
    username = CharField(primary_key=True)
    password = CharField(null=False)
    is_system_manager = BooleanField(null=False, default=False)


class Store(BaseModel):
    """
    table: store
    """
    store_name = CharField(unique=True, null=False, primary_key=True)
    founder_username = ForeignKeyField(User, deferrable="INITIALLY DEFERRED", db_column="founder_username",
                                       to_field="username", on_delete="Cascade", on_update="Cascade")


class Product(BaseModel):
    """
    table: product
    """
    product_name = CharField(null=False)
    store_name = ForeignKeyField(Store, db_column="store_name", on_delete="Cascade", on_update="Cascade")
    price = FloatField(null=False)
    category = CharField(null=False)
    amount = IntegerField(null=False)
    purchase_type = IntegerField(null=False)

    class Meta:
        primary_key = CompositeKey("product_name", "store_name")


class StoreManagerAppointment(BaseModel):
    """
    table: store manager appointments
    """
    appointee_username = ForeignKeyField(User, db_column="appointee_username", on_delete="Cascade",
                                         on_update="Cascade")
    store_name = ForeignKeyField(Store, db_column="store_name", on_delete="Cascade", on_update="Cascade")
    appointer_username = ForeignKeyField(User, db_column="appointer_username", on_delete="Cascade",
                                         on_update="Cascade")
    can_edit_inventory = BooleanField(null=False, default=False)
    can_edit_policies = BooleanField(null=False, default=False)
    can_appoint_owner = BooleanField(null=False, default=False)
    can_delete_owner = BooleanField(null=False, default=False)
    can_appoint_manager = BooleanField(null=False, default=False)
    can_edit_manager_permissions = BooleanField(null=False, default=False)
    can_delete_manager = BooleanField(null=False, default=False)
    can_close_store = BooleanField(null=False, default=False)
    can_answer_user_questions = BooleanField(null=False, default=False)
    can_watch_purchase_history = BooleanField(null=False, default=False)

    class Meta:
        primary_key = CompositeKey("appointee_username", "store_name")

