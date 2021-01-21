from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class RunChromeTest():

    def test(self):
        driver = webdriver.Chrome("driver/chromedriver.exe")
        driver.maximize_window()
        driver.get("http://www.letskodeit.com")
        print(driver.title)


Test = RunChromeTest()
Test.test()
