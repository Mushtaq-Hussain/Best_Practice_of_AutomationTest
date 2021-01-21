from selenium import webdriver
from utilities.Hand_Wrapper import HandyWrappers
import time
import os


class UsingWrapper():

    def test(self):

        driver = webdriver.Chrome(executable_path=r"C:\Users\mushtaq.hussain\PycharmProjects\Selenium\chromedriver.exe")
        driver.maximize_window()
        driver.get("https://learn.letskodeit.com/p/practice")
        hw = HandyWrappers(driver)
        driver.implicitly_wait(2)

        element1 = hw.getElement("name")
        element1.send_keys("text")
        time.sleep(2)

        element2 = hw.getElement("//input[@id='name']",locatorType= "xpath")
        element2.clear()


ff = UsingWrapper()
ff.test()