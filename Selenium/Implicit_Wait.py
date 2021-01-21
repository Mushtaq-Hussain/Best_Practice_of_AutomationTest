from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class ImplicitWait():

    def test(self):

        driver = webdriver.Chrome(executable_path=r"C:\Users\mushtaq.hussain\PycharmProjects\Selenium\driver\chromedriver.exe")
        driver.maximize_window()
        driver.get("https://learn.letskodeit.com/p/practice")
        driver.implicitly_wait(10)

        loginLink = driver.find_element(By.XPATH, "//div[@id='navbar']//a[@href='/sign_in']")
        loginLink.click()

        emailField = driver.find_element(By.ID, "user_email")
        emailField.send_keys("test")


ff = ImplicitWait()
ff.test()