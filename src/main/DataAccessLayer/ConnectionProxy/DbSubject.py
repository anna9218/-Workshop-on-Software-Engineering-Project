# from __future__ import annotations
from abc import ABC, abstractmethod
from peewee import Expression


class DbSubject(ABC):

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def create_tables(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass

    @abstractmethod
    def is_connected(self) -> bool:
        pass

    @abstractmethod
    def read(self, tbl, where_expr: Expression = None):
        pass

    @abstractmethod
    def write(self, tbl, attributes_as_dictionary: {}):
        pass

    @abstractmethod
    def update(self, tbl, attributes_as_dictionary: {}, where_expr: Expression):
        pass

    @abstractmethod
    def delete(self, tbl, where_expr: Expression):
        pass

    @abstractmethod
    def execute(self, queries):
        pass

    # @abstractmethod
    # def read_discount_policies(self, where_expresion: {} = None):
    #     pass

    @abstractmethod
    def execute_atomic_purchase_write(self, mother_write_query, daughters_write_queries_attributes: [{}],
                                      other_update_stoke_queries: [], other_update_basket_queries: []):
        pass
