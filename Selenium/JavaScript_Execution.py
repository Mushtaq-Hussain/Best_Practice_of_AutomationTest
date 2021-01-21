from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class JavaScriptExecution():

    def test(self):
        driver = webdriver.Chrome(executable_path= r"C:\Users\mushtaq.hussain\PycharmProjects\Selenium\driver\chromedriver.exe")
        driver.maximize_window()
        #driver.get("https://letskodeit.teachable.com/p/practice")
        driver.execute_script("window.location = 'https://letskodeit.teachable.com/p/practice';")
        driver.implicitly_wait(2)

        #element = driver.find_element(By.ID, "name")
        element = driver.execute_script("return document.getElementById('name');")
        element.send_keys("test")
        time.sleep(5)


ff = JavaScriptExecution()
ff.test()
