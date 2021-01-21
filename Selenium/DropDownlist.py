from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

class DropDownList:

    def test(self):
        driver = webdriver.Chrome("driver/chromedriver.exe")
        driver.maximize_window()
        driver.get("https://learn.letskodeit.com/p/practice")
        driver.implicitly_wait(3)

        element = driver.find_element_by_id("carselect")
        select = Select(element)

        select.select_by_value("benz")
        print("Benz has been selected by Value")
        time.sleep(2)

        select.select_by_index("2")
        print("Honda has been selected by Index")
        time.sleep(2)

        select.select_by_visible_text("BMW")
        print("BMW has been selected by Visible text")
        time.sleep(2)

        select.select_by_index(2)
        print("Hinda has been selected by index again")
        time.sleep(2)


ele = DropDownList()
ele.test()
