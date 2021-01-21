from selenium import webdriver
from selenium.webdriver.support.select import Select
import time


class AirBnb:

    def test(self):
        driver = webdriver.Chrome("driver/chromedriver.exe")
        driver.maximize_window()
        driver.get("https://www.airbnb.com/")
        driver.implicitly_wait(3)

        address = driver.find_element_by_id("bigsearch-query-attached-query")
        address.send_keys("New York, NY")
        print("Location has been selected")

        date = driver.find_element_by_xpath("//div[contains(text(),'Add dates')]")
        date.click()
        time.sleep(2)
        print("Clicked on date dropdown menu")

        sel = driver.find_element_by_xpath("//div[@class='_1lds9wb']//tr[5]//td[6]//div[1]//div[1]//div[1]")
        sel.click()
        time.sleep(2)
        print("Check in date has been selected")

        sel1 = driver.find_element_by_xpath("//tr[1]//td[2]//div[1]//div[1]//div[1]")
        sel1.click()
        time.sleep(2)
        print("Check out date has been selected")

        guest = driver.find_element_by_xpath("//div[contains(text(),'Guests')]")
        guest.click()
        guest1 = driver.find_element_by_xpath("//div[@id='stepper-adults']//button[2]//*[local-name()='svg']")
        guest1.click()
        time.sleep(2)
        print("Guest has been selected")

        search = driver.find_element_by_xpath("//span[@class='_m9v25n']")
        search.click()
        time.sleep(2)
        print("Searched has been successfully")


ele = AirBnb()
ele.test()

