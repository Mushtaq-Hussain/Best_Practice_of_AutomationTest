import logging
import LoggingPackages.Custom_logger as CL


class UsingCustomLogger():

    log = CL.CustomLogger(logging.DEBUG)

    def method1(self):
        self.log.debug(" Debug message")
        self.log.info("Info Message")
        self.log.warning("Warning message")
        self.log.error("Error Message")
        self.log.critical("Critical message")

    def method2(self):
        m2log = CL.CustomLogger(logging.INFO)
        m2log.debug(" Debug message")
        m2log.info("Info Message")
        m2log.warning("Warning message")
        m2log.error("Error Message")
        m2log.critical("Critical message")

    def method3(self):
        m3log = CL.CustomLogger(logging.INFO)
        m3log.debug(" Debug message")
        m3log.info("Info Message")
        m3log.warning("Warning message")
        m3log.error("Error Message")
        m3log.critical("Critical message")


logs = UsingCustomLogger()
logs.method1()
logs.method2()
logs.method3()