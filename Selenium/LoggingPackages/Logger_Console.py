import logging


class LoggerConsole():
    def testlog(self):

        # Create logger
        logger = logging.getLogger(LoggerConsole.__name__)
        logger.setLevel(logging.INFO)

        # Create Console handler and set level to info
        consolhandler = logging.StreamHandler()
        consolhandler.setLevel(logging.INFO)

        # Create formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s : %(message)s',datefmt= '%d/%m/%y %I:%M:%S %p')

        # Add formatter to console handler
        consolhandler.setFormatter(formatter)

        # Add console handler to logger
        logger.addHandler(consolhandler)

        # Messages
        logger.debug(" Debug message")
        logger.info("Info Message")
        logger.warning("Warning message")
        logger.error("Error Message")
        logger.critical("Critical message")


logs = LoggerConsole()
logs.testlog()


