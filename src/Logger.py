import logging

class Logger:

    def __init__(self):

        # Create and configure logger
        # logging.basicConfig(filename="WorkshopProject.log",
        #                     format='%(asctime)s >> %(levelName)s: %(message)s',
        #                     # format='%(asctime)s >> %(levelName)s: %(module)s %(funcName)s %(message)s',
        #                     filemode='w')

        # Creating a self._logger object with the relevant module name
        logger = logging.getLogger(__name__)

        # Setting the threshold of self._logger to DEBUG
        logger.setLevel(logging.INFO)

        formatter = logging.Formatter('%(asctime)s >> %(levelName)s: %(module)s %(funcName)s %(message)s')
        file_handler = logging.FileHandler("WorkshopProject.log")
        file_handler.setFormatter(formatter)

        # Creating a self._logger handler object
        logger.addHandler(file_handler)

    def add_to_log(self):

        self.logger.info("msg")
