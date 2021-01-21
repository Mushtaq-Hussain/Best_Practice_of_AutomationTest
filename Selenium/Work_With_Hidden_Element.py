from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

class HiddenElement:

    def test(self):
        driver = webdriver.Chrome("driver/chromedriver.exe")
        driver.maximize_window()
        driver.get("https://learn.letskodeit.com/p/practice")
        driver.implicitly_wait(3)

        textbox = driver.find_element_by_id("displayed-text")
        textboxstate = textbox.is_displayed()
        print("Text is Visible?" + str(textboxstate))
        time.sleep(2)

        driver.find_element_by_id("hide-textbox").click()
        textboxstate = textbox.is_displayed()
        print("Text is Visible?" + str(textboxstate))
        time.sleep(2)

        driver.find_element_by_id("show-textbox").click()
        textboxstate = textbox.is_displayed()
        print("Text is Visible?" + str(textboxstate))
        time.sleep(2)


ele = HiddenElement()
ele.test()