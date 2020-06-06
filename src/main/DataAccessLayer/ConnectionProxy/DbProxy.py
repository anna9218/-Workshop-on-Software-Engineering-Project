from peewee import Expression, OP
from src.Logger import errorLogger, loggerStaticMethod, logger
from src.main.DataAccessLayer.ConnectionProxy.DbSubject import DbSubject
from src.main.DataAccessLayer.ConnectionProxy.RealDb import RealDb


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
                DbProxy.__instance = self.__realSubject
                self.__realSubject.connect()
                self.__realSubject.create_tables()
            else:
                DbProxy.__instance = self

    @logger
    def connect(self):
        try:
            if not self.__isConnected:
                self.__isConnected = True
                return True
            else:
                return False
        except Exception:
            errorLogger("System is down!")
            raise ResourceWarning("System is down!")

    @logger
    def disconnect(self):
        try:
            if self.__isConnected:
                self.__isConnected = False
                return True
            else:
                return False
        except Exception:
            errorLogger("System is down!")
            raise ResourceWarning("System is down!")

    @logger
    def is_connected(self) -> bool:
        return self.__isConnected

    def create_tables(self):
        pass

    def read(self, tbl, where_expr: Expression = None):
        pass

    def write(self, tbl, attributes_as_dictionary: {}):
        pass

    def update(self, tbl, attributes_as_dictionary: {}, where_expr: Expression):
        pass

    def delete(self, tbl, where_expr: Expression):
        pass

    def __delete__(self):
        DbProxy.__instance = None

    def __repr__(self):
        return repr("DbProxy")
