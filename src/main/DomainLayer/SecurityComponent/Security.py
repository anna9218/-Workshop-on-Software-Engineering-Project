from src.Logger import loggerStaticMethod, logger, errorLogger


class Security:
    __instance = None

    @staticmethod
    def get_instance():
        """ Static access method. """
        # loggerStaticMethod("SecurityComponent.get_instance", [])
        if Security.__instance is None:
            Security()
        return Security.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if Security.__instance is not None:
            errorLogger("This class is a singleton!")
            raise Exception("This class is a singleton!")
        else:
            Security.__instance = self

    @staticmethod
    def validated_password(password) -> bool:
        # loggerStaticMethod("SecurityComponent.validated_password", [password])
        return len(password) != 0

    def __repr__(self):
        return repr("SecurityComponent")

    def __delete__(self):
        Security.__instance = None
