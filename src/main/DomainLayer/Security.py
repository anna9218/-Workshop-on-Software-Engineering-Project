class Security:
    __instance = None

    @staticmethod
    def get_instance():
        """ Static access method. """
        if Security.__instance is None:
            Security()
        return Security.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if Security.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            Security.__instance = self

    @staticmethod
    def validated_password(password) -> bool:
        return len(password) != 0

