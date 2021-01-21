from selenium import webdriver
import time

class Artribute:

    def test(self):
        driver = webdriver.Chrome("driver/chromedriver.exe")
        driver.maximize_window()
        driver.get("https://learn.letskodeit.com/p/practice")
        driver.implicitly_wait(2)

        element = driver.find_element_by_id("bmwradio")
        text = element.get_attribute("value")
        print("Artribute is: " + text)





ff = Artribute()
ff.test()



