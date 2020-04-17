import inspect
import logging


class BaseClass:
    def getLogger(self):
        # To get actual file name of the test file
        loggerName = inspect.stack()[1][3]
        # log file object = enabling the file logging
        logger = logging.getLogger(loggerName)

        # Log file object = log file name/file where logs to be stored
        fileHandler = logging.FileHandler('Logfile.log')
        # log file object  = Setting log file format
        logFormatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        fileHandler.setFormatter(logFormatter)

        # File handler object
        logger.addHandler(fileHandler)
        # Setting the log level
        logger.setLevel(logging.DEBUG)
        return logger
