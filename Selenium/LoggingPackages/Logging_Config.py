import logging
import logging.config


class LoggingConfig():

    def testlog(self):

        logging.config.fileConfig('140 logging.conf')
        logger = logging.getLogger(LoggingConfig.__name__)

         # Messages
        logger.debug(" Debug message")
        logger.info("Info Message")
        logger.warning("Warning message")
        logger.error("Error Message")
        logger.critical("Critical message")


logs = LoggingConfig()
logs.testlog()