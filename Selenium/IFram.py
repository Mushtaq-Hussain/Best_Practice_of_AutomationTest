from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class iFram():

    def test(self):
        driver = webdriver.Chrome(executable_path= r"C:\Users\mushtaq.hussain\PycharmProjects\Selenium\driver\chromedriver.exe")
        driver.maximize_window()
        driver.get("https://letskodeit.teachable.com/p/practice")
        #driver.implicitly_wait(2)
        driver.execute_script("window.scrollBy(0, 1000);")
        time.sleep(2)

        # Switch to Ifram
        driver.switch_to.frame("courses-iframe")
        print("Switched to Ifram")
        time.sleep(2)

        # Find elements
        searchbox = driver.find_element(By.ID, "search-courses")
        searchbox.send_keys("python")
        time.sleep(2)

        # Switch back to Parent Ifram
        driver.switch_to.default_content()
        print("Sitched back to current window")
        driver.execute_script("window.scrollBy(0, -1000);")
        time.sleep(2)

        # Find element on current window
        element = driver.find_element(By.ID, "name")
        element.send_keys("Test Successful")
        time.sleep(2)


bb = iFram()
bb.test()
