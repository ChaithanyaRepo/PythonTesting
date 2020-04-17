import logging


def test_loggingPractice():
    # log file object = enabling the file logging
    logger = logging.getLogger(__name__)

    # Log file object = log file name/file where logs to be stored
    fileHandler = logging.FileHandler('Logfile.log')
    # log file object  = Setting log file format
    logFormatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
    fileHandler.setFormatter(logFormatter)

    # File handler object
    logger.addHandler(fileHandler)

    # Setting the log level
    logger.setLevel(logging.DEBUG)
    logger.debug("A debug statement is executed")
    logger.info("Information about test case")
    logger.warning("Warning/Alert statement")
    logger.error("A major error is occurred")
    logger.critical("Critical issue")
