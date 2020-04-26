import logging

def logger(f, name=None):
    # if logger.fhwr isn't defined and open ...
    try:
        if logger.fhwr:
            pass
    except:
        # ... open it
        logger.fhwr = open("EventLog.log", "w")
    if name is None:
        name = f.__qualname__

    def wrapped(*args, **kwargs):
        logger.fhwr.write("The function " + str(name) + " was called\n"
                          # + "arguments: " + str(args) + "\n\n")
                          + "arguments: " + str(args) + str(kwargs) + "\n\n")
        result = f(*args, **kwargs)
        return result

    wrapped.__doc__ = f.__doc__
    return wrapped

def secureLogger(f, name=None):
    # if logger.fhwr isn't defined and open ...
    try:
        if logger.fhwr:
            pass
    except:
        # ... open it
        logger.fhwr = open("EventLog.log", "w")
    if name is None:
        name = f.__qualname__

    def wrapped(*args, **kwargs):
        log_str = "The function " + name + " was called\n" + "arguments: ("
        for arg in args:
            log_str += "string, "
        log_str += (")\n\n")
        logger.fhwr.write(log_str)
        # logger.fhwr.write("The function " + str(name) + " was called\n"
        #                   # + "arguments: " + str(args) + "\n\n")
        #                   + "arguments: " + str(args) + str(kwargs) + "\n\n")
        result = f(*args, **kwargs)
        return result

    wrapped.__doc__ = f.__doc__
    return wrapped


def loggerStaticMethod(name, args):
    # if logger.fhwr isn't defined and open ...
    try:
        if loggerStaticMethod.fhwr:
            pass
    except:
        # ... open it
        loggerStaticMethod.fhwr = open("EventLog.log", "w")
        log_str = "The function " + name + " was called\n" + "arguments: ("
        for arg in args:
            log_str += str(arg)
        log_str += (")\n\n")
        logger.fhwr.write(log_str)

def errorLogger(msg):
    # Creating a self._logger object with the relevant module name
    logger = logging.getLogger(__name__)
    # Setting the threshold of self._logger to DEBUG
    logger.setLevel(logging.ERROR)

    formatter = logging.Formatter('%(asctime)s >> %(message)s')
    file_handler = logging.FileHandler("ErrorLog.log")
    file_handler.setFormatter(formatter)

    # Creating a self._logger handler object
    logger.addHandler(file_handler)

    logger.error(msg)

# def __init__(self):
    #
    #     # Create and configure logger
    #     # logging.basicConfig(filename="WorkshopProject.log",
    #     #                     format='%(asctime)s >> %(levelName)s: %(message)s',
    #     #                     # format='%(asctime)s >> %(levelName)s: %(module)s %(funcName)s %(message)s',
    #     #                     filemode='w')
    #
    #     # Creating a self._logger object with the relevant module name
    #     logger = logging.getLogger(__name__)
    #
    #     # Setting the threshold of self._logger to DEBUG
    #     logger.setLevel(logging.INFO)
    #
    #     formatter = logging.Formatter('%(asctime)s >> %(levelName)s: %(module)s %(funcName)s %(message)s')
    #     file_handler = logging.FileHandler("WorkshopProject.log")
    #     file_handler.setFormatter(formatter)
    #
    #     # Creating a self._logger handler object
    #     logger.addHandler(file_handler)
    #
    # def add_to_log(self):
    #
    #     self.logger.info("msg")
