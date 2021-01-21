from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time


class Slider():

    def test(self):
        driver = webdriver.Chrome(executable_path= r"C:\Users\mushtaq.hussain\PycharmProjects\Selenium\driver\chromedriver.exe")
        driver.maximize_window()
        driver.get("https://jqueryui.com/slider/")
        driver.implicitly_wait(2)
        # First move to iFram
        driver.switch_to.frame(0)

        slideElement = driver.find_element(By.XPATH, "//body/div[@id='slider']/span[1]")
        time.sleep(2)
        try:
            actions = ActionChains(driver)
            actions.drag_and_drop_by_offset(slideElement, 100, 0).perform()
            time.sleep(2)
            print("Slider moved successfully")
        except:
            print("Slider failed")


ff = Slider()
ff.test()