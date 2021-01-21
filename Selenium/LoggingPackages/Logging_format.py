import logging

logging.basicConfig(format= '%(asctime)s : %(levelname)s : %(message)s',datefmt= '%d/%m/%y %I:%M:%S', level= logging.DEBUG)
logging.warning("This is Warning Message")
logging.info("This is info Message")
logging.error("This is Error Message")