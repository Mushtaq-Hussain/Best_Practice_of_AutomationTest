"""
Logging Demo 1
Logging Levels
DEBUG
INFO
WARNING
ERROR
CRITICAL
"""

import logging

logging.basicConfig(filename= "test.log", level= logging.DEBUG)
logging.warning("This is Warning Message")
logging.info("This is info Message")
logging.error("This is Error Message")