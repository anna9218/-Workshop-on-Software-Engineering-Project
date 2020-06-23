from peewee import Expression, OP
from src.Logger import errorLogger, loggerStaticMethod, logger
from src.main.DataAccessLayer.ConnectionProxy.DbSubject import DbSubject
from src.main.DataAccessLayer.ConnectionProxy.RealDb import RealDb
from src.main.ResponseFormat import ret


def and_exprs(const_lst: [Expression]):
    if len(const_lst) <= 0:
        return None

    if len(const_lst) == 1:
        return const_lst[0]

    expr: Expression = Expression(const_lst[0], OP.AND, const_lst[1])
    for i in range(2, len(const_lst)):
        expr = Expression(expr, OP.AND, const_lst[i])

    return expr


class DbProxy(DbSubject):
    __instance = None
    __realSubject = RealDb()

    @staticmethod
    def get_instance() -> DbSubject:
        """ Static access method. """
        loggerStaticMethod("FacadeDelivery.get_instance", [])
        if DbProxy.__instance is None:
            DbProxy()
        return DbProxy.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if DbProxy.__instance is not None:
            errorLogger("This class is a singleton!")
            raise Exception("This class is a singleton!")
        else:
            super().__init__()
            self.__isConnected = False
            if DbProxy.__realSubject:
                DbProxy.__instance = self
                self.__real_doesnt_exist_error_msg = "We having some tech problems, but we will rise again!"
                self.__realSubject.connect()
                self.__realSubject.create_tables()
            else:
                DbProxy.__instance = self

    @logger
    def connect(self):
        if not self.has_real_subject():
            return ret(False, self.__real_doesnt_exist_error_msg)
        return self.__realSubject.connect()

    @logger
    def disconnect(self):
        if not self.has_real_subject():
            return ret(False, self.__real_doesnt_exist_error_msg)
        return self.__realSubject.disconnect()

    @logger
    def is_connected(self) -> bool:
        if not self.has_real_subject():
            return ret(False, self.__real_doesnt_exist_error_msg)
        return self.__realSubject.is_connected()

    def create_tables(self):
        pass

    def has_real_subject(self):
        return not (self.__realSubject is None)

    def read(self, tbl, where_expr: Expression = None):
        if not self.has_real_subject():
            return ret(False, self.__real_doesnt_exist_error_msg)
        if not self.__realSubject.is_connected():
            return ret(False, self.__real_doesnt_exist_error_msg)
        return self.__realSubject.read(tbl, where_expr)

    def write(self, tbl, attributes_as_dictionary: {}):
        if not self.has_real_subject():
            return ret(False, self.__real_doesnt_exist_error_msg)
        if not self.__realSubject.is_connected():
            return ret(False, self.__real_doesnt_exist_error_msg)
        return self.__realSubject.write(tbl, attributes_as_dictionary)

    def update(self, tbl, attributes_as_dictionary: {}, where_expr: Expression):
        if not self.has_real_subject():
            return ret(False, self.__real_doesnt_exist_error_msg)
        if not self.__realSubject.is_connected():
            return ret(False, self.__real_doesnt_exist_error_msg)
        return self.__realSubject.update(tbl, attributes_as_dictionary, where_expr)

    def delete(self, tbl, where_expr: Expression):
        if not self.has_real_subject():
            return ret(False, self.__real_doesnt_exist_error_msg)
        if not self.__realSubject.is_connected():
            return ret(False, self.__real_doesnt_exist_error_msg)
        return self.__realSubject.delete(tbl, where_expr)

    # def read_discount_policies(self, where_expresion: {} = None):
    #     if not self.has_real_subject():
    #         return ret(False, self.__real_doesnt_exist_error_msg)
    #     if not self.__realSubject.is_connected():
    #         return ret(False, self.__real_doesnt_exist_error_msg)
    #     return self.__realSubject.read_discount_policies()

    def execute(self, queries):
        if not self.has_real_subject():
            return ret(False, self.__real_doesnt_exist_error_msg)
        if not self.__realSubject.is_connected():
            return ret(False, self.__real_doesnt_exist_error_msg)
        return self.__realSubject.execute(queries)

    def execute_atomic_purchase_write(self, mother_write_query, daughters_write_queries_attributes: [{}],
                                      other_update_stoke_queries: [], other_update_basket_queries: []):
        if not self.has_real_subject():
            return ret(False, self.__real_doesnt_exist_error_msg)
        if not self.__realSubject.is_connected():
            return ret(False, self.__real_doesnt_exist_error_msg)
        return self.__realSubject.execute_atomic_purchase_write(mother_write_query, daughters_write_queries_attributes,
                                                                other_update_stoke_queries, other_update_basket_queries)

    def __delete__(self):
        DbProxy.__instance = None

    def __repr__(self):
        return repr("DbProxy")
