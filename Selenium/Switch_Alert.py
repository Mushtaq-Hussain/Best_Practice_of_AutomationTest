from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class SwitchAlert():

    def test(self):
        driver = webdriver.Chrome(executable_path= r"C:\Users\mushtaq.hussain\PycharmProjects\Selenium\driver\chromedriver.exe")
        driver.maximize_window()
        driver.get("https://letskodeit.teachable.com/p/practice")
        driver.implicitly_wait(2)

        Text = driver.find_element(By.ID, "name")
        Text.send_keys("Mushtaq")
        driver.find_element(By.ID, "alertbtn").click()
        time.sleep(2)
        alert1 = driver.switch_to.alert
        alert1.accept()

        Text = driver.find_element(By.ID, "name")
        Text.send_keys("Mushtaq")
        driver.find_element(By.ID, "confirmbtn").click()
        time.sleep(2)
        alert2 = driver.switch_to.alert
        alert2.dismiss()

DD = switchAlert()
DD.test()